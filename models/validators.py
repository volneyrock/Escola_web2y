# -*- coding: utf-8 -*-

## Validador tabela Notas
Notas.aluno.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s', zero = 'Selecione um')
Notas.professor.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s', zero = 'Selecione um')

## Validador tabela biblioteca
Biblioteca.arquivo.requires = IS_UPLOAD_FILENAME(extension = 'pdf', error_message = 'Precisa ser um arquivo do tipo pdf')
Biblioteca.professor.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s', zero = 'Selecione um')

## Validador tabela forum
Forum.mensagem.requires = IS_NOT_EMPTY(error_message = 'Não pode estra vazio')

## Validador tabela comentarios
Comentarios.mensagem.requires = IS_NOT_EMPTY(error_message = 'Não pode estra vazio')
Comentarios.postagem.requires = IS_IN_DB(db, 'forum.id', '%(titulo)s', zero = 'Selecione um')
