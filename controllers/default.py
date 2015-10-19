# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def contato():
    form = SQLFORM.factory(
        Field('nome', requires=IS_NOT_EMPTY(), label='Nome'),
        Field('email', requires=IS_EMAIL()),
        Field('mensagem', 'text', requires=IS_NOT_EMPTY(), label='Mesagem')
        )
    if form.process().accepted:
        mail.send(
            to=['volneyrock@gmail.com'],
            subject='Novo email de %s' %form.vars.nome,
            reply_to=form.vars.email,
            message=form.vars.mensagem,
            )
        session.flash = 'Mensagem enviada'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'Ops, algo errado no formulário'
    else:
        response.flash = 'Preencha o formulário'
    return dict(form = form)

@auth.requires_membership('professor')
def inserir_notas():
    form = crud.create(Notas)
    return dict(form=form)

@auth.requires_membership('professor')
def novo_arquivo():
    form = crud.create(Biblioteca)
    return dict(form=form)

@auth.requires_login()
def nova_mensagem():
    form = crud.create(Forum)
    return dict(form=form)

def forum():
    response.title += " - Fórum"
    posts = db(Forum.id>0).select() 
    return dict(posts=posts)

@auth.requires_login()
def ver_mensagem():
    id_mensagem = request.args(0, cast = int)
    mensagem = db(db.forum.id == id_mensagem).select().first()

    Comentarios.postagem.default = id_mensagem
    Comentarios.postagem.writable = Comentarios.postagem.readable = False
    form = crud.create(Comentarios)
    coments = db(Comentarios.postagem == id_mensagem).select()
    user = db(db.auth_user.id == Comentarios.created_by).select(db.auth_user.ALL).first()['avatar']## pesquisa a imagem do usuário que fez o comentário
    return dict(mensagem=mensagem, form=form, coments=coments, user = user)
    
@auth.requires_login()
def notas():
    form = SQLFORM.grid(Notas)
    return dict(form=form)

def biblioteca():
    form = SQLFORM.grid(Biblioteca)
    return dict(form=form)