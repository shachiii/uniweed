from models.item import WeedProductModel
import pandas as pd

def filldb():
    df = pd.read_excel('final_soy_prod.xlsx')

    for i in range(df.shape[0]): 
        item = WeedProductModel(name=df.Weed_Name.iloc[i], crop='Soybean', product=df.Product.iloc[i], dose=df.Dosage.iloc[i])
        if (WeedProductModel.find_object(item) == False):
            item.save_to_db()
        else:
            pass

