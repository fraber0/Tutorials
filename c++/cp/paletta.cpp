#include <iostream>
#include <vector>

using namespace std;

int n, sum=0;
long long int ans=0;
vector<int> pari;
vector<int> dispari;
vector<int> visitati;
vector<int> fen;

bool controlla(int arr[], int n)
{
    for(int i=0; i<n; i++) {
        if(arr[i]%2==0 && i%2==1 || arr[i]%2==1 && i%2==0) {
            return false;
        }
    }

    return true;
}

void add(int x)
{
    x++;
    while(x < fen.size()) {
        fen[x]++;
        x += x&-x;
    }
}

int get(int x)
{
    int sum2=0;
    while(x > 0) {
        sum2 += fen[x];
        x -= x&-x;
    }

    return sum2;
}

long long paletta_sort(int N, int V[]) {
    visitati.resize(N, 0);
    fen.resize(N+1, 0);

    for(int i=0; i<N; i++) {
        if(V[i]%2==0) {
            pari.push_back(V[i]);
        }else {
            dispari.push_back(V[i]);
        }
    }

    if(controlla(V, N)){
        for(int i=0; i<pari.size(); i++) {
            add(pari[i]);
            ans += sum-get(pari[i]);
            sum += 1; 
        }

        sum = 0;
        fen.assign(N+1, 0);

        for(int i=0; i<dispari.size(); i++) {
            add(dispari[i]);
            ans += sum-get(dispari[i]);
            sum += 1; 
        }

        return ans;
    }else {
        return -1;
    } 
}

