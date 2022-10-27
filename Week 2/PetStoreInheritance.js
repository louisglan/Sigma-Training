class Pet {
  constructor(name, weight) {
    this.name = name;
    this.weight = weight;
    this.noise = "animally noise";
  }

  makeNoise() {
    if (this.weight >= 100) {
      console.log(this.noise.toUpperCase());
    } else {
      console.log(this.noise.toLowerCase());
    }
  }
}

class Dog extends Pet {
  constructor() {
    super();
    this.noise = "woof";
  }
}

class Cat extends Pet {
  constructor() {
    super();
    this.noise = "meow";
  }
}
