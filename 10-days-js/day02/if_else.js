function getGrade(score) {
    let grade;
    // Write your code here
    if (25 < score && 30 >= score){
        return ("A");
    } else if (20 < score && 25 >= score){
        return ("B");
    } else if (15 < score && 20 >= score){
        return ("C");
    } else if (10 < score && 15 >= score){
        return ("D");
    } else if (5 < score && 10 >= score){
        return ("E");
    } else{
        return ("F");
    }

    return grade;
}