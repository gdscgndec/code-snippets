// Trapping Rain water problem

int trap(vector<int>& height) {
    int n = height.size(), area = 0;
    vector<int> prefix(n);
    vector<int> suffix(n);

    // Construction of prefix array
    prefix[0] = height[0];
    for(int i=1; i<n; i++)
        prefix[i] = max(prefix[i-1], height[i]);

    // Construction of Suffix array
    suffix[n-1] = height[n-1];
    for(int i=n-2; i>=0; i--)
        suffix[i] = max(suffix[i+1], height[i]);

    for(int i=1; i<n-1; i++)
        area += min(prefix[i], suffix[i]) - height[i];

    return area;
}
