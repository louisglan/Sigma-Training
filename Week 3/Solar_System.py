import random
import math
# Create solarSystem class

class SolarSystem:
  def __init__ (self, stars, planets):
    self.stars = stars
    self.planets = planets

  def addStar(self, star):
    self.stars.append(star)
  

  def addPlanet(self, planet):
    self.planets.append(planet)

  def get_min_circumference(self):

    smallest_radius = min([planet.radius for planet in self.planets])
    return round(smallest_radius * 2 * math.pi, -2)


#Create star class

class Star:
  def __init__(self, name, mass, temperature):
    self.name = name
    self.mass = mass
    self.temperature = temperature
  

  # def calculateClassification(self, ):


# create planet

class Planet:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def circumference(self):
        return self.radius * 2 * math.pi

Jupiter = Planet('Jupiter', 300)
Mars = Planet('Mars', 400)
Earth = Planet('Earth', 500)
Milky_Way = SolarSystem([], []) 
Milky_Way.addPlanet(Jupiter)
Milky_Way.addPlanet(Mars)
Milky_Way.addPlanet(Earth)
print(Milky_Way.get_min_circumference())


# class SolarSystem {
#   constructor(planets, stars) {
#     this.planets = planets;
#     this.stars = stars;
#   }

#   // Using getters for encapsulation
#   get systemStars() {
#     return this.stars;
#   }

#   get systemPlanets() {
#     return this.planets;
#   }
# }

# class Star {
#   constructor(name, mass, temperature) {
#     this.name = name;
#     this.mass = mass;
#     this.temperature = temperature;
#   }

#   get classification() {
#     if (this.temperature > 40000 && this.mass >= 50) return "O";
#     else if (this.temperature > 20000 && this.mass >= 10) return "B";
#     else if (this.temperature > 8500 && this.mass >= 2) return "A";
#     else if (this.temperature > 6500 && this.mass >= 1.5) return "F";
#     else if (this.temperature > 5700 && this.mass >= 1) return "G";
#     else if (this.temperature > 4500 && this.mass >= 0.2) return "K";
#     else return "M";
#   }
# }

# class Planet {
#   constructor(name, radius) {
#     this.name = name;
#     this.radius = radius;
#   }

#   get circumference() {
#     return Math.ceil(Math.PI * this.radius * 2);
#   }
# }

# function calcHeaviestStar(solarSystem) {
#   // Get the first star - this will be the baseline to compare the
#   // rest of the stars from. We want to return the whole star - not
#   // just the weight!
#   let currentHeaviest = solarSystem.systemStars[0];
#   for (let i = 1; i < solarSystem.systemStars.length; i++) {
#     const star = solarSystem.systemStars[i];
#     if (star.starMass > currentHeaviest.starMass) {
#       currentHeaviest = star;
#     }
#   }
#   return currentHeaviest;
# }

# function calcSmallestPlanet(milkyWay) {
#   const allPlanetCircs = milkyWay.systemPlanets.map(
#     (planet) => planet.circumference
#   );
#   return Math.min(...allPlanetCircs);
# }

# function main() {
#   const milkyWay = createSolarSystem();
#   const heaviestStar = calcHeaviestStar(milkyWay);

#   // Calculate heaviest star
#   console.log(
#     `The heaviest star has the mass of ${heaviestStar.mass} suns. It is called ${heaviestStar.name} and has a classification of ${heaviestStar.classification}.`
#   );
#   // Calculate smallest circumference
#   console.log(
#     `The circumference of the smallest planet is ${calcSmallestPlanet(
#       milkyWay
#     )}km.`
#   );
# }

# main();

# // Create a randomly generated planet
# function createPlanet() {
#   return new Planet(generateId(), getRandomNumber(500, 10000));
# }

# // Create a randomly generated star
# function createStar() {
#   return new Star(
#     generateId(),
#     getRandomNumber(0.0, 60),
#     getRandomNumber(3000, 50000)
#   );
# }

# // Create arrays of random planets or stars
# function createSolarArray(min, max, type) {
#   const solarArr = [];
#   for (let i = 0; i < getRandomNumber(min, max); i++) {
#     if (type === "planet" || type === "star") {
#       // Check if we want to make Planets or Stars!
#       const solarEntity = type === "star" ? createStar() : createPlanet();
#       solarArr.push(solarEntity);
#     } else {
#       console.log(`Please enter either 'planet' or 'star'.`);
#     }
#   }
#   return solarArr;
# }

# // Create a random solar system with between 3-6 stars and 6-10 planets
# function createSolarSystem() {
#   const planets = createSolarArray(6, 10, "planet");
#   const stars = createSolarArray(3, 6, "star");
#   const solarSystem = new SolarSystem(planets, stars);
#   return solarSystem;
# }

# // Utility functions
# function generateId() {
#   return "_" + Math.random().toString(36).substr(2, 9);
# }

# function getRandomNumber(min, max) {
#   min = Math.ceil(min);
#   max = Math.floor(max);
#   return Math.floor(Math.random() * (max - min + 1)) + min;
# }