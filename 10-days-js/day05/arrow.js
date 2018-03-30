/*
 * Modify and return the array so that all even elements are doubled and all odd elements are tripled.
 *
 * Parameter(s):
 * nums: An array of numbers.
 */
function modifyArray(nums) {
    nums = nums.map(num => (num % 2 === 0 ? 2 : 3) * num);
    return nums;
}