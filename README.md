## Maze

1. <b>개괄</b>

	다섯개의 미로가 있다. 각 미로에 대해 BFS, DFS, USC, GREEDY, IDS, A*등의 Search 알고리즘 중 어떤 알고리즘이 최적일지를 판단하고 그 이유를 설명하여라.

2. <b>과정</b>

	(1) <b>1번, 2번 미로 : DFS </b>

※ 1,2번 미로에서 optimal path보다 더 간 부분

![](https://i.imgur.com/iqzkw2U.png)
		
* 일단 둘다 bfs 나 ucs를 쓰며 느긋하게 확장해서 골을 찾기엔 maze size가 너무 커보였다. 그렇다고 ids 를 쓸 정도로 maze size가 크진 않아서, ids의 반복하게 되는 단점이 두드러질 것 같았다.
*  maze를 볼 때 dfs 를 쓰기 적절하다고 판단했던 부분은 어떤 block 이 두개의 block을 expand했다 할 때, 틀린길을 간다해도 그 길이 그다지 깊지 않고 금방 막힌다는 점이였다. 즉 dfs 로 잘못된 길을 집입하게되어도 time을 별로 소모하지 않고 다시 바른길로 돌아올 수 있었다. 1번 미로에서는 이 경향이 두드러지지 않았지만 2번 미로에서는 효과를 잘 발휘 했던 것 같다.


	(2) <b>3번, 4번, 5번 미로 :  Greedy Best Search</b>
	
![enter image description here](https://i.imgur.com/k1ZrgBV.png)

*  사이즈가 작은 만큼 BFS 나 USC도 문제는 없을 것 같았지만 BFS 나 USC는 time 소모를 거의 보장하는 알고리즘이라 피했다.

* 미로 3,4,5번은 미로 1,2번에 비해 DFS로 잘못된 길을 선택할 경우 많이 가야되는 지점들이 보였다. 그리고 이런 지점들은 heuristic을 썼을때 포함한 함수를 쓰면 피할 수 있는 경우가 많았다.(흰색원으로 표시한 부분)

* heuristic에 의해 잘못된 길을 들어설 수도 있었지만 (파란색원 부분) 그 정도를 비교했을 때 했을때 heuristic을 쓴 경우가 더 이익일 것 같아 heuristic을 포함한 알고리즘인 greedy와 a*을 써보았는데 실제 결과 모두 greedy가 최소로 나와서 이를 적용했다

3. <b>최종 탐색 경로</b>

![enter image description here](https://i.imgur.com/Q20F12h.png)

![enter image description here](https://i.imgur.com/ZwGe211.png)

![enter image description here](https://i.imgur.com/Nb7rXgD.png)

4. <b>결과</b>

	Node : 탐색된 노드의 수<br/>
	Time : 시간

![enter image description here](https://i.imgur.com/39KeZcm.png)
