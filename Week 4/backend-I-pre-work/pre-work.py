from flask import Flask
from flask import request
import json
from json import load, loads, dumps

app = Flask(__name__)
f = open('companies.json', 'r')
data = json.load(f)

def add_company(company_data):
    id = len(data) + 1
    company_data['id'] = id
    data.append(company_data)
    return f"Company added with ID {id}", 200

def get_companies():
    return dumps(data), 200

def get_company_by_id(id):
  company = filter(lambda company: company["id"] == id, data)
  return json.dumps(list(company))

  # [company['name'] for company in data if company['id'] == id]

def delete_company(company_id):
  company = list(filter(lambda company: company['id'] == company_id, data))
  data.remove(company)

@app.route("/companies", methods=['GET', 'POST'])
def companies():
  if request.method == 'GET':
    return get_companies()
  if request.method == 'POST':
    return add_company()

@app.route('/companies/<int:company_id>', methods = (['GET', 'DELETE']))
def by_id(company_id):
  if request.method == 'GET':
    get_company_by_id(company_id)
  if request.method == 'DELETE':
    return delete_company(company_id)



@app.route('/search')
def get_company_by_name():
  search_term = request.args.get('name')
  companies = filter(lambda company: company["name"] == search_term, data)
  return json.dumps(list(companies))








# @app.route("/companies/<int:company_id>")
# def get_company(company_id):
#     company = filter(lambda company: company["id"] == company_id, data)
#     return dumps(list(company))

# @app.route("/companies/<int:company_id>/<string:property>")
# def get_company_detail(company_id, property):
#     company = list(filter(lambda company: company["id"] == company_id, data))[0]
#     return dumps(company[property])

# @app.route("/companies/<int:company_id>/country")
# def get_company_country(company_id):
#     company = filter(lambda company: company["id"] == company_id, data)
#     return dumps(list(company)[0]['country'])


# @app.route("/search")
# def get_companies_search():
#     search_term = request.args.get("name")
#     companies = filter(lambda company: company["name"] == search_term, data)
#     return dumps(list(companies))


# @app.route("/employees/search")
# def find_employee():
#     search_terms = request.args
#     return search_terms