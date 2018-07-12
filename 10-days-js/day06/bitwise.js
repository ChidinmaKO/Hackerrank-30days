function getMaxLessThanK(n, k){
    let Max = 0;
    let current = 0;
    
    for(let i = 1; i < n; i++){
        for(let j = i + 1; j <= n; j++){
            current= i & j;
            if (current < k && current < n && current > Max){
                Max = current;
            }
        }
    }
    return Max;
}