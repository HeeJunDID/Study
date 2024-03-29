# 경로 압축 기법 소스코드
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 이렇게 함수를 수정하면 각 노드에 대하여 find 함수를 호출한 이후에, 해당 노드의 루트 노드가 바로 부모 노드가 된다. 아까와 동일하게 {1, 2,3,4,5}의 총 5개의 원소가 존재하는 상황에서 4개의 union 연산이 순서대로 (4, 5), (3, 4), (2, 3), (1, 2)와 같이 주어졌다고 가졍했을때 모든 union 함수를 처리한 후 각 원소에 대하여 find 함수를 수행하면 다음과 같이 부모 테이블이 형성된다. 겨로가적으로 경로 압축 기법을 이용하게 되면 루트 노드에 더욱 빠르게 접근할 수 있다는 점에서 기존의 기본적인 알고리즘과 비교했을 때 시간 복잡도가 개선된다.
