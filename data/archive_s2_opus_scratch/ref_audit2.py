exec(open(__import__("pathlib").Path(__file__).resolve().parent / "ref_audit.py").read().split("rm = lambda")[0])
rm = lambda x: float(np.sqrt(np.mean(np.square(x))))*1000
def signflip(y, a, b, n=20000):
    d = (y-b)**2-(y-a)**2; rng = np.random.default_rng(0)
    null = np.array([np.mean(d*rng.choice([-1, 1], len(d))) for _ in range(n)]); return (np.sum(null >= d.mean())+1)/(n+1)
# how much of D_ij is the strained-pure pressure?
Dp = {k: -0.5*sum(float(ES[el](np.log(p["V"]), 1)) for el in k) for k, p in ctx.pair.items()}
ks = sorted(ctx.pair); D = np.array([ctx.pair[k]["D"] for k in ks]); P = np.array([Dp[k] for k in ks])
print(f"binary D_ij vs strained-pure term -mean_k de_k/dlnV(V_ij): n {len(ks)} corr {np.corrcoef(D, P)[0,1]:.3f}  slope {np.polyfit(P, D, 1)[0]:.2f}  rms D {np.sqrt(np.mean(D**2)):.3f}  rms(D-P) {np.sqrt(np.mean((D-P)**2)):.3f} eV")
for f in ("h1_ev_rows_fixed.csv", "h3_fresh_rows_fixed.csv", "hm_fresh_rows_fixed.csv"):
    df = pd.read_csv(ROOT/"data"/f); df = df[df.n_el >= 3]
    rows = []
    for r in df.itertuples():
        c = parse_comp(r.comp_actual)
        if not all((a, b) in VS for a, b, _, _ in ctx.pairs(c)): continue
        v0 = ctx.vegard(c)
        L = {(a, b): np.log(v0/ctx.pair[(a, b)]["V"]) for a, b, _, _ in ctx.pairs(c)}
        pair = sum(4*xa*xb*ctx.pair[(a, b)]["E"] for a, b, xa, xb in ctx.pairs(c))
        lin = sum(4*xa*xb*ctx.pair[(a, b)]["D"]*L[(a, b)] for a, b, xa, xb in ctx.pairs(c))
        tr = sum(4*xa*xb*float(VS[(a, b)](L[(a, b)])) for a, b, xa, xb in ctx.pairs(c))
        own = sum(4*xa*xb*F[(a, b)] for a, b, xa, xb in ctx.pairs(c)) - sum(x*de(el, v0) for el, x in c.items())
        rows.append((r.E_mix, pair, pair+lin, pair+0.81*lin, tr, own))
    a = np.array(rows); y = a[:, 0]
    print(f"{f:24s} n {len(a):3d} RMSE meV  pair {rm(y-a[:,1]):5.1f} | champion k=1 {rm(y-a[:,2]):5.1f}  k=0.81 {rm(y-a[:,3]):5.1f}  exact {rm(y-a[:,4]):5.1f} | own-ref Muggianu {rm(y-a[:,5]):5.1f}"
          f" | p(champion k=1 beats own) {signflip(y, a[:,2], a[:,5]):.2f}  p(exact beats own) {signflip(y, a[:,4], a[:,5]):.1e}")
