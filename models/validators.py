# -*- coding: utf-8 -*-

## Validador tabela Notas
notas.aluno.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s', zero = 'Selecione um')
notas.professor.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s', zero = 'Selecione um')

## Validador tabela biblioteca
biblioteca.arquivo.requires = IS_UPLOAD_FILENAME(extension = 'pdf', error_message = 'Precisa ser um arquivo do tipo pdf')
biblioteca.professor.requires = IS_IN_DB(db, 'auth_user.id', '%(first_name)s %(last_name)s', zero = 'Selecione um')

## Validador tabela forum
forum.mensagem.requires = IS_NOT_EMPTY(error_message = 'Não pode estra vazio')

## Validador tabela comentarios
comentarios.mensagem.requires = IS_NOT_EMPTY(error_message = 'Não pode estra vazio')
comentarios.postagem.requires = IS_IN_DB(db, 'forum.id', '%(titulo)s', zero = 'Selecione um')
