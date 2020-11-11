from flask_restful import Resource, reqparse
from flask import request
from models.item import WeedProductModel
from predict_weed import predict
import base64
import re
import datetime

class Ping(Resource):
    def get(self):
        return "working"

class Item(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #                     type=float,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    # parser.add_argument('store_id',
    #                     type=int,
    #                     required=True,
    #                     help="Every item needs a store_id."
    #                     )
    parser.add_argument('image',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    # parser.add_argument('crop',
    #                     type=str,
    #                     required=True,
    #                     help="Every item needs a store_id."
    #                     )


    def post(self):

        # Add code to predict weed name

        # if not WeedProductModel.find_by_name(crop):
        #     return {'message': "Crop with name '{}' doesnot exists.".format(name)}, 400

        # if ItemModel.find_by_name(weed_name):
        #     return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # data = Item.parser.parse_args()

        data = request.get_json()
        # print("\n\n---------------image data---------------------\n\n")
        # print(data)

        # Code to decode image

        
        imgdata = re.search('base64,(.*)', data['image']).group(1)
        imgdata = base64.b64decode(imgdata)
        filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
        filepath = 'temp_images/'+filename
        # print(type(imgdata))
        # print("img_data=\n", imgdata)

        x = datetime.datetime.now()
        print('\n\nPrediction called at:', x)

        with open(filepath, 'wb') as f:
            f.write(imgdata)

        # Code to save image

# ---- Change (Added a code below with prob model prediction)----
        result = predict(filename)
        print("\nresult keys:\n ", result.keys())

        if('message' in result.keys()):
            return result
        else:
            weed_name = result['result']

            if (WeedProductModel.find_by_name(weed_name)):
                # return {'weedname': weed_name,'items': list(map(lambda x: x.json(), WeedProductModel.find_by_name(weed_name)))}
                return {'botanicalName': weed_name,'productName': list(map(lambda x: {'prod': x.product, 'dose': x.dose}, WeedProductModel.find_by_name(weed_name)))}
                # return {'botanicalName': weed_name, 'productName': list(map(lambda x: {x.product, x.dose}.json(), WeedProductModel.query.filter(name=weed_name)))}
            else:
                return {'message': 'No product found for this crop'}




# ----Change (Commented the code below)----
#        weed_name = predict(filename)
#
#        if (WeedProductModel.find_by_name(weed_name)):
#            # return {'weedname': weed_name,'items': list(map(lambda x: x.json(), WeedProductModel.find_by_name(weed_name)))}
#            return {'botanicalName': weed_name,'productName': list(map(lambda x: {'prod': x.product, 'dose': x.dose}, WeedProductModel.find_by_name(weed_name)))}
#            # return {'botanicalName': weed_name, 'productName': list(map(lambda x: {x.product, x.dose}.json(), WeedProductModel.query.filter(name=weed_name)))}
#        else:
#            return {'message': 'No product found for this crop'}

        # try:
        #     if (ItemModel.query.filter(name=weed_name)):
        #         return {'items': list(map(lambda x: x.json(), ItemModel.query.filter(name=weed_name)))}
        #     else:
        #         return {'message': 'No product found for this crop'}
        # except:
        #     return {'message': 'Error Occured'}

  
