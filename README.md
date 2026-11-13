# Casa Roque Skills

Repositório destinado à organização de skills e instruções reutilizáveis da Casa Roque.

## Estado atual

Acervo coletado em 13/11/2026: **470 arquivos `SKILL.md`**, com instruções e materiais de apoio encontrados nas pastas locais e no cache de plugins do Codex. Origens e versões distintas foram preservadas; a contagem não representa habilidades únicas nem validação de funcionamento.

- [Catálogo completo](skills/CATALOGO.md)
- [Manifesto dos arquivos e hashes SHA-256](skills/manifest.json)

Os arquivos originais foram copiados sem edição. A coleta não instala plugins, runtimes, conectores ou contas exigidos pelas habilidades.

## Organização

- `skills/locais/codex/`: habilidades locais e de sistema do Codex.
- `skills/locais/agents/`: habilidades compartilhadas de agentes, incluindo áreas da Casa Roque.
- `skills/plugins/`: habilidades dos plugins, separadas por fornecedor, pacote e versão.

Cada pasta mantém seus arquivos de apoio. Licenças e avisos encontrados nos pacotes de origem foram preservados; materiais de terceiros continuam sujeitos às respectivas condições.

## Como contribuir

1. Crie ou atualize os arquivos da skill.
2. Revise o conteúdo e remova senhas, tokens, dados pessoais e informações internas que não devam ser compartilhadas.
3. Confira as mudanças com `git diff` e adicione somente os arquivos desejados com `git add <arquivo>`.
4. Registre a alteração com `git commit -m "Descrição da alteração"`.
5. Envie com `git push -u origin main` no primeiro envio; depois, use `git push`.

As pastas locais `work/` e `outputs/` são ignoradas pelo Git. Para publicar um material dessas pastas, mova uma cópia revisada para a pasta da skill correspondente.

## Cuidados

O `.gitignore` ajuda a evitar o envio acidental de arquivos locais e credenciais comuns, mas não substitui a revisão antes de cada commit.
