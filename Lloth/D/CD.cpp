#include<bits/stdc++.h>
using namespace std;

int main(void){
  unordered_set<long int> cdList;
  int counter = 0, in, n, m;

  while (1){
    scanf("%d %d", &n, &m);
    if (n == 0 || m == 0 ) { break; }

    for(long int i=0;i<n;i++){
        scanf("%d", &in);
        cdList.insert(in);
    }
    for(long int i=0;i<m;i++){
        scanf("%d", &in);
        if (cdList.count(in))
          counter++;
    }
    printf("%d\n", counter);
    counter = 0;
    cdList.clear();
  }
  return 0;
}
