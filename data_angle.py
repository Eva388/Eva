import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import math as mt
from lmfit import models

def create_plots(csv_file):
    # Open de CSV-file met behulp van Pandas
    data = pd.read_csv(csv_file)

    # Groepeer de datasets op basis van de 'Name'-kolom
    grouped_data = data.groupby('Name')
       

    # Itereer over elke groep en creëer een plot voor elke dataset
    for name, group in grouped_data:
        # Fit functie
        # error = data['Error'].tolist()
        # measure = data['Measure'].tolist()
        # concentration = data['Concentration'].tolist()
        # def functie_1(x,a,c):

        #     f = a * x**(-c)
        #     return f

        # functie = functie_1(measure[a], 1, 2)

        # model = models.Model(functie)
        # result = model.fit(measure, x = concentration, weights = error, a = 1, c = 2/5)
        
        # Maak een plot met de gegevens van de groep
        plt.plot(group['Concentration'], group['Measure'], label=name)
        # , linestyle = "None"
        plt.errorbar(group['Concentration'], group['Measure'], yerr=group['Error'], fmt='o')
        # plt.plot(group['Concentration'], result.init_fit, 'k--', label='initial fit')
    
    
    # Voeg labels en een legenda toe aan de plot
    plt.xlabel('Concentration')
    plt.ylabel('Measure')
    plt.legend()

    # Toon de plot
    plt.savefig('Angle_measurements.png')

# Pad naar de CSV-file
csv_file_path = 'Blad1.csv'

# Roep de functie aan om de plots te maken
create_plots(csv_file_path)