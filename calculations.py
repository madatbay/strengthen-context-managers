from decimal import Decimal, localcontext

with localcontext() as ctx:
    ctx.prec = 42
    print(Decimal("1") / Decimal("42"))