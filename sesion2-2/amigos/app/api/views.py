from flask import request, abort, jsonify
from .. import db
from . import api
from ..models import Amigo

# 1. GET /amigo/<id>
@api.route("/amigo/<int:id>")
def get_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    amigodict = {'id': amigo.id, 'name': amigo.name,
                 'lati': amigo.lati, 'longi': amigo.longi}
    return jsonify(amigodict)

# 2. GET /amigo/byName/<name>
@api.route("/amigo/byName/<name>")
def get_amigo_by_name(name):
    amigo = Amigo.query.filter_by(name=name).first()
    if not amigo:
        abort(404, "No se encuentra ningún amigo con ese nombre")
    amigodict = {'id': amigo.id, 'name': amigo.name,
                 'lati': amigo.lati, 'longi': amigo.longi}
    return jsonify(amigodict)

# 3. EJERCICIO RESUELTO: GET /amigos
@api.route("/amigos")
def list_amigos():
    amigos = Amigo.query.all()
    lista_amigos = []
    for amigo in amigos:
        lista_amigos.append({'id': amigo.id, 'name': amigo.name, 'lati': amigo.lati, 'longi': amigo.longi})
    return jsonify(lista_amigos)

# 4. PUT /amigo/<id>
@api.route("/amigo/<int:id>", methods=["PUT"])
def edit_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    if not request.json:
        abort(422, "No se ha enviado JSON")
    
    name = request.json.get("name")
    lati = request.json.get("lati")
    longi = request.json.get("longi")
    
    if name:
        amigo.name = name
    if lati:
        amigo.lati = lati
    if longi:
        amigo.longi = longi
        
    if name or lati or longi:
        db.session.commit()
        
    amigodict = {"id": amigo.id, "name": amigo.name,
                 "longi": amigo.longi, "lati": amigo.lati }
    return jsonify(amigodict)

# 5. EJERCICIO RESUELTO: DELETE /amigo/<id>
@api.route("/amigo/<int:id>", methods=["DELETE"])
def delete_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    db.session.delete(amigo)
    db.session.commit()
    return ('', 204)

# 6. POST /amigos
@api.route("/amigos", methods=["POST"])
def new_amigo():
    if not request.json:
        abort(422, "No se ha enviado JSON")
        
    name = request.json.get("name")
    if not name:
        abort(422, "El JSON no incluye el campo 'name'")
        
    amigo = Amigo.query.filter_by(name=name).first()
    if amigo:
        abort(422, "Ya existe un amigo con ese nombre")
        
    lati = request.json.get("lati", "0")
    longi = request.json.get("longi", "0")
    
    amigo = Amigo(name=name, lati=lati, longi=longi)
    db.session.add(amigo)
    db.session.commit()
    
    amigodict = {"id": amigo.id, "name": amigo.name,
                 "longi": amigo.longi, "lati": amigo.lati }
    return jsonify(amigodict)