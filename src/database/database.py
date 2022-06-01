from abc import ABC, abstractmethod
import logging
import sqlite3 as sql

# TODO refctor 'with' that executes sql statements into a Database function
class Database(ABC):

    _dbpath:str = 'database\\food.db'
    
    @abstractmethod
    def add():
        ...

    @abstractmethod
    def rm():
        ...

    @abstractmethod
    def u():
        ...

    @abstractmethod
    def q():
        ...
    
    @abstractmethod
    def e():
        ...

# TODO add an esists method which returns a bool
class Ingredients(Database):

    _logger = logging.getLogger('Ingredients')

    def add(ingredient: str, unit:str, price_per_unit:float) -> None:
        try:
            with sql.connect(Ingredients._dbpath) as db:
                db.execute('PRAGMA foreign_keys = ON;')
                db.execute(
                    'INSERT INTO ingredients(ingredient, unit, price_per_unit) values (?,?,?)',
                    (ingredient, unit, price_per_unit))

                Ingredients._logger.info(f'{ingredient}, {unit}, {price_per_unit} inserted into ingredients')
        except sql.IntegrityError:
            Ingredients._logger.info(f'{ingredient} already in ingredients table')

    # TODO maybe implement adding many
    def addMany(queue:list[tuple])-> None:
        ...

    # TODO implement a return error if item does not exist
    def rm(ingredient:str) -> None:
        with sql.connect(Ingredients._dbpath) as db:
            db.execute('PRAGMA foreign_keys = ON;')
            db.execute(
                'DELETE FROM ingredients WHERE ingredient=?;',
                (ingredient, ))
            Ingredients._logger.info(f'{ingredient} removed from ingredients')

    def u(ingredient:str, price_per_unit:float):
        '''
        Default to update price in ingredients
        '''
        with sql.connect(Ingredients._dbpath) as db:
            db.execute('PRAGMA foreign_keys = ON;')
            db.execute(
                '''
                UPDATE ingredients
                SET price_per_unit = :n_price
                WHERE ingredient = :n_ingredient;
                ''',
                {'n_price':price_per_unit, 'n_ingredient':ingredient}
            )
            Ingredients._logger.info(f'{ingredient}: price_per_unit -> {price_per_unit}')

    def q(ingredient:str):
        '''
        returns the id of the ingredient
        '''
        with sql.connect(Ingredients._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = (
                    db.execute(
                        '''
                        SELECT id
                        FROM ingredients 
                        WHERE ingredient=(?);
                        ''',
                    (ingredient, )).fetchone()
                )
            Ingredients._logger.info(f'{ingredient} returned {dict(query)} from ingredients')
        try:
            return query[0]
        except IndexError:
            Ingredients._logger.info(f'id for {ingredient} not found')

    def q_all() -> sql.Row:
        '''
        returns all ingredients
        '''
        with sql.connect(Foods._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = (
                    db.execute(
                        '''
                        SELECT ingredient, unit, price_per_unit
                        FROM ingredients;
                        '''
                    ).fetchall()
                )
            Foods._logger.info(f'queried all ingredients')
        return query

    # TODO implement something that checks whether an item exists, refactor query so
    # a list can be given and several items queried in one run, if database gets too big
    def by_name(ingredient:str) -> sql.Row:
        '''
        Default query for ingredients, by name
        '''
        with sql.connect(Ingredients._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = (
                    db.execute(
                        '''
                        SELECT id, unit, price_per_unit
                        FROM ingredients 
                        WHERE ingredient=(?);
                        ''',
                    (ingredient, )).fetchone()
                )
            Ingredients._logger.info(f'{ingredient} returned {dict(query)} from ingredients')
        return query

    def by_id(query_id:int) -> sql.Row:
        '''
        query for ingredients, by id
        '''
        with sql.connect(Ingredients._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = (
                    db.execute(
                        '''
                        SELECT ingredient, unit, price_per_unit
                        FROM ingredients 
                        WHERE id=(?);
                        ''',
                    (query_id, )).fetchone()
                )
            Ingredients._logger.info(f'{query_id} returned {dict(query)} from ingredients')
        return query

class Foods(Database):

    _logger = logging.getLogger('Foods')

    def add(food:str, servings:int) -> None:
        '''
        Adds a food
        '''
        try:
            with sql.connect(Foods._dbpath) as db:
                db.execute('PRAGMA foreign_keys = ON;')
                db.execute(
                    'INSERT INTO foods(food, servings) values (?,?)',
                    (food, servings)
                )
                Foods._logger.info(f'{food}, {servings} inserted into foods')
        except sql.IntegrityError:
            Foods._logger.info(f'{food} already in foods table')

    # TODO implement a return error if item does not exist
    def rm(food:str) -> None:
        '''
        Removes a food
        '''
        try:
            with sql.connect(Foods._dbpath) as db:
                db.execute('PRAGMA foreign_keys = ON;')
                db.execute(
                    'DELETE FROM foods WHERE food=?;',
                    (food, ))
                Ingredients._logger.info(f'{food} removed from foods')
        except sql.IntegrityError:
            Foods._logger.info(f'{food} still has ingredients')

    def u(food:str, servings:float):
        '''
        Default to update servings in foods
        '''
        with sql.connect(Ingredients._dbpath) as db:
            db.execute('PRAGMA foreign_keys = ON;')
            db.execute(
                '''
                UPDATE foods
                SET servings = :servings
                WHERE food = :food;
                ''',
                {'servings':servings, 'food':food}
            )
            Foods._logger.info(f'{food}: servings -> {servings}')

    def q(food:str):
        '''
        returns the id of the food
        '''
        with sql.connect(Foods._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = (
                    db.execute(
                        '''
                        SELECT id
                        FROM foods 
                        WHERE food=(?);
                        ''',
                    (food, )).fetchone()
                )
            Ingredients._logger.info(f'{food} returned {dict(query)} from foods')
        try:
            return query[0]
        except IndexError:
            Ingredients._logger.info(f'id for {food} not found')

    def q_all() -> sql.Row:
        '''
        returns all foods
        '''
        with sql.connect(Foods._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = (
                    db.execute(
                        '''
                        SELECT food, servings
                        FROM foods;
                        '''
                    ).fetchall()
                )
            Foods._logger.info(f'queried foods')
        return query

    def query_by_ingredient(ingredient:str) -> sql.Row:
        with sql.connect(Foods._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = db.execute(
                '''
                SELECT food, servings
                FROM foods
                WHERE id = (SELECT food_id FROM food_ingredients WHERE ingredient_id= (SELECT id FROM ingredients WHERE ingredient = :ingredient));
                ''',
                {'ingredient':ingredient}
            ).fetchall()
        Foods._logger.info(f'queried all foods with {ingredient}')
        return query

    def by_name(food:str) -> sql.Row:
        '''
        Default query for foods, by name
        '''
        with sql.connect(Foods._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = (
                    db.execute(
                        '''
                        SELECT id, servings
                        FROM foods 
                        WHERE food=(?);
                        ''',
                    (food, )).fetchone()
                )
            Foods._logger.info(f'{food} returned {dict(query)} from foods')
        return query

    def by_id(food_id:int) -> sql.Row:
        '''
        Default query for foods, by id
        '''
        with sql.connect(Foods._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = (
                    db.execute(
                        '''
                        SELECT food, servings
                        FROM foods 
                        WHERE id=(?);
                        ''',
                    (food_id, )).fetchone()
                )
            Foods._logger.info(f'{id} returned {dict(query)} from foods')
        return query

    def addTo(ammount:float, ingredient:str, food:str) -> None:
        '''
        Adds an ammount of an ingredient into a food
        '''
        ing_query = Ingredients.by_name(ingredient)
        food_query = Foods.by_name(food)

        try:
            with sql.connect(Foods._dbpath) as db:
                db.row_factory = sql.Row
                db.execute('PRAGMA foreign_keys = ON;')
                db.execute(
                    '''
                    INSERT INTO food_ingredients (food_id, ingredient_id, ammount, price_per_ammount)
                    VALUES (?, ?, ?, ?);
                    ''',
                    (
                        food_query['id'], 
                        ing_query['id'], 
                        ammount, 
                        ammount * ing_query['price_per_unit']
                    )
                )
            Foods._logger.info(f'added {ammount}{ing_query[1]} of {ingredient} into {food}')
        except sql.IntegrityError:
                Foods._logger.info('There was a conflict adding an ingredient, check arguments')
    
    def rmFrom(ingredient:str, food:str) -> None:
        '''
        Removes an ingredient from a food
        '''
        with sql.connect(Foods._dbpath) as db:
                db.execute('PRAGMA foreign_keys = ON;')
                db.execute(
                    '''
                    DELETE FROM food_ingredients
                     WHERE (food_id = (SELECT id FROM foods WHERE food= :food) AND ingredient_id = (SELECT id FROM ingredients WHERE ingredient= :ing));
                    ''',
                    {'food':food, 'ing':ingredient}
                )
        Foods._logger.info(f'{ingredient} removed from {food}')

    def uAmt(ammount:float, ingredient:str, food:str) -> None:
        '''
        Updates the ammount of an ingredient in a food
        '''
        ing_query = Ingredients.by_name(ingredient)
        with sql.connect(Foods._dbpath) as db:
                db.execute('PRAGMA foreign_keys = ON;')
                db.execute(
                    '''
                    UPDATE food_ingredients
                    SET ammount = :amt, price_per_ammount = :ppamt
                    WHERE (food_id = (SELECT id FROM foods WHERE food= :food) AND ingredient_id = (SELECT id FROM ingredients WHERE ingredient= :ing));
                    ''',
                    {'amt':ammount,'ppamt':ammount * ing_query['price_per_unit'], 'food':food, 'ing':ingredient}
                )
        Foods._logger.info(f'{food}: {ingredient} amt -> {ammount}')

    def query_ingredients(food:str) -> sql.Row:
        '''
        Returns the ingredient_id, ammount, and price_per_ammount of the ingredients in a given food entry
        '''
        with sql.connect(Foods._dbpath) as db:
            db.row_factory = sql.Row
            db.execute('PRAGMA foreign_keys = ON;')
            query = db.execute(
                '''
                SELECT ingredient_id, ammount, price_per_ammount
                FROM food_ingredients
                WHERE food_id = (SELECT id FROM foods WHERE food= :food);
                ''',
                {'food':food}
            ).fetchall()
        Foods._logger.info(f'ingredients for {food} queried')
        return query
