# This should gives all possible solutions
def partial_digest_recur(frags, points,previous_frags):
    points.sort()
    if len(frags) == 0:
        return points,previous_frags
    frags.sort()
    longest_frag = frags[-1]
    new_ptsA = points.copy()
    ptA = points[0] + longest_frag
    new_ptsA.append(ptA)
    frags_A = [abs(point - ptA) for point in points]
    if set(frags_A) <= set(frags):
        for frag in frags_A:
            frags.remove(frag)
        return partial_digest_recur(frags, new_ptsA,frags_A)

    new_ptsB = points.copy()
    ptB = points[-1] - longest_frag
    new_ptsB.append(ptB)
    frags_B = [abs(point - ptB) for point in points]

    if set(frags_B) <= set(frags):
        for frag in frags_B:
            frags.remove(frag)
        return partial_digest_recur(frags, new_ptsB,frags_B)


def partial_digest(digested_frags):
    digested_frags.sort()
    pts = [0, digested_frags[-1]]
    digested_frags.remove(digested_frags[-1])
    solutions = []
    solution,prev_frag = partial_digest_recur(digested_frags, pts)
    if not solution in solutions:
        solutions.append(solution)
        del(solution[-2])
        partial_digest_recur(prev_frag,solution,[])



L = [2,2,3,3,4,5,6,7,8,10]
X = partial_digest(L)
print(X)
