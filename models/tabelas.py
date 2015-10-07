# -*- coding: utf-8 -*-
from datetime import datetime

notas = db.define_table('notas_',
	Field('nota', 'float', default = 0, label = 'Nota'),
	Field('aluno', 'reference auth_user', notnull = True, label = 'Aluno'),
	Field('professor', 'reference auth_user', ondelete = "SET NULL", label = 'Professor'),
	)

biblioteca = db.define_table('biblioteca_',
	Field('arquivo', 'upload', notnull = True, label = 'Arquivo'),
	Field('professor', 'reference auth_user', ondelete = 'SET NULL', label = 'Professor')
	)

forum = db.define_table('forum_',
	Field('titulo', 'string', notnull = True, label = 'Título'),
	Field('mensagem', 'text', notnull = True, label = 'Mensagem'),
	auth.signature
	)

comentarios = db.define_table('comentarios_',
	Field('mensagem', 'text', notnull = True, label = 'Mensagem'),
	Field('postagem', 'reference forum_', label = 'Postagem'),
	auth.signature
	)