import numpy as np
import csv

def main():
    data = get_data()
    data = normalise_data(data)
    data = make_numpy_object(data)
    np.save('X_data', data['X'])
    np.save('Y_data', data['Y'])

def get_data():
    data = {}
    with open('../data/labeled.csv', newline='') as csvfile:
        rawdata = csv.reader(csvfile)
        skip = True
        for row in rawdata:
            if skip is True:
                skip = False
                continue
            key = row[0]
            data[key] = {}
            data[key]['year']           = row[1]
            data[key]['gender']         = row[2]
            data[key]['age']            = row[3]
            data[key]['country']        = row[4]
            data[key]['population']     = row[5]
            data[key]['profession']     = row[6]
            data[key]['degree']         = row[7]
            data[key]['glasses']        = row[8]
            data[key]['hair_colour']    = row[9]
            data[key]['height']         = row[10]
            data[key]['income']         = row[11]
    return data

def normalise_data(data):
    new_data = {}
    # predefined bins
    gender_bins = {
        'male': -1,
        'female': 1,
    }
    degree = {
        'Bachelor': 1,
        'Master': 2,
        'PhD': 3,
    }
    # other bins
    profession = {}
    profession_count = 1
    hair_colour = {}
    hair_colour_count = 1
    country = {}
    country_count = 1
    # other
    average_age = int(0)
    age_count = int(0)
    # calculate other bins
    for key in data:
        
        if data[key]['profession'] not in profession:
            profession[data[key]['profession']] = profession_count
            profession_count += 1
            
        if data[key]['hair_colour'] not in hair_colour:
            hair_colour[data[key]['hair_colour']] = hair_colour_count
            hair_colour_count += 1

        if data[key]['country'] not in country:
            country[data[key]['country']] = country_count
            country_count += 1
        
        try:
            average_age += int(data[key]['age'])
            age_count += 1
        except ValueError:
            pass
    
    average_age /= age_count

    # replace data
    for key in data:
        new_data[key] = {}
        try: # keep
            new_data[key]['year'] = int(data[key]['year'])
        except ValueError:
            new_data[key]['year'] = 0

        try: # replace
            new_data[key]['gender'] = int(gender_bins[data[key]['gender']])
        except KeyError:
            new_data[key]['gender'] = 0

        try:
            new_data[key]['age'] = int(data[key]['age']) # keep
        except ValueError:
            new_data[key]['age'] = average_age

        new_data[key]['country'] = int(country[data[key]['country']]) # replace

        new_data[key]['population'] = int(data[key]['population']) # keep
        new_data[key]['profession'] = int(profession[data[key]['profession']]) # replace

        try: # replace
            new_data[key]['degree'] = int(degree[data[key]['degree']])
        except KeyError:
            new_data[key]['degree'] = 0

        new_data[key]['glasses'] = int(data[key]['glasses']) # keep
        new_data[key]['hair_colour'] = int(hair_colour[data[key]['hair_colour']]) # replace
        new_data[key]['height'] = int(data[key]['height']) # keep
        new_data[key]['income'] = float(data[key]['income']) # keep
    
    return new_data

def make_numpy_object(data):
    data_x = []
    data_y = []
    for key in data:
        data_x.append([])
        data_y.append([])
        data_x[len(data_x) - 1].append(data[key]['year'])
        data_x[len(data_x) - 1].append(data[key]['gender'])
        data_x[len(data_x) - 1].append(data[key]['age'])
        data_x[len(data_x) - 1].append(data[key]['country'])
        data_x[len(data_x) - 1].append(data[key]['population'])
        data_x[len(data_x) - 1].append(data[key]['profession'])
        data_x[len(data_x) - 1].append(data[key]['degree'])
        data_x[len(data_x) - 1].append(data[key]['glasses'])
        data_x[len(data_x) - 1].append(data[key]['hair_colour'])
        data_x[len(data_x) - 1].append(data[key]['height'])
        data_y[len(data_y) - 1].append(data[key]['income'])
    
    X = np.array(data_x)
    Y = np.array(data_y)

    return {'X': X, 'Y': Y}
if __name__ == '__main__':
    main()