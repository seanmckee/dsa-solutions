class Vehicle {
    getType() {
        throw new Error('getType method must be overridden');
    }
}

class Car extends Vehicle {
    getType() {
        return 'Car';
    }
}

class Bike extends Vehicle {
    getType() {
        return 'Bike';
    }
}

class Truck extends Vehicle {
    getType() {
        return 'Truck';
    }
}

class VehicleFactory {
    createVehicle() {
        throw new Error('createVehicle method must be overridden');
    }
}

class CarFactory extends VehicleFactory {
    // Write your code here
    createVehicle(){
        let car = new Car()
        return car
    }
}

class BikeFactory extends VehicleFactory {
    // Write your code here
    createVehicle(){
        let bike = new Bike()
        return bike
    }
}

class TruckFactory extends VehicleFactory {
    // Write your code here
    createVehicle(){
        let truck = new Truck()
        return truck
    }
}
