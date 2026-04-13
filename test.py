''''num=[1,2,3,4,5,56,6]

print(num)'''


check = {num for num in range (100)}
print(check)

'''

Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 4th Season: 
2-nensei-hen 1 Gakki; Youkoso Jitsuryoku Shijou Shugi no Kyoushitsu e 4th Season
2-nensei-hen Ichi Gakki; Welcome to the Classroom of the Elite,
You-jitsu 4th Season, Classroom of the Elite IV: Year 2






'''

check = {num for num in range (100)}
print(check)

check = {num for num in range (100)}
print(check)
check = {num for num in range (100)}
print(check)
check = {num for num in range (100)}
print(check)
check = {num for num in range (100)}
print(check)
check = {num for num in range (100)}
print(check)


import logfire
from pydantic import BaseModel
from pydantic_ai import Agent

logfire.configure()
logfire.instrument_pydantic_ai()


class City(BaseModel):
    name: str
    country: str
    population: int
    tourist_population: int
    landmarks: list[str]
