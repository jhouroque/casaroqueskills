---
name: "freecad-techdraw-workflow"
description: "Use sempre que for gerar desenhos técnicos de fabricação (ABNT/ISO) a partir de um modelo 3D real no FreeCAD — Calefactor, Fogão-Calefator, Estação Única, churrasqueiras, ou qualquer peça metálica de projetos da Roque Gestão & Engenharia / Casa Roque. Define a ordem certa de trabalho e por que nunca redesenhar em outra ferramenta (matplotlib etc)."
---

## Fluxo correto para desenhos técnicos de fabricação a partir de um modelo FreeCAD

### Regra de ouro: o desenho nasce do modelo, nunca é redesenhado à parte
Nunca recriar as peças "à mão" em outra ferramenta (ex: matplotlib, Illustrator) tentando
imitar as dimensões do modelo 3D. Isso cria uma segunda fonte de verdade que pode divergir
do modelo real (erro de digitação, escala errada, cota errada) sem que ninguém perceba.
O desenho técnico tem que ser uma PROJEÇÃO REAL da geometria 3D verdadeira, gerada dentro do
próprio FreeCAD (workbench TechDraw), para que seja fisicamente impossível o desenho discordar
do modelo.

### Ordem de execução (nunca pular etapa nem inverter)
1. Modelar e corrigir a peça/produto inteiro em 3D primeiro. Cada peça física que será
   cortada/soldada/parafusada vira um objeto nomeado separado no mesmo documento (não uma
   peça só resolvida por partes futuras — pensar em cada peça individualmente, juntar só no fim).
2. Verificar o modelo 3D antes de desenhar qualquer coisa:
   - 0 formas quebradas (`Shape.isNull()`) E 0 formas vazias (`Shape.Volume < 0.01`) — uma
     peça pode não ser "null" e ainda assim ter volume zero (bug silencioso real, já visto).
   - massa calculada por volume real x densidade do material (não confiar em número solto) —
     comparar contra estimativa de chapa bruta / referência de benchmark; se o resultado for
     fisicamente implausível (ex: peça acabada mais pesada que a chapa bruta comprada), tem
     bug de modelagem, geralmente um "cut" que não removeu material de verdade.
   - checagem de colisão/interferência real entre pares de peças de alto risco:
     `BoundBox.intersect()` como pré-filtro rápido + `shapeA.common(shapeB).Volume` com limiar
     (ex: >20mm³) pra separar sobreposição real de soldas/flanges esperadas.
   - screenshot/render real (isométrica + outros ângulos) e OLHAR de verdade antes de seguir.
3. Só depois de tudo isso conferido: desenhar as folhas técnicas DENTRO do FreeCAD via TechDraw.
   - Uma página (ou poucas, quando fizer sentido agrupar ex: porta completa com vidro+dobradiça+
     puxador) por peça/subconjunto físico. Vistas reais (frente/topo/lateral/iso) via
     `TechDraw::DrawViewPart` com `.Source = [objeto_real]`, nunca retângulos desenhados a mão.
   - Cotas em tudo, e cada cota tem que bater com o modelo real (idealmente `DrawViewDimension`
     ligada à geometria projetada; quando isso não for viável, anotar o número lendo direto do
     `Shape.BoundBox` do objeto real no momento da geração, nunca copiar de um parâmetro Python
     que pode ter ficado desatualizado).
   - Depois de criar cada página, RENDERIZAR E OLHAR (exportar PNG/PDF da página e ler a imagem)
     antes de passar pra próxima. Confirmar que nada estourou a margem da folha, que nenhuma
     vista ficou sobreposta a outra, e que a estética/legibilidade está ok.
   - Só depois de TODAS as peças individuais verificadas: criar a(s) página(s) de montagem
     final (conjunto completo).
   - Só depois de tudo desenhado e verificado dentro do app: exportar o conjunto de páginas
     pra um PDF único.

### Notas técnicas do FreeCAD (TechDraw)
- Templates ISO ficam em `{App.getResourceDir()}Mod/TechDraw/Templates/ISO/` — ex:
  `A3_Landscape_ISO5457_minimal.svg` (título/carimbo padrão ISO5457, já pronto — não redesenhar
  um carimbo na mão). Não usar `os.walk` na Resources dir inteira pra procurar template (muito
  lento, pode travar a ponte RPC por minutos) — ir direto no subcaminho `Mod/TechDraw/Templates`.
- Padrão de página: `doc.addObject('TechDraw::DrawPage', nome)` +
  `doc.addObject('TechDraw::DrawSVGTemplate', nome)` com `.Template = caminho_svg` +
  `page.Template = tmpl`. Views: `doc.addObject('TechDraw::DrawViewPart', nome)`, setar
  `.Source`, `.Direction` (Vector), `.Scale`, `.X`/`.Y` (posição em mm na folha), depois
  `page.addView(view)` e `doc.recompute()`.

### Se a ponte RPC começar a travar (timeout mesmo em comando trivial tipo `print(1+1)`)
Duas causas já vistas, mesmo sintoma (GUI dispatch timeout ~90s):
1. Tela do Mac travada/bloqueada — o macOS suspende apps em segundo plano quando a tela
   trava, e o FreeCAD para de processar a fila de comandos. Pedir pro usuário destravar a tela.
2. Uma caixa de diálogo modal (task panel, ex: "Transformar") ficou aberta em FreeCAD esperando
   clique — trava a fila de qualquer jeito. Não dá pra resolver só com mais comando Python (eles
   ficam na fila atrás do travamento). A solução mais confiável e rápida: `kill -9 <pid>` no
   processo do freecad + `open -a FreeCAD` de novo, depois reabrir os documentos salvos
   (`App.openDocument(caminho)` pra cada .FCStd). Como tudo já foi salvo em disco depois de cada
   etapa verificada, um restart nunca perde trabalho real.

### Por que isso importa
O usuário (engenheiro mecânico/segurança do trabalho, CEO da Casa Roque) vai literalmente
cortar, soldar e parafusar essas peças a partir desses desenhos. Um desenho que "parece certo"
mas foi redesenhado à mão em outra ferramenta é um risco real de erro de fabricação. A regra
não é estética — é sobre o desenho ser tecnicamente confiável o bastante pra guiar corte e
solda reais.

