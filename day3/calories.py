fats=float(input("ENTER NO OF FATS :"))
carbo =float(input("enter carbohydrates:"))
fat_calories=(fats * 9)
carbo_calories =(carbo * 4)

total_calories= (fat_calories + carbo_calories)

print("Fat Calories = " ,fat_calories)
print("Carbohydrate Calories = " , carbo_calories )
print("Total Calories = " , total_calories )

print('LA')

def mass():{
    print("hello")
}


class Employee():
    def __init__(self,name, email ,dependants): 
        self.name = name 
        self.email = email
        self.dependants = dependants
    def EmployeeModel(self):
        
        name =db.Colomn(db.Integer(400))
        email = db.Column(db.Email)
        dependants =db.Column(db.String)

        return(name,email,dependants)

        employee =Employee()

