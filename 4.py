import random

def create_votes(parties, people):
    result = []
    for _ in range(people):
        vote = random.randint(0, parties)
        result.append(vote if vote > 0 else -1)
    return result

def election_resolts(parties, votes):
    results = {}
    for party in range(1, parties + 1):
        results[party] = votes.count(party)
    index = 0
    for party, vote_number in sorted(results.items(), key=lambda item: item[1], reverse=True):
        index += 1
        print(f'{index:>2}. Партія №{party:<3} | {vote_number:>8} |',
              f'{(vote_number/len(votes)*100):>10.2f}%')
        
votes = create_votes(10, 10000)
election_resolts(10, votes)