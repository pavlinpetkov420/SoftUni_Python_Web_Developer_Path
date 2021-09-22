from project1.customer import Customer
from project1.dvd import DVD


class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        customers_info = ""
        for c in self.customers:
            customers_info += f"{repr(c)}\n"

        dvd_info = ""
        for m in self.dvds:
            dvd_info += f"{repr(m)}\n"

        return customers_info + dvd_info

    @staticmethod
    def dvd_capacity():
        dvd_capacity = 15
        return dvd_capacity

    @staticmethod
    def customer_capacity():
        customer_capacity = 10
        return customer_capacity

    @staticmethod
    def check_age_restriction(c_age, dvd_age_restriction):
        if c_age < dvd_age_restriction:
            return True
        return False

    @staticmethod
    def is_rented_by_customer(customer_instance, dvd_instance):
        movie_name = dvd_instance.name
        filtered_movies = [movie_name for m in customer_instance.rented_dvds if m.name == movie_name]
        if filtered_movies:
            return True
        return False

    def check_dvd_capacity(self):
        dvds_count = len(self.dvds)
        if dvds_count < MovieWorld.dvd_capacity():
            return True
        return False

    def check_customer_capacity(self):
        customers_count = len(self.customers)
        if customers_count < MovieWorld.customer_capacity():
            return True
        return False

    def add_customer(self, customer: Customer):
        if self.check_customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if self.check_dvd_capacity():
            self.dvds.append(dvd)

    def customer_info(self, c_id):
        for c in self.customers:
            if c.last_id == c_id:
                return c

    def dvd_info(self, dvd_id):
        for d in self.dvds:
            if d.last_id == dvd_id:
                return d

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_instance = self.customer_info(customer_id)
        dvd_instance = self.dvd_info(dvd_id)
        customer_name = customer_instance.name
        dvd_name = dvd_instance.name

        if self.is_rented_by_customer(customer_instance, dvd_instance):
            return f"{customer_name} has already rented {dvd_name}"

        if dvd_instance.is_rented:
            return "DVD is already rented"

        if self.check_age_restriction(customer_instance.age, dvd_instance.age_restriction):
            age_r = dvd_instance.age_restriction
            return f"{customer_name} should be at least {age_r} to rent this movie"

        dvd_instance.is_rented = True
        customer_instance.rented_dvds.append(dvd_instance)
        return f"{customer_name} has successfully rented {dvd_name}"

    def return_dvd(self, customer_id, dvd_id):
        customer_instance = self.customer_info(customer_id)
        dvd_instance = self.dvd_info(dvd_id)
        customer_name = customer_instance.name
        dvd_name = dvd_instance.name

        if not self.is_rented_by_customer(customer_instance, dvd_instance):
            return f"{customer_name} does not have that DVD"

        dvd_instance.is_rented = False
        customer_instance.rented_dvds.remove(dvd_instance)
        return f"{customer_name} has successfully returned {dvd_name}"


# movie_world = MovieWorld("Test")
# d = DVD("A", 1, 1254, "February", 10)
# c = Customer("Pesho", 20, 4)
# movie_world.add_customer(c)
# movie_world.add_dvd(d)
# result = movie_world.rent_dvd(4, 1)
# print(c.rented_dvds[0])

