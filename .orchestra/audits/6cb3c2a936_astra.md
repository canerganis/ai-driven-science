OpenAI Codex v0.160.0
--------
workdir: C:\Users\can02\Projects\AI driven Science
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a1993d-4316-7311-8ec0-3d35a2e69ce8
--------
user
Independent audit of a pre-registered PBE test. You did not write it. Do not edit files.

Criterion (ledger claims/claims.jsonl id 6cb3c2a936, registered before any output): H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.

Code: scripts/hiso_l12_v2.py (v2 fixes the S1 audit: shared cutoff and k-grid for alloy and pure refs), harness/dft.py. Results: data/hiso_l12_dft_v2.csv (PBE, 8 cells), data/hiso_l12_mace.csv. Raw runs under data/dft_runs/hiso2/. A dense-k check (kspacing 0.08, Cu3Ir and Ag3Rh) is running now and is not available.

My reading: n=6 (Cu3Ir Cu3Rh Au3Ir Ag3Ir Ag3Rh Pt3Cu), each cell has K44 and Kp of the same sign, median ratio 0.94, so H-iso PASS in PBE; Ag cells are off (0.54, 0.39) and Pt3Cu is 2.6. MACE L1 FAIL (K44 sign wrong in Pd3Ir, Au3Ir, Ag3Rh; median |diff| 53% of median |PBE|).

Check: (1) is "all K44, Kp same sign" fairly read per cell, or does the text demand one global sign (Pt3Cu is a positive control)? Say which reading the registration supports and the verdict under each. (2) numerics: strain size, three-point curvature, symmetry shortcut (g-/t- copied from g+/t+ except Cu3Ir), unit conversion of K44 and Kp, Vegard volume, same cutoff/k for refs, convergence of the output files (scf converged, no warnings). (3) selection effects or criterion drift. (4) whether the result says anything about the paper's K' transfer rule (paper/draft_v3.md), which rests on MACE mixing shear curvatures.
End with one line: VERDICT PASS / FAIL / PLAUSIBLE for H-iso in PBE, and one line for MACE L1.

warning: Codex is ignoring 1 unrecognized configuration setting. Check for typos or deprecated settings.
  user (C:\Users\can02\.codex\config.toml): `computer_use.windows.always_allowed_app_ids` is ignored.
warning: Codex is ignoring 1 unrecognized configuration setting. Check for typos or deprecated settings.
  user (C:\Users\can02\.codex\config.toml): `computer_use.windows.always_allowed_app_ids` is ignored.
warning: Under-development features enabled: local_thread_store_compression. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in C:\Users\can02\.codex\config.toml.
warning: clamping SessionEnd hook timeout to 3s in C:\Users\can02\.codex\plugins\cache\openai-codex\codex\1.0.6\hooks\hooks.json
2026-11-01T22:31:35.629546Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when UnexpectedServerResponse("HTTP 403: <html>\n  <head>\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n    <style global>body{font-family:Arial,Helvetica,sans-serif}.container{align-items:center;display:flex;flex-direction:column;gap:2rem;height:100%;justify-content:center;width:100%}@keyframes enlarge-appear{0%{opacity:0;transform:scale(75%) rotate(-90deg)}to{opacity:1;transform:scale(100%) rotate(0deg)}}.logo{color:#8e8ea0}.scale-appear{animation:enlarge-appear .4s ease-out}@media (min-width:768px){.scale-appear{height:48px;width:48px}}.data:empty{display:none}.data{border-radius:5px;color:#8e8ea0;text-align:center}@media (prefers-color-scheme:dark){body{background-color:#343541}.logo{color:#acacbe}}</style>\n  <meta http-equiv=\"refresh\" content=\"360\"></head>\n  <body>\n    <div class=\"container\">\n      <div class=\"logo\">\n        <svg\n          width=\"41\"\n          height=\"41\"\n          viewBox=\"0 0 41 41\"\n          fill=\"none\"\n          xmlns=\"http://www.w3.org/2000/svg\"\n          strokeWidth=\"2\"\n          class=\"scale-appear\"\n        >\n          <path\n            d=\"M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z\"\n            fill=\"currentColor\"\n          />\n        </svg>\n      </div>\n      <div class=\"data\"><div class=\"main-wrapper\" role=\"main\"><div class=\"main-content\"><noscript><div class=\"h2\"><span id=\"challenge-error-text\">Enable JavaScript and cookies to continue</span></div></noscript></div></div><script>(function(){window._cf_chl_opt = {cFPWv: 'g',cH: 'VBUdb.B7HfV4qs2xiLh1apWvIu40igAVZeDMKg8WbwI-1793572296-1.2.1.1-NuJUBV5xQFRNlPv6BnclHfs1rADNMARHfKMtCoOek86yweHVwScz7ykmLUzPJUiE',cITimeS: '1793572296',cRay: 'a53e59c4b95db210',cTplC:1,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:\"/backend-api/product-account-links/mcp?__cf_chl_tk=lBpylW4sdGCCInlsGXb3lWakpGHfFAWChDvv5KFE_2w-1793572296-1.0.1.1-JDvj7wOZEnfEl.bY6aoiEvUqCExSztpe51_kePEBDW0\",cvId: '3',cZone: 'chatgpt.com',fa:\"/backend-api/product-account-links/mcp?__cf_chl_f_tk=lBpylW4sdGCCInlsGXb3lWakpGHfFAWChDvv5KFE_2w-1793572296-1.0.1.1-JDvj7wOZEnfEl.bY6aoiEvUqCExSztpe51_kePEBDW0\",md: 'SqhQFfnvQBh_AXFK_NiOyC9zFOwpv.E.oqoXMNpQpvc-1793572296-1.2.1.1-ldlOk59LB.EQl.uBGBvi2TFTYADuOndDfS_OMdScuUiXRew9.J6jK.27Q8Elf9RLfBqLOzntOuw0thTdmiGMV6Pl9JDEU869MjLnr2A5vlH9HAi4fcJHjljqOILm.wecjJu1zf_HUz6PGzCYVGMPYZJQ5SCv54BKcHHWvdGJeF.2vU2MJSD2DxZuDJw5Cmf8b9jWa6dncXeeuX4OCio9yiirto0pbTZ_jTuIiMkK7F3Yglc6e2UoBcksomGsJ6bWsViBxNEoGLj4SxwHpSU9Ddx_1mYepW8Qb6NOK9mLaOhjV7ibQEaXkD6R4WVaSs2ecs03EzJ1IDHlCMTZflaCIsBB9usi1qFrZSxvQ1l14C9noSSVhwqqYjzF2XKEPeEXaW3ybfAyjfzE6mEsQ.Afqe8PvRXtzl3ssYg7VR9LiA3535FmSUafTBGkGyZc37M9qKk7eg7SuQXwgVgzknc0PVnP6sTpOcYBDzec5Y1AOg.MwAntrK_IHpt8vMsYWgwBrhXsyk12MPVrkSUJIznLgkbCRJA8HmfAedq3e_toLlw1XP1RcNfhaAQ7SaSYHwQWwfVhM7sgfzjwFvwRB7H96HluulAdViPrupmAHOaLn5KwkoQbhFPLypm16ghCvkqV83BYN8wz1HBtJKzFe9JB2NTsB744IwTRBfQd7eAimYtcg9FgoMRxOZOjQ8MHbhCvGcSt9Ow36FHR6fRrZVNI6DVz4R84YLh.P5l9q6oYg_8flCBkwfV9LodVsyzC7X2mhfEphSLNX6TUTd8cy.f8MN9fLmRrrSu1IW79OOnbEK6nI0P5G._QnthaXEMEcaUkAGZCYO4ObkON8.VaWAB28kCPTbZVmj3xA_r1PwFcVqH9dHTqnO2S5EDDK0cJqtoiT0xPl.KQcZ.VWkd7iZkW0Ha1Ad_uPcxMMyuv1pw0M2c4h5BnDAx.ssXfMl38ey0dXb3TnOrQpN.rEFDQBOLMoDlhvpDFpN.8b9oBWOcfbQhGy8JUzSAPP1PUBd4JdchKLY.CCIVeObTMFbBeGZyIxUmB3B8G_g1815bcEN1qThBdob.avpePZt.yvUHCIpe2Z4LAYrPlu3QVpvIn22pH7XLcLrwqG8jv9kLBPtVvF0ndjTZIof36F1VMeF1vQwoJ6dHn.qlFUhqUsicozyYkug',mdrd: 'g6vfXF.czYuWKAEv2UeUVicZS71dM_xVqFStBgZP7dI-1793572296-1.2.1.1-JNLs7S_IU0WAvRhAPtMA_7WdPY0KewUmqqYpIt36FkQddsetP1xxfwTznaSczpD48I4yQMQvCMZOcQM7F.s5ffrpkzxz7v51qzHCIayU.kUQu5bq_tUCyJhHOPDs7wKovwNglsy2oG3w6uiJaspmRTNpDnCdnVCWpqFwwiyhGyXVbeqRC3A0AQ9PVoX7RDu7AfaE7mcK77HGddK9MGQk5QBDocls3EcscZt2WA2UA0d_EYuPgU9Bu7tdE0YMtr2XNWCyMDTBJmXJQIqv6_F.RmHaEGRqyaRD1NpAekAWGK7O2kH7rI6XK9HHAAPXyiWwmCutKVCAHu1seuLsseR4C9yk69gXKishl3M7g5XE1brUyARwYMIoQnJxVti31jOU9OttenBo2N1LdFjboh2XgRgL1LgsBykds0CxrWb.ko5YOVdopz5q.o9loPG5J3aqbBEuLczXAmPHRGX.s3pj1m4l1ekZdQ49pypt_mc6Abx0cvPIRUP.95DoGZ5llSJ3pbS138ynxX9B9nBoaX4FWBF0FxVG8Pg8MNrITxfMIfjfyDiArCoW88AjgEj9WxyyVPmoKCqYkqJC84_zA8NI99o9.Z04AbrUihPk_Y4SRPfXV3IlMc6cNChtcLgT_55UGS8tCT6.9gJKTUzeqccCls6jA.Aim_PinmOZW_vph9GVWwhTSJtTLsqfPg1lnQIKN4kpZ1WCTIOgLRm40T3ZiYWAC_cCEt9fzbJ1lxfZhfZxRffrS70YkaBM... (truncated 2376 bytes)")
2026-11-01T22:31:35.699368Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when AuthRequired(AuthRequiredError { www_authenticate_header: "Bearer resource_metadata=\"https://codex-app.tldraw.xyz/.well-known/oauth-protected-resource/mcp\", scope=\"openid profile email offline_access\"" })
2026-11-01T22:31:35.940209Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when AuthRequired(AuthRequiredError { www_authenticate_header: "Bearer resource_metadata=\"https://mcp.consensus.app/.well-known/oauth-protected-resource\", scope=\"search\"" })
2026-11-01T22:31:38.318804Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=OAuth tokens for server valency cannot be refreshed; authorization required
codex
Ön kayıt, hesap kodu ve ham PBE çıktısını salt okunur denetleyeceğim; iki işaret yorumunu ve makaledeki aktarım iddiasını ayrı değerlendireceğim.

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "rg -n \"H-iso|hiso|AI driven Science\" C:\\Users\\can02\\.codex\\memories\\MEMORY.md" in C:\Users\can02\Projects\AI driven Science
 succeeded in 784ms:
1:# Task Group: AI driven Science alloy-energy and elasticity claim audit
3:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=read `.orchestra/LESSONS.md`, inspect the live ledger/data/scripts, keep `data/sealed/` unread unless the current workflow explicitly authorizes the arena, and treat all historical numerical claims as checkout-specific.
9:- rollout_summaries/2026-10-31T21-44-08-GISz-emix_random_vec_filling_candidate_and_sro_diagnostics.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8677-7d23-8736-9feecdd1a527.jsonl, updated_at=2026-10-31T11:15:16+00:00, thread_id=01a193eb-8677-7d23-8736-9feecdd1a527, strongest candidate not sealed-tested)
10:- rollout_summaries/2026-10-31T21-44-08-Qzmv-k_volume_transfer_anharmonicity_and_triplet_candidates.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-865c-74c3-b444-bb194b9c0aaf.jsonl, updated_at=2026-10-31T11:15:22+00:00, thread_id=01a193eb-865c-74c3-b444-bb194b9c0aaf, physical interpretation remains unresolved)
11:- rollout_summaries/2026-10-31T09-44-10-dWvd-emix_random_target_artifact_and_candidate_analysis.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\31\rollout-2026-10-31T12-44-10-01a19158-6021-7482-9551-9958d2b1cbff.jsonl, updated_at=2026-10-31T07:44:28+00:00, thread_id=01a19158-6021-7482-9551-9958d2b1cbff, establishes generator bookkeeping error)
21:- rollout_summaries/2026-10-31T21-44-08-tMXk-audit_holdout_accounting_pbe_kmesh_and_l2_parent_errors.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8694-7b63-8ed9-478e5ea983e6.jsonl, updated_at=2026-10-31T11:13:12+00:00, thread_id=01a193eb-8694-7b63-8ed9-478e5ea983e6, three substantive issues)
22:- rollout_summaries/2026-10-31T21-44-08-bz70-audit_stale_derived_columns_composition_correction_zener_ani.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8606-7342-88b7-c496909afa26.jsonl, updated_at=2026-10-31T11:34:50+00:00, thread_id=01a193eb-8606-7342-88b7-c496909afa26, corrected-data audit)
23:- rollout_summaries/2026-10-31T21-44-08-3Ad3-silver_anomalies_mechanism_and_cutoff_error.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8654-7ab2-83f8-79124f513e41.jsonl, updated_at=2026-10-31T11:18:57+00:00, thread_id=01a193eb-8654-7ab2-83f8-79124f513e41, Ag mechanism partly unverified)
24:- rollout_summaries/2026-10-31T21-44-08-0sbZ-audit_ag_anomaly_claims_cutoff_kgrid_mechanism.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-85ea-7283-8340-585074438f97.jsonl, updated_at=2026-10-31T11:36:25+00:00, thread_id=01a193eb-85ea-7283-8340-585074438f97, controls corrected but reruns pending)
25:- rollout_summaries/2026-10-31T21-44-07-ik6S-cobalt_anomaly_mace_pbe_discriminator.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-835c-7861-9fb8-803628c6364a.jsonl, updated_at=2026-10-31T21:43:57+00:00, thread_id=01a193eb-835c-7861-9fb8-803628c6364a, diagnostic incomplete)
40:- For DFT finite differences, pin every strain partner to the unstrained k-mesh, use same-size/alloy-matched references and `ecut_elements`, then rerun property-specific controls. `scripts/hiso_l12_v2.py` implements shared cutoffs/fixed grids; old H-iso results remain non-evidential until rerun. [Task 2]
47:- Treat Ag shear/electronic mechanisms as hypotheses: cutoff mismatch and strain-dependent k-grid are real control failures but do not explain the anomaly; re-run corrected H-iso data before physical interpretation. Equal additive K44/K' corrections do not preserve Zener anisotropy. [Task 2]
368:# Task Group: AI driven Science HEA mechanical-discovery harness and bcc L3 validation
370:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=checkout-specific: inspect the current harness, environment, ledger, logs, and benchmark state before rerunning or claiming L3 validation.
376:- rollout_summaries/2026-10-29T17-19-34-Vft1-hea_mechanical_harness_qe_bcc_l3_validation.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\29\rollout-2026-10-29T20-19-34-01a188ac-952b-78c0-9f69-56055f0d602b.jsonl, updated_at=2026-10-28T09:38:53+00:00, thread_id=01a188ac-952b-78c0-9f69-56055f0d602b, fcc harness calibrated; bcc benchmark incomplete)
1137:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=use for project direction and first-vertical-slice planning only; confirm scope, active environment, provider choice, and real-data access before implementation or scientific claims.
1143:- rollout_summaries/2026-10-26T03-00-46-pz1h-metalurji_ai_co_scientist_anomali_avciligi_ksenometalurji.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\26\rollout-2026-10-26T06-00-46-01a17627-4307-7952-bd84-33be35351bd3.jsonl, updated_at=2026-10-25T16:45:57+00:00, thread_id=01a17627-4307-7952-bd84-33be35351bd3, architecture/planning only)

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Content C:\\Users\\can02\\.codex\\skills\\scientific-result-audit\\SKILL.md; Get-Item CODEX_START.md,STATUS.md -ErrorAction SilentlyContinue | Select-Object Name,Length" in C:\Users\can02\Projects\AI driven Science
 exited 1 in 523ms:
---
name: scientific-result-audit
description: "Bilimsel deney/simǬlasyon sonu��lar��n��n iddialarla, ham ����kt��yla ve kabul ��l��Ǭtleriyle tutarl��l��Y��n�� denetle; sonu�� kontrolǬ, deney raporu veya makaledeki say��sal iddialar��n do�Yrulanmas�� istendi�Yinde kullan. Genel literatǬr ara�Yt��rmas�� i��in kullanma."
---

# Bilimsel sonu�� denetimi

�Ŏ�kt��: iddia, dayanak dosya/sat��r veya tablo, ��l��Ǭt, ger��ek sonu�� ve karar. Yaln��z gerekli sat��rlar�� g��ster; PASS, FAIL, SKIPPED, UNAVAILABLE ve UNVALIDATED ayr��m��n�� koru.

1. ��lgili projenin kendi klas��rǬnde AGENTS, aktif karar ve gǬncel sonu�� durumunu oku. AKOR'da freeze/telemetry/Ǭcretli ��a�Yr�� s��n��rlar��; IsoShift'te START, DECISION, state/LEDGER ve tamamlanm��Y sonu�� JSON'u; Metalliksa'da STATUS, RULES ve ilgili fizik s��zle�Ymesi belirleyicidir.
2. Sonu�� dosyas��, girdi hash'i, kod/commit, y��ntem, birimler, ��rneklem, belirsizlik ve ��nceden tan��mlanm��Y kabul ��l��ǬtǬnǬ e�Yle�Ytir. Eksik olan�� a����k b��rak. Logdaki ilerleme veya sǬre�� ����k��Y�� tek ba�Y��na bilimsel ba�Yar�� kan��t�� de�Yildir.
3. ��ddia edilen say��lar�� mevcut ham kaynaktan yeniden hesapla; ba�Y��ms��z beklenen de�Yer kullan. �-l��Ǭlen, hesaplanan, tahmini, sentetik ve literatǬrden al��nan de�Yerleri ay��r. Sentetik kontrol deneysel validasyon say��lmaz.
4. Ba�Yar��s��z ��nkay��tl�� testi sonradan ge��en test olarak sunma; de�Yi�Yen y��ntem/��l��Ǭt i��in yeni sǬrǬm ve a����k gerek��e gerekir. Tarihsel model sonu��lar��n�� farkl�� modelin gǬncel ��l��ǬmǬyle birle�Ytirme. AKOR'da cache, reasoning, ba�Yar��s��z ��a�Yr�� ve retry tǬketimini bildir; batching etkisiyle format etkisini ay��r.
5. GPU/production ��al��Ymas�� veya model ��a�Yr��s��n�� yeniden ba�Ylatmak yerine ��nce var olan sonu��lar�� denetle. Ek ��al��Yt��rma gerekiyorsa proje yetkisini ve maliyet s��n��r��n�� kontrol et. IsoShift Ǭretim y��ntemini denetim s��ras��nda de�Yi�Ytirme.
6. Makale incelemesi istenmi�Yse mevcut ARS academic-research-suite ak��Y��n�� kullan; bu skill say��sal kan��t katman��n�� sa�Ylar. Al��nt��, denklem veya �Yekli ��zgǬn kaynakta do�Yrula; eksik at��f uydurma. Nitel ��nceki ��al��Ymayla projenin nicel katk��s��n�� ayr�� ifade et.

Sonu�� dosyas��n�� dǬzeltme talebi yoksa audit salt okunurdur. Kapan��Yta do�Yrulanan��, iddiay�� s��n��rlayan hatay�� ve tek somut sonraki ad��m�� bildir.

Name      Length
----      ------
STATUS.md   7105



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "@'
from pathlib import Path
paths=['AGENTS.md','STATUS.md','.orchestra/LESSONS.md','scripts/hiso_l12_v2.py','data/hiso_l12_dft_v2.csv','data/hiso_l12_mace.csv']
for f in paths:
 p=Path(f)
 if p.exists():
  print('\\nFILE',f)
  for i,l in enumerate(p.read_text(encoding='utf-8').splitlines(),1): print(f'{i}: {l}')
'@ | python -X utf8 -" in C:\Users\can02\Projects\AI driven Science
 exited 1 in 5845ms:
python : The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
 the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:10 char:6
+ '@ | python -X utf8 -
+      ~~~~~~
    + CategoryInfo          : ObjectNotFound: (python:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "rg -n \"6cb3c2a936|H-iso|hiso|K.prime|transfer|K′|K'\" claims/claims.jsonl paper/draft_v3.md; Get-Content harness/dft.py -Encoding utf8" in C:\Users\can02\Projects\AI driven Science
 succeeded in 490ms:
paper/draft_v3.md:1:# Binary shear curvatures read at the alloy's volume: a preregistered test of a transfer rule for fcc solid solutions with machine-learned potentials
paper/draft_v3.md:13:one specific, fixed-coefficient prescription for the clamped mixing part of the tetragonal shear curvature K' of
paper/draft_v3.md:17:1.9 GPa on 94 compositions; 4.8 to 2.2 GPa on 1200 further compositions under a second MACE model). The transfer is
paper/draft_v3.md:34:   including binary and ternary data. These studies motivate testing how shear transfers from simpler systems.
paper/draft_v3.md:38:   identify the specific fixed-coefficient transfer tested here: clamped multicomponent mixing K' estimated from
paper/draft_v3.md:45:   target representation of an ML model while keeping the model. Here the target stays K'_mix; what changes is the
paper/draft_v3.md:55:deformation F. K' from F = diag(e^t, e^-t, 1), K44 from F = I + g e_x e_y, five amplitudes in [-0.01, 0.01],
paper/draft_v3.md:56:quadratic fit, K' = c2/(2V), K44 = 2 c2/V. The target generators use the cell's actual integer-count fractions for
paper/draft_v3.md:58:mixing stress and Green-Lagrange energy coefficients, K44 = C^L_xyxy + s_yy and K' = (C^L_xxxx + C^L_yyyy -
paper/draft_v3.md:66:**Rule.** K'_mix(alloy) = sum_{i<j} 4 x_i x_j K'_ij(ln V0/V_ij). Baselines: the same sum at ln V0/V_ij = 0 ("pair at
paper/draft_v3.md:74:checks kept the K' improvement (gain 0.55 to 0.58, k 1.07 to 1.10) but showed sensitivity for K44.
paper/draft_v3.md:97:**3.1 Exploration (historical, a2).** On 62 ternary to quinary alloys used for exploration, K' RMSE 5.67 to 1.80 GPa,
paper/draft_v3.md:103:shear targets only. K': 4.77 to 2.03 GPa, gain 0.57, p 2.5e-4, k 1.08. The registered claim was joint (K44 and K'); it
paper/draft_v3.md:104:failed on K44 (p 0.023, 6e0923b413), so K' got a fresh test rather than a post-hoc split.
paper/draft_v3.md:106:**3.3 Fresh preregistered K' test (hm_fresh, 94 compositions, prereg 67a358fc59).** K': 4.22 to 1.89 GPa, gain 0.55,
paper/draft_v3.md:112:energy-consistent reference conversion that transfers V·K before dividing by the target volume; its errors are 4.49
paper/draft_v3.md:115:full fitted CALPHAD model of Marker et al. For the mixing energy, the earlier linearised k = 1 transfer gives 13.3
paper/draft_v3.md:118:or h3. K' differs from the energy because the binary curvatures change steeply with volume: at the binary Vegard
paper/draft_v3.md:119:volume the median dln|K'|/dlnV is -3.16 over the 12 pairs with |K'| > 10 GPa.
paper/draft_v3.md:133:under-prediction at large size mismatch: the pair transfer captures most of the volume effect but not all of it.
paper/draft_v3.md:140:  excluding them keeps the PASS with gain 0.467): the difference A = K44 - K' follows the rule (gain 0.49), the
paper/draft_v3.md:144:  correlates with the K' residual of the other (r 0.75; same cell 0.79), k 0.92, b 0.95.
paper/draft_v3.md:149:The diagnostic regression is K44 - pair44 ≈ k T44 + b (K' - rule'), with T44 = rule44 - pair44. Because the second
paper/draft_v3.md:150:covariate contains a measured K' target, this is a residual association, not a predictor of K44 from binary inputs
paper/draft_v3.md:174:   K44 = -32.4 GPa in PBE and +3.2 GPa in MACE; sign agreement is 8/8 for K' and 5/8 for K44. This does not validate
paper/draft_v3.md:175:   transfer to random alloys. An L3 test needs at least 15 independent DFT or experimental rows from composition
paper/draft_v3.md:177:2. Clamped, unrelaxed cells: K'_mix is not the measured C'. On 43 previously examined equiatomic ternaries, relaxed-
paper/draft_v3.md:178:   binary Muggianu gives C' RMSE 3.08 GPa and a volume-transfer chain 2.53 GPa (gain 0.18, p about 0.08). The chain
claims/claims.jsonl:20:{"id": "24add7fc3f", "time": "2026-10-30T23:22:48", "level": "L0", "claim": "H-iso (claude, from interim look at 24 rows): the clamped mixing shear curvature is isotropic when large, K44 ~= Kp, i.e. chemical mixing does not change the Zener anisotropy, contrary to the central NN closure (A2) which predicts K44/Kp != 1. Test on a2_shear_clamped rows NOT listed in data/a2_seen_interim.txt, restricted to max(|K44|,|Kp|) > 10 GPa. PASS iff n >= 15, Pearson r(K44,Kp) > 0.9 and median |K44-Kp|/mean(|K44|,|Kp|) < 0.3.", "parent": null, "evidence": {"data/a2_seen_interim.txt": "ef7353296efbeb16"}, "notes": "registered after seeing 24 of 160 rows; those 24 are excluded from the test"}
claims/claims.jsonl:21:{"id": "bca6a70915", "time": "2026-10-30T23:30:02", "level": "L0", "claim": "H-sm (Astra): second-moment band energy with dd hopping r^-5 predicts clamped mixing shear ratio K44/Kp = 2(p-2)/(p-6) = 4 (p=10), filling independent; competing with H-iso (ratio 1, 24add7fc3f). Same test rows as H-iso (a2_shear_clamped minus data/a2_seen_interim.txt, max(|K44|,|Kp|) > 10 GPa). PASS iff n >= 15 and median K44/Kp over rows with same sign in [3, 5] and >= 60% of rows same sign. Secondary (Astra conjecture): median d=|K44-Kp|/max larger for Ag-Rh, Au-Ir, Al-Ni, Al-Co containing alloys than for Pd-Pt, Ag-Au.", "parent": null, "evidence": {".orchestra/astra_iso.md": "f07c471b8eca7748"}, "notes": "pre-registered before unseen A2 rows were examined"}
claims/claims.jsonl:25:{"id": "6560a94ce0", "time": "2026-10-30T23:38:56", "level": "L0", "claim": "HM2 on second holdout data/hm_fresh_rows.csv (seed 2027, 3 SQS seeds averaged, not read by anyone). Delta = E_mix - sum_{i<j} x_i x_j W_ij (W from h1 equiatomic binaries). T1 (Astra, zero coefficient): volume transfer pred_vol = sum_{i<j} 4 x_i x_j (dE_mix/dlnV)_ij ln(V0/V_ij), (dE/dlnV)_ij from h1 equiatomic binary rows, V_ij = binary Vegard volume; PASS iff on n_el>=3 rows RMSE(Delta - pred_vol) <= 0.9*RMSE(Delta) and <= 0.9*RMSE(Delta - c_n) with frozen c_n = 5.915/19.090/28.691 meV for n=3/4/5. T2 (claude): residual R = Delta - pred_vol has positive mean on n_el>=3 rows, 99% bootstrap CI (2000, seed 0) lower bound > 0, i.e. a fixed-volume beyond-pair excess exists. T3: Astra frozen formula 2.1038*sum x_i x_j W_ij[(V_ij/V0)^(5/3)-1] with its criterion (astra_hm2.md).", "parent": null, "evidence": {".orchestra/astra_hm2.md": "ef51865cf818059b"}, "notes": "registered while hm_fresh is being generated; nobody has read it"}
claims/claims.jsonl:27:{"id": "dfadd8f7a7", "time": "2026-10-31T00:33:28", "level": "L0", "claim": "HM2-T4 Opus volume transfer on second holdout: fails (RMSE 15.0 vs limit 22.4, r 0.93, k CI [0.80,0.95])", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\hm2_test_rows.csv": "08727b809698a5e0"}, "notes": "criteria fixed in d6da56412c"}
claims/claims.jsonl:28:{"id": "32c7352c10", "time": "2026-10-31T00:33:28", "level": "L0", "claim": "HM2 on second holdout (n=94): T1 volume transfer passes (RMSE 37.5 -> 17.6 meV); T2 fixed-volume residual fails (mean -5.8, 99% CI [-10.1, -1.6]); T3 Astra passes", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\hm2_test_rows.csv": "08727b809698a5e0"}, "notes": "criteria fixed in 6560a94ce0"}
claims/claims.jsonl:29:{"id": "05f01df6ec", "time": "2026-10-31T00:34:23", "level": "L2", "claim": "Zero-parameter volume-transfer rule for multicomponent mixing energy: E_mix ~= sum_{i<j} x_i x_j [W_ij + 4 (dE_mix/dlnV)_ij ln(V0/V_ij)], binary inputs only (50:50 E_mix and its log-volume slope at the binary Vegard volume V_ij), V0 alloy Vegard volume. Clamped random fcc, MACE omat. Two holdouts pooled, n=207: RMSE 32.9 -> 17.6 meV/atom, gain 0.46, within-n permutation p 5.0e-05. The apparent positive multicomponent excess (HM) is this volume transfer; no fixed-volume many-body excess remains in random alloys (HM2-T2 failed).", "parent": "4c5076a083", "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\hm_l2_rows.csv": "49445ab791089e25"}, "notes": "parent L1 4c5076a083; pre-registered 6560a94ce0"}
claims/claims.jsonl:30:{"id": "6192ffda51", "time": "2026-10-31T00:35:52", "level": "L0", "claim": "L3 criteria for the volume-transfer rule (scripts/l3_transfer.py dft, 12 ABCD + 4 ABCC ordered 4-atom cells, families absent from all MACE data, PBE kspacing 0.15). y = E_mix(cell, V0) - naive (pairs at own binary Vegard volumes); term T = rule - naive = sum_bonds (dV_ij/dlnV) ln(V0/V_ij). PASS iff n >= 15, and with coefficient fixed at 1: RMSE(y - T - mean(y - T)) <= 0.9 * RMSE(y - mean(y)) (gain over intercept-only), and refit OLS y = c + k T gives 95% bootstrap CI (2000, seed 0) of k excluding 0 and inside [0.5, 2]. MACE run reported alongside as L1 consistency, not part of the gate.", "parent": null, "evidence": {"scripts/l3_transfer.py": "de8c7fc3e93eb33d"}, "notes": "registered before any l3_transfer output; quaternaries chosen by input volume spread only"}
claims/claims.jsonl:32:{"id": "ef4398f59a", "time": "2026-10-31T01:08:20", "level": "L0", "claim": "H-iso test: survives (n=60, r 0.95, median rel diff 0.20); H-sm: falsified (median ratio 1.05)", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\a2_shear_clamped.csv": "030ddff29fb49521"}, "notes": "criteria fixed in 24add7fc3f and bca6a70915; 24 interim rows excluded"}
claims/claims.jsonl:33:{"id": "6cb3c2a936", "time": "2026-10-31T01:09:25", "level": "L0", "claim": "H-iso PBE check (scripts/hiso_l12.py): cubic A3B L1_2 cells (Cu3Ir Au3Ir Ag3Ir Cu3Rh Ag3Rh Pd3Ir; controls Cu3Au Pt3Cu), clamped Vegard volume, pure refs same V and F, strain 0.02, PBE kspacing 0.10. H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.", "parent": null, "evidence": {"scripts/hiso_l12.py": "c76da785e56fb704"}, "notes": "registered before any hiso_l12 output; H-iso survived on MACE random alloys (n=60, r 0.95, also after removing the -P stress term)"}
claims/claims.jsonl:37:{"id": "0e4de24475", "time": "2026-10-31T06:55:33", "level": "L0", "claim": "L3 test of volume-transfer rule in 16 PBE ordered cells: fail (gain -0.03 over intercept-only, refit k 0.46 CI [0.03, 1.00], raw RMSE naive 35.3 -> rule 26.0 meV)", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\l3_transfer_dft.csv": "8d47ae7b07d95c65"}, "notes": "criteria fixed in 6192ffda51"}
claims/claims.jsonl:42:{"id": "337130e2ec", "time": "2026-10-31T09:37:11", "level": "L0", "claim": "verdict on 6192ffda51: L3 ordered cells fail", "parent": null, "evidence": {"data/l3_transfer_dft.csv": "8d47ae7b07d95c65", "scripts/power_retro.py": "0df3f8519efda0f3"}, "notes": "cause=design; audit: blind subagent: no coding bug, 16 rows reproduced from pw.out; intercept absorbs rule's common shift (mean T 31.7 vs sd 21.5 meV); retro power 0.375 at k=0.8 (scripts/power_retro.py); cutoff mismatch pending (scripts/ecut_bias.py)"}
claims/claims.jsonl:46:{"id": "a4cf2d5f62", "time": "2026-10-31T09:37:11", "level": "L0", "claim": "Transfer coefficient of the volume-transfer rule is k = 0.79 (IV, pooled n=207, 95% CI [0.73, 0.84]), stable across both holdouts (0.78, 0.79) and not explained by configurational noise in binary inputs (sd of dE/dlnV 10 meV vs 535 meV spread). Exploratory on used holdouts; a third holdout is needed before any k is claimed.", "parent": null, "evidence": {"data/binary_seeds.csv": "6b4675478ad5815b", "scripts/k_dilution.py": "a2439e2cc22439db"}, "notes": "diagnostic, not promotion"}
claims/claims.jsonl:48:{"id": "484fd5e712", "time": "2026-10-31T11:02:45", "level": "L0", "claim": "Cutoff-corrected PBE re-analysis (pure references at the alloy's cutoff): (1) L1 E_mix(V) pass (signs True, n_eff True, split 7/7); (2) L1 ordered Delta pass (sign 9/10, MAE 7.0, r 0.80; PBE quaternary mean +12.9 meV); (3) L3 ordered transfer fail (k 0.52 [0.08, 1.06])", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\l10_ev_dft_ecutfix.csv": "862387136ebae777", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\hm_ordered_dft_ecutfix.csv": "b463539867f95f19", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\l3_transfer_dft_ecutfix.csv": "a323de025123ded8", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\ecut_shift_table.csv": "a4fd8ace90e6fe3f"}, "notes": "criteria e5425db058, 7e0022b375, 6192ffda51 unchanged; numerics correction found by blind audit"}
claims/claims.jsonl:51:{"id": "8541e914ea", "time": "2026-10-31T11:03:42", "level": "L0", "claim": "verdict on 6192ffda51: L3 ordered cells: FAIL confirmed after cutoff correction (k 0.52 [0.08, 1.06])", "parent": null, "evidence": {"data/l3_transfer_dft_ecutfix.csv": "a323de025123ded8"}, "notes": "cause=design; audit: power 0.375 at k=0.8 (scripts/power_retro.py); proper L3 needs random SQS cells"}
claims/claims.jsonl:54:{"id": "e04c6451e1", "time": "2026-10-31T14:00:00", "level": "L0", "claim": "Direct common-volume control: exact binary transfer gives k_exact 0.94 [0.90, 0.98] (n 269); reading: inconclusive", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\binary_vgrid.csv": "cc81603a811cd9c5", "C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_direct.py": "88675ad955948f80"}, "notes": "diagnostic of champion k; prereg in the note before"}
claims/claims.jsonl:55:{"id": "d26bd71285", "time": "2026-10-31T14:39:35", "level": "L0", "claim": "Correction to 05f01df6ec and a4cf2d5f62 (swarm S1 audit, Opus; checked by Astra): only hm_fresh (n=94) was unseen when the volume-transfer rule was chosen; h3 (n=113) was used for model selection. On the truly unseen hm_fresh rows alone: 36.4 -> 13.1 meV, gain 0.64, k_ols 0.81, permutation p ~5e-5. The L2 verdict stands; 'two independent holdouts, n=207' is withdrawn.", "parent": null, "evidence": {".orchestra/swarm/S1/audit/opus.md": "472c1c783aa53cb3", "data/hm_l2_rows_fixed.csv": "7b2aaadc267c00ca"}, "notes": "erratum; parent 05f01df6ec"}
claims/claims.jsonl:58:{"id": "b363c5a618", "time": "2026-10-31T19:07:37", "level": "L0", "claim": "Design note, shear-curvature transfer: first design (sigma 4 GPa = pair-sum residual on exploratory a2 rows) had power 0.45 and was not registered; no h3 target computed. Exploratory a2 (n 62, seen): K44 pair 3.56 -> rule 2.66 GPa, Kp 5.67 -> 1.80, refit k 0.90 / 1.05. Redesign: sigma = rule residual on a2 {'K44': 2.6555154158509033, 'Kp': 1.800235411977806}, the arena convention", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_shear_transfer.py": "e7578efc4258544d", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\binary_kgrid.csv": "29a7aeffb5f8b9eb"}, "notes": "design; before registration"}
claims/claims.jsonl:59:{"id": "4c29d9754c", "time": "2026-10-31T19:07:46", "level": "L0", "claim": "Shear-curvature volume transfer: clamped mixing K44 and K' of random fcc alloys equal sum 4 x_i x_j K_ij(V0) with binary curvatures at the alloy volume (no parameter); PASS if in both channels RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005 on 113 h3_fresh alloys whose K has never been computed", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_shear_transfer.py": "e7578efc4258544d"}, "notes": "prereg; power {'power': np.float64(0.97), 'false_pass': np.float64(0.0)}; proposed by Opus in swarm S1 (open front), critiqued by Astra; binaries computed first"}
claims/claims.jsonl:60:{"id": "6e0923b413", "time": "2026-10-31T19:31:12", "level": "L0", "claim": "Shear-curvature volume transfer: FAIL on 113 unseen h3 alloys (K44 fail, Kp pass); binary slope prior {'K44': (14, -2.340508727571272), 'Kp': (12, -3.159947091704939)}", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\binary_kgrid.csv": "29a7aeffb5f8b9eb", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\h3_shear_clamped.csv": "6409bc344ff2f12a", "C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_shear_transfer.py": "e7578efc4258544d"}, "notes": "prereg 4c29d9754c"}
claims/claims.jsonl:61:{"id": "67a358fc59", "time": "2026-10-31T19:38:57", "level": "L0", "claim": "Shear-curvature volume transfer, K' channel: clamped mixing K' of random fcc alloys equals sum 4 x_i x_j K'_ij(V0) with binary curvatures at the alloy volume (no parameter); PASS if RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005 on 94 hm_fresh alloys whose shear has never been computed", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_shear_kp_hm.py": "897cdd9d1de16dfe"}, "notes": "prereg; power {'power': np.float64(1.0), 'false_pass': np.float64(0.0)}; fresh test after joint claim 4c29d9754c failed on K44 only (6e0923b413)"}
claims/claims.jsonl:62:{"id": "d92844787f", "time": "2026-10-31T19:56:03", "level": "L0", "claim": "Shear-curvature volume transfer, K' channel: PASS on 94 unseen hm_fresh alloys; K44 reported, not gated: fail", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\hm_shear_clamped.csv": "1bd3a3ff0d05986a", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\binary_kgrid.csv": "29a7aeffb5f8b9eb", "C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_shear_kp_hm.py": "897cdd9d1de16dfe"}, "notes": "prereg 67a358fc59"}
claims/claims.jsonl:63:{"id": "697c2d6d75", "time": "2026-10-31T19:56:30", "level": "L2", "claim": "Shear-curvature volume transfer, K' channel (medium-omat-0, clamped random fcc, 3 to 5 components): the mixing tetragonal shear curvature equals sum 4 x_i x_j K'_ij(V0), the 50:50 binary curvatures taken at the alloy's Vegard volume, with no fitted parameter. Blind pre-registered test 67a358fc59 on 94 alloys never computed before: RMSE 4.22 -> 1.89 GPa vs binaries at their own volume, gain 0.55, sign-flip p 2.5e-4 (resolution limit), free refit k 1.08, rule better in 75/94. Replicates the h3 channel result (113 alloys, gain 0.57, k 1.08; joint claim 4c29d9754c failed on K44). K44 does not pass (gain 0.12 to 0.20, k 0.69 to 0.86). Open before L3: MACE shear bias at L1, Co-rich outliers, PBE check.", "parent": "e5ef5a57a3", "evidence": {"data/hm_shear_clamped.csv": "1bd3a3ff0d05986a", "data/h3_shear_clamped.csv": "6409bc344ff2f12a", "data/binary_kgrid.csv": "29a7aeffb5f8b9eb", "scripts/k_shear_kp_hm.py": "897cdd9d1de16dfe", "scripts/k_shear_transfer.py": "2b30f66ccf93f57a"}, "notes": "blind result d92844787f; prereg 67a358fc59"}
claims/claims.jsonl:64:{"id": "851aec6883", "time": "2026-10-31T20:21:54", "level": "L0", "claim": "Model swap, K' volume transfer (prereg, before any mpa curvature exists): redo binaries and the 94 hm_fresh alloys with medium-mpa-0 (fcc C' bias -11% vs omat ~0); survives if K' RMSE(rule) <= 0.9 pair-at-V_ij, sign-flip p < 0.005 and bootstrap 95% CI of refit k contains 1", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_shear_mpa.py": "01ecb5fd85f205a2"}, "notes": "prereg; robustness of 697c2d6d75"}
claims/claims.jsonl:65:{"id": "86767e478d", "time": "2026-10-31T22:02:31", "level": "L0", "claim": "Model swap, K' volume transfer: K' FAILS under medium-mpa-0 on 94 hm_fresh alloys (K44 not gated: fail)", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\binary_kgrid_mpa.csv": "92160b8d1d1c00bc", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\hm_shear_clamped_mpa.csv": "fe3eb0ee95e62ddc", "C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_shear_mpa.py": "01ecb5fd85f205a2"}, "notes": "robustness of 697c2d6d75; prereg in the entry before"}
claims/claims.jsonl:66:{"id": "e410c96a32", "time": "2026-10-31T22:37:26", "level": "L0", "claim": "K44 volume transfer without Co: clamped mixing K44 of Co-free random fcc alloys equals sum 4 x_i x_j K44_ij(V0) with binary curvatures at the alloy volume (no parameter); PASS if RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005 on 120 fresh random Co-free alloys; 60 Co >= 15% alloys reported, not gated", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k44_cofree.py": "e5b20e7e30af396d"}, "notes": "prereg; power {'power': np.float64(1.0), 'false_pass': np.float64(0.0)}; hypothesis: K44 failure (LESSONS 14-16) is a Co effect; exploratory hint from seen rows"}
claims/claims.jsonl:67:{"id": "d9460850ce", "time": "2026-10-31T23:36:29", "level": "L0", "claim": "K44 volume transfer without Co: PASS on 120 fresh Co-free alloys; not gated: Co K44 fail, Co-free Kp pass, Co Kp pass", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\k44_cofree_clamped.csv": "1d060c8fae3465dd", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\binary_kgrid.csv": "29a7aeffb5f8b9eb", "C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k44_cofree.py": "e5b20e7e30af396d"}, "notes": "prereg e410c96a32"}
claims/claims.jsonl:68:{"id": "c75e865217", "time": "2026-10-31T23:51:33", "level": "L0", "claim": "Swarm S2 k44 front, Opus blind predictions on the 60 Co alloys of k44_cofree (written 23:04, first Co row 23:22; file timestamp, not a ledger prereg): (a) anisotropy rule A = K44 - K' = sum 4 x_i x_j A_ij(V0): pair 3.40 -> rule 2.08 GPa, gain 0.39, p 1e-3, k 0.83, all predicted ranges met; (b) isotropic floor: corr(e44, e') 0.71, joint fit k 1.00, b 1.05 (predicted k [0.70,1.10], b [0.80,1.25]), plain K44 k 0.71 (predicted <= 0.70), K' k 1.13 (predicted [0.95,1.30])", "parent": null, "evidence": {".orchestra/swarm/S2/k44/opus.md": "5230ce5cf84c5e6f", "data/k44_cofree_clamped.csv": "1d060c8fae3465dd"}, "notes": "blind by timestamp; fresh ledger prereg follows"}
claims/claims.jsonl:69:{"id": "9cfc8edaf0", "time": "2026-10-31T23:53:05", "level": "L0", "claim": "Shared shear floor: in clamped random fcc alloys the volume-transfer pair rule misses a part common to K44 and K'; PASS if on 150 new random alloys (half Co >= 15%) (1) A = K44 - K' rule sum 4 x_i x_j A_ij(V0) has RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005, (2) corr(e44, e') >= 0.5, (3) joint fit K44 - pair44 = k T44 + b e' gives k, b in [0.7, 1.3]", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_aniso_fresh.py": "66b091221a5fd1c6"}, "notes": "prereg; power {'power': 1.0, 'false_pass': 0.0}; Opus swarm S2 k44 front; seen confirmation on k44_cofree Co set (LESSONS 18)"}
claims/claims.jsonl:70:{"id": "42c0fd3ee0", "time": "2026-11-01T00:14:55", "level": "L0", "claim": "verdict on 9cfc8edaf0: WITHDRAWN before any target was read", "parent": null, "evidence": {".orchestra/swarm/S2/audit/opus.md": "d4668748e2d1cc18"}, "notes": "cause=design; audit: Opus swarm S2 audit_1, confirmed by Astra: compute.py:56 permutation depends only on (seed, n), so seed-0 targets share configuration noise with seed-0 binary inputs; this inflates K44 transfer. 44 targets were computed, none read. Re-registered with target seed 100."}
claims/claims.jsonl:71:{"id": "e7d441a4eb", "time": "2026-11-01T00:14:55", "level": "L0", "claim": "Amendment: results d9460850ce (K44 without Co) and the S2 Opus blind check on the Co set used seed-0 targets with splines that include seed-0 binaries (shared-permutation leak, S2 audit_1). K44 numbers there are inflated by about 0.06 to 0.18 in gain; K' is unaffected (same gain for every seed split). Both are superseded by the disjoint-seed test that follows.", "parent": null, "evidence": {".orchestra/swarm/S2/audit/opus.md": "d4668748e2d1cc18"}, "notes": "amendment; leak"}
claims/claims.jsonl:72:{"id": "c2eff007ad", "time": "2026-11-01T00:15:47", "level": "L0", "claim": "Shared shear floor, disjoint seeds: in clamped random fcc alloys the volume-transfer pair rule misses a part common to K44 and K'; PASS if on 150 new random alloys (half Co >= 15%) (1) A = K44 - K' rule sum 4 x_i x_j A_ij(V0) has RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005, (2) corr(e44, e') >= 0.5, (3) joint fit K44 - pair44 = k T44 + b e' gives k, b in [0.7, 1.3]", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_aniso_fresh.py": "e6d0c50bb4d32dc8"}, "notes": "prereg; power {'power': 1.0, 'false_pass': 0.0}; Opus swarm S2 k44 front; seen confirmation on k44_cofree Co set (LESSONS 18)"}
claims/claims.jsonl:73:{"id": "270b2a4019", "time": "2026-11-01T00:18:50", "level": "L0", "claim": "Amendment to L2 05f01df6ec (energy volume transfer), S2 open-front audit by Opus, RMSEs recomputed by Astra: against the standard baseline (Muggianu of binary formation energies, pure elements at their own volumes, converted to the clamped reference) the k=1 rule is not better on any set (h1/h3/hm_fresh RMSE 13.7/13.3/13.3 vs 11.4/11.4/11.5 meV). The binary volume slope is mostly reference strain energy (corr 0.986 with -(1/2) sum de_k/dlnV). Energy rule demoted to known regular-solution extrapolation; not a finding. K' rule 697c2d6d75 passes the same audit: own-volume Muggianu 5.45/5.71/5.41 GPa vs rule 2.03/1.89/1.94 on h3/hm_fresh/a2 (p 5e-5).", "parent": null, "evidence": {".orchestra/swarm/S2/open/opus.md": "cd8383c84f2f873d", ".orchestra/swarm/S2/open/critique_of_opus_by_astra.md": "68c10699a477c328"}, "notes": "amendment; baseline audit"}
claims/claims.jsonl:75:{"id": "fd786169e3", "time": "2026-11-01T01:06:19", "level": "L0", "claim": "Shared shear floor is compositional: the residual shared by K44 and K' (b86e0d8a40) belongs to the composition, not the cell; PASS if on two new cells per composition (unique seeds) for the 150 compositions of b86e0d8a40 the cross-cell corr(e44_a, e'_b) >= 0.5 and the joint fit K44_a - pair44 = k T44 + b e'_b gives k in [0.7, 1.3], b in [0.6, 1.3]", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_floor_cells.py": "c8e3893f1f3df7b1"}, "notes": "prereg; power {'power': 1.0, 'false_pass': 0.0}; Astra audit of b86e0d8a40 (.orchestra/audits/b86e0d8a40_astra.md), finding 2"}
claims/claims.jsonl:76:{"id": "ee7786d744", "time": "2026-11-01T01:06:28", "level": "L0", "claim": "Audit of b86e0d8a40 (Astra, independent; .orchestra/audits/b86e0d8a40_astra.md): PLAUSIBLE. Numbers reproduced (A gain 0.494, corr 0.767, k 0.910, b 0.943, p 2.5e-4); no gate change after data; 45 of 150 compositions overlap the withdrawn seed-0 set (ledger said 44), dropping them still passes (gain 0.467). Main doubt: the registered null cannot tell a compositional shared floor from shared single-cell noise; joint fit uses the same cell's K'. Follow-up test fd786169e3 (two new cells per composition, unique seeds).", "parent": null, "evidence": {".orchestra/audits/b86e0d8a40_astra.md": "55babd97e37e0217"}, "notes": "audit"}
claims/claims.jsonl:78:{"id": "6bc0e190a8", "time": "2026-11-01T02:01:56", "level": "L0", "claim": "Model dependence of K' transfer is a Co effect: under medium-mpa-0 the K' rule on the 150 compositions of b86e0d8a40 (cells with unique seeds 3000+i) gives, for Co-free alloys, gain >= 0.10, p < 0.005 and a k CI containing 1, and k(Co >= 15%) - k(Co-free) >= 0.15 with bootstrap CI above 0", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_mpa_co.py": "5bd3ed85f9886da0"}, "notes": "prereg; power {'power': 0.86, 'false_pass': 0.0}; swarm S3 cobalt front, Opus opus_2 (seen split of 86767e478d: 1.05 vs 1.48)"}
claims/claims.jsonl:79:{"id": "65fbd3d483", "time": "2026-11-01T02:05:37", "level": "L0", "claim": "Audit of fd786169e3 PASS (Astra, independent; .orchestra/audits/fd786169e3_astra.md): PLAUSIBLE. Recomputed cross-cell r 0.750 [0.675, 0.818], k 0.924 [0.83, 1.03], b 0.945 [0.81, 1.09]; same-cell vs cross-cell covariance 3.92 vs 3.73 GPa^2 (cell noise ~5%); 300 unique seeds verified; linear instead of cubic splines and disjoint binary-seed references still pass. Open: the clamped pre-stress enters both curvatures (K44 = C + sigma_yy, K' = C' + (sigma_xx + sigma_yy)/2, both -P if hydrostatic), a known identity; approximate hydrostatic removal drops r 0.75 -> 0.70. Decisive follow-up: full stress tensors of targets, pures and binary grid.", "parent": null, "evidence": {".orchestra/audits/fd786169e3_astra.md": "61c4c0c1c3430021"}, "notes": "audit"}
claims/claims.jsonl:80:{"id": "5b8ec14bfa", "time": "2026-11-01T02:15:47", "level": "L0", "claim": "Model dependence of K' transfer is a Co effect: FAIL (Co-free gain 0.45, k 1.10 [0.85, 1.31]; Co k 1.09; diff CI [-0.30, 0.33])", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\k_mpa_co.csv": "ed308bbad73d03f6", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\binary_kgrid_mpa.csv": "92160b8d1d1c00bc", "C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_mpa_co.py": "5bd3ed85f9886da0"}, "notes": "prereg 6bc0e190a8"}
claims/claims.jsonl:81:{"id": "ede47f1d65", "time": "2026-11-01T02:16:04", "level": "L0", "claim": "Shared shear floor beyond pre-stress: after subtracting the clamped initial mixing stress (K44 - s_yy, K' - (s_xx + s_yy)/2) from targets and binaries alike, the fd786169e3 floor test still passes on the same 150 compositions x 2 cells: cross-cell corr >= 0.5, joint k in [0.7, 1.3], b in [0.6, 1.3]", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_floor_stress.py": "0357a03030fd028c"}, "notes": "prereg; power {'power': 1.0, 'false_pass': 0.0}; Astra audit of fd786169e3, finding 4; known identity K = C + initial stress"}
claims/claims.jsonl:84:{"id": "88b9465108", "time": "2026-11-01T02:43:54", "level": "L0", "claim": "K' transfer k = 1 under medium-mpa-0: on 1200 new compositions (Co yes/no x 3/4/5 elements, 200 each, two cells) with two independent mpa binary panels, the cross-panel k of the K' volume-transfer rule has a 90% CI inside [0.90, 1.10]", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_mpa_equiv.py": "c3aa55f4e4d5fc36"}, "notes": "prereg; power {'power': 1.0, 'false_pass': 0.0}; Astra audit of 6bc0e190a8; old mpa k 1.33 (86767e478d), leak-free 150 alloys 1.10"}
claims/claims.jsonl:86:{"id": "43370bbb27", "time": "2026-11-01T10:11:44", "level": "L0", "claim": "K' transfer k = 1 under medium-mpa-0: FAIL (k 1.138, 90% CI [1.098, 1.182], 95% CI [1.091, 1.189])", "parent": null, "evidence": {"C:\\Users\\can02\\Projects\\AI driven Science\\data\\k_mpa_equiv_binaries.csv": "5724afbe11d1a8d1", "C:\\Users\\can02\\Projects\\AI driven Science\\data\\k_mpa_equiv_targets.csv": "c038f0f51b97bcf6", "C:\\Users\\can02\\Projects\\AI driven Science\\scripts\\k_mpa_equiv.py": "c3aa55f4e4d5fc36"}, "notes": "prereg 88b9465108"}
claims/claims.jsonl:87:{"id": "736bcac471", "time": "2026-11-01T10:17:02", "level": "L0", "claim": "verdict on 88b9465108: FAIL, k = 1 equivalence retired; volume transfer itself survives (rule RMSE 2.21 vs pair-at-V_ij 4.81 GPa, 54% gain, better on 934/1200)", "parent": null, "evidence": {".orchestra/audits/88b9465108_astra.md": "4c17700ac246f723", "data/k_mpa_equiv_targets.csv": "c038f0f51b97bcf6", "data/k_mpa_equiv_binaries.csv": "5724afbe11d1a8d1"}, "notes": "cause=hypothesis; audit: Astra, independent (.orchestra/audits/88b9465108_astra.md): no coding error; k 1.138 reproduced, 90% CI [1.098, 1.182]; panel splits 1.138-1.139. k is composition dependent (exploratory): 3 el 1.00, 4 el 1.25, 5 el 1.17; Cu-free 1.00, Cu 1.24; max|dlnV| <=0.15 1.07, >0.25 1.41. omat floor cells give 1.11 [1.02, 1.20] with seed split 0|1,2, same stratification. Power sim was optimistic (target residual is compositional, not cell noise)."}
"""Quantum ESPRESSO (pw.x in WSL) as the L3 reference for stresses and elastic constants.

QE lives in a conda-forge env inside WSL (micromamba env "qe", no sudo needed).
Pseudopotentials: SSSP 1.3.0 PBE efficiency, md5 a58f1b3373f330179fd0832c48bb9a52,
Materials Cloud Archive 2023.65, doi:10.24435/materialscloud:f3-ym.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from ase import Atoms
from ase.io import read, write

from harness.compute import GPA, cubic_average, voigt_reuss_hill

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "data" / "dft_runs"
DISTRO = "Ubuntu-22.04"
PSEUDO_DIR = "/home/can02/pseudo/sssp_eff_1.3"
SSSP = json.loads((Path(__file__).parent / "data" / "sssp_1.3.0_pbe_efficiency.json").read_text())

# Collinear starting moments for the magnetic 3d metals. Cr gets an antiferromagnetic
# start on the two bcc sublattices; a commensurate AFM cell is an approximation of its SDW.
MAGNETIC = {"Fe": 0.4, "Co": 0.4, "Ni": 0.3, "Mn": 0.4, "Cr": 0.4}


@dataclass
class Settings:
    kspacing: float = 0.15          # 1/A, Monkhorst-Pack density (2*pi included)
    ecut_scale: float = 1.25        # stresses need a margin above the SSSP energy cutoff
    degauss: float = 0.01           # Ry, Marzari-Vanderbilt
    np: int = 8                     # 8 physical cores
    extra: dict = field(default_factory=dict)
    # Elements whose cutoffs also set this run's cutoff. For mixing energies and curvatures pass the alloy's elements
    # to the pure references too, so all terms share one basis (before 2026-10-31 each run used only its own).
    ecut_elements: tuple = ()
    # Fixed Monkhorst-Pack grid. Finite-strain curvatures must use one grid for every strain; the default picks it from
    # the strained cell, which changes it between strains (18x18x18 vs 17x18x18 for Cu3Ir, found 2026-10-31).
    kpts: tuple | None = None


def wsl_path(p: Path) -> str:
    s = str(p.resolve()).replace("\\", "/")
    return f"/mnt/{s[0].lower()}{s[2:]}"


def kgrid(atoms: Atoms, kspacing: float) -> tuple[int, int, int]:
    rec = np.linalg.norm(atoms.cell.reciprocal(), axis=1) * 2 * np.pi
    return tuple(max(1, int(np.ceil(r / kspacing))) for r in rec)


def magnetize(atoms: Atoms) -> bool:
    """Set initial moments in place; AFM checkerboard for Cr. Returns True if spin polarised."""
    mags = np.array([MAGNETIC.get(s, 0.0) for s in atoms.get_chemical_symbols()])
    if not mags.any():
        return False
    if "Cr" in atoms.get_chemical_symbols():
        a = (2 * atoms.get_volume() / len(atoms)) ** (1 / 3)  # bcc conventional lattice parameter
        parity = np.round(2 * atoms.positions[:, 0] / a).astype(int) % 2  # corner vs body centre
        mags = np.where(np.array(atoms.get_chemical_symbols()) == "Cr", mags * (1 - 2 * parity), mags)
    atoms.set_initial_magnetic_moments(mags * 5)  # ASE maps moments to starting_magnetization
    return True


def run_pw(atoms: Atoms, tag: str, s: Settings, relax_ions: bool = False) -> Atoms:
    """Run one pw.x scf/relax with stress. Cached: an existing finished output is reused."""
    d = RUNS / tag
    d.mkdir(parents=True, exist_ok=True)
    out = d / "pw.out"
    els = sorted(set(atoms.get_chemical_symbols()))
    basis = set(els) | set(s.ecut_elements)
    ecut = float(s.extra.get("system.ecutwfc", s.ecut_scale * max(SSSP[e]["cutoff_wfc"] for e in basis)))
    ecutrho = s.ecut_scale * max(SSSP[e]["cutoff_rho"] for e in basis)
    if out.exists() and "JOB DONE" in out.read_text(errors="ignore"):
        cached = re.search(r"ecutwfc\s*=\s*([\d.]+)", (d / "pw.in").read_text())
        if cached and abs(float(cached.group(1)) - ecut) > 1e-6:  # a cache hit must not silently change the basis
            raise RuntimeError(f"{tag}: cached run used ecutwfc {cached.group(1)}, requested {ecut}; use a new tag")
        return read(out, format="espresso-out", index=-1)
    scratch = tag.replace("/", "__")
    atoms = atoms.copy()
    # extra={'system.nspin': 1} must switch magnetism off: initial moments make ASE write nspin 2 back (S3 audit)
    spin = s.extra.get("system.nspin", 2) != 1 and magnetize(atoms)
    data = {"control": {"calculation": "relax" if relax_ions else "scf", "tstress": True,
                        "tprnfor": True, "pseudo_dir": PSEUDO_DIR, "outdir": f"/tmp/qe/{scratch}",
                        "disk_io": "low", "forc_conv_thr": 1e-4},
            "system": {"ecutwfc": ecut, "ecutrho": ecutrho, "occupations": "smearing",
                       "smearing": "mv", "degauss": s.degauss, "nspin": 2 if spin else 1},
            "electrons": {"conv_thr": 1e-10 * len(atoms), "mixing_beta": 0.3}}
    for k, v in s.extra.items():
        data.setdefault(k.split(".")[0], {})[k.split(".")[1]] = v
    write(d / "pw.in", atoms, format="espresso-in", input_data=data,
          pseudopotentials={e: SSSP[e]["filename"] for e in els}, kpts=s.kpts or kgrid(atoms, s.kspacing))
    cmd = (f"export MAMBA_ROOT_PREFIX=~/mamba OMP_NUM_THREADS=1; mkdir -p /tmp/qe/{scratch}; cd '{wsl_path(d)}' && "
           f"~/bin/micromamba run -n qe mpirun -np {s.np} pw.x -nk {min(s.np, 4)} -in pw.in > pw.out 2> pw.err; "
           f"rm -rf /tmp/qe/{scratch}")
    subprocess.run(["wsl", "-d", DISTRO, "--", "bash", "-lc", cmd], check=True)
    text = out.read_text(errors="ignore")
    if "JOB DONE" not in text or "convergence NOT achieved" in text:
        raise RuntimeError(f"pw.x failed for {tag}, see {out}")
    return read(out, format="espresso-out", index=-1)


def stress(atoms: Atoms, tag: str, s: Settings, relax_ions: bool) -> np.ndarray:
    return read_stress(run_pw(atoms, tag, s, relax_ions))


def read_stress(a: Atoms) -> np.ndarray:
    return a.get_stress(voigt=True) * GPA  # ASE sign: tensile positive


def elastic_cubic(atoms: Atoms, tag: str, s: Settings, eps: float = 0.01, full: bool = False,
                  relax_ions: bool | None = None) -> np.ndarray:
    """6x6 tensor (GPa) by central differences. full=False uses only e_xx and e_yz,
    which is exact for a cubic crystal and enough for pure elements (4 pw.x runs)."""
    if relax_ions is None:
        relax_ions = len(set(atoms.get_chemical_symbols())) > 1
    cell0 = atoms.get_cell().array.copy()
    voigt = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
    cols = range(6) if full else (0, 3)
    C = np.full((6, 6), np.nan)
    for j in cols:
        k, l = voigt[j]
        sig = []
        for sign in (+1, -1):
            e = np.zeros((3, 3))
            if k == l:
                e[k, k] = sign * eps
            else:
                e[k, l] = e[l, k] = sign * eps / 2
            st = atoms.copy()
            st.set_cell(cell0 @ (np.eye(3) + e), scale_atoms=True)
            sig.append(stress(st, f"{tag}/e{j}{'p' if sign > 0 else 'm'}", s, relax_ions))
        C[:, j] = (sig[0] - sig[1]) / (2 * eps)
    if not full:  # fill the cubic tensor from the two columns
        c11, c12, c44 = C[0, 0], 0.5 * (C[1, 0] + C[2, 0]), C[3, 3]
        C = np.zeros((6, 6))
        C[:3, :3] = c12
        np.fill_diagonal(C[:3, :3], c11)
        C[3:, 3:] = np.eye(3) * c44
    return 0.5 * (C + C.T)


def relax_lattice(atoms: Atoms, tag: str, s: Settings, eps: float = 0.01) -> Atoms:
    """Cubic lattice parameter from a parabola fit of pressure vs volume (3 pw.x runs).
    Avoids vc-relax Pulay stress issues and keeps every run cached and inspectable."""
    cell0 = atoms.get_cell().array.copy()
    scales = np.array([1 - eps, 1.0, 1 + eps])
    P = []
    for sc in scales:
        a = atoms.copy()
        a.set_cell(cell0 * sc, scale_atoms=True)
        sig = stress(a, f"{tag}/lat{sc:.3f}", s, relax_ions=len(set(a.symbols)) > 1)
        P.append(-sig[:3].mean())
    root = np.roots(np.polyfit(scales, P, 2))
    root = root[np.isreal(root)].real
    best = root[np.argmin(abs(root - 1))]
    out = atoms.copy()
    out.set_cell(cell0 * best, scale_atoms=True)
    return out


def run_alloy(comp_atoms: Atoms, label: str, s: Settings, full: bool | None = None) -> dict:
    full = (len(set(comp_atoms.symbols)) > 1) if full is None else full
    tag = f"{label}_k{s.kspacing}_e{s.ecut_scale}"
    a = relax_lattice(comp_atoms, tag, s)
    c11, c12, c44 = cubic_average(elastic_cubic(a, tag, s, full=full))
    row = {"label": label, "formula": a.get_chemical_formula(mode="metal"), "natoms": len(a),
           "vol_per_atom": a.get_volume() / len(a), "C11": c11, "C12": c12, "C44": c44,
           "method": f"QE7.6 PBE SSSP1.3eff k{s.kspacing} ecut x{s.ecut_scale} mv{s.degauss}",
           "time": dt.datetime.now().isoformat(timespec="seconds")}
    row.update(voigt_reuss_hill(c11, c12, c44))
    return row

codex
`scientific-result-audit` skill’ini kullanıyorum. Kayıt sekiz hücreyi ve eşiği açıkça sabitliyor; işaret cümlesinin belirsizliği ile sayısal yakınsama güvencesini ayrı ele almak gerekiyor.

2026-11-01T22:32:04.356632Z ERROR codex_core::tools::router: error=collab spawn failed: no thread with id: 01a1993d-980f-7b31-83f3-32c8d6ff3a67
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content scripts/hiso_l12_v2.py -Encoding utf8; Get-Content data/hiso_l12_dft_v2.csv; Get-Content data/hiso_l12_mace.csv; Get-Item .venv/Scripts/python.exe' in C:\Users\can02\Projects\AI driven Science
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content STATUS.md -Encoding utf8; Get-Content .orchestra/LESSONS.md -Encoding utf8; Get-Content scripts/hiso_l12.py -Encoding utf8' in C:\Users\can02\Projects\AI driven Science
 succeeded in 884ms:
# Durum (1 Kas�m 2026)

Tek giri� noktas�. Ayr�nt� ve kan�t defterde (`claims/claims.jsonl`, kimlikler a�a��da), dersler `.orchestra/LESSONS.md` i�inde. `.orchestra/NIGHT_REPORT.md` 31 Ekim sabah�na ait ve eskidir ("iki ba��ms�z holdout" ifadesi d26bd71285 ile d�zeltildi).

## Bulgular

| # | Bulgu | Seviye | Kan�t | A��k olan |
|---|---|---|---|---|
| 1 | **K' hacim transferi.** Rastgele fcc ala��m�n kar���m K' de�eri = ? 4 x_i x_j K'_ij(V0), ikililer ala��m hacminde. �ki k�r sette hata yar�ya iniyor, k 1.08 ve 1.08. | L2 (697c2d6d75) | h3: 4c29d9754c  6e0923b413 (ortak iddia K44 y�z�nden FAIL); hm_fresh: 67a358fc59  d92844787f (PASS) | mpa modelinde k 1.33 [1.11, 1.51] (851aec6883  86767e478d), ama s�z�nt�s�z 150 ala��mda 1.10 [0.94, 1.26] (kay�ts�z; 6bc0e190a8 FAIL, sebep design). Denklik testi 88b9465108 FAIL: 1200 ala��m, k 1.14 [1.10, 1.18], kural yine hatay� 4.81'den 2.21 GPa'ya indiriyor (43370bbb27, verdict 736bcac471, Astra: kod hatas� yok). k kompozisyona ba�l� (ke�ifsel): 3 element 1.00, Cu'suz 1.00, Cu'lu 1.24, max|dlnV| > 0.25 iken 1.41. omat da benzer (1.11). k = 1 iddias� d��t�; b�y�k hacim fark�nda transfer eksik kal�yor. PBE yok. Literat�r (tam metin): k�smen biliniyor; hacim ad�m�, k�r test ve K'/K44 kar��tl��� bulunamad�. "Hacim transferli regular-solution / kesik tens�rel CE kural�" diye yaz�lmal�, Marker 2017 okunmadan yaz�lmamal�. |
| 2 | **Enerji hacim transferi: D��T�.** Standart Muggianu (saf elementler kendi hacminde) ayn� i�i yap�yor, 11.4 ile 11.5 meV, kural 13.3 (S2 denetimi, defterde d�zeltme). Eski metin: E_mix hatas� 36.4  13.1 meV, yaln�z hm_fresh (n 94) ger�ekten k�rd�. Tam hesapta k 0.94 ile 0.98; 0.81 do�rusalla�t�rma etkisi. | L2 (05f01df6ec, d�zeltme d26bd71285) | 1708d0db77, k_direct | Fikrin �z� Zunger 1987-89'da biliniyor (`claims/literature.jsonl`). PBE d�zenli h�cre L3'� FAIL (8541e914ea). |
| 3 | **K44 Co'suz ala��mlarda transfer oluyor** (�n kay�t e410c96a32  d9460850ce, 120 taze ala��m, kazan� 0.51, p 2.5e-4, k 1.23); Co'lularda olmuyor (kazan� 0.11). Eski g�zlem: Ayn� kural K44'te zay�f: kazan� 0.12 ile 0.20, k 0.69 ile 0.86. En k�t� hatalar Co'ca zengin ala��mlarda. | g�zlem | LESSONS 14 ile 16 | Neden a��k; ba��ms�z denetim yap�lmad�. Ke�if bak��� (g�r�lm�� 269 sat�r, kay�t de�il): "E_F'de y�ksek DOS" a��klamas� desteklenmiyor, art�k Pd/Pt/Ni/Rh/Ir/Co oran�yla iki kanalda da benzer b�y�yor (K44/K' rms oran� 1.15 ile 1.4). En b�y�k hatalar iki kanalda da Co'lu ala��mlarda (|r44| ile Co r 0.33): s�radaki ��pheli Co manyetizmas�. K44'�n hacim kaymas� da k���k, kazan� i�in az yer var (a2: pair 3.56  kural 2.66, K' 5.67  1.80). |
| 3b | **Ortak kayma taban�.** Hacim kural�n�n K44 ve K''te ka��rd��� k�s�m ayn� ve kompozisyona ait: K44 - K' kural� ge�iyor (kazan� 0.49), h�creler aras� r 0.75, bilinen �n gerilme �zde�li�i ��kar�l�nca r 0.67, k 0.99. K44'�n "tutmamas�" bu tabandan. | L0, �� �n kay�tl� PASS (b86e0d8a40, fd786169e3, ede47f1d65), ��� de Astra denetimi PLAUSIBLE | `data/k_aniso_s100_clamped.csv`, `k_floor_cells.csv`, `k_floor_stress_*.csv`; LESSONS 20-22 | �kili referanslardan gelen ortak hata d��lanmad� (iki ba��ms�z ikili paneli gerekli). Fiziksel anlam� a��k; MACE only. |
| 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
| 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |

Yanl��lanan adaylar (A2, H-sm, R3, R3b, HM2-T4, Astra EOS kapan���) ve gerek�eleri defterde `verdict on ...` kay�tlar�nda.

## �al��an i�ler

- **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.

## S�radaki ad�mlar

1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
2. K' kural� i�in PBE (L3). **Tasar�m uyar�s�:** d�zenli 4 atomlu h�creler enerji kural�nda PBE'de +10 meV'lik sabit hacim �ok cisim terimi ta��d��� i�in yanl�� test ��kt� (d440b9eb7b, 8541e914ea). K' i�in de d�zenli h�cre kullan�lacaksa bu �nce d���n�lmeli; do�ru alan PBE SQS h�creleri (32 atom ve �st�) ve bu laptopta g�nler s�rer, kiral�k sunucu se�ene�i var.
3. PBE h�zland�rma: Cu3Ir'de smearing ve k-a�� gev�etmeyi referansa kar�� test et.
4. Veri d�zeltmesi: ��l�lerdeki 0.3333 hatas� ve eski B_chem/R s�tunlar� i�in yeni `*_fixed2` dosyalar�, m�h�rl� holdout i�in yeni m�h�r.
5. L4: Zunger 1987-89, Sanchez 2019, Zhang 2022 tam metinleri; Aidhy grubu (HEA Cij, ayn� element seti).
5b. Deney verisi (ajan taramas� 1 Kas�m): bu dokuz elementte �l��lm�� tek kristal ala��m sabitleri yaln�z kapal� eri�imde (Cu-Ni Epstein-Carlson 1965, Schmunk-Smith 1960; Cu-Au Chiarodo 1972, dC/dP ile; Pd-Ag Hoare-Yates 1954; Co-Ni Weston-Granato 1975). 3+ bile�enli �l��m yok. K�t�phane PDF'i gerekli.
5c. PBE hatas� (S3 cobalt, Astra, kodda do�ruland�): `harness/dft.py` i�inde `extra={'system.nspin': 1}` Co/Ni manyetizmas�n� kapatm�yor; `magnetize()` ba�lang�� momentlerini koyuyor, ASE nspin'i 2'ye geri �eviriyor. �al��an H-iso h�crelerinde Co/Ni yok, etkilenmiyor. Co'lu PBE'den �nce d�zeltilmeli.
6. Makale: `paper/draft_v1.md` (K' �ekirdekli taslak, TODO'lar: PBE L3, c2eff007ad, Marker 2017, denetim tablosu). `paper/outline.md` eski, enerji kural�na g�re.

## Harness haritas�

| Par�a | Yer |
|---|---|
| Hesap (MACE, SQS, curvature) | `harness/compute.py`, `harness/context.py` (ikili V_ij, Vegard) |
| PBE | `harness/dft.py` (`Settings(kpts=..., ecut_elements=...)` zorunlu) |
| Defter, �n kay�t, g�� | `harness/ledger.py`, `harness/power.py` |
| Arena (m�h�rl� holdout) | `harness/arena.py`, `data/sealed/`, `candidates/` |
| Ajanlar | `scripts/discovery_round.py` (arena turu), `scripts/swarm.py` (cepheler `.orchestra/fronts/`) |
| K' testleri | `scripts/k_shear_transfer.py` (h3), `k_shear_kp_hm.py` (hm_fresh), `k_shear_mpa.py` (model de�i�imi); veri `data/binary_kgrid*.csv`, `data/*_shear_clamped*.csv` |
| Enerji kural� | `scripts/hm_l2_fixed.py`, `scripts/k_direct.py`, `candidates/champion_volume_transfer.py` |

Veri k�meleri: h1 (ke�if, g�r�lm��), h3 (model se�iminde kullan�ld�, K i�in k�rd�), hm_fresh (enerji ve K' i�in k�rd�, art�k g�r�ld�), hm3fix (m�h�rl�, ajanlar g�rmez).
# Lessons for derivation agents (Astra, Opus)

Read before proposing. Each line is a way a candidate died or nearly died for the wrong reason. Updated 2026-10-31.

1. Ratios of energies blow up where the denominator crosses zero (R3: n_eff = -3 b/a reached -102 for Cu-Ir). Prefer
   predictions linear in measured quantities; if a ratio is essential, say where it is undefined.
2. Compare like with like: clamped with clamped, relaxed with relaxed, random with random. R3 compared a relaxed random
   volume with a clamped L1_0 volume; even the exact formula then had slope 0.20.
3. Ordered cells are not random alloys. In PBE, 4-atom ordered cells carry a fixed-volume many-body term (~10 meV/atom)
   that random alloys lack. A random-alloy rule must be tested on random (SQS) cells.
4. If your rule's main content is a common shift, a test with a free intercept cannot see it. State the test you expect
   to pass, and check its power by simulation (harness/power.py) before data exist.
5. Results that survived so far: volume transfer of binary interactions (L2, refit k = 0.79 on both holdouts, not
   input noise); isotropic chemical shear softening K44 ~ K' in Ir/Rh alloys (MACE, PBE pending). Build on these.
6. Results that died for real: A2 (shear from hydrostatic derivatives; even a free 2-term fit has r 0.37), H-sm
   (predicted K44/K' = 4, measured 1.05), R3b (exponent sharing). Do not resubmit without a new mechanism.
7. PBE: pure references must share the alloy's cutoff (dft.Settings(ecut_elements=...)). Earlier PBE mixing numbers
   carry a cutoff mismatch; its size is being measured (data/ecut_bias.csv).
8. Round R1 (Astra and Opus independently): 108-atom cells round atom counts, but references used nominal fractions,
   so every non-integer composition carried up to ~60 meV/atom of bookkeeping error. Fixed in data/*_fixed.csv
   (column comp_actual is the real composition) and in the generators. Always reference the composition the cell has.
9. PBE cutoff mismatch corrected (harness/ecutfix.py, validated to 0.002 meV/atom). MACE now PASSES L1 for the
   ordered-cell beyond-pair Delta (sign 9/10, r 0.80); PBE quaternary Delta +12.9 meV is real. MACE data on ordered
   multicomponent cells can be used.
10. Round R2 (Astra): the arena's permutation count capped the smallest reachable p at 1/501, so after five tests no
    candidate could pass however good it was. Fixed: n_perm grows with m. Also open: generators set V0 from nominal
    fractions while comp_actual differs (~0.5% in volume, ~0.06 meV RMSE effect, not the cause of k ~ 0.8).
11. k ~ 0.8 was mostly linearisation: E_ij(V) is strongly nonlinear over |ln(V0/V_ij)| up to 0.36. Exact binary
    energies at the alloy volume give k 0.94 [0.90, 0.98] and RMSE 10.3 meV with no parameter (data/binary_vgrid.csv).
12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
    from the strained cell (18x18x18 vs 17x18x18), so 0.1 meV/atom of strain-dependent error moves K by 1.6 to 4.7
    GPa. H-iso results before the fix are not evidence either way; the run is stopped. (b) fix_counts.py treated
    0.3333 as the reference weight of equiatomic ternaries (36+36+36 atoms are exact): +0.3 to +0.7 meV added.
    (c) B_chem and R in *_fixed.csv are stale. (d) K44 ~ K' is not Zener invariance.
13. k at fixed composition (h1/h3 E(V) curves vs exact binary response): 0.976 [0.956, 1.001]. No reduced volume
    response; k ~ 0.8 is the curvature the linear transfer leaves out (94% of the shift).

14. Shear-curvature volume transfer (prereg 4c29d9754c, result 6e0923b413), 113 unseen h3 alloys, binary curvatures
    at the alloy volume, no parameter. Kp: 4.77 -> 2.03 GPa, gain 0.57, p 2.5e-4, refit k 1.08 (pass). K44: 3.29 -> 2.62,
    gain 0.20, p 0.023, refit k 0.86 (fail at p < 0.005). Joint claim FAIL. The first design (sigma = pair-sum residual,
    which contains the signal) had power 0.45 and was stopped before any target existed. K44's worst rule errors are
    Co-rich (Co ~0.46 with Pt or Cu), where the rule is worse than no transfer; cause not yet audited (hypothesis,
    design or numerics). Do not re-split the joint claim after the fact: a K44 or Kp claim needs its own fresh test.

15. K' alone, fresh blind test (prereg 67a358fc59, result d92844787f, L2 entry recorded): 94 hm_fresh alloys, K' 4.22 ->
    1.89 GPa, gain 0.55, p 2.5e-4, refit k 1.08, 75/94 better. Two independent blind sets now agree for K' (k 1.08 both).
    K44 again weaker (gain 0.12, k 0.69, not gated). Why K44 transfers worse than K' is open: Co-rich outliers, or
    internal (non-affine) relaxation channels that the clamped protocol suppresses differently for the two shears.

16. Model swap of the K' rule (prereg 851aec6883, result 86767e478d): medium-mpa-0, same geometry, same 94 hm_fresh
    alloys, binaries seed 0 only. K' 4.73 -> 2.28 GPa, gain 0.52, p 2.5e-4, but refit k 1.33 [1.11, 1.51]: the
    pre-registered k-contains-1 condition FAILS. K44 gain 0.16, k 0.77. Reading: that the alloy's K' follows the binaries
    at the alloy volume and cuts the error in half survives a model with a different shear bias; that the coefficient is
    exactly 1 does not (omat 1.08 twice, mpa 1.33). Binary seed noise would pull k down, not up. The two models disagree
    most at |dlnV| > 0.2 (K' corr 0.80 vs 0.96 within 0.1). Cause not yet audited. Do not claim "parameter-free" across
    models; the PBE check decides which k is physical.

17. K44 transfer fails only with Co (prereg e410c96a32, result d9460850ce). 120 fresh Co-free alloys: K44 pair 4.68 ->
    rule 2.30 GPa, gain 0.51, p 2.5e-4, k 1.23 (PASS). 60 fresh alloys with Co >= 15%: gain 0.11, p 0.08, k 0.70. K'
    passes in both. Open confound: the Co-free set has a larger volume signal (pair error 4.68 vs 3.36), so "Co breaks
    K44" and "K44 needs a large signal" are not yet separated; match the two sets on |rule - pair| before claiming
    a Co mechanism (magnetism is a guess, MACE has no spin).
    Confound check (exploratory, same fresh rows, tertiles of |rule - pair|): at matched signal Co-free gain 0.37 / 0.58
    vs Co 0.08 / 0.22 (mid / large), and Co alloys carry a larger floor at small signal (rule rms 2.61 vs 1.73 GPa).
    The Co effect survives signal matching; not yet a registered claim.

18. Why K44 looked broken (Opus, swarm S2, blind by file timestamp, confirmed on 60 Co alloys). The part the pair rule
    misses is the same in both shears (corr 0.71, slope ~1). K44's volume signal is half of K''s, so the shared floor
    swamps it; in Co alloys the floor anticorrelates with the signal and drags k to 0.7. Remove the floor (A = K44 - K'
    or e' as covariate) and K44 transfers with k ~1. LESSONS 14-16 failure reason: design, not hypothesis.

19. Shared SQS seed leak (Opus S2 audit, Astra confirmed). compute.py:56 draws the site permutation from (seed, n)
    only, so every seed-0 cell thresholds one random field: seed-0 targets and seed-0 binaries share configuration
    noise. K' is immune (gain 0.55-0.58, k 1.07-1.10 for every seed split). K44 is not: leak-free gain 0.06-0.14,
    k 0.60-0.77. d9460850ce and the LESSONS 18 Co check used the leak; 9cfc8edaf0 was withdrawn before reading and
    re-registered as c2eff007ad with target seed 100. Rule: targets and inputs never share a seed.

20. Shared floor, disjoint seeds (c2eff007ad -> b86e0d8a40 PASS, 150 alloys): A = K44 - K' transfers (gain 0.49),
    corr(e44, e') 0.77, joint k 0.91, b 0.94; plain K44 Co-free gain 0.47, Co 0.09. Astra audit: PLAUSIBLE, the
    null could not separate a compositional floor from same-cell noise. A shared-channel claim needs targets for the
    two channels from different cells. Test fd786169e3.

21. The shared floor is compositional (fd786169e3 PASS, two cells per composition, unique seeds): cross-cell corr
    0.75 vs same-cell 0.79, k 0.92, b 0.95; Astra audit PLAUSIBLE (cell noise ~5% of the shared covariance). Next
    doubt is a known identity: clamped curvatures carry the initial stress, K44 = C44 + s_yy, K' = C' + (s_xx+s_yy)/2.
    A floor claim must survive subtracting it (k_floor_stress.py). Pre-register every step; one audit, one test.

22. The floor survives the known pre-stress identity (ede47f1d65 PASS; Astra PLAUSIBLE): corrected cross-cell r
    0.67, k 0.99, b 0.79. Mixing pre-stress is 7 GPa rms but pair-additive (rule leaves 0.7 GPa), so it was never the
    floor. Remaining doubt: error shared through the binary references (b drops to 0.4-0.5 with single disjoint
    seeds). Shared-residual claims need two independent binary panels, as in k_mpa_equiv.py.
23. k = 1 is retired (88b9465108 FAIL, cause hypothesis; Astra found no coding error). Under mpa, 1200 alloys: k 1.14
    [1.10, 1.18]; the rule still halves the error (4.81 to 2.21 GPa). k is not a model constant but composition
    dependent: 3 elements 1.00, Cu-free 1.00, Cu 1.24, alloys with max|dlnV| > 0.25 1.41; omat shows the same pattern
    (1.11). The pair transfer under-predicts at large size mismatch. A power sim that treats the target residual as
    cell noise is optimistic: most of it is compositional and does not average out over cells.
"""H-iso check in cubic L1_2 cells: clamped mixing shear curvatures K44, Kp with MACE or PBE.

python scripts/hiso_l12.py mace | dft
A3B L1_2 (4-atom cubic cell, B on the corner site), clamped at Vegard volume, pure fcc references at the same volume
and the same deformation. Strains +-0.02 (three-point curvature). PBE uses kspacing 0.10 (shear needs the fine grid).
"""

import datetime as dt
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

from harness.compute import GPA  # noqa: E402

CELLS = [("Cu", "Ir"), ("Cu", "Rh"), ("Pd", "Ir"), ("Au", "Ir"), ("Ag", "Ir"), ("Ag", "Rh"),  # A3B with Ir/Rh
         ("Cu", "Au"), ("Pt", "Cu")]  # controls without Ir/Rh; order = MACE |K| (PBE is slow, strongest first)
S = 0.02
SYM_DONE = {"Cu3Ir": ("g-", "t-")}  # computed both signs here; used as the symmetry check
METHOD = sys.argv[1]
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]

if METHOD == "mace":
    from harness import compute
    calc = compute.calculator()

    def energy(atoms, tag):
        atoms.calc = calc
        return atoms.get_potential_energy() / len(atoms)
else:
    from harness import dft
    st = dft.Settings(kspacing=0.10, np=int(os.environ.get("HISO_NP", "4")))

    def energy(atoms, tag):
        return dft.run_pw(atoms, f"hiso/{tag}", st).get_potential_energy() / len(atoms)

DEF = {"0": np.eye(3), "g+": np.eye(3) + S * np.outer([1, 0, 0], [0, 1, 0]),
       "g-": np.eye(3) - S * np.outer([1, 0, 0], [0, 1, 0]),
       "t+": np.diag([np.exp(S), np.exp(-S), 1.0]), "t-": np.diag([np.exp(-S), np.exp(S), 1.0])}


def strained(symbols, v, F):
    a = bulk("Cu", "fcc", a=4.0, cubic=True)
    a.symbols = list(symbols)
    a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    return a


OUT = ROOT / "data" / f"hiso_l12_{METHOD}.csv"
done = set(pd.read_csv(OUT)["cell"]) if OUT.exists() else set()
for A, B in CELLS:
    name = f"{A}3{B}"
    if name in done:
        continue
    v = 0.75 * pv[A] + 0.25 * pv[B]
    vt = f"{v:.3f}"
    em = {}
    for k, F in DEF.items():
        if k in ("g-", "t-") and k not in SYM_DONE.get(name, ()):  # cubic L1_2: y -> -y and x <-> y are symmetries
            continue
        e_ab = energy(strained([B, A, A, A], v, F), f"{name}_{k}_v{vt}")
        e_a = energy(strained([A] * 4, v, F), f"{A}_{k}_v{vt}")
        e_b = energy(strained([B] * 4, v, F), f"{B}_{k}_v{vt}")
        em[k] = e_ab - 0.75 * e_a - 0.25 * e_b
    em.setdefault("g-", em["g+"])
    em.setdefault("t-", em["t+"])
    c44 = (em["g+"] + em["g-"] - 2 * em["0"]) / (2 * S**2)   # E = c s^2
    cp = (em["t+"] + em["t-"] - 2 * em["0"]) / (2 * S**2)
    r = {"cell": name, "method": METHOD, "V": v, "E_mix": em["0"], "K44": 2 * c44 / v * GPA, "Kp": cp / (2 * v) * GPA,
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(name, f"E_mix {em['0']*1000:+7.1f} meV  K44 {r['K44']:+7.2f}  Kp {r['Kp']:+7.2f} GPa", flush=True)

 succeeded in 2165ms:
"""H-iso check, corrected numerics (v2): clamped mixing shear curvatures K44, Kp of cubic L1_2 cells with PBE.

python scripts/hiso_l12_v2.py [dense]
Fixes found by the swarm S1 audit in scripts/hiso_l12.py: the alloy and both pure references now share one cutoff
(ecut_elements = (A, B)) and one k-grid, taken from the unstrained cell, for every strain. "dense" repeats Cu3Ir and
Ag3Rh at kspacing 0.08 as a convergence check. Criteria 6cb3c2a936 are unchanged; the old results are not used.
A3B L1_2 (4-atom cubic cell, B on the corner site), clamped at Vegard volume, pure fcc references at the same volume
and the same deformation. Strains +-0.02 (three-point curvature). PBE uses kspacing 0.10 (shear needs the fine grid).
"""

import datetime as dt
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["HARNESS_MODEL"] = "medium-omat-0"
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from ase.build import bulk  # noqa: E402

from harness.compute import GPA  # noqa: E402

CELLS = [("Cu", "Ir"), ("Cu", "Rh"), ("Pd", "Ir"), ("Au", "Ir"), ("Ag", "Ir"), ("Ag", "Rh"),  # A3B with Ir/Rh
         ("Cu", "Au"), ("Pt", "Cu")]  # controls without Ir/Rh; order = MACE |K| (PBE is slow, strongest first)
S = 0.02
SYM_DONE = {"Cu3Ir": ("g-", "t-")}  # computed both signs here; used as the symmetry check
METHOD = "dft"
DENSE = "dense" in sys.argv
KSP = 0.08 if DENSE else 0.10
if DENSE:
    CELLS = [("Cu", "Ir"), ("Ag", "Rh")]
pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]

from harness import dft  # noqa: E402

NP = int(os.environ.get("HISO_NP", "2"))
ST = {}


def energy(atoms, tag):
    return dft.run_pw(atoms, f"hiso2{'d' if DENSE else ''}/{tag}", ST["s"]).get_potential_energy() / len(atoms)

DEF = {"0": np.eye(3), "g+": np.eye(3) + S * np.outer([1, 0, 0], [0, 1, 0]),
       "g-": np.eye(3) - S * np.outer([1, 0, 0], [0, 1, 0]),
       "t+": np.diag([np.exp(S), np.exp(-S), 1.0]), "t-": np.diag([np.exp(-S), np.exp(S), 1.0])}


def strained(symbols, v, F):
    a = bulk("Cu", "fcc", a=4.0, cubic=True)
    a.symbols = list(symbols)
    a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
    a.set_cell(a.cell @ F.T, scale_atoms=True)
    return a


OUT = ROOT / "data" / f"hiso_l12_dft_v2{'_dense' if DENSE else ''}.csv"
done = set(pd.read_csv(OUT)["cell"]) if OUT.exists() else set()
for A, B in CELLS:
    name = f"{A}3{B}"
    if name in done:
        continue
    v = 0.75 * pv[A] + 0.25 * pv[B]
    vt = f"{v:.3f}"
    ST["s"] = dft.Settings(kspacing=KSP, np=NP, ecut_elements=(A, B),
                           kpts=dft.kgrid(strained([B, A, A, A], v, np.eye(3)), KSP))
    em = {}
    for k, F in DEF.items():
        if k in ("g-", "t-") and k not in SYM_DONE.get(name, ()):  # cubic L1_2: y -> -y and x <-> y are symmetries
            continue
        e_ab = energy(strained([B, A, A, A], v, F), f"{name}_{k}_v{vt}")
        e_a = energy(strained([A] * 4, v, F), f"{A}_{name}_{k}_v{vt}")
        e_b = energy(strained([B] * 4, v, F), f"{B}_{name}_{k}_v{vt}")
        em[k] = e_ab - 0.75 * e_a - 0.25 * e_b
    em.setdefault("g-", em["g+"])
    em.setdefault("t-", em["t+"])
    c44 = (em["g+"] + em["g-"] - 2 * em["0"]) / (2 * S**2)   # E = c s^2
    cp = (em["t+"] + em["t-"] - 2 * em["0"]) / (2 * S**2)
    r = {"cell": name, "method": "dft_v2", "kpts": "x".join(map(str, ST["s"].kpts)), "V": v, "E_mix": em["0"], "K44": 2 * c44 / v * GPA, "Kp": cp / (2 * v) * GPA,
         "time": dt.datetime.now().isoformat(timespec="seconds")}
    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
    print(name, f"E_mix {em['0']*1000:+7.1f} meV  K44 {r['K44']:+7.2f}  Kp {r['Kp']:+7.2f} GPa", flush=True)
cell,method,kpts,V,E_mix,K44,Kp,time
Cu3Ir,dft_v2,18x18x18,12.570930746342615,0.01557259878734385,-54.74691675055384,-57.38539420465976,2026-10-31T20:37:36
Cu3Rh,dft_v2,18x18x18,12.466046926632401,-0.008250364034438462,-34.78715578271392,-37.42050958615326,2026-11-01T00:29:27
Pd3Ir,dft_v2,17x17x17,15.090881358268899,0.1289190757158849,6.644682704355299,-5.321163067938075,2026-11-01T02:08:10
Au3Ir,dft_v2,16x16x16,17.01764835574268,0.2510520404655381,-32.3727567076859,-33.84664741248657,2026-11-01T04:10:20
Ag3Ir,dft_v2,16x16x16,16.958300131244606,0.3207653609897534,-15.691494965360748,-29.08829505587699,2026-11-01T05:55:23
Ag3Rh,dft_v2,16x16x16,16.853416311534392,0.13165629432899095,-7.037878294590145,-17.96665812599528,2026-11-01T07:00:57
Cu3Au,dft_v2,17x17x17,13.473338466415823,-0.32097306888442745,-5.5914144369890275,6.832279696830556,2026-11-01T09:14:36
Pt3Cu,dft_v2,17x17x17,14.643363572487065,-0.1959511480412175,23.828501484675826,9.127699571762257,2026-11-01T11:42:51
cell,method,V,E_mix,K44,Kp,time
Cu3Ir,mace,12.570930746342615,0.007922966900131723,-60.480692622198305,-73.26377353391179,2026-10-31T01:09:46
Au3Ir,mace,17.01764835574268,0.1980301038873411,3.2063930667627205,-11.842309290055715,2026-10-31T01:09:48
Ag3Ir,mace,16.958300131244606,0.2825353511949964,-1.6943321412785415,-14.231864501045454,2026-10-31T01:09:49
Cu3Rh,mace,12.466046926632401,-0.022119947332217782,-30.506540090852575,-36.0052297807868,2026-10-31T01:09:50
Ag3Rh,mace,16.853416311534392,0.10310185849292175,1.1388933635108385,-3.20914102683622,2026-10-31T01:09:51
Pd3Ir,mace,15.090881358268899,0.13232800965835922,-14.347444565088127,-12.80101099840087,2026-10-31T01:09:53
Cu3Au,mace,13.473338466415823,-0.3208622345675217,-10.161705065912527,1.0358830436384283,2026-10-31T01:09:55
Pt3Cu,mace,14.643363572487065,-0.19250834620571533,9.76255799019013,9.89059517207147,2026-10-31T01:09:56


    Directory: C:\Users\can02\Projects\AI driven Science\.venv\Scripts


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
-a----        28.10.2026     10:23         274424 python.exe                                                           



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$i=0; Get-Content paper/draft_v3.md -Encoding utf8 | ForEach-Object { $i++; if(($i -le 80) -or ($i -ge 160 -and $i -le 190)){"${i}: $_"} }; Get-ChildItem data/dft_runs/hiso2 | Select-Object Name; git status --short' in C:\Users\can02\Projects\AI driven Science
 exited 1 in 848ms:
1: # Binary shear curvatures read at the alloy's volume: a preregistered test of a transfer rule for fcc solid solutions with machine-learned potentials
2: 
3: Muhammet Can Ergani�
4: Independent researcher, METU graduate, Ankara, T�rkiye. ORCID 0009-0001-1397-6366
5: 
6: Draft v3, 2026-11-01, after the Astra audit of v2 (`.orchestra/audits/draft_v2_astra.md`). Numerical provenance is
7: given through ledger entries in `claims/claims.jsonl` and named analysis files. Exploratory calculations are marked
8: as such and kept apart from preregistered tests. The only open item before submission is the archive DOI.
9: 
10: ## Abstract
11: 
12: Building on established binary extrapolation, volume-dependent interactions and tensorial cluster expansions, we test
13: one specific, fixed-coefficient prescription for the clamped mixing part of the tetragonal shear curvature K' of
14: random fcc solid solutions: each equiatomic binary curvature is evaluated at the multicomponent alloy's Vegard volume
15: rather than at the binary's own. For 3 to 5 component alloys of Ag, Au, Co, Cu, Ir, Ni, Pd, Pt and Rh evaluated with
16: the MACE machine-learned potential, this halves the error of the same pair sum taken at the binary volumes (4.2 to
17: 1.9 GPa on 94 compositions; 4.8 to 2.2 GPa on 1200 further compositions under a second MACE model). The transfer is
18: not exact. The refit slope is 1.08 under one model and 1.14 (90% CI 1.10 to 1.18) under the other, and in
19: exploratory splits it rises with the size mismatch between components, so the rule under-predicts alloys with large
20: volume differences. For the C44-type shear K44 the rule is weak. Correlated residuals of the two shears persist
21: across independent target cells and after removal of the clamped pre-stress, which supports a composition-dependent
22: shared residual, but error shared through the binary references remains an unresolved alternative. Primary tests
23: were entered in an append-only ledger, with simulated power, before their new target calculations, and passing
24: results received separate code-and-data audits by a second language model. All targets are machine-learned-potential
25: energies; first-principles validation is pending and is the main limit of this work.
26: 
27: ## 1. Introduction
28: 
29: 1. Liu et al. (2010) developed CALPHAD-style models for elastic coefficients, and Marker et al. (2017) applied this
30:    approach to bcc Ti alloys using relaxed first-principles inputs, each at its own equilibrium volume. Marker
31:    reported average Young's modulus deviations of about 7 GPa with binary parameters and 5 GPa with ternary terms for
32:    13 multicomponent alloys. Huhn et al. (2014) compared alloy moduli with effective-medium estimates based on pure
33:    elements. Linton and Aidhy (2023) trained ML models on binaries, and Mirzaee et al. (2024) a CNN on charge densities
34:    including binary and ternary data. These studies motivate testing how shear transfers from simpler systems.
35: 2. Volume-dependent effective cluster interactions (Asta et al. 1992; Geng et al. 2005), the alloy-volume formalism
36:    for binaries (Ferreira et al. 1987, 1989) and tensorial or strain-dependent cluster expansions (van de
37:    Walle 2008; Behara et al. 2023, which includes shear strain variables) are established. Our search did not
38:    identify the specific fixed-coefficient transfer tested here: clamped multicomponent mixing K' estimated from
39:    equiatomic binary curvatures at the alloy Vegard volume. This is a search-bounded statement, not proof that no
40:    prior work exists.
41: 3. Formally the rule is a pair-truncated tensorial cluster expansion or a zeroth-order Redlich-Kister sum with a
42:    specified evaluation volume. The contribution is this prescription and its tested performance: (i) where the
43:    binary terms are evaluated, (ii) a preregistered test of that choice, (iii) where it stops working, and (iv) how
44:    the C44-type shear differs. In a different field, Hofgard et al. (2026) obtained large gains by changing the
45:    target representation of an ML model while keeping the model. Here the target stays K'_mix; what changes is the
46:    volume at which unchanged binary inputs are read.
47: 
48: ## 2. Methods
49: 
50: **Cells.** Random fcc solid solutions in 108-atom cubic supercells (3x3x3), built by randomly shuffling species over
51: the sites without SQS optimisation. Atoms stay on ideal sites (no ionic or cell relaxation). The volume is fixed at
52: the composition's Vegard volume V0 from the model's pure-element volumes.
53: 
54: **Observable.** E_mix(V, F) = E_alloy - sum x_i E_i per atom, every pure reference at the same volume and the same
55: deformation F. K' from F = diag(e^t, e^-t, 1), K44 from F = I + g e_x e_y, five amplitudes in [-0.01, 0.01],
56: quadratic fit, K' = c2/(2V), K44 = 2 c2/V. The target generators use the cell's actual integer-count fractions for
57: the pure references; the historical exploratory a2 dataset is an exception (Section 3.1). With tensile-positive
58: mixing stress and Green-Lagrange energy coefficients, K44 = C^L_xyxy + s_yy and K' = (C^L_xxxx + C^L_yyyy -
59: 2 C^L_xxyy)/4 + (s_xx + s_yy)/2. The elastic part reduces to (C11 - C12)/2 only in the cubic limit, and subtracting
60: the stress terms does not give relaxed, zero-pressure elastic constants.
61: 
62: **Binary inputs.** All 36 equiatomic pairs, 13 log-volume points ln(V/V_ij) in [-0.4, 0.4], cubic spline per pair.
63: The omat grid uses seeds 0 to 2; the first mpa grid seed 0; the 1200-composition test two three-seed panels (20 to 22,
64: 23 to 25).
65: 
66: **Rule.** K'_mix(alloy) = sum_{i<j} 4 x_i x_j K'_ij(ln V0/V_ij). Baselines: the same sum at ln V0/V_ij = 0 ("pair at
67: V_ij"), and two own-volume Muggianu analogues built from pure-element curvatures (Section 3.4).
68: 
69: **Seeds.** The site permutation of a cell depends only on (seed, n), so cells with equal seed and size share a
70: permutation field. The original h3 and hm_fresh shear tests used target seed 0 and binary seeds 0 to 2, and the first
71: mpa model swap used seed 0 for both; these historical tests shared a permutation field between targets and inputs.
72: After this was found (Section 4) target and binary seeds were separated: the floor tests use target seeds of 100 and
73: above, and the 1200-composition test uses unique target seeds from 10000 with binary panels 20 to 25. Omat seed-split
74: checks kept the K' improvement (gain 0.55 to 0.58, k 1.07 to 1.10) but showed sensitivity for K44.
75: 
76: **Models.** MACE medium-omat-0 (Batatia et al.), calibrated in this project on 14 cubic metals (fcc B, G MAE about
77: 12%, e5ef5a57a3). Second model: medium-mpa-0, with omat geometry (V_ij, V0) so that only the energies change.
78: 
79: **Protocol.** Hypotheses come from two LLM agents (GPT-6-Astra via Codex, Claude Opus), who see the problem, the
80: limits and the training data, never sealed holdouts. Before the new target calculations of a primary test, the
160: |---|---|---|---|
161: | Integer-count reference mismatch | R1 audits | up to 56.6 meV/atom in the Al-free set; 60.7 including Al | energy references corrected; historical a2 shear and some derived columns remain uncorrected |
162: | PBE cutoff mismatch | audit, 7e0ff785d1 | 30.7 meV/atom shift in the Pt reference; correction checked to 0.002 meV/atom | alloy-matched cutoffs; ordered-cell L1 check changed from FAIL to PASS |
163: | Holdout used for model selection | audit, d26bd71285 | 113 of 207 pooled energy rows were selection data | "two independent holdouts" withdrawn; hm_fresh-only RMSE 36.4 to 13.1 meV/atom |
164: | Shared random-site permutation between targets and binaries | S2 audit (Opus), confirmed by Astra; e7d441a4eb | K44 gains inflated by about 0.06 to 0.18 | historical results amended; 9cfc8edaf0 withdrawn before its targets were read and rerun with disjoint seeds |
165: | Weak baseline made a linearised energy rule look new | audit | 13.3 vs 11.5 meV/atom | energy rule demoted |
166: | Power simulation treated a composition-level residual as cell noise | audit of 88b9465108 | reported simulated power 1.0 under an optimistic noise model | audit identified the flaw; the archived preregistration script still uses the original noise model |
167: | Original power simulation covered only the correlation gate | audit of ede47f1d65, 7ceca1b668 | full-gate audit simulation: 5000/5000 passes under the simulated alternative and 0/5000 under the simulated null | additional simulation recorded; rates remain conditional on the assumed noise models |
168: | PBE runs with nspin 1 still magnetize Co and Ni | Astra, S3 | not used in any result | Co/Ni PBE blocked until fixed |
169: 
170: ## 5. Discussion and limits
171: 
172: 1. Model only. Every target is a MACE energy. The slope already differs between datasets and models (1.08 to 1.14).
173:    In an eight-cell ordered L1_2 A3B diagnostic (preliminary, subject to convergence checks and audit), Au3Ir has
174:    K44 = -32.4 GPa in PBE and +3.2 GPa in MACE; sign agreement is 8/8 for K' and 5/8 for K44. This does not validate
175:    transfer to random alloys. An L3 test needs at least 15 independent DFT or experimental rows from composition
176:    families absent from training, with the rule and coefficient frozen beforehand. This is future work.
177: 2. Clamped, unrelaxed cells: K'_mix is not the measured C'. On 43 previously examined equiatomic ternaries, relaxed-
178:    binary Muggianu gives C' RMSE 3.08 GPa and a volume-transfer chain 2.53 GPa (gain 0.18, p about 0.08). The chain
179:    also uses the measured relaxed target volume. This exploratory comparison shows neither a significant improvement
180:    nor equivalence at zero pressure.
181: 3. The rule under-predicts at large size mismatch (Section 3.5). A correction has not been tested.
182: 4. fcc late transition and noble metals only. None of the three calibrated MACE models passed the bcc shear
183:    criterion in this project.
184: 5. The rule is a regular-solution or tensorial-CE truncation with a specified volume; we do not claim a new law.
185: 
186: ## Data and code
187: 
188: The ledger, literature log, harness, scripts, data tables, audit records and agent transcripts are in the
189: reproducibility archive (built by `scripts/build_repro.py`, SHA256 manifest included). The exploratory baseline and
190: relaxed-chain inputs of Sections 3.4 and 5.2 are in `data/archive_s2_opus_scratch` with their scripts. The sealed holdout and raw

fatal: not a git repository (or any of the parent directories): .git
Name               
----               
Ag3Ir_0_v16.958    
Ag3Ir_g+_v16.958   
Ag3Ir_t+_v16.958   
Ag3Rh_0_v16.853    
Ag3Rh_g+_v16.853   
Ag3Rh_t+_v16.853   
Ag_Ag3Ir_0_v16.958 
Ag_Ag3Ir_g+_v16.958
Ag_Ag3Ir_t+_v16.958
Ag_Ag3Rh_0_v16.853 
Ag_Ag3Rh_g+_v16.853
Ag_Ag3Rh_t+_v16.853
Au3Ir_0_v17.018    
Au3Ir_g+_v17.018   
Au3Ir_t+_v17.018   
Au_Au3Ir_0_v17.018 
Au_Au3Ir_g+_v17.018
Au_Au3Ir_t+_v17.018
Au_Cu3Au_0_v13.473 
Au_Cu3Au_g+_v13.473
Au_Cu3Au_t+_v13.473
Cu3Au_0_v13.473    
Cu3Au_g+_v13.473   
Cu3Au_t+_v13.473   
Cu3Ir_0_v12.571    
Cu3Ir_g+_v12.571   
Cu3Ir_g-_v12.571   
Cu3Ir_t+_v12.571   
Cu3Ir_t-_v12.571   
Cu3Rh_0_v12.466    
Cu3Rh_g+_v12.466   
Cu3Rh_t+_v12.466   
Cu_Cu3Au_0_v13.473 
Cu_Cu3Au_g+_v13.473
Cu_Cu3Au_t+_v13.473
Cu_Cu3Ir_0_v12.571 
Cu_Cu3Ir_g+_v12.571
Cu_Cu3Ir_g-_v12.571
Cu_Cu3Ir_t+_v12.571
Cu_Cu3Ir_t-_v12.571
Cu_Cu3Rh_0_v12.466 
Cu_Cu3Rh_g+_v12.466
Cu_Cu3Rh_t+_v12.466
Cu_Pt3Cu_0_v14.643 
Cu_Pt3Cu_g+_v14.643
Cu_Pt3Cu_t+_v14.643
Ir_Ag3Ir_0_v16.958 
Ir_Ag3Ir_g+_v16.958
Ir_Ag3Ir_t+_v16.958
Ir_Au3Ir_0_v17.018 
Ir_Au3Ir_g+_v17.018
Ir_Au3Ir_t+_v17.018
Ir_Cu3Ir_0_v12.571 
Ir_Cu3Ir_g+_v12.571
Ir_Cu3Ir_g-_v12.571
Ir_Cu3Ir_t+_v12.571
Ir_Cu3Ir_t-_v12.571
Ir_Pd3Ir_0_v15.091 
Ir_Pd3Ir_g+_v15.091
Ir_Pd3Ir_t+_v15.091
Pd3Ir_0_v15.091    
Pd3Ir_g+_v15.091   
Pd3Ir_t+_v15.091   
Pd_Pd3Ir_0_v15.091 
Pd_Pd3Ir_g+_v15.091
Pd_Pd3Ir_t+_v15.091
Pt3Cu_0_v14.643    
Pt3Cu_g+_v14.643   
Pt3Cu_t+_v14.643   
Pt_Pt3Cu_0_v14.643 
Pt_Pt3Cu_g+_v14.643
Pt_Pt3Cu_t+_v14.643
Rh_Ag3Rh_0_v16.853 
Rh_Ag3Rh_g+_v16.853
Rh_Ag3Rh_t+_v16.853
Rh_Cu3Rh_0_v12.466 
Rh_Cu3Rh_g+_v12.466
Rh_Cu3Rh_t+_v12.466



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "@'
from pathlib import Path
for f in ['scripts/hiso_l12_v2.py','harness/dft.py']:
 print('FILE',f)
 for i,l in enumerate(Path(f).read_text(encoding='utf-8').splitlines(),1):
  if f.startswith('scripts') or i<=122: print(f'{i}: {l}')
print('INPUT')
print(Path('data/dft_runs/hiso2/Cu3Ir_g+_v12.571/pw.in').read_text())
p=Path('data/dft_runs/hiso2/Cu3Ir_g+_v12.571/pw.out')
ls=p.read_text().splitlines()
for i,l in enumerate(ls,1):
 if any(x in l.lower() for x in ['convergence','total energy','accuracy','warning','job done','kinetic-energy cutoff','charge density cutoff','smearing','number of k points']): print(i,l)
print('GPA definition')
for i,l in enumerate(Path('harness/compute.py').read_text().splitlines(),1):
 if 'GPA' in l: print(i,l)
'@ | ./.venv/Scripts/python.exe -B -X utf8 -" in C:\Users\can02\Projects\AI driven Science
 exited 1 in 653ms:
Unable to create process using '"C:\Users\can02\AppData\Local\Programs\Python\Python312\python.exe" -B -X utf8 -'

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Command python*,py*,wsl* -ErrorAction SilentlyContinue | Select-Object Name,Source; Get-Content data/dft_runs/hiso2/Cu3Ir_g+_v12.571/pw.in; rg -n "convergence|total energy|accuracy|WARNING|Warning|JOB DONE|kinetic-energy cutoff|charge density cutoff|smearing|number of k points" data/dft_runs/hiso2/Cu3Ir_g+_v12.571/pw.out; rg -n "GPA" harness/compute.py; Get-ChildItem C:/Users/can02/AppData/Local/Programs/Python -ErrorAction SilentlyContinue; Get-ChildItem C:/Python*,C:/Users/can02/.local/bin -ErrorAction SilentlyContinue | Select-Object Name,FullName' in C:\Users\can02\Projects\AI driven Science
 succeeded in 4289ms:

21:Warning: card &CELL ignored
22:Warning: card &FCP ignored
23:Warning: card &RISM ignored
54:     kinetic-energy cutoff     =     112.5000  Ry
55:     charge density cutoff     =     900.0000  Ry
56:     scf convergence threshold =      4.0E-10
124:     number of k points=  1640  Marzari-Vanderbilt smearing, width (Ry)=  0.0100
156:     total energy              =    -820.82332753 Ry
157:     estimated scf accuracy    <       1.25956622 Ry
167:     total energy              =    -820.98389446 Ry
168:     estimated scf accuracy    <       0.19575328 Ry
178:     total energy              =    -821.02221000 Ry
179:     estimated scf accuracy    <       0.22208637 Ry
189:     total energy              =    -821.03870343 Ry
190:     estimated scf accuracy    <       0.00711923 Ry
200:     total energy              =    -821.03996146 Ry
201:     estimated scf accuracy    <       0.00449082 Ry
211:     total energy              =    -821.04035209 Ry
212:     estimated scf accuracy    <       0.00019832 Ry
222:     total energy              =    -821.04037466 Ry
223:     estimated scf accuracy    <       0.00010012 Ry
233:     total energy              =    -821.04038674 Ry
234:     estimated scf accuracy    <       0.00000488 Ry
244:     total energy              =    -821.04038888 Ry
245:     estimated scf accuracy    <       0.00000091 Ry
255:     total energy              =    -821.04038897 Ry
256:     estimated scf accuracy    <       0.00000026 Ry
266:     total energy              =    -821.04038888 Ry
267:     estimated scf accuracy    <       0.00000105 Ry
277:     total energy              =    -821.04038899 Ry
278:     estimated scf accuracy    <          4.8E-09 Ry
288:     total energy              =    -821.04038899 Ry
289:     estimated scf accuracy    <          8.0E-10 Ry
305:!    total energy              =    -821.04038899 Ry
306:     estimated scf accuracy    <          1.4E-10 Ry
307:     smearing contrib. (-TS)   =       0.00002381 Ry
310:     The total energy is F=E-TS. E is the sum of the following terms:
317:     convergence has been achieved in  14 iterations
392:   JOB DONE.
18:GPA = 160.21766208  # eV/A^3 -> GPa
95:            sig.append(strained.get_stress(voigt=True) * GPA)  # ASE: tensile stress positive
Name                     Source                           
----                     ------                           
wsl.exe                  C:\WINDOWS\system32\wsl.exe      
wslconfig.exe            C:\WINDOWS\system32\wslconfig.exe
&CONTROL
   calculation      = 'scf'
   tstress          = .true.
   tprnfor          = .true.
   outdir           = '/tmp/qe/hiso2__Cu3Ir_g+_v12.571'
   forc_conv_thr    = 0.0001
   disk_io          = 'low'
   pseudo_dir       = '/home/can02/pseudo/sssp_eff_1.3'
/
&SYSTEM
   ecutwfc          = 112.5
   ecutrho          = 900.0
   occupations      = 'smearing'
   degauss          = 0.01
   smearing         = 'mv'
   nspin            = 1
   ntyp             = 2
   nat              = 4
   ibrav            = 0
/
&ELECTRONS
   conv_thr         = 4e-10
   mixing_beta      = 0.3
/
&IONS
/
&CELL
/
&FCP
/
&RISM
/
ATOMIC_SPECIES
Ir 192.217 Ir_pbe_v1.2.uspp.F.UPF
Cu 63.546 Cu.paw.z_11.ld1.psl.v1.0.0-low.upf

K_POINTS automatic
18 18 18  0 0 0

CELL_PARAMETERS angstrom
3.69098665569636 0.00000000000000 0.00000000000000
0.07381973311393 3.69098665569636 0.00000000000000
0.00000000000000 0.00000000000000 3.69098665569636

ATOMIC_POSITIONS angstrom
Ir 0.0000000000 0.0000000000 0.0000000000  
Cu 0.0369098666 1.8454933278 1.8454933278  
Cu 1.8454933278 0.0000000000 1.8454933278  
Cu 1.8824031944 1.8454933278 0.0000000000  

claude.exe                                                
jupyter-lab.exe                                           
jupyter-labextension.exe                                  
jupyter-labhub.exe                                        
ruff.exe                                                  



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '
$records = @(Get-ChildItem data/dft_runs/hiso2 -Directory | ForEach-Object {
 $d=$_
 $ins=Get-Content -LiteralPath (Join-Path $d.FullName '"'pw.in') -Raw
 "'$outs=Get-Content -LiteralPath (Join-Path $d.FullName '"'pw.out') -Raw
 "'$errs=Get-Content -LiteralPath (Join-Path $d.FullName '"'pw.err') -Raw -ErrorAction SilentlyContinue
 "'$energy=[regex]::Matches($outs,'"'"'!'"\\s+total energy\\s*=\\s*([-\\d.]+)')
 "'$acc=[regex]::Matches($outs,'"'estimated scf accuracy\\s*<\\s*([\\d.Ee+-]+)')
 [pscustomobject]@{
 name="'$d.Name
 energyRy=$energy[$energy.Count-1].Groups[1].Value
 energyCount=$energy.Count
 accuracyRy=$acc[$acc.Count-1].Groups[1].Value
 done=$outs.Contains('"'JOB DONE')
 converged="'$outs.Contains('"'convergence has been achieved')
 badConvergence="'$outs.Contains('"'convergence NOT achieved')
 warnings=@("'$outs -split "'"\\r?\\n\" | Where-Object {"'$_ -match '"'(?i)warning|error|negative|not converged|not achieved'})
 err="'$errs
 ecutwfc=[regex]::Match($ins,'"'ecutwfc\\s*=\\s*([\\d.]+)').Groups[1].Value
 ecutrho=[regex]::Match("'$ins,'"'ecutrho\\s*=\\s*([\\d.]+)').Groups[1].Value
 degauss=[regex]::Match("'$ins,'"'degauss\\s*=\\s*([\\d.]+)').Groups[1].Value
 conv_thr=[regex]::Match("'$ins,'"'conv_thr\\s*=\\s*([\\d.eE+-]+)').Groups[1].Value
 kgrid=[regex]::Match("'$ins,'"'K_POINTS automatic\\s*\\r?\\n(["'^'"\\r\\n]+)').Groups[1].Value
 matrix=[regex]::Match("'$ins,'"'CELL_PARAMETERS angstrom\\s*\\r?\\n((?:["'^'"\\r\\n]+\\r?\\n){3})').Groups[1].Value
 positions=[regex]::Match("'$ins,'"'ATOMIC_POSITIONS angstrom\\s*\\r?\\n((?:["'^'"\\r\\n]+\\r?\\n){4})').Groups[1].Value
 cutOutput=[regex]::Match("'$outs,'"'kinetic-energy cutoff\\s*=\\s*([\\d.]+)').Groups[1].Value
 inputTime="'$d.LastWriteTime.ToString('"'s')
 }
})
"'$records | ConvertTo-Json -Depth 5 -Compress
' in C:\Users\can02\Projects\AI driven Science
 succeeded in 3061ms:
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 

codex
CSV’deki altı hücre seçimi doğru. Ham çıktılarda ise “hiç uyarı yok” ifadesi doğru değil: QE, boş `&CELL`, `&FCP` ve `&RISM` bloklarını yok saydığına dair uyarılar veriyor. Bunların yanında yakınsama hatası bulunup bulunmadığını ve enerjilerden eğriliklerin yeniden üretildiğini kontrol ediyorum.

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '
$records = @(Get-ChildItem data/dft_runs/hiso2 -Directory | ForEach-Object {
 $d=$_
 $ins=Get-Content -LiteralPath (Join-Path $d.FullName '"'pw.in') -Raw
 "'$outs=Get-Content -LiteralPath (Join-Path $d.FullName '"'pw.out') -Raw
 "'$errs=Get-Content -LiteralPath (Join-Path $d.FullName '"'pw.err') -Raw -ErrorAction SilentlyContinue
 "'$energies=[regex]::Matches($outs,'"'"'!'"\\s+total energy\\s*=\\s*([-\\d.]+)')
 "'$acc=[regex]::Matches($outs,'"'estimated scf accuracy\\s*<\\s*([\\d.Ee+-]+)')
 [pscustomobject]@{
 name="'$d.Name
 energyRy=$energies[$energies.Count-1].Groups[1].Value
 energyCount=$energies.Count
 accuracyRy=$acc[$acc.Count-1].Groups[1].Value
 done=$outs.Contains('"'JOB DONE')
 converged="'$outs.Contains('"'convergence has been achieved')
 badConvergence="'$outs.Contains('"'convergence NOT achieved')
 warnings=@("'$outs -split "'"\\r?\\n\" | Where-Object {"'$_ -match '"'(?i)warning|error|negative|not converged|not achieved'})
 err="'$errs
 ecutwfc=[regex]::Match($ins,'"'ecutwfc\\s*=\\s*([\\d.]+)').Groups[1].Value
 ecutrho=[regex]::Match("'$ins,'"'ecutrho\\s*=\\s*([\\d.]+)').Groups[1].Value
 degauss=[regex]::Match("'$ins,'"'degauss\\s*=\\s*([\\d.]+)').Groups[1].Value
 conv_thr=[regex]::Match("'$ins,'"'conv_thr\\s*=\\s*([\\d.eE+-]+)').Groups[1].Value
 kgrid=[regex]::Match("'$ins,'"'K_POINTS automatic\\s*\\r?\\n(["'^'"\\r\\n]+)').Groups[1].Value
 matrix=[regex]::Match("'$ins,'"'CELL_PARAMETERS angstrom\\s*\\r?\\n((?:["'^'"\\r\\n]+\\r?\\n){3})').Groups[1].Value
 positions=[regex]::Match("'$ins,'"'ATOMIC_POSITIONS angstrom\\s*\\r?\\n((?:["'^'"\\r\\n]+\\r?\\n){4})').Groups[1].Value
 cutOutput=[regex]::Match("'$outs,'"'kinetic-energy cutoff\\s*=\\s*([\\d.]+)').Groups[1].Value
 }
})
"'$records | ConvertTo-Json -Depth 5 -Compress
' in C:\Users\can02\Projects\AI driven Science
 succeeded in 2412ms:
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:18 char:13
+  warnings=@($outs -split "\r?\n" | Where-Object {$_ -match '(?i)warni ...
+             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "rg -n \"create_units|units\\[.Ry|energy =|free_energy\" .venv/Lib/site-packages/ase/io/espresso.py; rg -n \"2006|_hplanck|_e|_me|_eps0|Rydberg|Ry =\" .venv/Lib/site-packages/ase/units.py; rg -n \"hiso|6cb3c2a936\" claims/claims.jsonl .orchestra/audits scripts -g '*.md' -g '*.py' -g '*.jsonl'" in C:\Users\can02\Projects\AI driven Science
 succeeded in 313ms:
37:from ase.units import create_units
41:units = create_units('2006')
231:        energy = find_thing(_get_energy, indexes[_PW_TOTEN])
351:        # its value must be assigned to free_energy.
363:                                        free_energy=energy,
2073:    return float(pwo_lines[energy_index].split()[-2]) * units['Ry']
2088:    return np.array(forces) * units['Ry'] / units['Bohr']
2097:    stress *= -1 * units['Ry'] / (units['Bohr'] ** 3)
40:             '_hplanck': 6.6260755e-34,     # Planck constant, J s
41:             '_e': 1.60217733e-19,          # elementary charge
42:             '_me': 9.1093897e-31,          # electron mass
53:             '_hplanck': 6.62606876e-34,
54:             '_e': 1.602176462e-19,
55:             '_me': 9.10938188e-31,
66:             '_hplanck': 6.6260693e-34,
67:             '_e': 1.60217653e-19,
68:             '_me': 9.1093826e-31,
74:    # CODATA 2006 taken from
76:    '2006': {'_c': 299792458.,
79:             '_hplanck': 6.62606896e-34,
80:             '_e': 1.602176487e-19,
81:             '_me': 9.10938215e-31,
92:             '_hplanck': 6.62606957e-34,
93:             '_e': 1.602176565e-19,
94:             '_me': 9.10938291e-31,
105:             '_hplanck': 6.626_070_040e-34,  # +/- 0.000_000_081e-34
106:             '_e': 1.602_176_6208e-19,       # +/- 0.000_000_0098e-19
107:             '_me': 9.109_383_56e-31,        # +/- 0.000_000_11e-31
118:             '_hplanck': 6.626_070_15e-34,   # Exact
119:             '_e': 1.602_176_634e-19,        # Exact
120:             '_me': 9.109_383_7015e-31,      # +/- 0.000_000_0028e-31
131:             '_hplanck': 6.626_070_15e-34,   # Exact
132:             '_e': 1.602_176_634e-19,        # Exact
133:             '_me': 9.109_383_7139e-31,      # +/- 0.000_000_0028e−31
157:        * '2006'
184:    u['_eps0'] = (1 / u['_mu0'] / u['_c']**2)  # permittivity of vacuum
185:    u['_hbar'] = u['_hplanck'] / (2 * pi)  # Planck constant / 2pi, J s
189:    u['Bohr'] = (4e10 * pi * u['_eps0'] * u['_hbar']**2 /
190:                 u['_me'] / u['_e']**2)  # Bohr radius
193:    u['Hartree'] = (u['_me'] * u['_e']**3 / 16 / pi**2 /
194:                    u['_eps0']**2 / u['_hbar']**2)
195:    u['kJ'] = 1000.0 / u['_e']
198:    u['Rydberg'] = 0.5 * u['Hartree']
199:    u['Ry'] = u['Rydberg']
202:    u['second'] = 1e10 * sqrt(u['_e'] / u['_amu'])
205:    u['kB'] = u['_k'] / u['_e']  # Boltzmann constant, eV/K
207:    u['Pascal'] = (1 / u['_e']) / 1e30  # J/m^3
211:    u['Debye'] = 1.0 / 1e11 / u['_e'] / u['_c']
212:    u['alpha'] = (u['_e']**2 / (4 * pi * u['_eps0']) /
214:    u['invcm'] = (100 * u['_c'] * u['_hplanck'] /
215:                  u['_e'])  # cm^-1 energy unit
219:    u['_aut'] = u['_hbar'] / (u['alpha']**2 * u['_me'] * u['_c']**2)
221:    u['_auv'] = u['_e']**2 / u['_hbar'] / (4 * pi * u['_eps0'])
223:    u['_auf'] = u['alpha']**3 * u['_me']**2 * u['_c']**3 / u['_hbar']
225:    u['_aup'] = u['alpha']**5 * u['_me']**4 * u['_c']**5 / u['_hbar']**3
233:    u['A'] = 1.0 / u['_e'] / u['s']  # ampere
236:    u['C'] = 1.0 / u['_e']  # Coulomb = A * s
245:(_Grav, _Nav, _amu, _auf, _aup, _aut, _auv, _c, _e, _eps0,
246: _hbar, _hplanck, _k, _me, _mp, _mu0, alpha, eV, fs, invcm,
248: Bohr, C, Debye, GPa, Ha, Hartree, J, Pascal, bar, Ry, Rydberg) = [0.0] * 44
claims/claims.jsonl:33:{"id": "6cb3c2a936", "time": "2026-10-31T01:09:25", "level": "L0", "claim": "H-iso PBE check (scripts/hiso_l12.py): cubic A3B L1_2 cells (Cu3Ir Au3Ir Ag3Ir Cu3Rh Ag3Rh Pd3Ir; controls Cu3Au Pt3Cu), clamped Vegard volume, pure refs same V and F, strain 0.02, PBE kspacing 0.10. H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.", "parent": null, "evidence": {"scripts/hiso_l12.py": "c76da785e56fb704"}, "notes": "registered before any hiso_l12 output; H-iso survived on MACE random alloys (n=60, r 0.95, also after removing the -P stress term)"}
.orchestra/audits\6cb3c2a936_prompt.md:3:Criterion (ledger claims/claims.jsonl id 6cb3c2a936, registered before any output): H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.
.orchestra/audits\6cb3c2a936_prompt.md:5:Code: scripts/hiso_l12_v2.py (v2 fixes the S1 audit: shared cutoff and k-grid for alloy and pure refs), harness/dft.py. Results: data/hiso_l12_dft_v2.csv (PBE, 8 cells), data/hiso_l12_mace.csv. Raw runs under data/dft_runs/hiso2/. A dense-k check (kspacing 0.08, Cu3Ir and Ag3Rh) is running now and is not available.
.orchestra/audits\draft_v3_astra.md:517:| 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
.orchestra/audits\draft_v3_astra.md:518:| 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |
.orchestra/audits\draft_v3_astra.md:524:- **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.
.orchestra/audits\draft_v3_astra.md:528:1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
.orchestra/audits\draft_v3_astra.md:579:12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\draft_v3_astra.md:685:- For DFT finite differences, pin every strain partner to the unstrained k-mesh, use same-size/alloy-matched references and `ecut_elements`, then rerun property-specific controls. `scripts/hiso_l12_v2.py` implements shared cutoffs/fixed grids; old H-iso results remain non-evidential until rerun. [Task 2]
.orchestra/audits\draft_v3_astra.md:839:.orchestra/LESSONS.md:30:12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\draft_v3_astra.md:918:STATUS.md:13:| 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
.orchestra/audits\draft_v3_astra.md:919:STATUS.md:14:| 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |
.orchestra/audits\draft_v3_astra.md:925:STATUS.md:20:- **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.
.orchestra/audits\draft_v3_astra.md:929:STATUS.md:24:1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
.orchestra/audits\draft_v3_astra.md:1951:33:{"id": "6cb3c2a936", "time": "2026-10-31T01:09:25", "level": "L0", "claim": "H-iso PBE check (scripts/hiso_l12.py): cubic A3B L1_2 cells (Cu3Ir Au3Ir Ag3Ir Cu3Rh Ag3Rh Pd3Ir; controls Cu3Au Pt3Cu), clamped Vegard volume, pure refs same V and F, strain 0.02, PBE kspacing 0.10. H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.", "parent": null, "evidence": {"scripts/hiso_l12.py": "c76da785e56fb704"}, "notes": "registered before any hiso_l12 output; H-iso survived on MACE random alloys (n=60, r 0.95, also after removing the -P stress term)"}
.orchestra/audits\draft_v3_astra.md:2054:scripts\hiso_l12_v2.py
.orchestra/audits\draft_v3_astra.md:2055:scripts\hiso_l12.py
.orchestra/audits\draft_v3_astra.md:2074:data\hiso_l12_mace.csv
.orchestra/audits\draft_v3_astra.md:2075:data\hiso_l12_dft_v2.csv
.orchestra/audits\draft_v3_astra.md:2076:data\hiso_l12_dft.csv
.orchestra/audits\draft_v3_astra.md:2480:.orchestra/audits\6bc0e190a8_astra.md:126:| 4 | **MACE kar???m kayma e?rili?inde yan?l?yor.** Au3Ir'de PBE yakla??k -32 GPa, MACE +3. | eski PBE, d?zeltilmi? ko?u s?r?yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle?ir. |
.orchestra/audits\draft_v3_astra.md:2481:.orchestra/audits\6bc0e190a8_astra.md:127:| 5 | **H-iso.** Ir/Rh ala??mlar?nda b?y?k kar???m kayma e?riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h?crelerinde oran 0.95 ile 0.98, Ag h?crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h?crenin 2'si bitti. |
.orchestra/audits\draft_v3_astra.md:2487:.orchestra/audits\6bc0e190a8_astra.md:133:- **H-iso v2 (PBE, 2 ?ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ??kt? `data/hiso_l12_dft_v2.csv`. H?cre ba??na yakla??k 3.7 saat, ana k?s?m 1 Kas?m ak?am? biter. Sonra `dense` arg?man?yla 2 h?cre yakla??k 10 saat. Yeniden ba?latma `scripts/resume_all.ps1`; biten ko?ular `data/dft_runs/hiso2/` alt?nda, tekrar ko?ulmaz.
.orchestra/audits\draft_v3_astra.md:2491:.orchestra/audits\6bc0e190a8_astra.md:137:1. H-iso bitince kriter 6cb3c2a936'y? uygula, sonucu deftere yaz.
.orchestra/audits\draft_v3_astra.md:2877:.orchestra/audits\6bc0e190a8_astra.md:523:30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\draft_v3_astra.md:5774:59:{"round": "S3/cobalt", "candidate": "astra_3", "prior": "UNCLEAR", "refs": ["arXiv:2605.28395", "arXiv:2312.17596", "arXiv:2507.18935 (non-magnetic vs spin-polarized DP for Fe-Cr-C: static properties need the spin branch)"], "verdict": "KEEP", "why": "Sound intervention. Switching spin on and off at fixed chemistry, volume and positions isolates the magnetic term. It says correctly that the nonspin arm is not paramagnetic, that the ordered cell is not the random alloy, and that this is not L3. It runs only after astra_2 and after the astra_1 fix. Fix before running: (1) CoCu2Pt in the 4-atom cubic cell is tetragonal (Co on the corner, Pt on one face centre, Cu on two). So C44 differs from C66, and Kp depends on the axes. Fix the Pt axis and use the exact F matrices from k_shear_transfer.py F_of in MACE and in both PBE arms. (2) Report D for the total cell curvature as well as the mixing curvature. Pure Co at 12.6 A^3/atom is expanded about 16% and strongly magnetic, so a mixing D alone can be driven by the reference. (3) Compare MACE on the Co minus Ni difference, so MACE's common shear softening cancels. Four numbers (2 cells x 2 channels) cannot carry an RMSE ratio on their own. (4) The cost is underestimated. Measured hiso2 runs (4-atom L12, kspacing 0.10, 2 MPI, nonmagnetic): 5 min wall unstrained, 18-51 min sheared. With lower symmetry and spin, about 50 SCF is more like 60-150 core-h than 20-50. Prior: implicit magnetism in MLIPs and MACE's partial magnetoelastic failures in Fe-Ni are known. No prior was found for Co in Cu/Pt fcc shear mixing curvatures."}
.orchestra/audits\draft_v3_astra.md:5816:40:- For DFT finite differences, pin every strain partner to the unstrained k-mesh, use same-size/alloy-matched references and `ecut_elements`, then rerun property-specific controls. `scripts/hiso_l12_v2.py` implements shared cutoffs/fixed grids; old H-iso results remain non-evidential until rerun. [Task 2]
.orchestra/audits\draft_v3_astra.md:5829:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'rg -n "''^" scripts/hiso_l12_v2.py | Select-Object -First 65; rg -n "''^" scripts/fix_counts.py | Select-Object -First 115; Get-Content -Encoding UTF8 data/h1_ev_rows_fixed.csv -TotalCount 2; Get-Content -Encoding UTF8 data/hm_l2_rows_fixed.csv -TotalCount 2; Get-Content -Encoding UTF8 data/calibration_medium-omat-0_20261028_103924.csv -TotalCount 2; rg -n "after|audit|VERDICT|correlation|null|0.86|0.19" .orchestra/audits/6bc0e190a8_astra.md | Select-Object -Last 10' in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\draft_v3_astra.md:5833:3:python scripts/hiso_l12_v2.py [dense]
.orchestra/audits\draft_v3_astra.md:5834:4:Fixes found by the swarm S1 audit in scripts/hiso_l12.py: the alloy and both pure references now share one cutoff
.orchestra/audits\draft_v3_astra.md:5836:6:Ag3Rh at kspacing 0.08 as a convergence check. Criteria 6cb3c2a936 are unchanged; the old results are not used.
.orchestra/audits\draft_v3_astra.md:5874:44:    return dft.run_pw(atoms, f"hiso2{'d' if DENSE else ''}/{tag}", ST["s"]).get_potential_energy() / len(atoms)
.orchestra/audits\draft_v3_astra.md:5889:59:OUT = ROOT / "data" / f"hiso_l12_dft_v2{'_dense' if DENSE else ''}.csv"
.orchestra/audits\draft_v3_astra.md:6031:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Content -Encoding UTF8 'data/hiso_l12_dft_v2.csv' -Raw" in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\draft_v3_astra.md:6033:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Content -Encoding UTF8 'data/hiso_l12_mace.csv' -Raw" in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\draft_v3_astra.md:7011:{"id": "6cb3c2a936", "time": "2026-10-31T01:09:25", "level": "L0", "claim": "H-iso PBE check (scripts/hiso_l12.py): cubic A3B L1_2 cells (Cu3Ir Au3Ir Ag3Ir Cu3Rh Ag3Rh Pd3Ir; controls Cu3Au Pt3Cu), clamped Vegard volume, pure refs same V and F, strain 0.02, PBE kspacing 0.10. H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.", "parent": null, "evidence": {"scripts/hiso_l12.py": "c76da785e56fb704"}, "notes": "registered before any hiso_l12 output; H-iso survived on MACE random alloys (n=60, r 0.95, also after removing the -P stress term)"}
.orchestra/audits\draft_v3_astra.md:7253:    G�ncel v2 CSV art�k sekiz h�cre i�eriyor. Au3Ir i�in PBE **-32.373**, MACE **+3.206 GPa** do�rulan�yor. K' "agreed better" yaln�z s�n�rl� ordered-cell kar��la�t�rmas� olarak s�ylenebilir; random-alloy validation de�ildir. Kan�t: `data/hiso_l12_dft_v2.csv:5`, `data/hiso_l12_mace.csv:3`; `scripts/hiso_l12_v2.py:4-8`.
.orchestra/audits\draft_v3_astra.md:7455:    G�ncel v2 CSV art�k sekiz h�cre i�eriyor. Au3Ir i�in PBE **-32.373**, MACE **+3.206 GPa** do�rulan�yor. K' "agreed better" yaln�z s�n�rl� ordered-cell kar��la�t�rmas� olarak s�ylenebilir; random-alloy validation de�ildir. Kan�t: `data/hiso_l12_dft_v2.csv:5`, `data/hiso_l12_mace.csv:3`; `scripts/hiso_l12_v2.py:4-8`.
.orchestra/audits\draft_v3_astra.md:8241:    G�ncel v2 CSV art�k sekiz h�cre i�eriyor. Au3Ir i�in PBE **-32.373**, MACE **+3.206 GPa** do�rulan�yor. K' "agreed better" yaln�z s�n�rl� ordered-cell kar��la�t�rmas� olarak s�ylenebilir; random-alloy validation de�ildir. Kan�t: `data/hiso_l12_dft_v2.csv:5`, `data/hiso_l12_mace.csv:3`; `scripts/hiso_l12_v2.py:4-8`.
.orchestra/audits\draft_v3_astra.md:8443:    G�ncel v2 CSV art�k sekiz h�cre i�eriyor. Au3Ir i�in PBE **-32.373**, MACE **+3.206 GPa** do�rulan�yor. K' "agreed better" yaln�z s�n�rl� ordered-cell kar��la�t�rmas� olarak s�ylenebilir; random-alloy validation de�ildir. Kan�t: `data/hiso_l12_dft_v2.csv:5`, `data/hiso_l12_mace.csv:3`; `scripts/hiso_l12_v2.py:4-8`.
.orchestra/audits\draft_v3_astra.md:8745:    G�ncel v2 CSV art�k sekiz h�cre i�eriyor. Au3Ir i�in PBE **-32.373**, MACE **+3.206 GPa** do�rulan�yor. K' "agreed better" yaln�z s�n�rl� ordered-cell kar��la�t�rmas� olarak s�ylenebilir; random-alloy validation de�ildir. Kan�t: `data/hiso_l12_dft_v2.csv:5`, `data/hiso_l12_mace.csv:3`; `scripts/hiso_l12_v2.py:4-8`.
.orchestra/audits\draft_v3_astra.md:9086:| 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
.orchestra/audits\draft_v3_astra.md:9087:| 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |
.orchestra/audits\draft_v3_astra.md:9093:- **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.
.orchestra/audits\draft_v3_astra.md:9097:1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
.orchestra/audits\draft_v3_astra.md:9193:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content -Encoding UTF8 .orchestra/swarm/S2/open/opus.md; Get-Content -Encoding UTF8 scripts/k_mpa_equiv.py | Select-Object -Skip 120 -First 70; Add-Type -AssemblyName System.IO.Compression.FileSystem; $z=[IO.Compression.ZipFile]::OpenRead((Resolve-Path paper/repro_20261101.zip)); $z.Entries | Where-Object { $_.FullName -match '"'scratch|baseline|muggian|relax|pure_shear|README.txt|draft_v3' } | Select-Object FullName,Length; "'$z.Dispose(); Get-Content -Encoding UTF8 data/hiso_l12_dft_v2.csv; Get-Content -Encoding UTF8 data/hiso_l12_mace.csv' in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\draft_v3_astra.md:9714:     3392  2026-10-31 12:38   scripts/hiso_l12.py
.orchestra/audits\draft_v3_astra.md:9715:     3899  2026-10-31 14:13   scripts/hiso_l12_v2.py
.orchestra/audits\draft_v3_astra.md:9811:      793  2026-10-31 11:47   data/hiso_l12_dft.csv
.orchestra/audits\draft_v3_astra.md:9812:        0  2026-10-31 01:09   data/hiso_l12_dft.err
.orchestra/audits\draft_v3_astra.md:9813:       54  2026-10-31 04:56   data/hiso_l12_dft.log
.orchestra/audits\draft_v3_astra.md:9814:        0  2026-10-31 04:57   data/hiso_l12_dft2.err
.orchestra/audits\draft_v3_astra.md:9815:      324  2026-10-31 11:47   data/hiso_l12_dft2.log
.orchestra/audits\draft_v3_astra.md:9816:        0  2026-10-31 13:30   data/hiso_l12_dft3.err
.orchestra/audits\draft_v3_astra.md:9817:        0  2026-10-31 13:30   data/hiso_l12_dft3.log
.orchestra/audits\draft_v3_astra.md:9818:      995  2026-11-01 11:42   data/hiso_l12_dft_v2.csv
.orchestra/audits\draft_v3_astra.md:9819:        0  2026-10-31 14:14   data/hiso_l12_dft_v2.err
.orchestra/audits\draft_v3_astra.md:9820:      432  2026-11-01 11:42   data/hiso_l12_dft_v2.log
.orchestra/audits\draft_v3_astra.md:9821:      907  2026-10-31 01:09   data/hiso_l12_mace.csv
.orchestra/audits\draft_v3_astra.md:10083:scripts/hiso_l12.py
.orchestra/audits\draft_v3_astra.md:10084:scripts/hiso_l12_v2.py
.orchestra/audits\draft_v3_astra.md:10180:data/hiso_l12_dft.csv
.orchestra/audits\draft_v3_astra.md:10181:data/hiso_l12_dft.err
.orchestra/audits\draft_v3_astra.md:10182:data/hiso_l12_dft.log
.orchestra/audits\draft_v3_astra.md:10183:data/hiso_l12_dft2.err
.orchestra/audits\draft_v3_astra.md:10184:data/hiso_l12_dft2.log
.orchestra/audits\draft_v3_astra.md:10185:data/hiso_l12_dft3.err
.orchestra/audits\draft_v3_astra.md:10186:data/hiso_l12_dft3.log
.orchestra/audits\draft_v3_astra.md:10187:data/hiso_l12_dft_v2.csv
.orchestra/audits\draft_v3_astra.md:10188:data/hiso_l12_dft_v2.err
.orchestra/audits\draft_v3_astra.md:10189:data/hiso_l12_dft_v2.log
.orchestra/audits\draft_v3_astra.md:10190:data/hiso_l12_mace.csv
.orchestra/audits\b86e0d8a40_astra.md:89:| 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
.orchestra/audits\b86e0d8a40_astra.md:90:| 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |
.orchestra/audits\b86e0d8a40_astra.md:96:- **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.
.orchestra/audits\b86e0d8a40_astra.md:100:1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
.orchestra/audits\b86e0d8a40_astra.md:799:30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\b86e0d8a40_astra.md:1747:Start-Process -FilePath ".\.venv\Scripts\python.exe" -ArgumentList "scripts/hiso_l12_v2.py" -RedirectStandardOutput "data\hiso_l12_dft_v2.log" -RedirectStandardError "data\hiso_l12_dft_v2.err" -WindowStyle Hidden
.orchestra/audits\6cb3c2a936_astra.md:15:Criterion (ledger claims/claims.jsonl id 6cb3c2a936, registered before any output): H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.
.orchestra/audits\6cb3c2a936_astra.md:17:Code: scripts/hiso_l12_v2.py (v2 fixes the S1 audit: shared cutoff and k-grid for alloy and pure refs), harness/dft.py. Results: data/hiso_l12_dft_v2.csv (PBE, 8 cells), data/hiso_l12_mace.csv. Raw runs under data/dft_runs/hiso2/. A dense-k check (kspacing 0.08, Cu3Ir and Ag3Rh) is running now and is not available.
.orchestra/audits\6cb3c2a936_astra.md:38:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "rg -n \"H-iso|hiso|AI driven Science\" C:\\Users\\can02\\.codex\\memories\\MEMORY.md" in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\6cb3c2a936_astra.md:50:40:- For DFT finite differences, pin every strain partner to the unstrained k-mesh, use same-size/alloy-matched references and `ecut_elements`, then rerun property-specific controls. `scripts/hiso_l12_v2.py` implements shared cutoffs/fixed grids; old H-iso results remain non-evidential until rerun. [Task 2]
.orchestra/audits\6cb3c2a936_astra.md:88:paths=['AGENTS.md','STATUS.md','.orchestra/LESSONS.md','scripts/hiso_l12_v2.py','data/hiso_l12_dft_v2.csv','data/hiso_l12_mace.csv']
.orchestra/audits\6cb3c2a936_astra.md:106:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "rg -n \"6cb3c2a936|H-iso|hiso|K.prime|transfer|K′|K'\" claims/claims.jsonl paper/draft_v3.md; Get-Content harness/dft.py -Encoding utf8" in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\6cb3c2a936_astra.md:144:claims/claims.jsonl:33:{"id": "6cb3c2a936", "time": "2026-10-31T01:09:25", "level": "L0", "claim": "H-iso PBE check (scripts/hiso_l12.py): cubic A3B L1_2 cells (Cu3Ir Au3Ir Ag3Ir Cu3Rh Ag3Rh Pd3Ir; controls Cu3Au Pt3Cu), clamped Vegard volume, pure refs same V and F, strain 0.02, PBE kspacing 0.10. H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.", "parent": null, "evidence": {"scripts/hiso_l12.py": "c76da785e56fb704"}, "notes": "registered before any hiso_l12 output; H-iso survived on MACE random alloys (n=60, r 0.95, also after removing the -P stress term)"}
.orchestra/audits\6cb3c2a936_astra.md:362:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content scripts/hiso_l12_v2.py -Encoding utf8; Get-Content data/hiso_l12_dft_v2.csv; Get-Content data/hiso_l12_mace.csv; Get-Item .venv/Scripts/python.exe' in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\6cb3c2a936_astra.md:364:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content STATUS.md -Encoding utf8; Get-Content .orchestra/LESSONS.md -Encoding utf8; Get-Content scripts/hiso_l12.py -Encoding utf8' in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\6cb3c2a936_astra.md:378:| 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
.orchestra/audits\6cb3c2a936_astra.md:379:| 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |
.orchestra/audits\6cb3c2a936_astra.md:385:- **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.
.orchestra/audits\6cb3c2a936_astra.md:389:1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
.orchestra/audits\6cb3c2a936_astra.md:440:12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\6cb3c2a936_astra.md:509:python scripts/hiso_l12.py mace | dft
.orchestra/audits\6cb3c2a936_astra.md:548:        return dft.run_pw(atoms, f"hiso/{tag}", st).get_potential_energy() / len(atoms)
.orchestra/audits\6cb3c2a936_astra.md:563:OUT = ROOT / "data" / f"hiso_l12_{METHOD}.csv"
.orchestra/audits\6cb3c2a936_astra.md:591:python scripts/hiso_l12_v2.py [dense]
.orchestra/audits\6cb3c2a936_astra.md:592:Fixes found by the swarm S1 audit in scripts/hiso_l12.py: the alloy and both pure references now share one cutoff
.orchestra/audits\6cb3c2a936_astra.md:594:Ag3Rh at kspacing 0.08 as a convergence check. Criteria 6cb3c2a936 are unchanged; the old results are not used.
.orchestra/audits\6cb3c2a936_astra.md:632:    return dft.run_pw(atoms, f"hiso2{'d' if DENSE else ''}/{tag}", ST["s"]).get_potential_energy() / len(atoms)
.orchestra/audits\6cb3c2a936_astra.md:647:OUT = ROOT / "data" / f"hiso_l12_dft_v2{'_dense' if DENSE else ''}.csv"
.orchestra/audits\6cb3c2a936_astra.md:703:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$i=0; Get-Content paper/draft_v3.md -Encoding utf8 | ForEach-Object { $i++; if(($i -le 80) -or ($i -ge 160 -and $i -le 190)){"${i}: $_"} }; Get-ChildItem data/dft_runs/hiso2 | Select-Object Name; git status --short' in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\6cb3c2a936_astra.md:904:for f in ['scripts/hiso_l12_v2.py','harness/dft.py']:
.orchestra/audits\6cb3c2a936_astra.md:909:print(Path('data/dft_runs/hiso2/Cu3Ir_g+_v12.571/pw.in').read_text())
.orchestra/audits\6cb3c2a936_astra.md:910:p=Path('data/dft_runs/hiso2/Cu3Ir_g+_v12.571/pw.out')
.orchestra/audits\6cb3c2a936_astra.md:922:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Command python*,py*,wsl* -ErrorAction SilentlyContinue | Select-Object Name,Source; Get-Content data/dft_runs/hiso2/Cu3Ir_g+_v12.571/pw.in; rg -n "convergence|total energy|accuracy|WARNING|Warning|JOB DONE|kinetic-energy cutoff|charge density cutoff|smearing|number of k points" data/dft_runs/hiso2/Cu3Ir_g+_v12.571/pw.out; rg -n "GPA" harness/compute.py; Get-ChildItem C:/Users/can02/AppData/Local/Programs/Python -ErrorAction SilentlyContinue; Get-ChildItem C:/Python*,C:/Users/can02/.local/bin -ErrorAction SilentlyContinue | Select-Object Name,FullName' in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\6cb3c2a936_astra.md:974:   outdir           = '/tmp/qe/hiso2__Cu3Ir_g+_v12.571'
.orchestra/audits\6cb3c2a936_astra.md:1030:$records = @(Get-ChildItem data/dft_runs/hiso2 -Directory | ForEach-Object {
.orchestra/audits\6cb3c2a936_astra.md:1691:$records = @(Get-ChildItem data/dft_runs/hiso2 -Directory | ForEach-Object {
.orchestra/audits\6cb3c2a936_astra.md:2347:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "rg -n \"create_units|units\\[.Ry|energy =|free_energy\" .venv/Lib/site-packages/ase/io/espresso.py; rg -n \"2006|_hplanck|_e|_me|_eps0|Rydberg|Ry =\" .venv/Lib/site-packages/ase/units.py; rg -n \"hiso|6cb3c2a936\" claims/claims.jsonl .orchestra/audits scripts -g '*.md' -g '*.py' -g '*.jsonl'" in C:\Users\can02\Projects\AI driven Science
scripts\hiso_l12.py:3:python scripts/hiso_l12.py mace | dft
scripts\hiso_l12.py:42:        return dft.run_pw(atoms, f"hiso/{tag}", st).get_potential_energy() / len(atoms)
scripts\hiso_l12.py:57:OUT = ROOT / "data" / f"hiso_l12_{METHOD}.csv"
scripts\hiso_l12_v2.py:3:python scripts/hiso_l12_v2.py [dense]
scripts\hiso_l12_v2.py:4:Fixes found by the swarm S1 audit in scripts/hiso_l12.py: the alloy and both pure references now share one cutoff
scripts\hiso_l12_v2.py:6:Ag3Rh at kspacing 0.08 as a convergence check. Criteria 6cb3c2a936 are unchanged; the old results are not used.
scripts\hiso_l12_v2.py:44:    return dft.run_pw(atoms, f"hiso2{'d' if DENSE else ''}/{tag}", ST["s"]).get_potential_energy() / len(atoms)
scripts\hiso_l12_v2.py:59:OUT = ROOT / "data" / f"hiso_l12_dft_v2{'_dense' if DENSE else ''}.csv"
.orchestra/audits\88b9465108_astra.md:82:| 4 | **MACE kar��Y��m kayma e�Yrili�Yinde yan��l��yor.** Au3Ir'de PBE yakla�Y��k �^'32 GPa, MACE +3. | eski PBE, dǬzeltilmi�Y ko�Yu sǬrǬyor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�Yir. |
.orchestra/audits\88b9465108_astra.md:83:| 5 | **H-iso.** Ir/Rh ala�Y��mlar��nda bǬyǬk kar��Y��m kayma e�Yriliklerinde K44 �%^ K'. MACE'te r 0.95; eski PBE'de Cu ve Au hǬcrelerinde oran 0.95 ile 0.98, Ag hǬcrelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 hǬcrenin 2'si bitti. |
.orchestra/audits\88b9465108_astra.md:89:- **H-iso v2 (PBE, 2 ��ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ����kt�� `data/hiso_l12_dft_v2.csv`. HǬcre ba�Y��na yakla�Y��k 3.7 saat, ana k��s��m 1 Kas��m ak�Yam�� biter. Sonra `dense` argǬman��yla 2 hǬcre yakla�Y��k 10 saat. Yeniden ba�Ylatma `scripts/resume_all.ps1`; biten ko�Yular `data/dft_runs/hiso2/` alt��nda, tekrar ko�Yulmaz.
.orchestra/audits\88b9465108_astra.md:93:1. H-iso bitince kriter 6cb3c2a936'y�� uygula, sonucu deftere yaz.
.orchestra/audits\88b9465108_astra.md:190:40: - For DFT finite differences, pin every strain partner to the unstrained k-mesh, use same-size/alloy-matched references and `ecut_elements`, then rerun property-specific controls. `scripts/hiso_l12_v2.py` implements shared cutoffs/fixed grids; old H-iso results remain non-evidential until rerun. [Task 2]
.orchestra/audits\88b9465108_astra.md:324:126: | 4 | **MACE kar???m kayma e?rili?inde yan?l?yor.** Au3Ir'de PBE yakla??k -32 GPa, MACE +3. | eski PBE, d?zeltilmi? ko?u s?r?yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle?ir. |
.orchestra/audits\88b9465108_astra.md:325:127: | 5 | **H-iso.** Ir/Rh ala??mlar?nda b?y?k kar???m kayma e?riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h?crelerinde oran 0.95 ile 0.98, Ag h?crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h?crenin 2'si bitti. |
.orchestra/audits\88b9465108_astra.md:331:133: - **H-iso v2 (PBE, 2 ?ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ??kt? `data/hiso_l12_dft_v2.csv`. H?cre ba??na yakla??k 3.7 saat, ana k?s?m 1 Kas?m ak?am? biter. Sonra `dense` arg?man?yla 2 h?cre yakla??k 10 saat. Yeniden ba?latma `scripts/resume_all.ps1`; biten ko?ular `data/dft_runs/hiso2/` alt?nda, tekrar ko?ulmaz.
.orchestra/audits\88b9465108_astra.md:335:137: 1. H-iso bitince kriter 6cb3c2a936'y? uygula, sonucu deftere yaz.
.orchestra/audits\88b9465108_astra.md:721:523: 30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\88b9465108_astra.md:2052:30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\6bc0e190a8_astra.md:126:| 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
.orchestra/audits\6bc0e190a8_astra.md:127:| 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |
.orchestra/audits\6bc0e190a8_astra.md:133:- **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.
.orchestra/audits\6bc0e190a8_astra.md:137:1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
.orchestra/audits\6bc0e190a8_astra.md:523:30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\fd786169e3_astra.md:76:12: | 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
.orchestra/audits\fd786169e3_astra.md:77:13: | 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |
.orchestra/audits\fd786169e3_astra.md:83:19: - **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.
.orchestra/audits\fd786169e3_astra.md:87:23: 1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
.orchestra/audits\fd786169e3_astra.md:198:89: | 4 | **MACE kar???m kayma e?rili?inde yan?l?yor.** Au3Ir'de PBE yakla??k -32 GPa, MACE +3. | eski PBE, d?zeltilmi? ko?u s?r?yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle?ir. |
.orchestra/audits\fd786169e3_astra.md:199:90: | 5 | **H-iso.** Ir/Rh ala??mlar?nda b?y?k kar???m kayma e?riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h?crelerinde oran 0.95 ile 0.98, Ag h?crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h?crenin 2'si bitti. |
.orchestra/audits\fd786169e3_astra.md:205:96: - **H-iso v2 (PBE, 2 ?ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ??kt? `data/hiso_l12_dft_v2.csv`. H?cre ba??na yakla??k 3.7 saat, ana k?s?m 1 Kas?m ak?am? biter. Sonra `dense` arg?man?yla 2 h?cre yakla??k 10 saat. Yeniden ba?latma `scripts/resume_all.ps1`; biten ko?ular `data/dft_runs/hiso2/` alt?nda, tekrar ko?ulmaz.
.orchestra/audits\fd786169e3_astra.md:209:100: 1. H-iso bitince kriter 6cb3c2a936'y? uygula, sonucu deftere yaz.
.orchestra/audits\fd786169e3_astra.md:908:799: 30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\fd786169e3_astra.md:1714:1747: Start-Process -FilePath ".\.venv\Scripts\python.exe" -ArgumentList "scripts/hiso_l12_v2.py" -RedirectStandardOutput "data\hiso_l12_dft_v2.log" -RedirectStandardError "data\hiso_l12_dft_v2.err" -WindowStyle Hidden
.orchestra/audits\ede47f1d65_astra.md:145:  12 | 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
.orchestra/audits\ede47f1d65_astra.md:146:  13 | 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |
.orchestra/audits\ede47f1d65_astra.md:152:  19 - **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.
.orchestra/audits\ede47f1d65_astra.md:156:  23 1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
.orchestra/audits\ede47f1d65_astra.md:254:  76 12: | 4 | **MACE kar???m kayma e?rili?inde yan?l?yor.** Au3Ir'de PBE yakla??k -32 GPa, MACE +3. | eski PBE, d?zeltilmi? ko?u s?r?yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle?ir. |
.orchestra/audits\ede47f1d65_astra.md:255:  77 13: | 5 | **H-iso.** Ir/Rh ala??mlar?nda b?y?k kar???m kayma e?riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h?crelerinde oran 0.95 ile 0.98, Ag h?crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h?crenin 2'si bitti. |
.orchestra/audits\ede47f1d65_astra.md:261:  83 19: - **H-iso v2 (PBE, 2 ?ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ??kt? `data/hiso_l12_dft_v2.csv`. H?cre ba??na yakla??k 3.7 saat, ana k?s?m 1 Kas?m ak?am? biter. Sonra `dense` arg?man?yla 2 h?cre yakla??k 10 saat. Yeniden ba?latma `scripts/resume_all.ps1`; biten ko?ular `data/dft_runs/hiso2/` alt?nda, tekrar ko?ulmaz.
.orchestra/audits\ede47f1d65_astra.md:265:  87 23: 1. H-iso bitince kriter 6cb3c2a936'y? uygula, sonucu deftere yaz.
.orchestra/audits\ede47f1d65_astra.md:376: 198 89: | 4 | **MACE kar???m kayma e?rili?inde yan?l?yor.** Au3Ir'de PBE yakla??k -32 GPa, MACE +3. | eski PBE, d?zeltilmi? ko?u s?r?yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle?ir. |
.orchestra/audits\ede47f1d65_astra.md:377: 199 90: | 5 | **H-iso.** Ir/Rh ala??mlar?nda b?y?k kar???m kayma e?riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h?crelerinde oran 0.95 ile 0.98, Ag h?crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h?crenin 2'si bitti. |
.orchestra/audits\ede47f1d65_astra.md:383: 205 96: - **H-iso v2 (PBE, 2 ?ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ??kt? `data/hiso_l12_dft_v2.csv`. H?cre ba??na yakla??k 3.7 saat, ana k?s?m 1 Kas?m ak?am? biter. Sonra `dense` arg?man?yla 2 h?cre yakla??k 10 saat. Yeniden ba?latma `scripts/resume_all.ps1`; biten ko?ular `data/dft_runs/hiso2/` alt?nda, tekrar ko?ulmaz.
.orchestra/audits\ede47f1d65_astra.md:387: 209 100: 1. H-iso bitince kriter 6cb3c2a936'y? uygula, sonucu deftere yaz.
.orchestra/audits\ede47f1d65_astra.md:1086: 908 799: 30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\ede47f1d65_astra.md:1739:1714 1747: Start-Process -FilePath ".\.venv\Scripts\python.exe" -ArgumentList "scripts/hiso_l12_v2.py" -RedirectStandardOutput "data\hiso_l12_dft_v2.log" -RedirectStandardError "data\hiso_l12_dft_v2.err" -WindowStyle Hidden
.orchestra/audits\draft_v2_astra.md:145:.orchestra/LESSONS.md:30:12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\draft_v2_astra.md:224:STATUS.md:13:| 4 | **MACE karışım kayma eğriliğinde yanılıyor.** Au3Ir'de PBE yaklaşık −32 GPa, MACE +3. | eski PBE, düzeltilmiş koşu sürüyor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinleşir. |
.orchestra/audits\draft_v2_astra.md:225:STATUS.md:14:| 5 | **H-iso.** Ir/Rh alaşımlarında büyük karışım kayma eğriliklerinde K44 ≈ K'. MACE'te r 0.95; eski PBE'de Cu ve Au hücrelerinde oran 0.95 ile 0.98, Ag hücrelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 hücrenin 2'si bitti. |
.orchestra/audits\draft_v2_astra.md:231:STATUS.md:20:- **H-iso v2 (PBE, 2 çekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, çıktı `data/hiso_l12_dft_v2.csv`. Hücre başına yaklaşık 3.7 saat, ana kısım 1 Kasım akşamı biter. Sonra `dense` argümanıyla 2 hücre yaklaşık 10 saat. Yeniden başlatma `scripts/resume_all.ps1`; biten koşular `data/dft_runs/hiso2/` altında, tekrar koşulmaz.
.orchestra/audits\draft_v2_astra.md:235:STATUS.md:24:1. H-iso bitince kriter 6cb3c2a936'yı uygula, sonucu deftere yaz.
.orchestra/audits\draft_v2_astra.md:1257:33:{"id": "6cb3c2a936", "time": "2026-10-31T01:09:25", "level": "L0", "claim": "H-iso PBE check (scripts/hiso_l12.py): cubic A3B L1_2 cells (Cu3Ir Au3Ir Ag3Ir Cu3Rh Ag3Rh Pd3Ir; controls Cu3Au Pt3Cu), clamped Vegard volume, pure refs same V and F, strain 0.02, PBE kspacing 0.10. H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.", "parent": null, "evidence": {"scripts/hiso_l12.py": "c76da785e56fb704"}, "notes": "registered before any hiso_l12 output; H-iso survived on MACE random alloys (n=60, r 0.95, also after removing the -P stress term)"}
.orchestra/audits\draft_v2_astra.md:1360:scripts\hiso_l12_v2.py
.orchestra/audits\draft_v2_astra.md:1361:scripts\hiso_l12.py
.orchestra/audits\draft_v2_astra.md:1380:data\hiso_l12_mace.csv
.orchestra/audits\draft_v2_astra.md:1381:data\hiso_l12_dft_v2.csv
.orchestra/audits\draft_v2_astra.md:1382:data\hiso_l12_dft.csv
.orchestra/audits\draft_v2_astra.md:1786:.orchestra/audits\6bc0e190a8_astra.md:126:| 4 | **MACE kar���m kayma e�rili�inde yan�l�yor.** Au3Ir'de PBE yakla��k -32 GPa, MACE +3. | eski PBE, d�zeltilmi� ko�u s�r�yor | `data/hiso_l12_dft.csv`, `_mace.csv` | H-iso v2 bitince kesinle�ir. |
.orchestra/audits\draft_v2_astra.md:1787:.orchestra/audits\6bc0e190a8_astra.md:127:| 5 | **H-iso.** Ir/Rh ala��mlar�nda b�y�k kar���m kayma e�riliklerinde K44 ? K'. MACE'te r 0.95; eski PBE'de Cu ve Au h�crelerinde oran 0.95 ile 0.98, Ag h�crelerinde 0.4 ile 0.5. | L0, kriter 6cb3c2a936 | `scripts/hiso_l12_v2.py` | 8 h�crenin 2'si bitti. |
.orchestra/audits\draft_v2_astra.md:1793:.orchestra/audits\6bc0e190a8_astra.md:133:- **H-iso v2 (PBE, 2 �ekirdek):** `HISO_NP=2 python scripts/hiso_l12_v2.py`, log `data/hiso_l12_dft_v2.log`, ��kt� `data/hiso_l12_dft_v2.csv`. H�cre ba��na yakla��k 3.7 saat, ana k�s�m 1 Kas�m ak�am� biter. Sonra `dense` arg�man�yla 2 h�cre yakla��k 10 saat. Yeniden ba�latma `scripts/resume_all.ps1`; biten ko�ular `data/dft_runs/hiso2/` alt�nda, tekrar ko�ulmaz.
.orchestra/audits\draft_v2_astra.md:1797:.orchestra/audits\6bc0e190a8_astra.md:137:1. H-iso bitince kriter 6cb3c2a936'y� uygula, sonucu deftere yaz.
.orchestra/audits\draft_v2_astra.md:2183:.orchestra/audits\6bc0e190a8_astra.md:523:30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
.orchestra/audits\draft_v2_astra.md:4619:Start-Process -FilePath ".\.venv\Scripts\python.exe" -ArgumentList "scripts/hiso_l12_v2.py" -RedirectStandardOutput "data\hiso_l12_dft_v2.log" -RedirectStandardError "data\hiso_l12_dft_v2.err" -WindowStyle Hidden
.orchestra/audits\draft_v2_astra.md:5162:.orchestra/swarm/S1/audit/opus.md:13: "size": "L1_0 PBE: E_mix shifts by up to 3.5 meV. Rebuilding Ag-Ir with same-mesh 4-atom references gives dE/dlnV -437 to -469 meV (7%) and n_eff 2.57 to 2.74. Pd-Pt moves 13.88 to 13.93, so the L1 verdict 4c5076a083 stands. H-iso: Kp changes by 200272/V GPa per eV, which is 15.9 GPa per meV/atom at V=12.57. The Nb k-test (conv/, 0.10 against 0.07) shows a mesh-switched cell 0.22 meV/atom off against 0.06 for its partner. That implies 1.5 to 5 GPa on Kp for Cu3Ir (-55.7) and Cu3Rh (-36.9), and leaves the sign of Pd3Ir's Kp (-1.5) unresolved. K44 and the silver cells are clean. Also, scripts/hiso_l12.py:39 sets no ecut_elements, so pure references run at their own cutoff (Rh at 43.75 Ry against Cu3Rh at 112.5). The E_mix column in hiso_l12_dft.csv is off by up to 6 meV: Cu3Rh -14.2 should be about -8.2 by ecut_shift_table. The curvatures should be insensitive to this because the strains are isochoric and a volume-only basis error drops out.",
.orchestra/audits\draft_v2_astra.md:5322:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'rg -n "''^assistant$|''^tokens used|''^VERDICT|''^'"\\*\\*VERDICT|"'^1'"\\. \\*\\*|"'^1'"\\. \\[|"'^1'"\\.\" .orchestra/audits/draft_v2_astra.md | Select-Object -Last 15; rg -n \""'^" data/hiso_l12_dft_v2.csv data/hiso_l12_dft.csv data/hiso_l12_mace.csv; rg -n "''^" claims/claims.jsonl | Select-Object -Skip 31 -First 11' in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\draft_v2_astra.md:5339:data/hiso_l12_dft_v2.csv:1:cell,method,kpts,V,E_mix,K44,Kp,time
.orchestra/audits\draft_v2_astra.md:5340:data/hiso_l12_dft_v2.csv:2:Cu3Ir,dft_v2,18x18x18,12.570930746342615,0.01557259878734385,-54.74691675055384,-57.38539420465976,2026-10-31T20:37:36
.orchestra/audits\draft_v2_astra.md:5341:data/hiso_l12_dft_v2.csv:3:Cu3Rh,dft_v2,18x18x18,12.466046926632401,-0.008250364034438462,-34.78715578271392,-37.42050958615326,2026-11-01T00:29:27
.orchestra/audits\draft_v2_astra.md:5342:data/hiso_l12_dft_v2.csv:4:Pd3Ir,dft_v2,17x17x17,15.090881358268899,0.1289190757158849,6.644682704355299,-5.321163067938075,2026-11-01T02:08:10
.orchestra/audits\draft_v2_astra.md:5343:data/hiso_l12_dft_v2.csv:5:Au3Ir,dft_v2,16x16x16,17.01764835574268,0.2510520404655381,-32.3727567076859,-33.84664741248657,2026-11-01T04:10:20
.orchestra/audits\draft_v2_astra.md:5344:data/hiso_l12_dft_v2.csv:6:Ag3Ir,dft_v2,16x16x16,16.958300131244606,0.3207653609897534,-15.691494965360748,-29.08829505587699,2026-11-01T05:55:23
.orchestra/audits\draft_v2_astra.md:5345:data/hiso_l12_dft_v2.csv:7:Ag3Rh,dft_v2,16x16x16,16.853416311534392,0.13165629432899095,-7.037878294590145,-17.96665812599528,2026-11-01T07:00:57
.orchestra/audits\draft_v2_astra.md:5346:data/hiso_l12_dft_v2.csv:8:Cu3Au,dft_v2,17x17x17,13.473338466415823,-0.32097306888442745,-5.5914144369890275,6.832279696830556,2026-11-01T09:14:36
.orchestra/audits\draft_v2_astra.md:5347:data/hiso_l12_dft_v2.csv:9:Pt3Cu,dft_v2,17x17x17,14.643363572487065,-0.1959511480412175,23.828501484675826,9.127699571762257,2026-11-01T11:42:51
.orchestra/audits\draft_v2_astra.md:5348:data/hiso_l12_dft.csv:1:cell,method,V,E_mix,K44,Kp,time
.orchestra/audits\draft_v2_astra.md:5349:data/hiso_l12_dft.csv:2:Cu3Ir,dft,12.570930746342615,0.011400200767297974,-54.67105172219048,-55.735736173810075,2026-10-31T04:56:53
.orchestra/audits\draft_v2_astra.md:5350:data/hiso_l12_dft.csv:3:Cu3Rh,dft,12.466046926632401,-0.014219019517781817,-34.9571024549038,-36.93566975106572,2026-10-31T06:38:56
.orchestra/audits\draft_v2_astra.md:5351:data/hiso_l12_dft.csv:4:Pd3Ir,dft,15.090881358268899,0.1261769080317663,6.715101891345876,-1.5249592156548393,2026-10-31T07:32:02
.orchestra/audits\draft_v2_astra.md:5352:data/hiso_l12_dft.csv:5:Au3Ir,dft,17.01764835574268,0.24963803491641556,-32.343935325273456,-33.826832738836465,2026-10-31T08:40:36
.orchestra/audits\draft_v2_astra.md:5353:data/hiso_l12_dft.csv:6:Ag3Ir,dft,16.958300131244606,0.32072661027859795,-15.683059324204956,-29.083173415069425,2026-10-31T09:40:34
.orchestra/audits\draft_v2_astra.md:5354:data/hiso_l12_dft.csv:7:Ag3Rh,dft,16.853416311534392,0.12799282571927506,-7.151053462291373,-18.01101874891471,2026-10-31T10:32:20
.orchestra/audits\draft_v2_astra.md:5355:data/hiso_l12_dft.csv:8:Cu3Au,dft,13.473338466415823,-0.3216856584958805,-5.579785669490148,6.835945287393839,2026-10-31T11:47:13
.orchestra/audits\draft_v2_astra.md:5356:data/hiso_l12_mace.csv:1:cell,method,V,E_mix,K44,Kp,time
.orchestra/audits\draft_v2_astra.md:5357:data/hiso_l12_mace.csv:2:Cu3Ir,mace,12.570930746342615,0.007922966900131723,-60.480692622198305,-73.26377353391179,2026-10-31T01:09:46
.orchestra/audits\draft_v2_astra.md:5358:data/hiso_l12_mace.csv:3:Au3Ir,mace,17.01764835574268,0.1980301038873411,3.2063930667627205,-11.842309290055715,2026-10-31T01:09:48
.orchestra/audits\draft_v2_astra.md:5359:data/hiso_l12_mace.csv:4:Ag3Ir,mace,16.958300131244606,0.2825353511949964,-1.6943321412785415,-14.231864501045454,2026-10-31T01:09:49
.orchestra/audits\draft_v2_astra.md:5360:data/hiso_l12_mace.csv:5:Cu3Rh,mace,12.466046926632401,-0.022119947332217782,-30.506540090852575,-36.0052297807868,2026-10-31T01:09:50
.orchestra/audits\draft_v2_astra.md:5361:data/hiso_l12_mace.csv:6:Ag3Rh,mace,16.853416311534392,0.10310185849292175,1.1388933635108385,-3.20914102683622,2026-10-31T01:09:51
.orchestra/audits\draft_v2_astra.md:5362:data/hiso_l12_mace.csv:7:Pd3Ir,mace,15.090881358268899,0.13232800965835922,-14.347444565088127,-12.80101099840087,2026-10-31T01:09:53
.orchestra/audits\draft_v2_astra.md:5363:data/hiso_l12_mace.csv:8:Cu3Au,mace,13.473338466415823,-0.3208622345675217,-10.161705065912527,1.0358830436384283,2026-10-31T01:09:55
.orchestra/audits\draft_v2_astra.md:5364:data/hiso_l12_mace.csv:9:Pt3Cu,mace,14.643363572487065,-0.19250834620571533,9.76255799019013,9.89059517207147,2026-10-31T01:09:56
.orchestra/audits\draft_v2_astra.md:5366:33:{"id": "6cb3c2a936", "time": "2026-10-31T01:09:25", "level": "L0", "claim": "H-iso PBE check (scripts/hiso_l12.py): cubic A3B L1_2 cells (Cu3Ir Au3Ir Ag3Ir Cu3Rh Ag3Rh Pd3Ir; controls Cu3Au Pt3Cu), clamped Vegard volume, pure refs same V and F, strain 0.02, PBE kspacing 0.10. H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.", "parent": null, "evidence": {"scripts/hiso_l12.py": "c76da785e56fb704"}, "notes": "registered before any hiso_l12 output; H-iso survived on MACE random alloys (n=60, r 0.95, also after removing the -P stress term)"}
.orchestra/audits\draft_v2_astra.md:14773:59:{"round": "S3/cobalt", "candidate": "astra_3", "prior": "UNCLEAR", "refs": ["arXiv:2605.28395", "arXiv:2312.17596", "arXiv:2507.18935 (non-magnetic vs spin-polarized DP for Fe-Cr-C: static properties need the spin branch)"], "verdict": "KEEP", "why": "Sound intervention. Switching spin on and off at fixed chemistry, volume and positions isolates the magnetic term. It says correctly that the nonspin arm is not paramagnetic, that the ordered cell is not the random alloy, and that this is not L3. It runs only after astra_2 and after the astra_1 fix. Fix before running: (1) CoCu2Pt in the 4-atom cubic cell is tetragonal (Co on the corner, Pt on one face centre, Cu on two). So C44 differs from C66, and Kp depends on the axes. Fix the Pt axis and use the exact F matrices from k_shear_transfer.py F_of in MACE and in both PBE arms. (2) Report D for the total cell curvature as well as the mixing curvature. Pure Co at 12.6 A^3/atom is expanded about 16% and strongly magnetic, so a mixing D alone can be driven by the reference. (3) Compare MACE on the Co minus Ni difference, so MACE's common shear softening cancels. Four numbers (2 cells x 2 channels) cannot carry an RMSE ratio on their own. (4) The cost is underestimated. Measured hiso2 runs (4-atom L12, kspacing 0.10, 2 MPI, nonmagnetic): 5 min wall unstrained, 18-51 min sheared. With lower symmetry and spin, about 50 SCF is more like 60-150 core-h than 20-50. Prior: implicit magnetism in MLIPs and MACE's partial magnetoelastic failures in Fe-Ni are known. No prior was found for Co in Cu/Pt fcc shear mixing curvatures."}
.orchestra/audits\draft_v2_astra.md:14815:40:- For DFT finite differences, pin every strain partner to the unstrained k-mesh, use same-size/alloy-matched references and `ecut_elements`, then rerun property-specific controls. `scripts/hiso_l12_v2.py` implements shared cutoffs/fixed grids; old H-iso results remain non-evidential until rerun. [Task 2]
.orchestra/audits\draft_v2_astra.md:14828:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'rg -n "''^" scripts/hiso_l12_v2.py | Select-Object -First 65; rg -n "''^" scripts/fix_counts.py | Select-Object -First 115; Get-Content -Encoding UTF8 data/h1_ev_rows_fixed.csv -TotalCount 2; Get-Content -Encoding UTF8 data/hm_l2_rows_fixed.csv -TotalCount 2; Get-Content -Encoding UTF8 data/calibration_medium-omat-0_20261028_103924.csv -TotalCount 2; rg -n "after|audit|VERDICT|correlation|null|0.86|0.19" .orchestra/audits/6bc0e190a8_astra.md | Select-Object -Last 10' in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\draft_v2_astra.md:14832:3:python scripts/hiso_l12_v2.py [dense]
.orchestra/audits\draft_v2_astra.md:14833:4:Fixes found by the swarm S1 audit in scripts/hiso_l12.py: the alloy and both pure references now share one cutoff
.orchestra/audits\draft_v2_astra.md:14835:6:Ag3Rh at kspacing 0.08 as a convergence check. Criteria 6cb3c2a936 are unchanged; the old results are not used.
.orchestra/audits\draft_v2_astra.md:14873:44:    return dft.run_pw(atoms, f"hiso2{'d' if DENSE else ''}/{tag}", ST["s"]).get_potential_energy() / len(atoms)
.orchestra/audits\draft_v2_astra.md:14888:59:OUT = ROOT / "data" / f"hiso_l12_dft_v2{'_dense' if DENSE else ''}.csv"
.orchestra/audits\draft_v2_astra.md:15030:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Content -Encoding UTF8 'data/hiso_l12_dft_v2.csv' -Raw" in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\draft_v2_astra.md:15032:"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Content -Encoding UTF8 'data/hiso_l12_mace.csv' -Raw" in C:\Users\can02\Projects\AI driven Science
.orchestra/audits\draft_v2_astra.md:16010:{"id": "6cb3c2a936", "time": "2026-10-31T01:09:25", "level": "L0", "claim": "H-iso PBE check (scripts/hiso_l12.py): cubic A3B L1_2 cells (Cu3Ir Au3Ir Ag3Ir Cu3Rh Ag3Rh Pd3Ir; controls Cu3Au Pt3Cu), clamped Vegard volume, pure refs same V and F, strain 0.02, PBE kspacing 0.10. H-iso holds in PBE iff among cells with max(|K44|,|Kp|) > 10 GPa (need n >= 4): all K44, Kp same sign and median K44/Kp in [0.75, 1.33]. MACE passes L1 for this quantity iff sign of K44 and Kp agrees with PBE in all cells and median |MACE-PBE| <= 30% of median |PBE|.", "parent": null, "evidence": {"scripts/hiso_l12.py": "c76da785e56fb704"}, "notes": "registered before any hiso_l12 output; H-iso survived on MACE random alloys (n=60, r 0.95, also after removing the -P stress term)"}
.orchestra/audits\draft_v2_astra.md:16252:    Güncel v2 CSV artık sekiz hücre içeriyor. Au3Ir için PBE **−32.373**, MACE **+3.206 GPa** doğrulanıyor. K′ “agreed better” yalnız sınırlı ordered-cell karşılaştırması olarak söylenebilir; random-alloy validation değildir. Kanıt: `data/hiso_l12_dft_v2.csv:5`, `data/hiso_l12_mace.csv:3`; `scripts/hiso_l12_v2.py:4–8`.
.orchestra/audits\draft_v2_astra.md:16454:    Güncel v2 CSV artık sekiz hücre içeriyor. Au3Ir için PBE **−32.373**, MACE **+3.206 GPa** doğrulanıyor. K′ “agreed better” yalnız sınırlı ordered-cell karşılaştırması olarak söylenebilir; random-alloy validation değildir. Kanıt: `data/hiso_l12_dft_v2.csv:5`, `data/hiso_l12_mace.csv:3`; `scripts/hiso_l12_v2.py:4–8`.

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '
$records = @(Get-ChildItem data/dft_runs/hiso2 -Directory | ForEach-Object {
 $d=$_
 $ins=Get-Content -LiteralPath (Join-Path $d.FullName '"'pw.in') -Raw
 "'$outs=Get-Content -LiteralPath (Join-Path $d.FullName '"'pw.out') -Raw
 "'$errs=Get-Content -LiteralPath (Join-Path $d.FullName '"'pw.err') -Raw -ErrorAction SilentlyContinue
 "'$energies=[regex]::Matches($outs,'"'"'!'"\\s+total energy\\s*=\\s*([-\\d.]+)')
 "'$acc=[regex]::Matches($outs,'"'estimated scf accuracy\\s*<\\s*([\\d.Ee+-]+)')
 @{
 name="'$d.Name
 energyRy=$energies[$energies.Count-1].Groups[1].Value
 energyCount=$energies.Count
 accuracyRy=$acc[$acc.Count-1].Groups[1].Value
 done=$outs.Contains('"'JOB DONE')
 converged="'$outs.Contains('"'convergence has been achieved')
 badConvergence="'$outs.Contains('"'convergence NOT achieved')
 warnings=@("'$outs -split "'"\\r?\\n\" | Where-Object {"'$_ -match '"'(?i)warning|error|negative|not converged|not achieved'})
 err="'$errs
 ecutwfc=[regex]::Match($ins,'"'ecutwfc\\s*=\\s*([\\d.]+)').Groups[1].Value
 ecutrho=[regex]::Match("'$ins,'"'ecutrho\\s*=\\s*([\\d.]+)').Groups[1].Value
 degauss=[regex]::Match("'$ins,'"'degauss\\s*=\\s*([\\d.]+)').Groups[1].Value
 conv_thr=[regex]::Match("'$ins,'"'conv_thr\\s*=\\s*([\\d.eE+-]+)').Groups[1].Value
 kgrid=[regex]::Match("'$ins,'"'K_POINTS automatic\\s*\\r?\\n(["'^'"\\r\\n]+)').Groups[1].Value
 matrix=[regex]::Match("'$ins,'"'CELL_PARAMETERS angstrom\\s*\\r?\\n((?:["'^'"\\r\\n]+\\r?\\n){3})').Groups[1].Value
 positions=[regex]::Match("'$ins,'"'ATOMIC_POSITIONS angstrom\\s*\\r?\\n((?:["'^'"\\r\\n]+\\r?\\n){4})').Groups[1].Value
 cutOutput=[regex]::Match("'$outs,'"'kinetic-energy cutoff\\s*=\\s*([\\d.]+)').Groups[1].Value
 }
})
"'$records | ConvertTo-Json -Depth 5 -Compress
' in C:\Users\can02\Projects\AI driven Science
 succeeded in 1854ms:
[{"accuracyRy":"3.8E-10","converged":true,"matrix":"4.07831502664735 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.07831502664735 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.07831502664735\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0000000000 2.0391575133 2.0391575133  \r\nAg 2.0391575133 0.0000000000 2.0391575133  \r\nAg 2.0391575133 2.0391575133 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.638E-01 0.000E+00","     negative rho (up, down):  3.337E-01 0.000E+00","     negative rho (up, down):  3.410E-01 0.000E+00","     negative rho (up, down):  3.356E-01 0.000E+00","     negative rho (up, down):  3.303E-01 0.000E+00","     negative rho (up, down):  3.298E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00","     negative rho (up, down):  3.293E-01 0.000E+00","     negative rho (up, down):  3.293E-01 0.000E+00","     negative rho (up, down):  3.293E-01 0.000E+00","     negative rho (up, down):  3.293E-01 0.000E+00","     negative rho (up, down):  3.293E-01 0.000E+00","     negative rho (up, down):  3.293E-01 0.000E+00"],"done":true,"energyRy":"-1043.64953332","name":"Ag3Ir_0_v16.958","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.3E-11","converged":true,"matrix":"4.07831502664735 0.00000000000000 0.00000000000000\r\n0.08156630053295 4.07831502664735 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.07831502664735\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0407831503 2.0391575133 2.0391575133  \r\nAg 2.0391575133 0.0000000000 2.0391575133  \r\nAg 2.0799406636 2.0391575133 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.639E-01 0.000E+00","     negative rho (up, down):  3.336E-01 0.000E+00","     negative rho (up, down):  3.410E-01 0.000E+00","     negative rho (up, down):  3.356E-01 0.000E+00","     negative rho (up, down):  3.303E-01 0.000E+00","     negative rho (up, down):  3.298E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00"],"done":true,"energyRy":"-1043.64918194","name":"Ag3Ir_g+_v16.958","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"6.7E-11","converged":true,"matrix":"4.16070245523688 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.99755897844674 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.07831502664735\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0000000000 1.9987794892 2.0391575133  \r\nAg 2.0803512276 0.0000000000 2.0391575133  \r\nAg 2.0803512276 1.9987794892 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.641E-01 0.000E+00","     negative rho (up, down):  3.335E-01 0.000E+00","     negative rho (up, down):  3.408E-01 0.000E+00","     negative rho (up, down):  3.354E-01 0.000E+00","     negative rho (up, down):  3.302E-01 0.000E+00","     negative rho (up, down):  3.296E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00"],"done":true,"energyRy":"-1043.64923660","name":"Ag3Ir_t+_v16.958","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.1E-10","converged":true,"matrix":"4.06988976888434 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.06988976888434 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.06988976888434\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0000000000 2.0349448844 2.0349448844  \r\nAg 2.0349448844 0.0000000000 2.0349448844  \r\nAg 2.0349448844 2.0349448844 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"250.0","err":{},"ecutwfc":"62.5","badConvergence":false,"cutOutput":"62.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1078.85032069","name":"Ag3Rh_0_v16.853","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"3.4E-10","converged":true,"matrix":"4.06988976888434 0.00000000000000 0.00000000000000\r\n0.08139779537769 4.06988976888434 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.06988976888434\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0406988977 2.0349448844 2.0349448844  \r\nAg 2.0349448844 0.0000000000 2.0349448844  \r\nAg 2.0756437821 2.0349448844 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"250.0","err":{},"ecutwfc":"62.5","badConvergence":false,"cutOutput":"62.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1078.84998166","name":"Ag3Rh_g+_v16.853","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.6E-10","converged":true,"matrix":"4.15210699597698 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.98930055196516 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.06988976888434\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0000000000 1.9946502760 2.0349448844  \r\nAg 2.0760534980 0.0000000000 2.0349448844  \r\nAg 2.0760534980 1.9946502760 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"250.0","err":{},"ecutwfc":"62.5","badConvergence":false,"cutOutput":"62.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1078.85003036","name":"Ag3Rh_t+_v16.853","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.0E-10","converged":true,"matrix":"4.07831502664735 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.07831502664735 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.07831502664735\r\n","conv_thr":"0.0001","positions":"Ag 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0000000000 2.0391575133 2.0391575133  \r\nAg 2.0391575133 0.0000000000 2.0391575133  \r\nAg 2.0391575133 2.0391575133 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1149.31351985","name":"Ag_Ag3Ir_0_v16.958","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.0E-11","converged":true,"matrix":"4.07831502664735 0.00000000000000 0.00000000000000\r\n0.08156630053295 4.07831502664735 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.07831502664735\r\n","conv_thr":"0.0001","positions":"Ag 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0407831503 2.0391575133 2.0391575133  \r\nAg 2.0391575133 0.0000000000 2.0391575133  \r\nAg 2.0799406636 2.0391575133 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1149.31319427","name":"Ag_Ag3Ir_g+_v16.958","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"1.9E-10","converged":true,"matrix":"4.16070245523688 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.99755897844674 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.07831502664735\r\n","conv_thr":"0.0001","positions":"Ag 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0000000000 1.9987794892 2.0391575133  \r\nAg 2.0803512276 0.0000000000 2.0391575133  \r\nAg 2.0803512276 1.9987794892 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1149.31308847","name":"Ag_Ag3Ir_t+_v16.958","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"1.3E-10","converged":true,"matrix":"4.06988976888434 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.06988976888434 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.06988976888434\r\n","conv_thr":"0.0001","positions":"Ag 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0000000000 2.0349448844 2.0349448844  \r\nAg 2.0349448844 0.0000000000 2.0349448844  \r\nAg 2.0349448844 2.0349448844 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"250.0","err":{},"ecutwfc":"62.5","badConvergence":false,"cutOutput":"62.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1149.31244948","name":"Ag_Ag3Rh_0_v16.853","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.6E-11","converged":true,"matrix":"4.06988976888434 0.00000000000000 0.00000000000000\r\n0.08139779537769 4.06988976888434 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.06988976888434\r\n","conv_thr":"0.0001","positions":"Ag 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0406988977 2.0349448844 2.0349448844  \r\nAg 2.0349448844 0.0000000000 2.0349448844  \r\nAg 2.0756437821 2.0349448844 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"250.0","err":{},"ecutwfc":"62.5","badConvergence":false,"cutOutput":"62.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1149.31211542","name":"Ag_Ag3Rh_g+_v16.853","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"1.7E-10","converged":true,"matrix":"4.15210699597698 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.98930055196516 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.06988976888434\r\n","conv_thr":"0.0001","positions":"Ag 0.0000000000 0.0000000000 0.0000000000  \r\nAg 0.0000000000 1.9946502760 2.0349448844  \r\nAg 2.0760534980 0.0000000000 2.0349448844  \r\nAg 2.0760534980 1.9946502760 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"250.0","err":{},"ecutwfc":"62.5","badConvergence":false,"cutOutput":"62.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1149.31200621","name":"Ag_Ag3Rh_t+_v16.853","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"1.6E-10","converged":true,"matrix":"4.08306705463028 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.08306705463028 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.08306705463028\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nAu 0.0000000000 2.0415335273 2.0415335273  \r\nAu 2.0415335273 0.0000000000 2.0415335273  \r\nAu 2.0415335273 2.0415335273 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.642E-01 0.000E+00","     negative rho (up, down):  3.371E-01 0.000E+00","     negative rho (up, down):  3.425E-01 0.000E+00","     negative rho (up, down):  3.350E-01 0.000E+00","     negative rho (up, down):  3.300E-01 0.000E+00","     negative rho (up, down):  3.293E-01 0.000E+00","     negative rho (up, down):  3.288E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00"],"done":true,"energyRy":"-1005.69970249","name":"Au3Ir_0_v17.018","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"3.8E-11","converged":true,"matrix":"4.08306705463028 0.00000000000000 0.00000000000000\r\n0.08166134109261 4.08306705463028 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.08306705463028\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nAu 0.0408306705 2.0415335273 2.0415335273  \r\nAu 2.0415335273 0.0000000000 2.0415335273  \r\nAu 2.0823641979 2.0415335273 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.643E-01 0.000E+00","     negative rho (up, down):  3.370E-01 0.000E+00","     negative rho (up, down):  3.424E-01 0.000E+00","     negative rho (up, down):  3.349E-01 0.000E+00","     negative rho (up, down):  3.301E-01 0.000E+00","     negative rho (up, down):  3.292E-01 0.000E+00","     negative rho (up, down):  3.288E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00","     negative rho (up, down):  3.290E-01 0.000E+00"],"done":true,"energyRy":"-1005.69945949","name":"Au3Ir_g+_v17.018","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.3E-10","converged":true,"matrix":"4.16555048055291 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.00221690997112 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.08306705463028\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nAu 0.0000000000 2.0011084550 2.0415335273  \r\nAu 2.0827752403 0.0000000000 2.0415335273  \r\nAu 2.0827752403 2.0011084550 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.644E-01 0.000E+00","     negative rho (up, down):  3.369E-01 0.000E+00","     negative rho (up, down):  3.423E-01 0.000E+00","     negative rho (up, down):  3.348E-01 0.000E+00","     negative rho (up, down):  3.305E-01 0.000E+00","     negative rho (up, down):  3.291E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     negative rho (up, down):  3.287E-01 0.000E+00","     negative rho (up, down):  3.288E-01 0.000E+00","     negative rho (up, down):  3.288E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00","     negative rho (up, down):  3.289E-01 0.000E+00"],"done":true,"energyRy":"-1005.69948983","name":"Au3Ir_t+_v17.018","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"9.6E-11","converged":true,"matrix":"4.08306705463028 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.08306705463028 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.08306705463028\r\n","conv_thr":"0.0001","positions":"Au 0.0000000000 0.0000000000 0.0000000000  \r\nAu 0.0000000000 2.0415335273 2.0415335273  \r\nAu 2.0415335273 0.0000000000 2.0415335273  \r\nAu 2.0415335273 2.0415335273 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1098.68774404","name":"Au_Au3Ir_0_v17.018","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"6.9E-11","converged":true,"matrix":"4.08306705463028 0.00000000000000 0.00000000000000\r\n0.08166134109261 4.08306705463028 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.08306705463028\r\n","conv_thr":"0.0001","positions":"Au 0.0000000000 0.0000000000 0.0000000000  \r\nAu 0.0408306705 2.0415335273 2.0415335273  \r\nAu 2.0415335273 0.0000000000 2.0415335273  \r\nAu 2.0823641979 2.0415335273 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1098.68741996","name":"Au_Au3Ir_g+_v17.018","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.8E-11","converged":true,"matrix":"4.16555048055291 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.00221690997112 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.08306705463028\r\n","conv_thr":"0.0001","positions":"Au 0.0000000000 0.0000000000 0.0000000000  \r\nAu 0.0000000000 2.0011084550 2.0415335273  \r\nAu 2.0827752403 0.0000000000 2.0415335273  \r\nAu 2.0827752403 2.0011084550 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1098.68725584","name":"Au_Au3Ir_t+_v17.018","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.0E-10","converged":true,"matrix":"3.77727325596354 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.77727325596354 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.77727325596354\r\n","conv_thr":"0.0001","positions":"Au 0.0000000000 0.0000000000 0.0000000000  \r\nAu 0.0000000000 1.8886366280 1.8886366280  \r\nAu 1.8886366280 0.0000000000 1.8886366280  \r\nAu 1.8886366280 1.8886366280 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1098.42553606","name":"Au_Cu3Au_0_v13.473","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"5.4E-12","converged":true,"matrix":"3.77727325596354 0.00000000000000 0.00000000000000\r\n0.07554546511927 3.77727325596354 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.77727325596354\r\n","conv_thr":"0.0001","positions":"Au 0.0000000000 0.0000000000 0.0000000000  \r\nAu 0.0377727326 1.8886366280 1.8886366280  \r\nAu 1.8886366280 0.0000000000 1.8886366280  \r\nAu 1.9264093605 1.8886366280 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-1098.42477857","name":"Au_Cu3Au_g+_v13.473","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"2.1E-11","converged":true,"matrix":"3.85357923738123 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.70247823421255 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.77727325596354\r\n","conv_thr":"0.0001","positions":"Au 0.0000000000 0.0000000000 0.0000000000  \r\nAu 0.0000000000 1.8512391171 1.8886366280  \r\nAu 1.9267896187 0.0000000000 1.8886366280  \r\nAu 1.9267896187 1.8512391171 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-1098.42473352","name":"Au_Cu3Au_t+_v13.473","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"2.0E-11","converged":true,"matrix":"3.77727325596354 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.77727325596354 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.77727325596354\r\n","conv_thr":"0.0001","positions":"Au 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8886366280 1.8886366280  \r\nCu 1.8886366280 0.0000000000 1.8886366280  \r\nCu 1.8886366280 1.8886366280 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-913.97773958","name":"Cu3Au_0_v13.473","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"2.1E-10","converged":true,"matrix":"3.77727325596354 0.00000000000000 0.00000000000000\r\n0.07554546511927 3.77727325596354 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.77727325596354\r\n","conv_thr":"0.0001","positions":"Au 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0377727326 1.8886366280 1.8886366280  \r\nCu 1.8886366280 0.0000000000 1.8886366280  \r\nCu 1.9264093605 1.8886366280 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-913.97740495","name":"Cu3Au_g+_v13.473","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"1.6E-10","converged":true,"matrix":"3.85357923738123 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.70247823421255 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.77727325596354\r\n","conv_thr":"0.0001","positions":"Au 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8512391171 1.8886366280  \r\nCu 1.9267896187 0.0000000000 1.8886366280  \r\nCu 1.9267896187 1.8512391171 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-913.97714303","name":"Cu3Au_t+_v13.473","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"2.8E-10","converged":true,"matrix":"3.69098665569636 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.69098665569636 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8454933278 1.8454933278  \r\nCu 1.8454933278 0.0000000000 1.8454933278  \r\nCu 1.8454933278 1.8454933278 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.660E-01 0.000E+00","     negative rho (up, down):  3.384E-01 0.000E+00","     negative rho (up, down):  3.374E-01 0.000E+00","     negative rho (up, down):  3.325E-01 0.000E+00","     negative rho (up, down):  3.250E-01 0.000E+00","     negative rho (up, down):  3.244E-01 0.000E+00","     negative rho (up, down):  3.237E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00"],"done":true,"energyRy":"-821.04085475","name":"Cu3Ir_0_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"1.4E-10","converged":true,"matrix":"3.69098665569636 0.00000000000000 0.00000000000000\r\n0.07381973311393 3.69098665569636 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0369098666 1.8454933278 1.8454933278  \r\nCu 1.8454933278 0.0000000000 1.8454933278  \r\nCu 1.8824031944 1.8454933278 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.660E-01 0.000E+00","     negative rho (up, down):  3.385E-01 0.000E+00","     negative rho (up, down):  3.374E-01 0.000E+00","     negative rho (up, down):  3.324E-01 0.000E+00","     negative rho (up, down):  3.250E-01 0.000E+00","     negative rho (up, down):  3.244E-01 0.000E+00","     negative rho (up, down):  3.241E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00"],"done":true,"energyRy":"-821.04038899","name":"Cu3Ir_g+_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"1.4E-10","converged":true,"matrix":"3.69098665569636 0.00000000000000 0.00000000000000\r\n-0.07381973311393 3.69098665569636 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nCu -0.0369098666 1.8454933278 1.8454933278  \r\nCu 1.8454933278 0.0000000000 1.8454933278  \r\nCu 1.8085834613 1.8454933278 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.660E-01 0.000E+00","     negative rho (up, down):  3.385E-01 0.000E+00","     negative rho (up, down):  3.374E-01 0.000E+00","     negative rho (up, down):  3.324E-01 0.000E+00","     negative rho (up, down):  3.250E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.243E-01 0.000E+00","     negative rho (up, down):  3.241E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00"],"done":true,"energyRy":"-821.04038899","name":"Cu3Ir_g-_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"3.6E-10","converged":true,"matrix":"3.76554953216230 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.61790022310651 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8089501116 1.8454933278  \r\nCu 1.8827747661 0.0000000000 1.8454933278  \r\nCu 1.8827747661 1.8089501116 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.659E-01 0.000E+00","     negative rho (up, down):  3.384E-01 0.000E+00","     negative rho (up, down):  3.374E-01 0.000E+00","     negative rho (up, down):  3.324E-01 0.000E+00","     negative rho (up, down):  3.254E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.246E-01 0.000E+00","     negative rho (up, down):  3.241E-01 0.000E+00","     negative rho (up, down):  3.236E-01 0.000E+00","     negative rho (up, down):  3.236E-01 0.000E+00","     negative rho (up, down):  3.237E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00"],"done":true,"energyRy":"-821.04040979","name":"Cu3Ir_t+_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"3.7E-11","converged":true,"matrix":"3.61790022310651 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.76554953216230 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8827747661 1.8454933278  \r\nCu 1.8089501116 0.0000000000 1.8454933278  \r\nCu 1.8089501116 1.8827747661 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.659E-01 0.000E+00","     negative rho (up, down):  3.384E-01 0.000E+00","     negative rho (up, down):  3.374E-01 0.000E+00","     negative rho (up, down):  3.324E-01 0.000E+00","     negative rho (up, down):  3.253E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.246E-01 0.000E+00","     negative rho (up, down):  3.241E-01 0.000E+00","     negative rho (up, down):  3.236E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.236E-01 0.000E+00","     negative rho (up, down):  3.237E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00"],"done":true,"energyRy":"-821.04040979","name":"Cu3Ir_t-_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"2.4E-10","converged":true,"matrix":"3.68069289554402 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.68069289554402 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.68069289554402\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8403464478 1.8403464478  \r\nCu 1.8403464478 0.0000000000 1.8403464478  \r\nCu 1.8403464478 1.8403464478 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-856.20646211","name":"Cu3Rh_0_v12.466","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"1.5E-10","converged":true,"matrix":"3.68069289554402 0.00000000000000 0.00000000000000\r\n0.07361385791088 3.68069289554402 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.68069289554402\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0368069290 1.8403464478 1.8403464478  \r\nCu 1.8403464478 0.0000000000 1.8403464478  \r\nCu 1.8771533767 1.8403464478 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-856.20606773","name":"Cu3Rh_g+_v12.466","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"2.2E-10","converged":true,"matrix":"3.75504782426097 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.60781029306185 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.68069289554402\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8039051465 1.8403464478  \r\nCu 1.8775239121 0.0000000000 1.8403464478  \r\nCu 1.8775239121 1.8039051465 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-856.20609472","name":"Cu3Rh_t+_v12.466","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"2.4E-10","converged":true,"matrix":"3.77727325596354 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.77727325596354 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.77727325596354\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8886366280 1.8886366280  \r\nCu 1.8886366280 0.0000000000 1.8886366280  \r\nCu 1.8886366280 1.8886366280 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-852.36932162","name":"Cu_Cu3Au_0_v13.473","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"7.6E-12","converged":true,"matrix":"3.77727325596354 0.00000000000000 0.00000000000000\r\n0.07554546511927 3.77727325596354 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.77727325596354\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0377727326 1.8886366280 1.8886366280  \r\nCu 1.8886366280 0.0000000000 1.8886366280  \r\nCu 1.9264093605 1.8886366280 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.36909108","name":"Cu_Cu3Au_g+_v13.473","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"9.0E-11","converged":true,"matrix":"3.85357923738123 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.70247823421255 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.77727325596354\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8512391171 1.8886366280  \r\nCu 1.9267896187 0.0000000000 1.8886366280  \r\nCu 1.9267896187 1.8512391171 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-852.36897391","name":"Cu_Cu3Au_t+_v13.473","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"9.6E-13","converged":true,"matrix":"3.69098665569636 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.69098665569636 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8454933278 1.8454933278  \r\nCu 1.8454933278 0.0000000000 1.8454933278  \r\nCu 1.8454933278 1.8454933278 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-852.38515428","name":"Cu_Cu3Ir_0_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"3.2E-10","converged":true,"matrix":"3.69098665569636 0.00000000000000 0.00000000000000\r\n0.07381973311393 3.69098665569636 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0369098666 1.8454933278 1.8454933278  \r\nCu 1.8454933278 0.0000000000 1.8454933278  \r\nCu 1.8824031944 1.8454933278 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.38486346","name":"Cu_Cu3Ir_g+_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"1.2E-11","converged":true,"matrix":"3.69098665569636 0.00000000000000 0.00000000000000\r\n-0.07381973311393 3.69098665569636 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu -0.0369098666 1.8454933278 1.8454933278  \r\nCu 1.8454933278 0.0000000000 1.8454933278  \r\nCu 1.8085834613 1.8454933278 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.38486346","name":"Cu_Cu3Ir_g-_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"1.0E-10","converged":true,"matrix":"3.76554953216230 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.61790022310651 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8089501116 1.8454933278  \r\nCu 1.8827747661 0.0000000000 1.8454933278  \r\nCu 1.8827747661 1.8089501116 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.38473940","name":"Cu_Cu3Ir_t+_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"7.3E-11","converged":true,"matrix":"3.61790022310651 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.76554953216230 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8827747661 1.8454933278  \r\nCu 1.8089501116 0.0000000000 1.8454933278  \r\nCu 1.8089501116 1.8827747661 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.38473940","name":"Cu_Cu3Ir_t-_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"3.3E-11","converged":true,"matrix":"3.68069289554402 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.68069289554402 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.68069289554402\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8403464478 1.8403464478  \r\nCu 1.8403464478 0.0000000000 1.8403464478  \r\nCu 1.8403464478 1.8403464478 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.38626150","name":"Cu_Cu3Rh_0_v12.466","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"3.4E-11","converged":true,"matrix":"3.68069289554402 0.00000000000000 0.00000000000000\r\n0.07361385791088 3.68069289554402 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.68069289554402\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0368069290 1.8403464478 1.8403464478  \r\nCu 1.8403464478 0.0000000000 1.8403464478  \r\nCu 1.8771533767 1.8403464478 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.38596134","name":"Cu_Cu3Rh_g+_v12.466","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"1.4E-10","converged":true,"matrix":"3.75504782426097 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.60781029306185 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.68069289554402\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.8039051465 1.8403464478  \r\nCu 1.8775239121 0.0000000000 1.8403464478  \r\nCu 1.8775239121 1.8039051465 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.38583744","name":"Cu_Cu3Rh_t+_v12.466","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"7.6E-11","converged":true,"matrix":"3.88359212916966 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.88359212916966 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.88359212916966\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.9417960646 1.9417960646  \r\nCu 1.9417960646 0.0000000000 1.9417960646  \r\nCu 1.9417960646 1.9417960646 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.33703541","name":"Cu_Pt3Cu_0_v14.643","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"1.8E-10","converged":true,"matrix":"3.88359212916966 0.00000000000000 0.00000000000000\r\n0.07767184258339 3.88359212916966 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.88359212916966\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0388359213 1.9417960646 1.9417960646  \r\nCu 1.9417960646 0.0000000000 1.9417960646  \r\nCu 1.9806319859 1.9417960646 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.33688642","name":"Cu_Pt3Cu_g+_v14.643","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"9.9E-11","converged":true,"matrix":"3.96204589429625 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.80669185267666 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.88359212916966\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nCu 0.0000000000 1.9033459263 1.9417960646  \r\nCu 1.9810229471 0.0000000000 1.9417960646  \r\nCu 1.9810229471 1.9033459263 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged"],"done":true,"energyRy":"-852.33677102","name":"Cu_Pt3Cu_t+_v14.643","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"4.0E-11","converged":true,"matrix":"4.07831502664735 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.07831502664735 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.07831502664735\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0000000000 2.0391575133 2.0391575133  \r\nIr 2.0391575133 0.0000000000 2.0391575133  \r\nIr 2.0391575133 2.0391575133 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.498E+00 0.000E+00","     negative rho (up, down):  1.383E+00 0.000E+00","     negative rho (up, down):  1.288E+00 0.000E+00","     negative rho (up, down):  1.304E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00"],"done":true,"energyRy":"-727.03478687","name":"Ir_Ag3Ir_0_v16.958","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"7.8E-12","converged":true,"matrix":"4.07831502664735 0.00000000000000 0.00000000000000\r\n0.08156630053295 4.07831502664735 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.07831502664735\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0407831503 2.0391575133 2.0391575133  \r\nIr 2.0391575133 0.0000000000 2.0391575133  \r\nIr 2.0799406636 2.0391575133 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.499E+00 0.000E+00","     negative rho (up, down):  1.383E+00 0.000E+00","     negative rho (up, down):  1.288E+00 0.000E+00","     negative rho (up, down):  1.303E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00"],"done":true,"energyRy":"-727.03396746","name":"Ir_Ag3Ir_g+_v16.958","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"1.1E-10","converged":true,"matrix":"4.16070245523688 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.99755897844674 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.07831502664735\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0000000000 1.9987794892 2.0391575133  \r\nIr 2.0803512276 0.0000000000 2.0391575133  \r\nIr 2.0803512276 1.9987794892 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.499E+00 0.000E+00","     negative rho (up, down):  1.383E+00 0.000E+00","     negative rho (up, down):  1.287E+00 0.000E+00","     negative rho (up, down):  1.303E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00"],"done":true,"energyRy":"-727.03199759","name":"Ir_Ag3Ir_t+_v16.958","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.0E-11","converged":true,"matrix":"4.08306705463028 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.08306705463028 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.08306705463028\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0000000000 2.0415335273 2.0415335273  \r\nIr 2.0415335273 0.0000000000 2.0415335273  \r\nIr 2.0415335273 2.0415335273 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.498E+00 0.000E+00","     negative rho (up, down):  1.383E+00 0.000E+00","     negative rho (up, down):  1.288E+00 0.000E+00","     negative rho (up, down):  1.304E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.278E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00"],"done":true,"energyRy":"-727.03080962","name":"Ir_Au3Ir_0_v17.018","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"7.2E-12","converged":true,"matrix":"4.08306705463028 0.00000000000000 0.00000000000000\r\n0.08166134109261 4.08306705463028 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.08306705463028\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0408306705 2.0415335273 2.0415335273  \r\nIr 2.0415335273 0.0000000000 2.0415335273  \r\nIr 2.0823641979 2.0415335273 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.499E+00 0.000E+00","     negative rho (up, down):  1.383E+00 0.000E+00","     negative rho (up, down):  1.288E+00 0.000E+00","     negative rho (up, down):  1.304E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00"],"done":true,"energyRy":"-727.03000114","name":"Ir_Au3Ir_g+_v17.018","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"2.1E-12","converged":true,"matrix":"4.16555048055291 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.00221690997112 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.08306705463028\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0000000000 2.0011084550 2.0415335273  \r\nIr 2.0827752403 0.0000000000 2.0415335273  \r\nIr 2.0827752403 2.0011084550 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.499E+00 0.000E+00","     negative rho (up, down):  1.383E+00 0.000E+00","     negative rho (up, down):  1.288E+00 0.000E+00","     negative rho (up, down):  1.303E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.277E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00","     negative rho (up, down):  1.280E+00 0.000E+00"],"done":true,"energyRy":"-727.02804142","name":"Ir_Au3Ir_t+_v17.018","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"3.8E-11","converged":true,"matrix":"3.69098665569636 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.69098665569636 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0000000000 1.8454933278 1.8454933278  \r\nIr 1.8454933278 0.0000000000 1.8454933278  \r\nIr 1.8454933278 1.8454933278 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.501E+00 0.000E+00","     negative rho (up, down):  1.396E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.290E+00 0.000E+00","     negative rho (up, down):  1.265E+00 0.000E+00","     negative rho (up, down):  1.266E+00 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.268E+00 0.000E+00","     negative rho (up, down):  1.268E+00 0.000E+00","     negative rho (up, down):  1.268E+00 0.000E+00","     negative rho (up, down):  1.268E+00 0.000E+00"],"done":true,"energyRy":"-727.02626920","name":"Ir_Cu3Ir_0_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"3.9E-11","converged":true,"matrix":"3.69098665569636 0.00000000000000 0.00000000000000\r\n0.07381973311393 3.69098665569636 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0369098666 1.8454933278 1.8454933278  \r\nIr 1.8454933278 0.0000000000 1.8454933278  \r\nIr 1.8824031944 1.8454933278 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.501E+00 0.000E+00","     negative rho (up, down):  1.396E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.290E+00 0.000E+00","     negative rho (up, down):  1.265E+00 0.000E+00","     negative rho (up, down):  1.266E+00 0.000E+00","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00"],"done":true,"energyRy":"-727.02426833","name":"Ir_Cu3Ir_g+_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"8.7E-11","converged":true,"matrix":"3.69098665569636 0.00000000000000 0.00000000000000\r\n-0.07381973311393 3.69098665569636 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr -0.0369098666 1.8454933278 1.8454933278  \r\nIr 1.8454933278 0.0000000000 1.8454933278  \r\nIr 1.8085834613 1.8454933278 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.501E+00 0.000E+00","     negative rho (up, down):  1.396E+00 0.000E+00","     negative rho (up, down):  1.279E+00 0.000E+00","     negative rho (up, down):  1.290E+00 0.000E+00","     negative rho (up, down):  1.265E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00"],"done":true,"energyRy":"-727.02426833","name":"Ir_Cu3Ir_g-_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"1.2E-11","converged":true,"matrix":"3.76554953216230 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.61790022310651 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0000000000 1.8089501116 1.8454933278  \r\nIr 1.8827747661 0.0000000000 1.8454933278  \r\nIr 1.8827747661 1.8089501116 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.501E+00 0.000E+00","     negative rho (up, down):  1.396E+00 0.000E+00","     negative rho (up, down):  1.278E+00 0.000E+00","     negative rho (up, down):  1.289E+00 0.000E+00","     negative rho (up, down):  1.264E+00 0.000E+00","     negative rho (up, down):  1.266E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00"],"done":true,"energyRy":"-727.02149808","name":"Ir_Cu3Ir_t+_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"1.2E-11","converged":true,"matrix":"3.61790022310651 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.76554953216230 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.69098665569636\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0000000000 1.8827747661 1.8454933278  \r\nIr 1.8089501116 0.0000000000 1.8454933278  \r\nIr 1.8089501116 1.8827747661 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.501E+00 0.000E+00","     negative rho (up, down):  1.396E+00 0.000E+00","     negative rho (up, down):  1.278E+00 0.000E+00","     negative rho (up, down):  1.289E+00 0.000E+00","     negative rho (up, down):  1.264E+00 0.000E+00","     negative rho (up, down):  1.266E+00 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00","     negative rho (up, down):  1.267E+00 0.000E+00"],"done":true,"energyRy":"-727.02149808","name":"Ir_Cu3Ir_t-_v12.571","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"3.4E-10","converged":true,"matrix":"3.92275813788431 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.92275813788431 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.92275813788431\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0000000000 1.9613790689 1.9613790689  \r\nIr 1.9613790689 0.0000000000 1.9613790689  \r\nIr 1.9613790689 1.9613790689 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.512E+00 0.000E+00","     negative rho (up, down):  1.396E+00 0.000E+00","     negative rho (up, down):  1.285E+00 0.000E+00","     negative rho (up, down):  1.298E+00 0.000E+00","     negative rho (up, down):  1.270E+00 0.000E+00","     negative rho (up, down):  1.271E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00"],"done":true,"energyRy":"-727.12381145","name":"Ir_Pd3Ir_0_v15.091","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"2.2E-11","converged":true,"matrix":"3.92275813788431 0.00000000000000 0.00000000000000\r\n0.07845516275769 3.92275813788431 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.92275813788431\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0392275814 1.9613790689 1.9613790689  \r\nIr 1.9613790689 0.0000000000 1.9613790689  \r\nIr 2.0006066503 1.9613790689 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.512E+00 0.000E+00","     negative rho (up, down):  1.396E+00 0.000E+00","     negative rho (up, down):  1.285E+00 0.000E+00","     negative rho (up, down):  1.297E+00 0.000E+00","     negative rho (up, down):  1.270E+00 0.000E+00","     negative rho (up, down):  1.271E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00","     negative rho (up, down):  1.273E+00 0.000E+00"],"done":true,"energyRy":"-727.12260089","name":"Ir_Pd3Ir_g+_v15.091","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"1.6E-11","converged":true,"matrix":"4.00200310887043 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.84508232245748 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.92275813788431\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nIr 0.0000000000 1.9225411612 1.9613790689  \r\nIr 2.0010015544 0.0000000000 1.9613790689  \r\nIr 2.0010015544 1.9225411612 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  1.511E+00 0.000E+00","     negative rho (up, down):  1.395E+00 0.000E+00","     negative rho (up, down):  1.284E+00 0.000E+00","     negative rho (up, down):  1.297E+00 0.000E+00","     negative rho (up, down):  1.269E+00 0.000E+00","     negative rho (up, down):  1.270E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00","     negative rho (up, down):  1.272E+00 0.000E+00"],"done":true,"energyRy":"-727.12027345","name":"Ir_Pd3Ir_t+_v15.091","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"1.1E-11","converged":true,"matrix":"3.92275813788431 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.92275813788431 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.92275813788431\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nPd 0.0000000000 1.9613790689 1.9613790689  \r\nPd 1.9613790689 0.0000000000 1.9613790689  \r\nPd 1.9613790689 1.9613790689 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.668E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.359E-01 0.000E+00","     negative rho (up, down):  3.315E-01 0.000E+00","     negative rho (up, down):  3.263E-01 0.000E+00","     negative rho (up, down):  3.233E-01 0.000E+00","     negative rho (up, down):  3.228E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00"],"done":true,"energyRy":"-941.36189636","name":"Pd3Ir_0_v15.091","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"3.3E-11","converged":true,"matrix":"3.92275813788431 0.00000000000000 0.00000000000000\r\n0.07845516275769 3.92275813788431 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.92275813788431\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nPd 0.0392275814 1.9613790689 1.9613790689  \r\nPd 1.9613790689 0.0000000000 1.9613790689  \r\nPd 2.0006066503 1.9613790689 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.668E-01 0.000E+00","     negative rho (up, down):  3.240E-01 0.000E+00","     negative rho (up, down):  3.359E-01 0.000E+00","     negative rho (up, down):  3.314E-01 0.000E+00","     negative rho (up, down):  3.262E-01 0.000E+00","     negative rho (up, down):  3.234E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.229E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.227E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00","     negative rho (up, down):  3.226E-01 0.000E+00"],"done":true,"energyRy":"-941.36129019","name":"Pd3Ir_g+_v15.091","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"5.8E-11","converged":true,"matrix":"4.00200310887043 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.84508232245748 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.92275813788431\r\n","conv_thr":"0.0001","positions":"Ir 0.0000000000 0.0000000000 0.0000000000  \r\nPd 0.0000000000 1.9225411612 1.9613790689  \r\nPd 2.0010015544 0.0000000000 1.9613790689  \r\nPd 2.0010015544 1.9225411612 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  3.666E-01 0.000E+00","     negative rho (up, down):  3.238E-01 0.000E+00","     negative rho (up, down):  3.357E-01 0.000E+00","     negative rho (up, down):  3.326E-01 0.000E+00","     negative rho (up, down):  3.297E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.248E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.233E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.228E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.225E-01 0.000E+00","     c_bands:  1 eigenvalues not converged","     c_bands:  1 eigenvalues not converged","     negative rho (up, down):  3.224E-01 0.000E+00","     c_bands:  2 eigenvalues not converged","     negative rho (up, down):  3.224E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00","     negative rho (up, down):  3.225E-01 0.000E+00"],"done":true,"energyRy":"-941.36072333","name":"Pd3Ir_t+_v15.091","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"1.0E-10","converged":true,"matrix":"3.92275813788431 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.92275813788431 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.92275813788431\r\n","conv_thr":"0.0001","positions":"Pd 0.0000000000 0.0000000000 0.0000000000  \r\nPd 0.0000000000 1.9613790689 1.9613790689  \r\nPd 1.9613790689 0.0000000000 1.9613790689  \r\nPd 1.9613790689 1.9613790689 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1012.82512668","name":"Pd_Pd3Ir_0_v15.091","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"8.7E-11","converged":true,"matrix":"3.92275813788431 0.00000000000000 0.00000000000000\r\n0.07845516275769 3.92275813788431 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.92275813788431\r\n","conv_thr":"0.0001","positions":"Pd 0.0000000000 0.0000000000 0.0000000000  \r\nPd 0.0392275814 1.9613790689 1.9613790689  \r\nPd 1.9613790689 0.0000000000 1.9613790689  \r\nPd 2.0006066503 1.9613790689 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1012.82477104","name":"Pd_Pd3Ir_g+_v15.091","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"9.6E-12","converged":true,"matrix":"4.00200310887043 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.84508232245748 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.92275813788431\r\n","conv_thr":"0.0001","positions":"Pd 0.0000000000 0.0000000000 0.0000000000  \r\nPd 0.0000000000 1.9225411612 1.9613790689  \r\nPd 2.0010015544 0.0000000000 1.9613790689  \r\nPd 2.0010015544 1.9225411612 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"550.0","err":{},"ecutwfc":"68.75","badConvergence":false,"cutOutput":"68.7500","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-1012.82458480","name":"Pd_Pd3Ir_t+_v15.091","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"1.3E-10","converged":true,"matrix":"3.88359212916966 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.88359212916966 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.88359212916966\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nPt 0.0000000000 1.9417960646 1.9417960646  \r\nPt 1.9417960646 0.0000000000 1.9417960646  \r\nPt 1.9417960646 1.9417960646 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  5.631E-01 0.000E+00","     negative rho (up, down):  5.399E-01 0.000E+00","     negative rho (up, down):  5.311E-01 0.000E+00","     negative rho (up, down):  5.301E-01 0.000E+00","     negative rho (up, down):  5.282E-01 0.000E+00","     negative rho (up, down):  5.254E-01 0.000E+00","     negative rho (up, down):  5.258E-01 0.000E+00","     negative rho (up, down):  5.257E-01 0.000E+00","     negative rho (up, down):  5.258E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00"],"done":true,"energyRy":"-845.22421688","name":"Pt3Cu_0_v14.643","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"7.6E-12","converged":true,"matrix":"3.88359212916966 0.00000000000000 0.00000000000000\r\n0.07767184258339 3.88359212916966 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.88359212916966\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nPt 0.0388359213 1.9417960646 1.9417960646  \r\nPt 1.9417960646 0.0000000000 1.9417960646  \r\nPt 1.9806319859 1.9417960646 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  5.631E-01 0.000E+00","     negative rho (up, down):  5.404E-01 0.000E+00","     negative rho (up, down):  5.315E-01 0.000E+00","     negative rho (up, down):  5.304E-01 0.000E+00","     negative rho (up, down):  5.283E-01 0.000E+00","     negative rho (up, down):  5.254E-01 0.000E+00","     negative rho (up, down):  5.258E-01 0.000E+00","     negative rho (up, down):  5.257E-01 0.000E+00","     negative rho (up, down):  5.258E-01 0.000E+00","     negative rho (up, down):  5.258E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00"],"done":true,"energyRy":"-845.22367240","name":"Pt3Cu_g+_v14.643","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"3.9E-11","converged":true,"matrix":"3.96204589429625 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.80669185267666 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.88359212916966\r\n","conv_thr":"0.0001","positions":"Cu 0.0000000000 0.0000000000 0.0000000000  \r\nPt 0.0000000000 1.9033459263 1.9417960646  \r\nPt 1.9810229471 0.0000000000 1.9417960646  \r\nPt 1.9810229471 1.9033459263 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  5.635E-01 0.000E+00","     negative rho (up, down):  5.409E-01 0.000E+00","     negative rho (up, down):  5.320E-01 0.000E+00","     negative rho (up, down):  5.309E-01 0.000E+00","     negative rho (up, down):  5.287E-01 0.000E+00","     negative rho (up, down):  5.269E-01 0.000E+00","     negative rho (up, down):  5.259E-01 0.000E+00","     negative rho (up, down):  5.261E-01 0.000E+00","     negative rho (up, down):  5.261E-01 0.000E+00","     negative rho (up, down):  5.262E-01 0.000E+00","     negative rho (up, down):  5.262E-01 0.000E+00","     negative rho (up, down):  5.262E-01 0.000E+00","     negative rho (up, down):  5.262E-01 0.000E+00","     negative rho (up, down):  5.262E-01 0.000E+00","     negative rho (up, down):  5.262E-01 0.000E+00","     negative rho (up, down):  5.262E-01 0.000E+00","     negative rho (up, down):  5.262E-01 0.000E+00"],"done":true,"energyRy":"-845.22308695","name":"Pt3Cu_t+_v14.643","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"5.8E-11","converged":true,"matrix":"3.88359212916966 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.88359212916966 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.88359212916966\r\n","conv_thr":"0.0001","positions":"Pt 0.0000000000 0.0000000000 0.0000000000  \r\nPt 0.0000000000 1.9417960646 1.9417960646  \r\nPt 1.9417960646 0.0000000000 1.9417960646  \r\nPt 1.9417960646 1.9417960646 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  7.560E-01 0.000E+00","     negative rho (up, down):  7.248E-01 0.000E+00","     negative rho (up, down):  7.061E-01 0.000E+00","     negative rho (up, down):  7.088E-01 0.000E+00","     negative rho (up, down):  7.033E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00","     negative rho (up, down):  7.030E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00"],"done":true,"energyRy":"-842.77646593","name":"Pt_Pt3Cu_0_v14.643","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"1.2E-10","converged":true,"matrix":"3.88359212916966 0.00000000000000 0.00000000000000\r\n0.07767184258339 3.88359212916966 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.88359212916966\r\n","conv_thr":"0.0001","positions":"Pt 0.0000000000 0.0000000000 0.0000000000  \r\nPt 0.0388359213 1.9417960646 1.9417960646  \r\nPt 1.9417960646 0.0000000000 1.9417960646  \r\nPt 1.9806319859 1.9417960646 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  7.560E-01 0.000E+00","     negative rho (up, down):  7.254E-01 0.000E+00","     negative rho (up, down):  7.065E-01 0.000E+00","     negative rho (up, down):  7.088E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00","     negative rho (up, down):  7.031E-01 0.000E+00","     negative rho (up, down):  7.030E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.028E-01 0.000E+00","     negative rho (up, down):  7.027E-01 0.000E+00","     negative rho (up, down):  7.027E-01 0.000E+00","     negative rho (up, down):  7.027E-01 0.000E+00","     negative rho (up, down):  7.027E-01 0.000E+00"],"done":true,"energyRy":"-842.77596036","name":"Pt_Pt3Cu_g+_v14.643","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"1.6E-10","converged":true,"matrix":"3.96204589429625 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.80669185267666 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.88359212916966\r\n","conv_thr":"0.0001","positions":"Pt 0.0000000000 0.0000000000 0.0000000000  \r\nPt 0.0000000000 1.9033459263 1.9417960646  \r\nPt 1.9810229471 0.0000000000 1.9417960646  \r\nPt 1.9810229471 1.9033459263 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored","     negative rho (up, down):  7.566E-01 0.000E+00","     negative rho (up, down):  7.260E-01 0.000E+00","     negative rho (up, down):  7.071E-01 0.000E+00","     negative rho (up, down):  7.092E-01 0.000E+00","     negative rho (up, down):  7.036E-01 0.000E+00","     negative rho (up, down):  7.035E-01 0.000E+00","     negative rho (up, down):  7.034E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00","     negative rho (up, down):  7.032E-01 0.000E+00"],"done":true,"energyRy":"-842.77530910","name":"Pt_Pt3Cu_t+_v14.643","kgrid":"17 17 17  0 0 0"},{"accuracyRy":"2.1E-10","converged":true,"matrix":"4.06988976888434 0.00000000000000 0.00000000000000\r\n0.00000000000000 4.06988976888434 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.06988976888434\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nRh 0.0000000000 2.0349448844 2.0349448844  \r\nRh 2.0349448844 0.0000000000 2.0349448844  \r\nRh 2.0349448844 2.0349448844 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"250.0","err":{},"ecutwfc":"62.5","badConvergence":false,"cutOutput":"62.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-867.61875928","name":"Rh_Ag3Rh_0_v16.853","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"6.1E-11","converged":true,"matrix":"4.06988976888434 0.00000000000000 0.00000000000000\r\n0.08139779537769 4.06988976888434 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.06988976888434\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nRh 0.0406988977 2.0349448844 2.0349448844  \r\nRh 2.0349448844 0.0000000000 2.0349448844  \r\nRh 2.0756437821 2.0349448844 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"250.0","err":{},"ecutwfc":"62.5","badConvergence":false,"cutOutput":"62.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-867.61823122","name":"Rh_Ag3Rh_g+_v16.853","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"5.1E-11","converged":true,"matrix":"4.15210699597698 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.98930055196516 0.00000000000000\r\n0.00000000000000 0.00000000000000 4.06988976888434\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nRh 0.0000000000 1.9946502760 2.0349448844  \r\nRh 2.0760534980 0.0000000000 2.0349448844  \r\nRh 2.0760534980 1.9946502760 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"250.0","err":{},"ecutwfc":"62.5","badConvergence":false,"cutOutput":"62.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-867.61714976","name":"Rh_Ag3Rh_t+_v16.853","kgrid":"16 16 16  0 0 0"},{"accuracyRy":"3.2E-11","converged":true,"matrix":"3.68069289554402 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.68069289554402 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.68069289554402\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nRh 0.0000000000 1.8403464478 1.8403464478  \r\nRh 1.8403464478 0.0000000000 1.8403464478  \r\nRh 1.8403464478 1.8403464478 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-867.65736169","name":"Rh_Cu3Rh_0_v12.466","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"1.6E-10","converged":true,"matrix":"3.68069289554402 0.00000000000000 0.00000000000000\r\n0.07361385791088 3.68069289554402 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.68069289554402\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nRh 0.0368069290 1.8403464478 1.8403464478  \r\nRh 1.8403464478 0.0000000000 1.8403464478  \r\nRh 1.8771533767 1.8403464478 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-867.65604805","name":"Rh_Cu3Rh_g+_v12.466","kgrid":"18 18 18  0 0 0"},{"accuracyRy":"3.3E-10","converged":true,"matrix":"3.75504782426097 0.00000000000000 0.00000000000000\r\n0.00000000000000 3.60781029306185 0.00000000000000\r\n0.00000000000000 0.00000000000000 3.68069289554402\r\n","conv_thr":"0.0001","positions":"Rh 0.0000000000 0.0000000000 0.0000000000  \r\nRh 0.0000000000 1.8039051465 1.8403464478  \r\nRh 1.8775239121 0.0000000000 1.8403464478  \r\nRh 1.8775239121 1.8039051465 0.0000000000  \r\n","energyCount":1,"degauss":"0.01","ecutrho":"900.0","err":{},"ecutwfc":"112.5","badConvergence":false,"cutOutput":"112.5000","warnings":["Warning: card \u0026CELL ignored","Warning: card \u0026FCP ignored","Warning: card \u0026RISM ignored"],"done":true,"energyRy":"-867.65442515","name":"Rh_Cu3Rh_t+_v12.466","kgrid":"18 18 18  0 0 0"}]

web search: 
web search: site.quantum-espresso.org "negative rho" "c_bands" ...
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '@{pbe=(Get-Content data/hiso_l12_dft_v2.csv -Raw);mace=(Get-Content data/hiso_l12_mace.csv -Raw);pure=(Get-Content data/scan_fcc_omat_pure.csv -Raw);sssp=(Get-Content harness/data/sssp_1.3.0_pbe_efficiency.json -Raw)} | ConvertTo-Json -Compress' in C:\Users\can02\Projects\AI driven Science
 succeeded in 865ms:
{"pure":{"value":"formula,comp,lattice,natoms,seed,model,vol_per_atom,a_eff,relax_steps,cubic_spread,C11,C12,C44,time,B,G,E,nu,pugh,cauchy,zener,el\r\nNi4,Ni:1.0000,fcc,4,0,medium-omat-0,10.92074197468201,3.5218488452326864,13,1.095569688286899e-13,280.61433282249305,168.77756976661377,124.78295431302875,2026-10-30T14:34:31,206.0564907852402,90.41887912911963,236.64313992087708,0.308593637745425,2.278910032615956,43.99461545358501,2.2315194199724986,Ni\r\nCu4,Cu:1.0000,fcc,4,0,medium-omat-0,11.991099263282468,3.6333424238608667,30,1.405838335779906e-13,168.0025358218953,121.01239153357562,75.09695925217237,2026-10-30T14:34:34,136.67577296301553,47.216494808319254,127.02229441035695,0.34510508378500365,2.894661569391511,45.915432281403255,3.1962855355964166,Cu\r\nPd4,Pd:1.0000,fcc,4,0,medium-omat-0,15.351033412517511,3.94517133938984,13,4.9699739028243254e-14,185.90109911600925,144.2946384415743,70.91167958381673,2026-10-30T14:34:37,158.16345866638596,43.49185415214353,119.52031379642071,0.3740540168546718,3.6366225756459443,73.38295885775757,3.408685979742005,Pd\r\nPt4,Pt:1.0000,fcc,4,0,medium-omat-0,15.527451675555266,3.9602268070240547,21,1.118214085183768e-13,288.6719725837192,228.7753835412926,67.73645282743767,2026-10-30T14:34:40,248.74091322210145,48.81870702951912,137.4631327383066,0.4078940338914241,5.095196664501904,161.03893071385494,2.2617799747981597,Pt\r\nAg4,Ag:1.0000,fcc,4,0,medium-omat-0,17.840925109818457,4.147876214129697,5,1.616166448731835e-13,112.1099858006578,81.97999793145748,43.303228214372375,2026-10-30T14:34:41,92.02332722119093,28.377938262972968,77.1983946988286,0.3601832871621209,3.242777060420254,38.6767697170851,2.8744271920957587,Ag\r\nAu4,Au:1.0000,fcc,4,0,medium-omat-0,17.920056075815886,4.153999614413019,25,2.2314773485250702e-13,160.30671151377345,131.011185033473,29.310384382771343,2026-10-30T14:34:45,140.77636052690647,22.18762950139258,63.24046513548601,0.42512892446479694,6.3448130192579075,101.70080065070165,2.001014346165165,Au\r\nAl4,Al:1.0000,fcc,4,0,medium-omat-0,16.410446749313255,4.033915517450497,19,7.267221779888226e-13,105.72994761150709,50.51149588166774,32.66617356778958,2026-10-30T14:34:47,68.91764645828086,30.53983327254447,79.82797233987796,0.3069483979738009,2.2566477637007374,17.845322313878164,1.183161517371455,Al\r\nRh4,Rh:1.0000,fcc,4,0,medium-omat-0,13.890889916682202,3.8158973814458803,51,9.54002095479854e-14,429.5549984236652,201.73384991911846,202.88408394291477,2026-10-30T14:34:52,277.6742327539674,160.94047009892313,404.643961453133,0.25712308782376475,1.7253226151464145,-1.1502340237963153,1.781082092463121,Rh\r\nIr4,Ir:1.0000,fcc,4,0,medium-omat-0,14.310425195523056,3.853933143243623,28,1.0786645757558362e-13,630.1291989891391,269.6652516767145,277.71823060616293,2026-10-30T14:34:56,389.819900780856,233.52167169759574,583.9582543157651,0.25032989458891713,1.6693093105536787,-8.052978929448443,1.5408932442581085,Ir\r\nCo4,Co:1.0000,fcc,4,0,medium-omat-0,10.874016237580149,3.5168187767249437,25,2.604108491574032e-14,292.5000303172557,169.2120751038531,148.09668059613875,2026-10-30T14:34:59,210.3080601749873,104.19486326714247,268.2792369897726,0.28739185684201374,2.018411019320444,21.115394507714342,2.402451729202484,Co\r\n","PSPath":"C:\\Users\\can02\\Projects\\AI driven Science\\data\\scan_fcc_omat_pure.csv","PSParentPath":"C:\\Users\\can02\\Projects\\AI driven Science\\data","PSChildName":"scan_fcc_omat_pure.csv","PSDrive":{"CurrentLocation":"Users\\can02\\Projects\\AI driven Science","Name":"C","Provider":"Microsoft.PowerShell.Core\\FileSystem","Root":"C:\\","Description":"","MaximumSize":null,"Credential":"System.Management.Automation.PSCredential","DisplayRoot":null},"PSProvider":{"ImplementingType":"Microsoft.PowerShell.Commands.FileSystemProvider","HelpFile":"System.Management.Automation.dll-Help.xml","Name":"FileSystem","PSSnapIn":"Microsoft.PowerShell.Core","ModuleName":"Microsoft.PowerShell.Core","Module":null,"Description":"","Capabilities":52,"Home":"C:\\Users\\can02","Drives":"C"},"ReadCount":1},"mace":{"value":"cell,method,V,E_mix,K44,Kp,time\r\nCu3Ir,mace,12.570930746342615,0.007922966900131723,-60.480692622198305,-73.26377353391179,2026-10-31T01:09:46\r\nAu3Ir,mace,17.01764835574268,0.1980301038873411,3.2063930667627205,-11.842309290055715,2026-10-31T01:09:48\r\nAg3Ir,mace,16.958300131244606,0.2825353511949964,-1.6943321412785415,-14.231864501045454,2026-10-31T01:09:49\r\nCu3Rh,mace,12.466046926632401,-0.022119947332217782,-30.506540090852575,-36.0052297807868,2026-10-31T01:09:50\r\nAg3Rh,mace,16.853416311534392,0.10310185849292175,1.1388933635108385,-3.20914102683622,2026-10-31T01:09:51\r\nPd3Ir,mace,15.090881358268899,0.13232800965835922,-14.347444565088127,-12.80101099840087,2026-10-31T01:09:53\r\nCu3Au,mace,13.473338466415823,-0.3208622345675217,-10.161705065912527,1.0358830436384283,2026-10-31T01:09:55\r\nPt3Cu,mace,14.643363572487065,-0.19250834620571533,9.76255799019013,9.89059517207147,2026-10-31T01:09:56\r\n","PSPath":"C:\\Users\\can02\\Projects\\AI driven Science\\data\\hiso_l12_mace.csv","PSParentPath":"C:\\Users\\can02\\Projects\\AI driven Science\\data","PSChildName":"hiso_l12_mace.csv","PSDrive":{"CurrentLocation":"Users\\can02\\Projects\\AI driven Science","Name":"C","Provider":"Microsoft.PowerShell.Core\\FileSystem","Root":"C:\\","Description":"","MaximumSize":null,"Credential":"System.Management.Automation.PSCredential","DisplayRoot":null},"PSProvider":{"ImplementingType":"Microsoft.PowerShell.Commands.FileSystemProvider","HelpFile":"System.Management.Automation.dll-Help.xml","Name":"FileSystem","PSSnapIn":"Microsoft.PowerShell.Core","ModuleName":"Microsoft.PowerShell.Core","Module":null,"Description":"","Capabilities":52,"Home":"C:\\Users\\can02","Drives":"C"},"ReadCount":1},"sssp":{"value":"{\n    \"Ac\": {\n        \"filename\": \"Ac.us.z_11.ld1.psl.v1.0.0-high.upf\",\n        \"md5\": \"3a78bb30464666358a3ec0edb47f6656\",\n        \"pseudopotential\": \"100US\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Ag\": {\n        \"filename\": \"Ag_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"94f47bd0669c641108e45594df92fabc\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 50.0,\n        \"cutoff_rho\": 200.0\n    },\n    \"Al\": {\n        \"filename\": \"Al.pbe-n-kjpaw_psl.1.0.0.UPF\",\n        \"md5\": \"cfc449ca30b5f3223ec38ddd88ac046d\",\n        \"pseudopotential\": \"100PAW\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Am\": {\n        \"filename\": \"Am.paw.z_17.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"b90604daea46e7f2635bfe47e71ce977\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Ar\": {\n        \"filename\": \"Ar_ONCV_PBE-1.1.oncvpsp.upf\",\n        \"md5\": \"46d28409cdd246843f76b7675277a949\",\n        \"pseudopotential\": \"SG15-1.1\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"As\": {\n        \"filename\": \"As.pbe-n-rrkjus_psl.0.2.UPF\",\n        \"md5\": \"767315de957beeeb34f87d97bf945c8f\",\n        \"pseudopotential\": \"031US\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 280.0\n    },\n    \"At\": {\n        \"filename\": \"At.us.z_17.ld1.psl.v1.0.0-high.upf\",\n        \"md5\": \"171e941146fbb8d42c50c0ba61055d18\",\n        \"pseudopotential\": \"100US\",\n        \"cutoff_wfc\": 80.0,\n        \"cutoff_rho\": 640.0\n    },\n    \"Au\": {\n        \"filename\": \"Au_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"d14007822ba0e19f0206237467fc06c2\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 180.0\n    },\n    \"B\": {\n        \"filename\": \"b_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"cc6de2960df11db49a60e589f9ebb39b\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 280.0\n    },\n    \"Ba\": {\n        \"filename\": \"Ba.pbe-spn-kjpaw_psl.1.0.0.UPF\",\n        \"md5\": \"c432291d3e53af55f19d5e8866385beb\",\n        \"pseudopotential\": \"100PAW\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Be\": {\n        \"filename\": \"be_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"5ecff1440924c7c98ad504bef30f5264\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Bi\": {\n        \"filename\": \"Bi_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"cceb9f28ec65b6d7ff33140f5b0b1758\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 360.0\n    },\n    \"Bk\": {\n        \"filename\": \"Bk.paw.z_19.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"34a5c1d9790ca2603c79955cdb099600\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Br\": {\n        \"filename\": \"br_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"d3ffb7b29f6225aa16fe06858fb2a80b\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"C\": {\n        \"filename\": \"C.pbe-n-kjpaw_psl.1.0.0.UPF\",\n        \"md5\": \"5d2aebdfa2cae82b50a7e79e9516da0f\",\n        \"pseudopotential\": \"100PAW\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 360.0\n    },\n    \"Ca\": {\n        \"filename\": \"Ca_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"403a4c14b9e4d4dfdc3024c9a3812218\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Cd\": {\n        \"filename\": \"Cd.pbe-dn-rrkjus_psl.0.3.1.UPF\",\n        \"md5\": \"558e9f355611b531a870a69ef6ace9e2\",\n        \"pseudopotential\": \"031US\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Ce\": {\n        \"filename\": \"Ce.paw.z_12.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"2241420ff980c77e0c917a2dc8a7e08e\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 50.0,\n        \"cutoff_rho\": 400.0\n    },\n    \"Cf\": {\n        \"filename\": \"Cf.paw.z_20.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"0e4adf7627c2d1305f26dd63271f2b94\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Cl\": {\n        \"filename\": \"cl_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"fc6f6913ecf08c9257cb748ef0700058\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Cm\": {\n        \"filename\": \"Cm.paw.z_18.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"fa6219561ad2ecb899c96af402755927\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Co\": {\n        \"filename\": \"Co_pbe_v1.2.uspp.F.UPF\",\n        \"md5\": \"5f91765df6ddd3222702df6e7b74a16d\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 360.0\n    },\n    \"Cr\": {\n        \"filename\": \"cr_pbe_v1.5.uspp.F.UPF\",\n        \"md5\": \"0d52af634a40206e4dee301ad30da4bf\",\n        \"pseudopotential\": \"GBRV-1.5\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Cs\": {\n        \"filename\": \"Cs_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"3476d69cb178dfad3ffaa59df4e07ca4\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Cu\": {\n        \"filename\": \"Cu.paw.z_11.ld1.psl.v1.0.0-low.upf\",\n        \"md5\": \"619f40885d92a09a85a8b37550532d0c\",\n        \"pseudopotential\": \"100PAW-low\",\n        \"cutoff_wfc\": 90.0,\n        \"cutoff_rho\": 720.0\n    },\n    \"Dy\": {\n        \"filename\": \"Dy.paw.z_20.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"fad4f994dc38884d1fc17fd7bf5e13bf\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Er\": {\n        \"filename\": \"Er.paw.z_22.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"5ba6a5c626b1678e031aafe1da34e245\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Es\": {\n        \"filename\": \"Es.paw.z_21.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"4bc7a67aee4e34db40c77f63d9e88986\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Eu\": {\n        \"filename\": \"Eu.paw.z_17.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"52b6e423bc4e840b6e0dc4248fa51623\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"F\": {\n        \"filename\": \"f_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"4c38b6a325caf53ec0e86aed9459de46\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 360.0\n    },\n    \"Fe\": {\n        \"filename\": \"Fe.pbe-spn-kjpaw_psl.0.2.1.UPF\",\n        \"md5\": \"e86618425769142926afa95317d90200\",\n        \"pseudopotential\": \"031PAW\",\n        \"cutoff_wfc\": 90.0,\n        \"cutoff_rho\": 1080.0\n    },\n    \"Fm\": {\n        \"filename\": \"Fm.paw.z_22.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"2a5ec34d2abb196d3027bbefca4b5922\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Fr\": {\n        \"filename\": \"Fr.paw.z_19.ld1.psl.v1.0.0-high.upf\",\n        \"md5\": \"4e1baa83397213ef351c329de67c4222\",\n        \"pseudopotential\": \"100PAW\",\n        \"cutoff_wfc\": 150.0,\n        \"cutoff_rho\": 1200.0\n    },\n    \"Ga\": {\n        \"filename\": \"Ga.pbe-dn-kjpaw_psl.1.0.0.UPF\",\n        \"md5\": \"a27b4342b1af7e5f338de752e9ed7044\",\n        \"pseudopotential\": \"100PAW\",\n        \"cutoff_wfc\": 70.0,\n        \"cutoff_rho\": 560.0\n    },\n    \"Gd\": {\n        \"filename\": \"Gd.paw.z_18.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"a44f32af2ba180e1a67c5cef9ff7f39b\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Ge\": {\n        \"filename\": \"ge_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"9c9eaa91e581c3f09632fb3098b2c6b2\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"H\": {\n        \"filename\": \"H.pbe-rrkjus_psl.1.0.0.UPF\",\n        \"md5\": \"f52b6d4d1c606e5624b1dc7b2218f220\",\n        \"pseudopotential\": \"100US\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"He\": {\n        \"filename\": \"He_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"e7160162b946020f132a727efeb32d00\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 50.0,\n        \"cutoff_rho\": 200.0\n    },\n    \"Hf\": {\n        \"filename\": \"Hf-sp.oncvpsp.upf\",\n        \"md5\": \"417ed15784afe83d2e06dacf143de3f8\",\n        \"pseudopotential\": \"Dojo\",\n        \"cutoff_wfc\": 50.0,\n        \"cutoff_rho\": 200.0\n    },\n    \"Hg\": {\n        \"filename\": \"Hg_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"dd5a8773074bfcf4280086d4d95875c4\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 50.0,\n        \"cutoff_rho\": 200.0\n    },\n    \"Ho\": {\n        \"filename\": \"Ho.paw.z_21.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"f900adcc49abc9ab8113872cdbacec3e\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"I\": {\n        \"filename\": \"I.pbe-n-kjpaw_psl.0.2.UPF\",\n        \"md5\": \"d4ef18d9c8f18dc85e5843bca1e50dc0\",\n        \"pseudopotential\": \"031PAW\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 280.0\n    },\n    \"In\": {\n        \"filename\": \"In.pbe-dn-rrkjus_psl.0.2.2.UPF\",\n        \"md5\": \"25e7c42c3b55b68f4bf926be2e7201a4\",\n        \"pseudopotential\": \"031US\",\n        \"cutoff_wfc\": 50.0,\n        \"cutoff_rho\": 400.0\n    },\n    \"Ir\": {\n        \"filename\": \"Ir_pbe_v1.2.uspp.F.UPF\",\n        \"md5\": \"8836f839c3459d2b385c504ce6d91f2c\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 55.0,\n        \"cutoff_rho\": 440.0\n    },\n    \"K\": {\n        \"filename\": \"K.pbe-spn-kjpaw_psl.1.0.0.UPF\",\n        \"md5\": \"7d58810084cac21f60fbe77ea2b688fd\",\n        \"pseudopotential\": \"100PAW\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Kr\": {\n        \"filename\": \"Kr_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"f2280ecf57a6c8a47e066f0532d843fa\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 180.0\n    },\n    \"La\": {\n        \"filename\": \"La.paw.z_11.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"754494e15ae71f30e5b5f678af019e01\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Li\": {\n        \"filename\": \"li_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"e912e257baa3777c20ea3d68f190483c\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Lr\": {\n        \"filename\": \"Lr.paw.z_25.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"f945946d0d1ec8347dc1259eb00091c8\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Lu\": {\n        \"filename\": \"Lu.paw.z_25.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"a517b3205eadf2aa79773283867f4cbe\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 360.0\n    },\n    \"Md\": {\n        \"filename\": \"Md.paw.z_23.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"e3e4fed06ac619855d80864afca10136\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Mg\": {\n        \"filename\": \"Mg.pbe-n-kjpaw_psl.0.3.0.UPF\",\n        \"md5\": \"24ecedc7f3e3cbe212e682f4413594e4\",\n        \"pseudopotential\": \"031PAW\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Mn\": {\n        \"filename\": \"mn_pbe_v1.5.uspp.F.UPF\",\n        \"md5\": \"82ef2b46521d7a7d9e736dc3972e4928\",\n        \"pseudopotential\": \"GBRV-1.5\",\n        \"cutoff_wfc\": 65.0,\n        \"cutoff_rho\": 780.0\n    },\n    \"Mo\": {\n        \"filename\": \"Mo_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"1b5d28e075c9ccadda658a603575cd1f\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 140.0\n    },\n    \"N\": {\n        \"filename\": \"N.pbe-n-radius_5.UPF\",\n        \"md5\": \"16739722b17309cd8fe442a2ace49922\",\n        \"pseudopotential\": \"THEOS\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Na\": {\n        \"filename\": \"na_pbe_v1.5.uspp.F.UPF\",\n        \"md5\": \"44600605ef58000f06b90626533354dc\",\n        \"pseudopotential\": \"GBRV-1.5\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Nb\": {\n        \"filename\": \"Nb.pbe-spn-kjpaw_psl.0.3.0.UPF\",\n        \"md5\": \"411d72ad547312f8017e2943ceca08cc\",\n        \"pseudopotential\": \"031PAW\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Nd\": {\n        \"filename\": \"Nd.paw.z_14.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"8a77231a7dfbac907351543c5ef6bfc9\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Ne\": {\n        \"filename\": \"Ne_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"9b5acc4cb48b9d80e669eadd528e4e8f\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 50.0,\n        \"cutoff_rho\": 200.0\n    },\n    \"Ni\": {\n        \"filename\": \"ni_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"1ee80287db30b12d2bc1f57a5b5d6409\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 360.0\n    },\n    \"No\": {\n        \"filename\": \"No.paw.z_24.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"75d6fcbe3c3afebd97ab105f1656d1c1\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Np\": {\n        \"filename\": \"Np.paw.z_15.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"2b27845584d1ae013b107a04f9c09b5b\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"O\": {\n        \"filename\": \"O.pbe-n-kjpaw_psl.0.1.UPF\",\n        \"md5\": \"0234752ac141de4415c5fc33072bef88\",\n        \"pseudopotential\": \"031PAW\",\n        \"cutoff_wfc\": 50.0,\n        \"cutoff_rho\": 400.0\n    },\n    \"Os\": {\n        \"filename\": \"Os_pbe_v1.2.uspp.F.UPF\",\n        \"md5\": \"a3fb40a04f0c37c25c34bbc47164c9a8\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"P\": {\n        \"filename\": \"P.pbe-n-rrkjus_psl.1.0.0.UPF\",\n        \"md5\": \"8b930f418f0a4573dca56cd030ffe088\",\n        \"pseudopotential\": \"100US\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Pa\": {\n        \"filename\": \"Pa.paw.z_13.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"d7b89857b2b2f446a6f8a94fd7fc0316\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Pb\": {\n        \"filename\": \"Pb.pbe-dn-kjpaw_psl.0.2.2.UPF\",\n        \"md5\": \"9d431e6316058b74ade52399a6cf67da\",\n        \"pseudopotential\": \"031PAW\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Pd\": {\n        \"filename\": \"Pd_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"eb77f42b51d86fb18e25f68156a31cf1\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 180.0\n    },\n    \"Pm\": {\n        \"filename\": \"Pm.paw.z_15.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"73dcdc0c9fe91f97d1fdb9924a622ccb\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Po\": {\n        \"filename\": \"Po.pbe-dn-rrkjus_psl.1.0.0.UPF\",\n        \"md5\": \"3f8a5a8b7a531f42ca8381c21d3cd528\",\n        \"pseudopotential\": \"100US\",\n        \"cutoff_wfc\": 75.0,\n        \"cutoff_rho\": 600.0\n    },\n    \"Pr\": {\n        \"filename\": \"Pr.paw.z_13.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"e0f8e046fa815e336ba020f7e7bc75cb\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Pt\": {\n        \"filename\": \"pt_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"f09d6de1a584b5a045c4fc126da2d0c4\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 280.0\n    },\n    \"Pu\": {\n        \"filename\": \"Pu.paw.z_16.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"566c3e560fb5ccfacef076b74913ab0c\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Ra\": {\n        \"filename\": \"Ra.paw.z_20.ld1.psl.v1.0.0-high.upf\",\n        \"md5\": \"d3f31cdfcb736122946f367071bad67a\",\n        \"pseudopotential\": \"100PAW\",\n        \"cutoff_wfc\": 90.0,\n        \"cutoff_rho\": 720.0\n    },\n    \"Rb\": {\n        \"filename\": \"Rb_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"55a5172d6bfbce6759a58e35d43f6aa9\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 120.0\n    },\n    \"Re\": {\n        \"filename\": \"Re_pbe_v1.2.uspp.F.UPF\",\n        \"md5\": \"85f993410f3e006da9d71c142b4ad953\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Rh\": {\n        \"filename\": \"Rh_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"ba07c69523b14cacd10683cd4c4284c1\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 140.0\n    },\n    \"Rn\": {\n        \"filename\": \"Rn.pbe-dn-kjpaw_psl.1.0.0.UPF\",\n        \"md5\": \"03f6b960ab99273412830d0b4aa01365\",\n        \"pseudopotential\": \"100PAW\",\n        \"cutoff_wfc\": 120.0,\n        \"cutoff_rho\": 960.0\n    },\n    \"Ru\": {\n        \"filename\": \"Ru_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"be037bb81c227cfb9b1461a9f099f4bd\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 140.0\n    },\n    \"S\": {\n        \"filename\": \"s_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"88d86576ff6df21479756cfb9bdac1df\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 280.0\n    },\n    \"Sb\": {\n        \"filename\": \"sb_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"9bc50dfb53373b713f5709b9110fe27f\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Sc\": {\n        \"filename\": \"Sc_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"e21af8023abb52e52cb7cd3133e4a229\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 160.0\n    },\n    \"Se\": {\n        \"filename\": \"Se_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"1b3568f3a8ae88f9a2a0ad0698632c85\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Si\": {\n        \"filename\": \"Si.pbe-n-rrkjus_psl.1.0.0.UPF\",\n        \"md5\": \"0b0bb1205258b0d07b9f9672cf965d36\",\n        \"pseudopotential\": \"100US\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Sm\": {\n        \"filename\": \"Sm.paw.z_16.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"d38221e44bcfc3c784cbdb498a69732f\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Sn\": {\n        \"filename\": \"Sn_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"4cf58ce39ec5d5d420df3dd08604eb00\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Sr\": {\n        \"filename\": \"Sr_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"6b418c05fbe9db5448babca5e47b7a5b\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Ta\": {\n        \"filename\": \"Ta_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"f8bbe9446314a3b8ea5d9f3e3836c939\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 45.0,\n        \"cutoff_rho\": 360.0\n    },\n    \"Tb\": {\n        \"filename\": \"Tb.paw.z_19.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"9e397ff4c8e7fcf344a3e57e25721bc0\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Tc\": {\n        \"filename\": \"Tc_ONCV_PBE-1.0.oncvpsp.upf\",\n        \"md5\": \"1c2b1e6c8b361b656073c0c20ed4f60a\",\n        \"pseudopotential\": \"SG15\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 120.0\n    },\n    \"Te\": {\n        \"filename\": \"Te_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"c319670d6894cc26e93307826a071b75\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Th\": {\n        \"filename\": \"Th.paw.z_12.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"c778f5c1781d25750cbff4a0d60de988\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"Ti\": {\n        \"filename\": \"ti_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"88a00a6731bd790ddea75d31a80cb452\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 280.0\n    },\n    \"Tl\": {\n        \"filename\": \"Tl_pbe_v1.2.uspp.F.UPF\",\n        \"md5\": \"b76cf1f7e72655a2b2c53cf6385d7059\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 50.0,\n        \"cutoff_rho\": 400.0\n    },\n    \"Tm\": {\n        \"filename\": \"Tm.paw.z_23.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"65ac1a59d66520b67f41930ed0a84655\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"U\": {\n        \"filename\": \"U.paw.z_14.ld1.uni-marburg.v0.upf\",\n        \"md5\": \"0343693cc166857ace12183ecb4b0f49\",\n        \"pseudopotential\": \"MalteSachs\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 480.0\n    },\n    \"V\": {\n        \"filename\": \"v_pbe_v1.4.uspp.F.UPF\",\n        \"md5\": \"22b79981416ebb76fdaf5b1b8640f6fb\",\n        \"pseudopotential\": \"GBRV-1.4\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 280.0\n    },\n    \"W\": {\n        \"filename\": \"W_pbe_v1.2.uspp.F.UPF\",\n        \"md5\": \"9c083fa34c2a2ea0f02f1f893e16e1c8\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Xe\": {\n        \"filename\": \"Xe_ONCV_PBE-1.1.oncvpsp.upf\",\n        \"md5\": \"f6ea899d5a535d3f5731d9e48edfe3e3\",\n        \"pseudopotential\": \"SG15-1.1\",\n        \"cutoff_wfc\": 60.0,\n        \"cutoff_rho\": 240.0\n    },\n    \"Y\": {\n        \"filename\": \"Y_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"2cf71db95cafeb975fc457bd7f14888e\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 35.0,\n        \"cutoff_rho\": 280.0\n    },\n    \"Yb\": {\n        \"filename\": \"Yb.paw.z_24.atompaw.wentzcovitch.v1.2.upf\",\n        \"md5\": \"2246be0c1287a90a9096a0c3416daab6\",\n        \"pseudopotential\": \"Wentzcovitch\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Zn\": {\n        \"filename\": \"Zn_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"df62231357ef9e81f77b2b3087fa5675\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 40.0,\n        \"cutoff_rho\": 320.0\n    },\n    \"Zr\": {\n        \"filename\": \"Zr_pbe_v1.uspp.F.UPF\",\n        \"md5\": \"5db81b1e868ab7776c4564c113de050b\",\n        \"pseudopotential\": \"GBRV-1.2\",\n        \"cutoff_wfc\": 30.0,\n        \"cutoff_rho\": 240.0\n    }\n}","PSPath":"C:\\Users\\can02\\Projects\\AI driven Science\\harness\\data\\sssp_1.3.0_pbe_efficiency.json","PSParentPath":"C:\\Users\\can02\\Projects\\AI driven Science\\harness\\data","PSChildName":"sssp_1.3.0_pbe_efficiency.json","PSDrive":{"CurrentLocation":"Users\\can02\\Projects\\AI driven Science","Name":"C","Provider":"Microsoft.PowerShell.Core\\FileSystem","Root":"C:\\","Description":"","MaximumSize":null,"Credential":"System.Management.Automation.PSCredential","DisplayRoot":null},"PSProvider":{"ImplementingType":"Microsoft.PowerShell.Commands.FileSystemProvider","HelpFile":"System.Management.Automation.dll-Help.xml","Name":"FileSystem","PSSnapIn":"Microsoft.PowerShell.Core","ModuleName":"Microsoft.PowerShell.Core","Module":null,"Description":"","Capabilities":52,"Home":"C:\\Users\\can02","Drives":"C"},"ReadCount":1},"pbe":{"value":"cell,method,kpts,V,E_mix,K44,Kp,time\r\nCu3Ir,dft_v2,18x18x18,12.570930746342615,0.01557259878734385,-54.74691675055384,-57.38539420465976,2026-10-31T20:37:36\r\nCu3Rh,dft_v2,18x18x18,12.466046926632401,-0.008250364034438462,-34.78715578271392,-37.42050958615326,2026-11-01T00:29:27\r\nPd3Ir,dft_v2,17x17x17,15.090881358268899,0.1289190757158849,6.644682704355299,-5.321163067938075,2026-11-01T02:08:10\r\nAu3Ir,dft_v2,16x16x16,17.01764835574268,0.2510520404655381,-32.3727567076859,-33.84664741248657,2026-11-01T04:10:20\r\nAg3Ir,dft_v2,16x16x16,16.958300131244606,0.3207653609897534,-15.691494965360748,-29.08829505587699,2026-11-01T05:55:23\r\nAg3Rh,dft_v2,16x16x16,16.853416311534392,0.13165629432899095,-7.037878294590145,-17.96665812599528,2026-11-01T07:00:57\r\nCu3Au,dft_v2,17x17x17,13.473338466415823,-0.32097306888442745,-5.5914144369890275,6.832279696830556,2026-11-01T09:14:36\r\nPt3Cu,dft_v2,17x17x17,14.643363572487065,-0.1959511480412175,23.828501484675826,9.127699571762257,2026-11-01T11:42:51\r\n","PSPath":"C:\\Users\\can02\\Projects\\AI driven Science\\data\\hiso_l12_dft_v2.csv","PSParentPath":"C:\\Users\\can02\\Projects\\AI driven Science\\data","PSChildName":"hiso_l12_dft_v2.csv","PSDrive":{"CurrentLocation":"Users\\can02\\Projects\\AI driven Science","Name":"C","Provider":"Microsoft.PowerShell.Core\\FileSystem","Root":"C:\\","Description":"","MaximumSize":null,"Credential":"System.Management.Automation.PSCredential","DisplayRoot":null},"PSProvider":{"ImplementingType":"Microsoft.PowerShell.Commands.FileSystemProvider","HelpFile":"System.Management.Automation.dll-Help.xml","Name":"FileSystem","PSSnapIn":"Microsoft.PowerShell.Core","ModuleName":"Microsoft.PowerShell.Core","Module":null,"Description":"","Capabilities":52,"Home":"C:\\Users\\can02","Drives":"C"},"ReadCount":1}}

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'rg -n "c_bands|negative rho|convergence has|iteration #|estimated scf accuracy" data/dft_runs/hiso2/Pd3Ir_t+_v15.091/pw.out | Select-Object -Last 30; Get-ChildItem data/dft_runs/hiso2 -Recurse -Filter pw.err | Where-Object {$_.Length -gt 0} | Select-Object FullName,Length; rg -n "''^" scripts/hiso_l12_v2.py; rg -n "''^" harness/dft.py | Select-Object -First 125' in C:\Users\can02\Projects\AI driven Science
 succeeded in 1081ms:
245:     estimated scf accuracy    <       0.00031828 Ry
247:     iteration #  9     ecut=    68.75 Ry     beta= 0.30
249:     c_bands:  1 eigenvalues not converged
250:     c_bands:  1 eigenvalues not converged
253:     negative rho (up, down):  3.224E-01 0.000E+00
258:     estimated scf accuracy    <       0.00021263 Ry
260:     iteration # 10     ecut=    68.75 Ry     beta= 0.30
262:     c_bands:  2 eigenvalues not converged
265:     negative rho (up, down):  3.224E-01 0.000E+00
270:     estimated scf accuracy    <       0.00000930 Ry
272:     iteration # 11     ecut=    68.75 Ry     beta= 0.30
276:     negative rho (up, down):  3.225E-01 0.000E+00
281:     estimated scf accuracy    <       0.00000049 Ry
283:     iteration # 12     ecut=    68.75 Ry     beta= 0.30
287:     negative rho (up, down):  3.225E-01 0.000E+00
292:     estimated scf accuracy    <       0.00000005 Ry
294:     iteration # 13     ecut=    68.75 Ry     beta= 0.30
298:     negative rho (up, down):  3.225E-01 0.000E+00
303:     estimated scf accuracy    <          5.7E-09 Ry
305:     iteration # 14     ecut=    68.75 Ry     beta= 0.30
309:     negative rho (up, down):  3.225E-01 0.000E+00
314:     estimated scf accuracy    <          5.0E-10 Ry
316:     iteration # 15     ecut=    68.75 Ry     beta= 0.30
320:     negative rho (up, down):  3.225E-01 0.000E+00
331:     estimated scf accuracy    <          5.8E-11 Ry
341:     convergence has been achieved in  15 iterations
343:     negative rho (up, down):  3.225E-01 0.000E+00
358:     negative rho (up, down):  3.225E-01 0.000E+00
379:     c_bands      :    483.24s CPU    493.67s WALL (      15 calls)
385:     Called by c_bands:
1:"""H-iso check, corrected numerics (v2): clamped mixing shear curvatures K44, Kp of cubic L1_2 cells with PBE.
2:
3:python scripts/hiso_l12_v2.py [dense]
4:Fixes found by the swarm S1 audit in scripts/hiso_l12.py: the alloy and both pure references now share one cutoff
5:(ecut_elements = (A, B)) and one k-grid, taken from the unstrained cell, for every strain. "dense" repeats Cu3Ir and
6:Ag3Rh at kspacing 0.08 as a convergence check. Criteria 6cb3c2a936 are unchanged; the old results are not used.
7:A3B L1_2 (4-atom cubic cell, B on the corner site), clamped at Vegard volume, pure fcc references at the same volume
8:and the same deformation. Strains +-0.02 (three-point curvature). PBE uses kspacing 0.10 (shear needs the fine grid).
9:"""
10:
11:import datetime as dt
12:import os
13:import sys
14:from pathlib import Path
15:
16:ROOT = Path(__file__).resolve().parent.parent
17:os.environ["HARNESS_MODEL"] = "medium-omat-0"
18:sys.path.insert(0, str(ROOT))
19:
20:import numpy as np  # noqa: E402
21:import pandas as pd  # noqa: E402
22:from ase.build import bulk  # noqa: E402
23:
24:from harness.compute import GPA  # noqa: E402
25:
26:CELLS = [("Cu", "Ir"), ("Cu", "Rh"), ("Pd", "Ir"), ("Au", "Ir"), ("Ag", "Ir"), ("Ag", "Rh"),  # A3B with Ir/Rh
27:         ("Cu", "Au"), ("Pt", "Cu")]  # controls without Ir/Rh; order = MACE |K| (PBE is slow, strongest first)
28:S = 0.02
29:SYM_DONE = {"Cu3Ir": ("g-", "t-")}  # computed both signs here; used as the symmetry check
30:METHOD = "dft"
31:DENSE = "dense" in sys.argv
32:KSP = 0.08 if DENSE else 0.10
33:if DENSE:
34:    CELLS = [("Cu", "Ir"), ("Ag", "Rh")]
35:pv = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")["vol_per_atom"]
36:
37:from harness import dft  # noqa: E402
38:
39:NP = int(os.environ.get("HISO_NP", "2"))
40:ST = {}
41:
42:
43:def energy(atoms, tag):
44:    return dft.run_pw(atoms, f"hiso2{'d' if DENSE else ''}/{tag}", ST["s"]).get_potential_energy() / len(atoms)
45:
46:DEF = {"0": np.eye(3), "g+": np.eye(3) + S * np.outer([1, 0, 0], [0, 1, 0]),
47:       "g-": np.eye(3) - S * np.outer([1, 0, 0], [0, 1, 0]),
48:       "t+": np.diag([np.exp(S), np.exp(-S), 1.0]), "t-": np.diag([np.exp(-S), np.exp(S), 1.0])}
49:
50:
51:def strained(symbols, v, F):
52:    a = bulk("Cu", "fcc", a=4.0, cubic=True)
53:    a.symbols = list(symbols)
54:    a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
55:    a.set_cell(a.cell @ F.T, scale_atoms=True)
56:    return a
57:
58:
59:OUT = ROOT / "data" / f"hiso_l12_dft_v2{'_dense' if DENSE else ''}.csv"
60:done = set(pd.read_csv(OUT)["cell"]) if OUT.exists() else set()
61:for A, B in CELLS:
62:    name = f"{A}3{B}"
63:    if name in done:
64:        continue
65:    v = 0.75 * pv[A] + 0.25 * pv[B]
66:    vt = f"{v:.3f}"
67:    ST["s"] = dft.Settings(kspacing=KSP, np=NP, ecut_elements=(A, B),
68:                           kpts=dft.kgrid(strained([B, A, A, A], v, np.eye(3)), KSP))
69:    em = {}
70:    for k, F in DEF.items():
71:        if k in ("g-", "t-") and k not in SYM_DONE.get(name, ()):  # cubic L1_2: y -> -y and x <-> y are symmetries
72:            continue
73:        e_ab = energy(strained([B, A, A, A], v, F), f"{name}_{k}_v{vt}")
74:        e_a = energy(strained([A] * 4, v, F), f"{A}_{name}_{k}_v{vt}")
75:        e_b = energy(strained([B] * 4, v, F), f"{B}_{name}_{k}_v{vt}")
76:        em[k] = e_ab - 0.75 * e_a - 0.25 * e_b
77:    em.setdefault("g-", em["g+"])
78:    em.setdefault("t-", em["t+"])
79:    c44 = (em["g+"] + em["g-"] - 2 * em["0"]) / (2 * S**2)   # E = c s^2
80:    cp = (em["t+"] + em["t-"] - 2 * em["0"]) / (2 * S**2)
81:    r = {"cell": name, "method": "dft_v2", "kpts": "x".join(map(str, ST["s"].kpts)), "V": v, "E_mix": em["0"], "K44": 2 * c44 / v * GPA, "Kp": cp / (2 * v) * GPA,
82:         "time": dt.datetime.now().isoformat(timespec="seconds")}
83:    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
84:    print(name, f"E_mix {em['0']*1000:+7.1f} meV  K44 {r['K44']:+7.2f}  Kp {r['Kp']:+7.2f} GPa", flush=True)
1:"""Quantum ESPRESSO (pw.x in WSL) as the L3 reference for stresses and elastic constants.
2:
3:QE lives in a conda-forge env inside WSL (micromamba env "qe", no sudo needed).
4:Pseudopotentials: SSSP 1.3.0 PBE efficiency, md5 a58f1b3373f330179fd0832c48bb9a52,
5:Materials Cloud Archive 2023.65, doi:10.24435/materialscloud:f3-ym.
6:"""
7:
8:from __future__ import annotations
9:
10:import datetime as dt
11:import json
12:import re
13:import subprocess
14:from dataclasses import dataclass, field
15:from pathlib import Path
16:
17:import numpy as np
18:from ase import Atoms
19:from ase.io import read, write
20:
21:from harness.compute import GPA, cubic_average, voigt_reuss_hill
22:
23:ROOT = Path(__file__).resolve().parent.parent
24:RUNS = ROOT / "data" / "dft_runs"
25:DISTRO = "Ubuntu-22.04"
26:PSEUDO_DIR = "/home/can02/pseudo/sssp_eff_1.3"
27:SSSP = json.loads((Path(__file__).parent / "data" / "sssp_1.3.0_pbe_efficiency.json").read_text())
28:
29:# Collinear starting moments for the magnetic 3d metals. Cr gets an antiferromagnetic
30:# start on the two bcc sublattices; a commensurate AFM cell is an approximation of its SDW.
31:MAGNETIC = {"Fe": 0.4, "Co": 0.4, "Ni": 0.3, "Mn": 0.4, "Cr": 0.4}
32:
33:
34:@dataclass
35:class Settings:
36:    kspacing: float = 0.15          # 1/A, Monkhorst-Pack density (2*pi included)
37:    ecut_scale: float = 1.25        # stresses need a margin above the SSSP energy cutoff
38:    degauss: float = 0.01           # Ry, Marzari-Vanderbilt
39:    np: int = 8                     # 8 physical cores
40:    extra: dict = field(default_factory=dict)
41:    # Elements whose cutoffs also set this run's cutoff. For mixing energies and curvatures pass the alloy's elements
42:    # to the pure references too, so all terms share one basis (before 2026-10-31 each run used only its own).
43:    ecut_elements: tuple = ()
44:    # Fixed Monkhorst-Pack grid. Finite-strain curvatures must use one grid for every strain; the default picks it from
45:    # the strained cell, which changes it between strains (18x18x18 vs 17x18x18 for Cu3Ir, found 2026-10-31).
46:    kpts: tuple | None = None
47:
48:
49:def wsl_path(p: Path) -> str:
50:    s = str(p.resolve()).replace("\\", "/")
51:    return f"/mnt/{s[0].lower()}{s[2:]}"
52:
53:
54:def kgrid(atoms: Atoms, kspacing: float) -> tuple[int, int, int]:
55:    rec = np.linalg.norm(atoms.cell.reciprocal(), axis=1) * 2 * np.pi
56:    return tuple(max(1, int(np.ceil(r / kspacing))) for r in rec)
57:
58:
59:def magnetize(atoms: Atoms) -> bool:
60:    """Set initial moments in place; AFM checkerboard for Cr. Returns True if spin polarised."""
61:    mags = np.array([MAGNETIC.get(s, 0.0) for s in atoms.get_chemical_symbols()])
62:    if not mags.any():
63:        return False
64:    if "Cr" in atoms.get_chemical_symbols():
65:        a = (2 * atoms.get_volume() / len(atoms)) ** (1 / 3)  # bcc conventional lattice parameter
66:        parity = np.round(2 * atoms.positions[:, 0] / a).astype(int) % 2  # corner vs body centre
67:        mags = np.where(np.array(atoms.get_chemical_symbols()) == "Cr", mags * (1 - 2 * parity), mags)
68:    atoms.set_initial_magnetic_moments(mags * 5)  # ASE maps moments to starting_magnetization
69:    return True
70:
71:
72:def run_pw(atoms: Atoms, tag: str, s: Settings, relax_ions: bool = False) -> Atoms:
73:    """Run one pw.x scf/relax with stress. Cached: an existing finished output is reused."""
74:    d = RUNS / tag
75:    d.mkdir(parents=True, exist_ok=True)
76:    out = d / "pw.out"
77:    els = sorted(set(atoms.get_chemical_symbols()))
78:    basis = set(els) | set(s.ecut_elements)
79:    ecut = float(s.extra.get("system.ecutwfc", s.ecut_scale * max(SSSP[e]["cutoff_wfc"] for e in basis)))
80:    ecutrho = s.ecut_scale * max(SSSP[e]["cutoff_rho"] for e in basis)
81:    if out.exists() and "JOB DONE" in out.read_text(errors="ignore"):
82:        cached = re.search(r"ecutwfc\s*=\s*([\d.]+)", (d / "pw.in").read_text())
83:        if cached and abs(float(cached.group(1)) - ecut) > 1e-6:  # a cache hit must not silently change the basis
84:            raise RuntimeError(f"{tag}: cached run used ecutwfc {cached.group(1)}, requested {ecut}; use a new tag")
85:        return read(out, format="espresso-out", index=-1)
86:    scratch = tag.replace("/", "__")
87:    atoms = atoms.copy()
88:    # extra={'system.nspin': 1} must switch magnetism off: initial moments make ASE write nspin 2 back (S3 audit)
89:    spin = s.extra.get("system.nspin", 2) != 1 and magnetize(atoms)
90:    data = {"control": {"calculation": "relax" if relax_ions else "scf", "tstress": True,
91:                        "tprnfor": True, "pseudo_dir": PSEUDO_DIR, "outdir": f"/tmp/qe/{scratch}",
92:                        "disk_io": "low", "forc_conv_thr": 1e-4},
93:            "system": {"ecutwfc": ecut, "ecutrho": ecutrho, "occupations": "smearing",
94:                       "smearing": "mv", "degauss": s.degauss, "nspin": 2 if spin else 1},
95:            "electrons": {"conv_thr": 1e-10 * len(atoms), "mixing_beta": 0.3}}
96:    for k, v in s.extra.items():
97:        data.setdefault(k.split(".")[0], {})[k.split(".")[1]] = v
98:    write(d / "pw.in", atoms, format="espresso-in", input_data=data,
99:          pseudopotentials={e: SSSP[e]["filename"] for e in els}, kpts=s.kpts or kgrid(atoms, s.kspacing))
100:    cmd = (f"export MAMBA_ROOT_PREFIX=~/mamba OMP_NUM_THREADS=1; mkdir -p /tmp/qe/{scratch}; cd '{wsl_path(d)}' && "
101:           f"~/bin/micromamba run -n qe mpirun -np {s.np} pw.x -nk {min(s.np, 4)} -in pw.in > pw.out 2> pw.err; "
102:           f"rm -rf /tmp/qe/{scratch}")
103:    subprocess.run(["wsl", "-d", DISTRO, "--", "bash", "-lc", cmd], check=True)
104:    text = out.read_text(errors="ignore")
105:    if "JOB DONE" not in text or "convergence NOT achieved" in text:
106:        raise RuntimeError(f"pw.x failed for {tag}, see {out}")
107:    return read(out, format="espresso-out", index=-1)
108:
109:
110:def stress(atoms: Atoms, tag: str, s: Settings, relax_ions: bool) -> np.ndarray:
111:    return read_stress(run_pw(atoms, tag, s, relax_ions))
112:
113:
114:def read_stress(a: Atoms) -> np.ndarray:
115:    return a.get_stress(voigt=True) * GPA  # ASE sign: tensile positive
116:
117:
118:def elastic_cubic(atoms: Atoms, tag: str, s: Settings, eps: float = 0.01, full: bool = False,
119:                  relax_ions: bool | None = None) -> np.ndarray:
120:    """6x6 tensor (GPa) by central differences. full=False uses only e_xx and e_yz,
121:    which is exact for a cubic crystal and enough for pure elements (4 pw.x runs)."""
122:    if relax_ions is None:
123:        relax_ions = len(set(atoms.get_chemical_symbols())) > 1
124:    cell0 = atoms.get_cell().array.copy()
125:    voigt = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]

codex
78 ham koşunun tamamı SCF yakınsamasını tamamlamış; enerjilerden yeniden hesaplanan K44 ve K′ değerleri CSV ile uyuşuyor. Ancak ek bir sayısal sınır var: 34 çıktıda son aşamaya kadar `negative rho`, 27 çıktıda da ara iterasyonlarda özdeğer yakınsama uyarıları bulunuyor. Bu nedenle SCF’nin bitmesini, eğriliklerin k-ağı ve cutoff bakımından yakınsadığına eşitlemeyeceğim.

2026-11-01T22:33:58.730067Z ERROR codex_core::tools::router: error=apply_patch verification failed: Failed to find expected lines in C:\Users\can02\.codex\memories\MEMORY.md:
- rollout_summaries/2026-10-11T05-55-40-QDRm-daily_materials_brief_stainless_steel_sensitization_weld_dec.md (cwd=\\?\C:\Users\can02\Documents\Codex\2026-10-11\every-day-create-a-substantial-english, rollout_path=\\?\C:\Users\can02\.codex\sessions\2026\10\11\rollout-2026-10-11T08-55-40-01a12987-fee8-7440-890f-c8dbd09a1fa8.jsonl, updated_at=2026-10-11T05:58:52+00:00, thread_id=01a12987-fee8-7440-890f-c8dbd09a1fa8, validated output)
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '
Get-ChildItem data/dft_runs/hiso2 -Directory | ForEach-Object {
 $lines=Get-Content -LiteralPath (Join-Path $_.FullName '"'pw.out')
 "'$iter=0; $lastbad=0; $neg='"''; "'$negline=0; $ln=0
 foreach($l in $lines){
  $ln++
  if($l -match '"'iteration #\\s+(\\d+)'){"'$iter=[int]$Matches[1]}
  if($l -match '"'c_bands:\\s+\\d+ eigenvalues not converged'){"'$lastbad=$iter}
  if($l -match '"'negative rho'){"'$neg=$l.Trim();$negline=$ln}
 }
 if($lastbad -gt 0){"BANDS $($_.Name) last_warning_iteration=$lastbad final_iteration=$iter"}
 if($_.Name -match '"'"'^(Ir_Cu3Ir|Cu3Ir|Pt3Cu|Pt_Pt3Cu|Au3Ir|Ag3Ir)_0_'"'){\"RHO "'$($_.Name) line=$negline $neg"}
}
rg -n '"'"'^'"\\s+conv_thr|charge density cutoff|scf convergence threshold|nspin|calculation' data/dft_runs/hiso2 -g pw.in -g pw.out | Select-Object -First 12
Get-FileHash scripts/hiso_l12.py,scripts/hiso_l12_v2.py -Algorithm SHA256 | Format-List
rg -n \"Starting|Program PWSCF|JOB DONE\" data/dft_runs/hiso2/Cu3Ir_0_v12.571/pw.out
rg -n \""'^" C:/Users/can02/.codex/memories/MEMORY.md | Select-Object -First 50
' in C:\Users\can02\Projects\AI driven Science
 exited 1 in 1181ms:
RHO Ag3Ir_0_v16.958 line=308 negative rho (up, down):  3.293E-01 0.000E+00
RHO Au3Ir_0_v17.018 line=321 negative rho (up, down):  3.291E-01 0.000E+00
BANDS Au3Ir_g+_v17.018 last_warning_iteration=9 final_iteration=13
BANDS Au_Cu3Au_g+_v13.473 last_warning_iteration=7 final_iteration=9
BANDS Au_Cu3Au_t+_v13.473 last_warning_iteration=1 final_iteration=9
BANDS Cu3Au_g+_v13.473 last_warning_iteration=4 final_iteration=12
BANDS Cu3Au_t+_v13.473 last_warning_iteration=4 final_iteration=12
RHO Cu3Ir_0_v12.571 line=325 negative rho (up, down):  3.240E-01 0.000E+00
BANDS Cu3Ir_g-_v12.571 last_warning_iteration=7 final_iteration=14
BANDS Cu3Ir_t+_v12.571 last_warning_iteration=5 final_iteration=14
BANDS Cu3Ir_t-_v12.571 last_warning_iteration=14 final_iteration=15
BANDS Cu3Rh_g+_v12.466 last_warning_iteration=5 final_iteration=14
BANDS Cu_Cu3Au_g+_v13.473 last_warning_iteration=6 final_iteration=14
BANDS Cu_Cu3Ir_g+_v12.571 last_warning_iteration=6 final_iteration=13
BANDS Cu_Cu3Ir_g-_v12.571 last_warning_iteration=13 final_iteration=15
BANDS Cu_Cu3Ir_t+_v12.571 last_warning_iteration=4 final_iteration=13
BANDS Cu_Cu3Ir_t-_v12.571 last_warning_iteration=13 final_iteration=14
BANDS Cu_Cu3Rh_0_v12.466 last_warning_iteration=6 final_iteration=12
BANDS Cu_Cu3Rh_g+_v12.466 last_warning_iteration=14 final_iteration=15
BANDS Cu_Cu3Rh_t+_v12.466 last_warning_iteration=12 final_iteration=13
BANDS Cu_Pt3Cu_0_v14.643 last_warning_iteration=4 final_iteration=11
BANDS Cu_Pt3Cu_g+_v14.643 last_warning_iteration=4 final_iteration=13
BANDS Cu_Pt3Cu_t+_v14.643 last_warning_iteration=4 final_iteration=13
BANDS Ir_Ag3Ir_t+_v16.958 last_warning_iteration=6 final_iteration=14
BANDS Ir_Cu3Ir_0_v12.571 last_warning_iteration=6 final_iteration=12
RHO Ir_Cu3Ir_0_v12.571 line=297 negative rho (up, down):  1.268E+00 0.000E+00
BANDS Ir_Cu3Ir_g+_v12.571 last_warning_iteration=6 final_iteration=12
BANDS Ir_Cu3Ir_g-_v12.571 last_warning_iteration=6 final_iteration=12
BANDS Ir_Cu3Ir_t-_v12.571 last_warning_iteration=6 final_iteration=14
BANDS Pd3Ir_g+_v15.091 last_warning_iteration=7 final_iteration=15
BANDS Pd3Ir_t+_v15.091 last_warning_iteration=10 final_iteration=15
RHO Pt3Cu_0_v14.643 line=324 negative rho (up, down):  5.259E-01 0.000E+00
RHO Pt_Pt3Cu_0_v14.643 line=295 negative rho (up, down):  7.028E-01 0.000E+00
data/dft_runs/hiso2\Ag3Ir_t+_v16.958\pw.out:54:     charge density cutoff     =     550.0000  Ry
data/dft_runs/hiso2\Ag3Ir_t+_v16.958\pw.out:55:     scf convergence threshold =      4.0E-10
data/dft_runs/hiso2\Ag3Ir_t+_v16.958\pw.out:285:     End of self-consistent calculation
data/dft_runs/hiso2\Ag3Ir_0_v16.958\pw.out:54:     charge density cutoff     =     550.0000  Ry
data/dft_runs/hiso2\Ag3Ir_0_v16.958\pw.out:55:     scf convergence threshold =      4.0E-10
data/dft_runs/hiso2\Ag3Ir_0_v16.958\pw.out:274:     End of self-consistent calculation
data/dft_runs/hiso2\Ag3Ir_t+_v16.958\pw.in:2:   calculation      = 'scf'
data/dft_runs/hiso2\Ag3Ir_t+_v16.958\pw.in:16:   nspin            = 1
data/dft_runs/hiso2\Ag3Ir_t+_v16.958\pw.in:22:   conv_thr         = 4e-10
data/dft_runs/hiso2\Ag3Ir_0_v16.958\pw.in:2:   calculation      = 'scf'
data/dft_runs/hiso2\Ag3Ir_0_v16.958\pw.in:16:   nspin            = 1
data/dft_runs/hiso2\Ag3Ir_0_v16.958\pw.in:22:   conv_thr         = 4e-10


Algorithm : SHA256
Hash      : 7177EED8629CF5D084942C8E01DA24E2BFA108C16260E28DC05F3986FE71A370
Path      : C:\Users\can02\Projects\AI driven Science\scripts\hiso_l12.py

Algorithm : SHA256
Hash      : C45E4122A6D27BEBB034A6BC9F39BB865C3D134D7750E0D63B9C9B6D1F4A94C3
Path      : C:\Users\can02\Projects\AI driven Science\scripts\hiso_l12_v2.py



2:     Program PWSCF v.7.6 starts on 31Oct2026 at 14:14:20 
141:     Starting wfcs are   39 randomized atomic wfcs
383:   JOB DONE.
1:# Task Group: AI driven Science alloy-energy and elasticity claim audit
2:scope: Read-only review of candidate formulas, data/generator defects, PBE controls, and claim wording; use before treating alloy-energy, shear, or L2 results as validated discoveries.
3:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=read `.orchestra/LESSONS.md`, inspect the live ledger/data/scripts, keep `data/sealed/` unread unless the current workflow explicitly authorizes the arena, and treat all historical numerical claims as checkout-specific.
4:
5:## Task 1: Diagnose emix_random residuals and propose ctx-only candidates, partial
6:
7:### rollout_summary_files
8:
9:- rollout_summaries/2026-10-31T21-44-08-GISz-emix_random_vec_filling_candidate_and_sro_diagnostics.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8677-7d23-8736-9feecdd1a527.jsonl, updated_at=2026-10-31T11:15:16+00:00, thread_id=01a193eb-8677-7d23-8736-9feecdd1a527, strongest candidate not sealed-tested)
10:- rollout_summaries/2026-10-31T21-44-08-Qzmv-k_volume_transfer_anharmonicity_and_triplet_candidates.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-865c-74c3-b444-bb194b9c0aaf.jsonl, updated_at=2026-10-31T11:15:22+00:00, thread_id=01a193eb-865c-74c3-b444-bb194b9c0aaf, physical interpretation remains unresolved)
11:- rollout_summaries/2026-10-31T09-44-10-dWvd-emix_random_target_artifact_and_candidate_analysis.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\31\rollout-2026-10-31T12-44-10-01a19158-6021-7482-9551-9958d2b1cbff.jsonl, updated_at=2026-10-31T07:44:28+00:00, thread_id=01a19158-6021-7482-9551-9958d2b1cbff, establishes generator bookkeeping error)
12:
13:### keywords
14:
15:- emix_random, champion_volume_transfer.py, comp_actual, exact-count references, VEC, SRO, k_direct.py, ctx-only, sealed-holdout
16:
17:## Task 2: Audit holdout accounting, PBE controls, stale corrections, and anomaly claims, success/partial
18:
19:### rollout_summary_files
20:
21:- rollout_summaries/2026-10-31T21-44-08-N62j-l3_ci_gate_confidence_interval_defect.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8452-7b32-8fa5-dc42e5b07c5f.jsonl, updated_at=2026-10-31T20:51:16+00:00, thread_id=01a193eb-8452-7b32-8fa5-dc42e5b07c5f, latent L3 CI-gate defect)
22:- rollout_summaries/2026-10-31T21-44-08-ZwwK-alloy_regularity_audit_and_muggianu_baseline.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8488-7e21-ac6a-1e70f3f52ec6.jsonl, updated_at=2026-10-31T20:49:29+00:00, thread_id=01a193eb-8488-7e21-ac6a-1e70f3f52ec6, energy baseline demotion; K' survives)
23:- rollout_summaries/2026-10-31T21-44-08-KHDr-audit_shared_seed_leakage_pbe_shear_and_fixed_volume_excess.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8481-7b31-b53b-774b6fa2efa9.jsonl, updated_at=2026-10-31T20:15:15+00:00, thread_id=01a193eb-8481-7b31-b53b-774b6fa2efa9, shared-seed and validation-gate audit)
24:- rollout_summaries/2026-10-31T21-44-07-Uafy-audit_backfill_emix_structure_mismatch.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-83d0-7c91-a6e0-3820ae4da47c.jsonl, updated_at=2026-10-31T21:13:54+00:00, thread_id=01a193eb-83d0-7c91-a6e0-3820ae4da47c, structural reconstruction mismatch)
25:- rollout_summaries/2026-10-31T21-44-08-tMXk-audit_holdout_accounting_pbe_kmesh_and_l2_parent_errors.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8694-7b63-8ed9-478e5ea983e6.jsonl, updated_at=2026-10-31T11:13:12+00:00, thread_id=01a193eb-8694-7b63-8ed9-478e5ea983e6, three substantive issues)
26:- rollout_summaries/2026-10-31T21-44-08-bz70-audit_stale_derived_columns_composition_correction_zener_ani.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8606-7342-88b7-c496909afa26.jsonl, updated_at=2026-10-31T11:34:50+00:00, thread_id=01a193eb-8606-7342-88b7-c496909afa26, corrected-data audit)
27:- rollout_summaries/2026-10-31T21-44-08-3Ad3-silver_anomalies_mechanism_and_cutoff_error.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8654-7ab2-83f8-79124f513e41.jsonl, updated_at=2026-10-31T11:18:57+00:00, thread_id=01a193eb-8654-7ab2-83f8-79124f513e41, Ag mechanism partly unverified)
28:- rollout_summaries/2026-10-31T21-44-08-0sbZ-audit_ag_anomaly_claims_cutoff_kgrid_mechanism.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-85ea-7283-8340-585074438f97.jsonl, updated_at=2026-10-31T11:36:25+00:00, thread_id=01a193eb-85ea-7283-8340-585074438f97, controls corrected but reruns pending)
29:- rollout_summaries/2026-10-31T21-44-07-ik6S-cobalt_anomaly_mace_pbe_discriminator.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-835c-7861-9fb8-803628c6364a.jsonl, updated_at=2026-10-31T21:43:57+00:00, thread_id=01a193eb-835c-7861-9fb8-803628c6364a, diagnostic incomplete)
30:
31:### keywords
32:
33:- 207 unseen alloys, h3_fresh_rows_fixed, hm_fresh_rows_fixed, fixed k-mesh, ecut_elements, l2_search.py, Zener anisotropy, shared-permutation leak, backfill_emix.py, L3 95% CI, own-volume Muggianu
34:
35:## Task 3: Audit cobalt K44 controls, spin state, and matched MACE/PBE design, success/partial
36:
37:### rollout_summary_files
38:
39:- rollout_summaries/2026-11-01T21-57-13-hXmh-audit_cobalt_anomaly_spin_mace_pbe_tests.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfb-72e3-85ce-9cf49c2550d9.jsonl, updated_at=2026-10-31T22:53:56+00:00, thread_id=01a1991d-dbfb-72e3-85ce-9cf49c2550d9, spin-control bug verified; experiments redesigned)
40:- rollout_summaries/2026-10-31T21-44-07-VJVR-validate_k44_shear_transfer_hypotheses.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-8431-7393-ae70-82453cb5df2f.jsonl, updated_at=2026-10-31T20:57:09+00:00, thread_id=01a193eb-8431-7393-ae70-82453cb5df2f, direction/seed averaging retained; composition asymmetry dropped)
41:
42:### keywords
43:
44:- cobalt anomaly, Co K44, nspin, magnetize(), ASE espresso.py, MACE, PBE, disjoint seeds, same-site substitution, K44/Kp, seed permutation
45:
46:## User preferences
47:
48:- when auditing, the user required errors over new formulas and `file:line`, evidence, and numerical size -> lead with concrete reproducible defects quantified in meV/GPa; keep the investigation read-only and use concise structured proposals when requested. [Task 2]
49:- when proposing alloy rules, the user said “Do not edit files. Put your candidates in your answer” and prohibited `data/sealed/` access -> use only the `ctx` contract, at most the requested fitted coefficient count, a physical mechanism, numerical prediction, test, falsifier, and cost; do not present cross-source or synthetic estimates as sealed validation. [Task 1]
50:

web search: 
web search: https://lists.quantum-espresso.org/pipermail/users/2019-January/041908.html
web search: 
web search: 
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "
rg -n 'c_bands:|iteration #\\s+1[345]|convergence has' data/dft_runs/hiso2/Cu3Ir_t-_v12.571/pw.out
rg -n 'negative rho|convergence has' data/dft_runs/hiso2/Ir_Cu3Ir_0_v12.571/pw.out | Select-Object -Last 5
rg -n 'create_units|energy=energy|free_energy=energy|_get_energy' .venv/Lib/site-packages/ase/io/espresso.py
Get-ChildItem data/dft_runs/hiso2 -Directory | ForEach-Object {
 "'$ins=Get-Content -LiteralPath (Join-Path $_.FullName '"'pw.in') -Raw
 "'$outs=Get-Content -LiteralPath (Join-Path $_.FullName '"'pw.out') -Raw
 "'$inrho=[regex]::Match($ins,'"'ecutrho\\s*=\\s*([\\d.]+)').Groups[1].Value
 "'$outrho=[regex]::Match($outs,'"'charge density cutoff\\s*=\\s*([\\d.]+)').Groups[1].Value
 "'$conv=[regex]::Match($ins,'"'(?m)"'^'"\\s+conv_thr\\s*=\\s*([\\d.eE+-]+)').Groups[1].Value
 if(([double]"'$inrho -ne [double]$outrho) -or ([double]$conv -ne 4e-10)){"MISMATCH $($_.Name)"}
}
' in C:\Users\can02\Projects\AI driven Science
 succeeded in 1558ms:
196:     c_bands:  1 eigenvalues not converged
230:     c_bands:  1 eigenvalues not converged
284:     iteration # 13     ecut=   112.50 Ry     beta= 0.30
295:     iteration # 14     ecut=   112.50 Ry     beta= 0.30
297:     c_bands:  1 eigenvalues not converged
307:     iteration # 15     ecut=   112.50 Ry     beta= 0.30
333:     convergence has been achieved in  15 iterations
378:     Called by c_bands:
248:     negative rho (up, down):  1.268E+00 0.000E+00
259:     negative rho (up, down):  1.268E+00 0.000E+00
280:     convergence has been achieved in  12 iterations
282:     negative rho (up, down):  1.268E+00 0.000E+00
297:     negative rho (up, down):  1.268E+00 0.000E+00
37:from ase.units import create_units
41:units = create_units('2006')
231:        energy = find_thing(_get_energy, indexes[_PW_TOTEN])
362:        calc = SinglePointDFTCalculator(structure, energy=energy,
363:                                        free_energy=energy,
2072:def _get_energy(pwo_lines, energy_index):

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "rg -n \"sha256|hashlib|hexdigest\" harness/ledger.py; Get-ChildItem .orchestra -Filter '*hiso*' -Recurse | Select-Object -First 10 FullName; rg -n \""'^" scripts/hiso_l12.py | Select-Object -Last 30' in C:\Users\can02\Projects\AI driven Science
 succeeded in 947ms:
10:import hashlib
19:    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]
37:    entry = {"id": hashlib.sha256(f"{now}{claim}".encode()).hexdigest()[:10], "time": now,
51:    a.symbols = list(symbols)
52:    a.set_cell(a.cell * (v * 4 / a.get_volume()) ** (1 / 3), scale_atoms=True)
53:    a.set_cell(a.cell @ F.T, scale_atoms=True)
54:    return a
55:
56:
57:OUT = ROOT / "data" / f"hiso_l12_{METHOD}.csv"
58:done = set(pd.read_csv(OUT)["cell"]) if OUT.exists() else set()
59:for A, B in CELLS:
60:    name = f"{A}3{B}"
61:    if name in done:
62:        continue
63:    v = 0.75 * pv[A] + 0.25 * pv[B]
64:    vt = f"{v:.3f}"
65:    em = {}
66:    for k, F in DEF.items():
67:        if k in ("g-", "t-") and k not in SYM_DONE.get(name, ()):  # cubic L1_2: y -> -y and x <-> y are symmetries
68:            continue
69:        e_ab = energy(strained([B, A, A, A], v, F), f"{name}_{k}_v{vt}")
70:        e_a = energy(strained([A] * 4, v, F), f"{A}_{k}_v{vt}")
71:        e_b = energy(strained([B] * 4, v, F), f"{B}_{k}_v{vt}")
72:        em[k] = e_ab - 0.75 * e_a - 0.25 * e_b
73:    em.setdefault("g-", em["g+"])
74:    em.setdefault("t-", em["t+"])
75:    c44 = (em["g+"] + em["g-"] - 2 * em["0"]) / (2 * S**2)   # E = c s^2
76:    cp = (em["t+"] + em["t-"] - 2 * em["0"]) / (2 * S**2)
77:    r = {"cell": name, "method": METHOD, "V": v, "E_mix": em["0"], "K44": 2 * c44 / v * GPA, "Kp": cp / (2 * v) * GPA,
78:         "time": dt.datetime.now().isoformat(timespec="seconds")}
79:    pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
80:    print(name, f"E_mix {em['0']*1000:+7.1f} meV  K44 {r['K44']:+7.2f}  Kp {r['Kp']:+7.2f} GPa", flush=True)

web search: 
web search: https://lists.quantum-espresso.org/pipermail/users/2019-January/041911.html
2026-11-01T22:35:04.040675Z ERROR codex_core::tools::router: error=apply_patch verification failed: Failed to find expected lines in C:\Users\can02\.codex\memories\memory_summary.md:
- Alloy-energy candidates and scientific-claim audit: emix_random, comp_actual, k_direct.py, fixed k-mesh, ecut_elements, 207 unseen alloys, shared-permutation leak
  - desc: Search first for ctx-only candidate work, holdout accounting, PBE finite-difference controls, data-correction bugs, or Co/Ag anomaly claims in cwd=C:\Users\can02\Projects\AI driven Science.
  - learnings: Exact common-volume transfer is near k=0.94 rather than linear k�%^0.81; separate selection/holdout/sealed data, preserve actual compositions, and rerun PBE with fixed k-mesh/shared cutoff before physical claims.
codex
**Sayısal okuman doğru; ancak H-iso için koşulsuz PASS yerine PLAUSIBLE veriyorum.** Hücre-içi işaret yorumuyla kayıtlı eşik geçiliyor; global yorumda geçilmiyor. Ayrıca ham çıktılar “uyarısız” değil. Dosya değiştirmedim.

[Ön kayıttaki](</C:/Users/can02/Projects/AI driven Science/claims/claims.jsonl:33>) `K44 ≈ Kp` hipotezi ve oran ölçütü, **her hücrede iki kanalın işaretinin uyuşması** yorumunu destekliyor. Fakat “all K44, Kp same sign” bunu açıkça belirtmiyor; bütün değerlerin ortak işaret taşıması da metnin mümkün, daha katı okuması. Kayıt Pt3Cu’yu kontrol olarak tanımlıyor, pozitif işaret beklentisini ayrıca belirtmiyor.

[PBE verisinden](</C:/Users/can02/Projects/AI driven Science/data/hiso_l12_dft_v2.csv:2>) yeniden hesaplanan seçili hücreler:

| Hücre | K44, GPa | K′, GPa | K44/K′ |
|---|---:|---:|---:|
| Cu3Ir | −54.747 | −57.385 | 0.954 |
| Cu3Rh | −34.787 | −37.421 | 0.930 |
| Au3Ir | −32.373 | −33.847 | 0.956 |
| Ag3Ir | −15.691 | −29.088 | 0.539 |
| Ag3Rh | −7.038 | −17.967 | 0.392 |
| Pt3Cu | +23.829 | +9.128 | 2.611 |

- **Hücre-içi yorum: PASS.** n=6; altısında da işaretler uyuşuyor; medyan oran **0.941825**.
- **Global yorum: FAIL.** Beş hücre negatif, Pt3Cu pozitif. Kontrol olması, eşik üstündeki Pt3Cu’yu dışlama yetkisi vermiyor.
- Bu, yalnızca kayıtlı **medyan** testinin başarısıdır. Altı oranın üçü aralığın dışında; “her hücre yaklaşık izotropik” sonucu çıkmaz.

Sayısal denetimde şunları doğruladım:

- **Ham enerji → CSV:** 78 `pw.out` dosyasındaki son enerjilerden sekiz hücreyi yeniden hesapladım. K değerlerinde en büyük fark **4.3×10⁻⁸ GPa**; hesaplama ve aktarım uyuşuyor. Bu fark, fiziksel doğruluk tahmini değildir.
- **Birimler ve üç nokta:** [79–81. satırlardaki](</C:/Users/can02/Projects/AI driven Science/scripts/hiso_l12_v2.py:79>) katsayılar doğru. Atom başına enerji için  
  \(K_{44}=160.21766208\,\Delta_g^2E/(Vs^2)\),  
  \(K'=160.21766208\,\Delta_t^2E/(4Vs^2)\).  
  `s=0.02` kayıtla uyumlu. Ancak tek genlik, \(O(s^2)\) sonlu-fark hatasını veya dördüncü derece katkıyı ölçmüyor.
- **Simetri kısayolu:** İdeal, clamped kübik L1₂ hücrelerinde yansıma `g↔−g`, eksen değişimi `t↔−t` eşdeğerliğini sağlıyor. Bu yüzden kopyalama geçerli. Cu3Ir’de ayrı hesaplanan ± dallarının karışım enerjileri çıktı hassasiyetinde eşit. Diğer hücrelerde bu eşitlik ölçülmüş değil, simetriyle uygulanmış.
- **Hacim ve referanslar:** Sekiz hacim de tam olarak `0.75 V_A + 0.25 V_B`; kaynak **MACE-omat saf-element hacimleri**, PBE denge hacimleri değil. PBE–MACE aynı geometride karşılaştırılıyor. Bütün girdilerde atom sayıları, deformasyonlar ve saf referans geometrileri doğru.
- **Cutoff/k-ağı düzeltmesi:** 78 girdide alaşım ve referansların `ecutwfc`, `ecutrho`, tam k-ağı ve kaydırmaları eşleşiyor; strain boyunca sabitler. Çıktı cutoff’ları da girdilerle uyumlu. [v2 düzeltmesi](</C:/Users/can02/Projects/AI driven Science/scripts/hiso_l12_v2.py:65>) gerçekten uygulanmış.
- **SCF tamam; “uyarı yok” yanlış.** 78/78 koşuda yakınsama ve `JOB DONE` var; son tahmini SCF hatası en fazla **3.8×10⁻¹⁰ Ry**. Boş namelist uyarılarına ek olarak 27 dosyada `c_bands` uyarısı var; son iterasyonda kalmıyor, fakat bazılarında sondan bir önceki iterasyona ulaşıyor. Daha önemlisi, 34 dosyada `negative rho` sürüyor: örneğin [saf Ir referansında 1.268](</C:/Users/can02/Projects/AI driven Science/data/dft_runs/hiso2/Ir_Cu3Ir_0_v12.571/pw.out:297>), [Pt3Cu’da 0.5259](</C:/Users/can02/Projects/AI driven Science/data/dft_runs/hiso2/Pt3Cu_0_v14.643/pw.out:324>). Bunlar tek başına eğriliklerin yanlışlığını kanıtlamaz; fakat zararsız oldukları gösterilmeden geçiştirilemez. [QE kılavuzu](https://www.quantum-espresso.org/Doc/pw_user_guide/node21.html) bu durumda yük yoğunluğu cutoff’unun kontrolünü öneriyor.

Dolayısıyla dense-k sonucu, strain-genliği kontrolü ve özellikle `ecutrho` duyarlılığı hâlâ önemli. **Dense-k tek başına cutoff sorununu çözmez.** Enerjiler ayrıca `degauss=0.01 Ry` ile hesaplanan sonlu-smearing enerjileri; sıfır-smearing yakınsaması gösterilmiş değil.

Seçim bakımından sekiz kayıtlı hücrenin tamamı mevcut; sonuca göre hücre atıldığını görmedim. Pd3Ir ve Cu3Au’nun H-iso’dan çıkarılması önceden tanımlanan eşikten kaynaklanıyor. MACE L1 için ise sekizinin tamamı kullanılmalı. Medyanı sonradan hücre başına toleransa çevirmek veya Pt3Cu’yu çıkarmak ölçüt değişikliği olur. Bir provenance sınırı da var: mevcut `hiso_l12.py` hash’i `7177eed8629cf5d0`, kayıttaki `c76da785e56fb704` ile aynı değil; kayıt anındaki kodun birebir sürümünü bu dosyadan doğrulayamıyorum.

**MACE L1 açıkça FAIL:** K44 işareti Pd3Ir, Au3Ir ve Ag3Rh’de yanlış; K′ işaretleri 8/8 doğru. İki kanalı birleştirince medyan mutlak fark **11.087 GPa**, medyan mutlak PBE **20.898 GPa**, oran **%53.05**. Kanallar ayrı değerlendirilse de sonuç kurtulmuyor: K44 **%56.11**, K′ **%47.26**. Fiziksel kalibrasyonun kesinliği yukarıdaki PBE yakınsama sınırlarına bağlı.

Bu test **makalenin K′ transfer kuralını ne doğruluyor ne çürütüyor**: ordered A₃B hücrelerini karşılaştırıyor; PBE ikili girdilerden bağımsız multicomponent hedef tahmini yapmıyor. Ancak K′ işaretlerinin tutmasının nicel kalibrasyon sağlamadığını gösteriyor. [Taslağın PBE doğrulamasını gelecekteki iş olarak bırakması](</C:/Users/can02/Projects/AI driven Science/paper/draft_v3.md:172>) yerinde.

VERDICT PLAUSIBLE — H-iso in PBE  
VERDICT FAIL — MACE L1


tokens used
140.921
**Sayısal okuman doğru; ancak H-iso için koşulsuz PASS yerine PLAUSIBLE veriyorum.** Hücre-içi işaret yorumuyla kayıtlı eşik geçiliyor; global yorumda geçilmiyor. Ayrıca ham çıktılar “uyarısız” değil. Dosya değiştirmedim.

[Ön kayıttaki](</C:/Users/can02/Projects/AI driven Science/claims/claims.jsonl:33>) `K44 ≈ Kp` hipotezi ve oran ölçütü, **her hücrede iki kanalın işaretinin uyuşması** yorumunu destekliyor. Fakat “all K44, Kp same sign” bunu açıkça belirtmiyor; bütün değerlerin ortak işaret taşıması da metnin mümkün, daha katı okuması. Kayıt Pt3Cu’yu kontrol olarak tanımlıyor, pozitif işaret beklentisini ayrıca belirtmiyor.

[PBE verisinden](</C:/Users/can02/Projects/AI driven Science/data/hiso_l12_dft_v2.csv:2>) yeniden hesaplanan seçili hücreler:

| Hücre | K44, GPa | K′, GPa | K44/K′ |
|---|---:|---:|---:|
| Cu3Ir | −54.747 | −57.385 | 0.954 |
| Cu3Rh | −34.787 | −37.421 | 0.930 |
| Au3Ir | −32.373 | −33.847 | 0.956 |
| Ag3Ir | −15.691 | −29.088 | 0.539 |
| Ag3Rh | −7.038 | −17.967 | 0.392 |
| Pt3Cu | +23.829 | +9.128 | 2.611 |

- **Hücre-içi yorum: PASS.** n=6; altısında da işaretler uyuşuyor; medyan oran **0.941825**.
- **Global yorum: FAIL.** Beş hücre negatif, Pt3Cu pozitif. Kontrol olması, eşik üstündeki Pt3Cu’yu dışlama yetkisi vermiyor.
- Bu, yalnızca kayıtlı **medyan** testinin başarısıdır. Altı oranın üçü aralığın dışında; “her hücre yaklaşık izotropik” sonucu çıkmaz.

Sayısal denetimde şunları doğruladım:

- **Ham enerji → CSV:** 78 `pw.out` dosyasındaki son enerjilerden sekiz hücreyi yeniden hesapladım. K değerlerinde en büyük fark **4.3×10⁻⁸ GPa**; hesaplama ve aktarım uyuşuyor. Bu fark, fiziksel doğruluk tahmini değildir.
- **Birimler ve üç nokta:** [79–81. satırlardaki](</C:/Users/can02/Projects/AI driven Science/scripts/hiso_l12_v2.py:79>) katsayılar doğru. Atom başına enerji için  
  \(K_{44}=160.21766208\,\Delta_g^2E/(Vs^2)\),  
  \(K'=160.21766208\,\Delta_t^2E/(4Vs^2)\).  
  `s=0.02` kayıtla uyumlu. Ancak tek genlik, \(O(s^2)\) sonlu-fark hatasını veya dördüncü derece katkıyı ölçmüyor.
- **Simetri kısayolu:** İdeal, clamped kübik L1₂ hücrelerinde yansıma `g↔−g`, eksen değişimi `t↔−t` eşdeğerliğini sağlıyor. Bu yüzden kopyalama geçerli. Cu3Ir’de ayrı hesaplanan ± dallarının karışım enerjileri çıktı hassasiyetinde eşit. Diğer hücrelerde bu eşitlik ölçülmüş değil, simetriyle uygulanmış.
- **Hacim ve referanslar:** Sekiz hacim de tam olarak `0.75 V_A + 0.25 V_B`; kaynak **MACE-omat saf-element hacimleri**, PBE denge hacimleri değil. PBE–MACE aynı geometride karşılaştırılıyor. Bütün girdilerde atom sayıları, deformasyonlar ve saf referans geometrileri doğru.
- **Cutoff/k-ağı düzeltmesi:** 78 girdide alaşım ve referansların `ecutwfc`, `ecutrho`, tam k-ağı ve kaydırmaları eşleşiyor; strain boyunca sabitler. Çıktı cutoff’ları da girdilerle uyumlu. [v2 düzeltmesi](</C:/Users/can02/Projects/AI driven Science/scripts/hiso_l12_v2.py:65>) gerçekten uygulanmış.
- **SCF tamam; “uyarı yok” yanlış.** 78/78 koşuda yakınsama ve `JOB DONE` var; son tahmini SCF hatası en fazla **3.8×10⁻¹⁰ Ry**. Boş namelist uyarılarına ek olarak 27 dosyada `c_bands` uyarısı var; son iterasyonda kalmıyor, fakat bazılarında sondan bir önceki iterasyona ulaşıyor. Daha önemlisi, 34 dosyada `negative rho` sürüyor: örneğin [saf Ir referansında 1.268](</C:/Users/can02/Projects/AI driven Science/data/dft_runs/hiso2/Ir_Cu3Ir_0_v12.571/pw.out:297>), [Pt3Cu’da 0.5259](</C:/Users/can02/Projects/AI driven Science/data/dft_runs/hiso2/Pt3Cu_0_v14.643/pw.out:324>). Bunlar tek başına eğriliklerin yanlışlığını kanıtlamaz; fakat zararsız oldukları gösterilmeden geçiştirilemez. [QE kılavuzu](https://www.quantum-espresso.org/Doc/pw_user_guide/node21.html) bu durumda yük yoğunluğu cutoff’unun kontrolünü öneriyor.

Dolayısıyla dense-k sonucu, strain-genliği kontrolü ve özellikle `ecutrho` duyarlılığı hâlâ önemli. **Dense-k tek başına cutoff sorununu çözmez.** Enerjiler ayrıca `degauss=0.01 Ry` ile hesaplanan sonlu-smearing enerjileri; sıfır-smearing yakınsaması gösterilmiş değil.

Seçim bakımından sekiz kayıtlı hücrenin tamamı mevcut; sonuca göre hücre atıldığını görmedim. Pd3Ir ve Cu3Au’nun H-iso’dan çıkarılması önceden tanımlanan eşikten kaynaklanıyor. MACE L1 için ise sekizinin tamamı kullanılmalı. Medyanı sonradan hücre başına toleransa çevirmek veya Pt3Cu’yu çıkarmak ölçüt değişikliği olur. Bir provenance sınırı da var: mevcut `hiso_l12.py` hash’i `7177eed8629cf5d0`, kayıttaki `c76da785e56fb704` ile aynı değil; kayıt anındaki kodun birebir sürümünü bu dosyadan doğrulayamıyorum.

**MACE L1 açıkça FAIL:** K44 işareti Pd3Ir, Au3Ir ve Ag3Rh’de yanlış; K′ işaretleri 8/8 doğru. İki kanalı birleştirince medyan mutlak fark **11.087 GPa**, medyan mutlak PBE **20.898 GPa**, oran **%53.05**. Kanallar ayrı değerlendirilse de sonuç kurtulmuyor: K44 **%56.11**, K′ **%47.26**. Fiziksel kalibrasyonun kesinliği yukarıdaki PBE yakınsama sınırlarına bağlı.

Bu test **makalenin K′ transfer kuralını ne doğruluyor ne çürütüyor**: ordered A₃B hücrelerini karşılaştırıyor; PBE ikili girdilerden bağımsız multicomponent hedef tahmini yapmıyor. Ancak K′ işaretlerinin tutmasının nicel kalibrasyon sağlamadığını gösteriyor. [Taslağın PBE doğrulamasını gelecekteki iş olarak bırakması](</C:/Users/can02/Projects/AI driven Science/paper/draft_v3.md:172>) yerinde.

VERDICT PLAUSIBLE — H-iso in PBE  
VERDICT FAIL — MACE L1


