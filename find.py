import util

primeSize = 512
# p = util.getRandomPrime(primeSize)
# q = util.getRandomPrime(primeSize)

p = 12422160521539354950972405261644930617188546115135784299856216804262598374746363519064068304488324401297288137158417397964444100213248920933139268487305983
q = 13102400686731026620620607144506007577835792880009655217994874158729348390872980329048180249221990256946844587892499183078583850710968823924930657812567127

while p == q:
    q = util.getRandomPrime(primeSize)

if p > q:
    tmp = p
    p = q
    q = tmp

n, e, d = util.getKeys(p, q)

min = 1 << (primeSize - 1)
max = (1 << primeSize) - 1

import mpmath
mpmath.mp.dps = 200

n_s = mpmath.sqrt(n)

min_log = mpmath.ln(min)
p_log = mpmath.ln(p)
n_s_log = mpmath.ln(n_s)
q_log = mpmath.ln(q)
max_log = mpmath.ln(max)

def print_stuff():

    print("n:  ", n)
    print("p:  ", p)
    print("q:  ", q)
    print(f"min: {min}")
    print(f"max: {max}")
    print("")

    print("sqrt(n): ", n_s)
    print("")

    print(f"min_log: {min_log}")
    print(f"p_log: {p_log}")
    print(f"n_s_log: {n_s_log}")
    print(f"q_log: {q_log}")
    print(f"max_log: {max_log}")
    print("")

def get_mid(low, high):
    dividend = mpmath.fsub(high, low)
    quotient = mpmath.fdiv(dividend, mpmath.mpf('2'))

    return mpmath.fadd(low, quotient)

def are_primes(p_log, q_log):
    p = int(mpmath.nint(mpmath.exp(p_log)))
    q = int(mpmath.nint(mpmath.exp(q_log)))

    if not util.isPrime(p) or not util.isPrime(q):
        return False

    return True

def are_factors(p_log, q_log, n):
    p = int(mpmath.nint(mpmath.exp(p_log)))
    q = int(mpmath.nint(mpmath.exp(q_log)))

    product = p * q
    """
    I think the problem might be that im determing whether to move the bounds based on (possible_p * possible_q) compared to n 
    Maybe I should be comparing to sqrt(n) of ln(sqrt(n)) since that is what is centering this
    """

    if product < n:
        return -1
    elif product > n:
        return 1
    
    return 0



def search(min, max, n_s_log, n):

    # Binary search for p (between min and mid)
    low = min
    high = n_s_log

    count = 0
    
    while low <= high:
        count += 1
        # mid = (low + high) // 2
        # mid = low + (high - low) / 2

        mid = get_mid(low, high)

        print(f"low: {low}")
        print(f"mid: {mid}")
        print(f"high: {high}")
        print("")

        possible_p_log = mid
        possible_q_log = mpmath.fadd(n_s_log, mpmath.fsub(n_s_log, possible_p_log))

        print(f"possible_p_log: {possible_p_log}")
        print(f"possible_q_log: {possible_q_log}")
        print("")

        product_match = are_factors(possible_p_log, possible_q_log, n)

        if product_match == 0:
            p = int(mpmath.nint(mpmath.exp(p_log)))
            q = int(mpmath.nint(mpmath.exp(q_log)))
            return p,q
        elif product_match < 0:
            print("changing low")
            # low = mid
            low = mpmath.fadd(mid, mpmath.mpf('0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'))
        else:
            print("changing high")
            # high = mid
            high = mpmath.fsub(mid, mpmath.mpf('0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'))

    print(f"{count} iterations")
    return None, None  # Target not found


diff_from_min = mpmath.fsub(n_s_log, min_log)
diff_from_max = mpmath.fsub(max_log, n_s_log)

min_search = min_log
max_search = max_log

if diff_from_min < diff_from_max:
    diff_of_diffs = mpmath.fsub(diff_from_max, diff_from_min)
    max_search = mpmath.fsub(max_log, diff_of_diffs)
else:
    diff_of_diffs = mpmath.fsub(diff_from_min, diff_from_max)
    min_search = mpmath.fadd(min_log, diff_of_diffs)

found_p, found_q = search(min_search, max_search, n_s_log, n)

print("=========== Results ===========")
print(found_p)
print(found_q)
print("")

print_stuff()


"""
p_log: 354.27022013630919985266828366992123031393776710056240537681571503309758213761378747420918226913733876286353486832657463633327264409036384235024957828126519667632007884709711179313773714029761797049656


low: 354.26515728849970199940535064747997154891647461704262715941099957391248189402004751758750377038806347447031025090972345431736267866629747739712546379848329187739332365946183889056877287031010067060022
mid: 354.27631529222764348060530674453859575930579227686799254336825202771053873860438882475272771625774916455490249247607396171802965169861293785603058208397653776585857948715584480862241889256034325840959
high: 354.28747329595558496180526284159721996969510993669335792732550448150859558318873013191795166212743485463949473404242446911869662473092839831493570036946978365432383531484985072667606491481058584621895

changing low
low: 354.27631529222764348060530674453859575930579227686799254336825202771053873860438882475272771625774916455490249247607396171803965169861293785603058208397653776585857948715584480862241889256034325840959
mid: 354.28189429409161422120528479306790786450045110678067523534687825460956716089655947833533968919259200959719861325924921541836813821477066808548314122672316071009120740100284776764924190368546455231427
high: 354.28747329595558496180526284159721996969510993669335792732550448150859558318873013191795166212743485463949473404242446911869662473092839831493570036946978365432383531484985072667606491481058584621895
"""