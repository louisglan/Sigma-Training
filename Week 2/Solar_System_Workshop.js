// Create solarSystem class

class SolarSystem {
  constructor() {
    this.stars = [];
    this.planets = [];
  }

  addStar(star) {
    this.stars.push(star);
  }

  addPlanet(planet) {
    this.planets.push(planet);
  }
}

//Create star class

class Star {
  constructor(name, mass, temperature) {
    this.name = name;
    this.mass = mass;
    this.temperature = temperature;
  }

  calculateClassification() {}
}

//create planet

class Planet {
  constructor(name, radius) {
    this.name = name;
    this.radius = radius;
  }

  circumference() {}
}
