from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
import target_store
import logging
######################
log = logging.getLogger('test')
log.setLevel(logging.DEBUG)

log.warn('warn')
log.debug('debug')

log.root.setLevel(logging.DEBUG)
log.debug('debug again')
logging.basicConfig(level=logging.DEBUG)


#####################



app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()

# "employeeId","itemId","amount","type", "district","category","price","storeId"
# {
#     _id: "blah",
#     itemId: "blah",
#     amount: 15,
#     type: 'discrete',
#     dsitrict: "Mongkok",
#     storeId: "babi"
# }
# //initialise program 
target_store.init_program()

parser.add_argument('_id', location="form")
parser.add_argument('itemId', type=int, location="form")
parser.add_argument('amount',type=int, location="form")
parser.add_argument('type', location="form")
parser.add_argument('district', location="form")
parser.add_argument('category', location="form")
class Algorithm(Resource):
    def post(self):
        args = parser.parse_args()
        total = []
        template = [args["_id"], args["itemId"], args["amount"], args["type"], args["district"], args["category"]]
        total.append(template)
        values=target_store.get_target_and_store(total)
        print(values)

        # for name in args["name"]:
            # customer_price, employee_target = test.algorithm(name)
            # temp = {'name' : name,'customerPrice': customer_price, 'targetPrice': employee_target}
            # data.append(temp)
        return values, 200

# @app.route("/", methods=['POST'])
# def get_price():
#     print(request.get_json())
#     return jsonify({"bbullshit" :request.get_json()}), 201

api.add_resource(Algorithm, '/test')

if __name__ == '__main__':
    app.run(debug=True) 