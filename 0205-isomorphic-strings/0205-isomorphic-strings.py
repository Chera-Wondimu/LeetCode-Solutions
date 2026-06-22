class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False
        m_s_t ={}
        m_t_s = {}
        for a,b in zip(s,t):
            if a in m_s_t and m_s_t[a] !=b:
                return False
            if b in m_t_s  and m_t_s[b]!=a:
                return False
            m_s_t[a] = b
            m_t_s[b] = a
        return True