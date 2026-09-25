class Solution:

    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)
        i = 0

        def parse_expr():
            nonlocal i
            results = set()
            results.update(parse_term())
            while i < n and expression[i] == ',':
                i += 1
                results.update(parse_term())
            return results

        def parse_term():
            nonlocal i
            res = {''}
            while i < n and (expression[i].islower() or expression[i] == '{'):
                next_factor = parse_factor()
                new_res = set()
                for r in res:
                    for nf in next_factor:
                        new_res.add(r + nf)
                res = new_res
            return res

        def parse_factor():
            nonlocal i
            if expression[i] == '{':
                i += 1
                res = parse_expr()
                i += 1
                return res
            else:
                start = i
                while i < n and expression[i].islower():
                    i += 1
                return {expression[start:i]}
        return sorted(list(parse_expr()))
