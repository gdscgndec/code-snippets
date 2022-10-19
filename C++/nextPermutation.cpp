// Input => [1 2 3]
// Output => [1 3 2]

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

void reverse(vector<int> &nums, int i, int j) {
    while(i<j) {
        swap(nums[i], nums[j]);
        i++;
        j--;
    }
}

void nextPermutation(vector<int>& nums) {
    int i = nums.size() - 2;
    while(i >= 0 && nums[i] >= nums[i+1]) {
        i--;
    }
    if(i >= 0) {
        int j = nums.size()-1;
        while(j >= i && nums[j] <= nums[i]) {
            j--;
        }
        swap(nums[i], nums[j]);
    }
    reverse(nums, i+1, nums.size()-1);
}
