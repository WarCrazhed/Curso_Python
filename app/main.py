import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./app/data.csv')
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    labels, values = utils.get_world_percentages(data)
    charts.generate_pie_chart(labels, values)

"""     data = read_csv.read_csv('./app/data.csv')
    country = input('Type Country => ')

    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)

    print(result) """

if __name__ == '__main__':
    run()