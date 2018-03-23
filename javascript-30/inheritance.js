class Student extends Person {
    /*
    *   Class Constructor
    *
    *   @param firstName - A string denoting the Person's first name.
    *   @param lastName - A string denoting the Person's last name.
    *   @param id - An integer denoting the Person's ID number.
    *   @param scores - An array of integers denoting the Person's test scores.
    */
    // Write your constructor here
    constructor(firstName, lastName, id, scores){
        //this.firstName = firstName;
        //this.lastName = lastName;
        super(firstName, lastName, id);
        this.scores = scores;
    }

    /*
    *   Method Name: calculate
    *   @return A character denoting the grade.
    */
    // Write your method here
    calculate() {
        let totalGrade = 0;

        for (var i = 0; i < this.scores.length; i++){
            totalGrade += this.scores[i];
        }
        var averageGrade = (totalGrade / this.scores.length);

        if (averageGrade >= 90 && averageGrade <= 100){
            return "O";
        } else if (averageGrade >= 80 && averageGrade < 90){
            return "E";
        } else if (averageGrade >= 70 && averageGrade < 80){
            return "A";
        } else if (averageGrade >= 85 && averageGrade < 70){
            return "P";
        } else if (averageGrade >= 40 && averageGrade < 55){
            return "D";
        } else {
            return "T";
        }
    }
}