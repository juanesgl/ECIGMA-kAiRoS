#include <bits/stdc++.h>
using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n,k;

    //char letra1, letra2;
    //cin >> letra1 >> letra2;

    if (!(cin >> n >> k)) {
        return 0;
    }

    vector<int> v(n, 0);

    for (int i = 0; i < k; i++) {
        char type;
        cin >> type;
        if (type == 'F') {
            int num_o;
            cin >> num_o;
            v[num_o - 1] = !v[num_o - 1];
        } else if (type == 'C') {
            int l;
            int r;
            cin >> l >> r;

            int cont;

            for (int j = l - 1; j < r; j++) {
                if (v[j] == 1) {
                    cont += 1;
                }
            }

            cout << cont;
        }
    }
    
    return 0;
}
