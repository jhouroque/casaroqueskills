# Casa Roque Skills

Repositório destinado à organização de skills e instruções reutilizáveis da Casa Roque.

## Estado atual

Estrutura inicial de documentação e configuração do Git. Nenhuma skill foi adicionada ou validada neste repositório.

## Organização sugerida

Cada skill pode ter uma pasta própria dentro de `skills/`, contendo um arquivo `SKILL.md` com sua finalidade, instruções e exemplos. Arquivos de apoio devem ficar junto da skill correspondente.

## Como contribuir

1. Crie ou atualize os arquivos da skill.
2. Revise o conteúdo e remova senhas, tokens, dados pessoais e informações internas que não devam ser compartilhadas.
3. Confira as mudanças com `git diff` e adicione somente os arquivos desejados com `git add <arquivo>`.
4. Registre a alteração com `git commit -m "Descrição da alteração"`.
5. Envie com `git push -u origin main` no primeiro envio; depois, use `git push`.

As pastas locais `work/` e `outputs/` são ignoradas pelo Git. Para publicar um material dessas pastas, mova uma cópia revisada para a pasta da skill correspondente.

## Cuidados

O `.gitignore` ajuda a evitar o envio acidental de arquivos locais e credenciais comuns, mas não substitui a revisão antes de cada commit.
