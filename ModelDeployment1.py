import pandas as pd
from sklearn.externals import joblib
import sys
import os


def PredictPrice(Model, Make, Mileage, Year, State):

    #clf_VF = joblib.load(os.path.dirname(__file__) + '/price_forecast.pkl') 
    
   
    d = {'Model':[Model], 'Make': [Make], 'Mileage': [Mileage], 'Year': [Year], 'State': [State]}
    DF = pd.DataFrame(data=d)
    
    # Transformado
    estados = [["MD",0],["KY",1],["SC",2],["OK",3],["TN",4],["FL",5],["NH",6],["WI",7],["NY",8],["TX",9],["NJ",10],["MI",11],
           ["AL",12],["CA",13],["NC",14],["GA",15],["OR",16],["OH",17],["AR",18],["VA",19],["WA",20],["IL",21],["AZ",22],["MA",23],
           ["CO",24],["MN",25],["KS",26],["PA",27],["MO",28],["SD",29],["IN",30],["NE",31],["UT",32],["NM",33],["HI",34],["NV",35],
           ["DE",36],["MS",37],["ID",38],["IA",39],["ME",40],["CT",41],["MT",42],["VT",43],["WV",44],["LA",45],["ND",46],["AK",47],
           ["RI",48],["WY",49],["DC",50]]

 

    marca = [["Nissan",0],["Chevrolet",1],["Hyundai",2],["Jeep",3],["Ford",4],["Kia",5],["Mercedes-Benz",6],["Dodge",7],
         ["GMC",8],["Toyota",9],["Honda",10],["Volkswagen",11],["Cadillac",12],["Volvo",13],["BMW",14],["Subaru",15],
         ["Chrysler",16],["Buick",17],["Ram",18],["Lexus",19],["Porsche",20],["Audi",21],["Lincoln",22],["MINI",23],
         ["INFINITI",24],["Scion",25],["Land",26],["Acura",27],["Mazda",28],["Mercury",29],["Mitsubishi",30],
         ["Pontiac",31],["Jaguar",32],["Bentley",33],["Suzuki",34],["FIAT",35],["Tesla",36],["Freightliner",37]]

 

    df_estados = pd.DataFrame(estados, columns = ["State","State_2"])
    df_marca = pd.DataFrame(marca, columns = ["Make","Make_2"])
    df_modelos = pd.read_csv(r'../ModeloAvanzadosDecisionTrees/Modelos.csv')

 

    DF['State'] = DF['State'].str.strip()

 

    DF = pd.merge(DF,df_marca, how = "left", left_on = "Make",right_on = "Make")
    DF = pd.merge(DF,df_estados, how = "left", left_on = "State",right_on = "State")
    DF = pd.merge(DF,df_modelos, how = "left", left_on = "Model",right_on = "Model")
    DF = DF.drop(["Make","State", "Model"],axis=1)
    DF = DF.rename(columns = {"Make_2": "Make",
                                     "State_2": "State","Model_2": "Model" 
                                     })
  
    # Create features
    #DF['State'] = pd.factorize(DF.State)[0]
    #DF['Make'] = pd.factorize(DF.Make)[0]
    #DF['Model'] = pd.factorize(DF.Model)[0]
  
    

    # Make prediction
    p1 = clf_VF.predict(DF)

    return p1


#if __name__ == "__main__":
    
    #if len(sys.argv) == 1:
        #print('Please add an URL')
        
    #else:

        #DF = sys.argv[1]
        

#print(DF)
#print('forecast of price: ', p1)
 