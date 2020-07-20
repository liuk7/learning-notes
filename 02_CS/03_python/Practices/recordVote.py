while True:
    try:
        candidateNum = int(input())
        candidateName = input().split()
        votePeople = int(input())
        vote = input().split()
        
        if votePeople == 0 or vote is None:
            print(0)

        # result = dict()
        # for e in vote:
        #     if e in candidateName and not result.__contains__(e):
        #         result[e] = 1
        #     elif e in candidateName and result.__contains__(e):
        #         result[e] += 1
        #     elif not result.__contains__('Invalid'):
        #         result['Invalid'] = 1
        #     else:
        #         result['Invalid'] += 1

        # sorted(result.items(), key = lambda x:x[0])
        # for item in result.items():
        #     print(str(item[0]) + ' : ' + str(item[1]))    

        valid = 0
        for e in candidateName:
            if e in vote:
                print(str(e) + ' : ' + str(vote.count(e)))
                valid += vote.count(e)
            else:
                print(str(e) + ' : ' + str(vote.count(e)))
        print('Invlid :' + str(votePeople - valid))
    except:
        break