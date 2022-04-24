from sqlalchemy import true
import src.database.database as db


class Utils:
    
    def menu() -> None:
        '''
        Prints all items in food in stdout
        '''
        for row in db.Foods.q_all():
            print(list(row))

    def by_ingredient(inrgedient:str) -> None:
        '''
        Prints all foods that contain certain ingredient
        '''
        for row in db.Foods.query_by_ingredient(inrgedient):
            print(list(row))

    # TODO refactor for a proper method, this one is borrowed from program.Foodlist.makeList
    def show_ingredients(food:str) -> None:
        '''
        shows servings and
        prints all ingredients from a certain food
        '''
        tmp_list = {}
        tmp_ing_list = db.Foods.query_ingredients(food)
        for ingredient in tmp_ing_list:
            tmp_ing = db.Ingredients.by_id(ingredient['ingredient_id'])
            if tmp_ing['ingredient'] in tmp_list:
                tmp_list[tmp_ing['ingredient']]['ammount'] += ingredient['ammount']
                tmp_list[tmp_ing['ingredient']]['total'] += ingredient['price_per_ammount']
            elif tmp_ing['ingredient'] not in tmp_list:
                tmp_list[tmp_ing['ingredient']] = {'ammount':ingredient['ammount']}
                tmp_list[tmp_ing['ingredient']]['unit'] = tmp_ing['unit']
                tmp_list[tmp_ing['ingredient']]['total'] = ingredient['price_per_ammount']
                tmp_list[tmp_ing['ingredient']]['price'] = tmp_ing['price_per_unit']
        print(db.Foods.by_name(food)['servings'])
        for key, item in tmp_list.items():
            print(f"{key} -> {item['ammount']}{item['unit']}")

    def build_list() -> None:
        
        tmp_list = []

        while True:
            item = input('item: ')

            if item == '0':
                return tmp_list
            
            n = int(input('repeated: '))
            tmp_list += [item] * n

class W:

    PLATANO = 0.2
    TORTILLA = 0.025
    HUEVO = 1/12
    PAN = 0.025
    MANGO = 0.15
    LATA_DE_GARBANZO = 0.4