OpenAI Codex v0.160.0
--------
workdir: C:\Users\can02\Projects\AI driven Science
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a1a0db-45b7-7423-86c1-0bf6e7b1704d
--------
user
Görev: scripts/k_asym_w1.py düzeltilmiş sürümünü yeniden denetle. Dosya değiştirme. Önceki incelemen .orchestra/audits/w1_design_astra.md içinde (NO-GO). Her maddenin düzeltilip düzeltilmediğini tek tek söyle: kol seçimi hatası, yan etkili import, kapsam/adlandırma (BV), hedef başına seed, bileşimsel gürültü ve sınır null'u, ekstrapolasyon ve t aralığı, bileşimle eşleştirme, ön kayıt hash kontrolü, alt grup raporu. Yeni hata var mı? Not: k_shear_transfer.curvatures ile kopyalanan curvatures() kanal sırası farklı (K44 sonra Kp yerine Kp sonra K44 hesaplanıyor), bu sonucu değiştirir mi?
Sonunda: VERDICT GO / GO WITH FIXES / NO-GO.

warning: Codex is ignoring 1 unrecognized configuration setting. Check for typos or deprecated settings.
  user (C:\Users\can02\.codex\config.toml): `computer_use.windows.always_allowed_app_ids` is ignored.
warning: Codex is ignoring 1 unrecognized configuration setting. Check for typos or deprecated settings.
  user (C:\Users\can02\.codex\config.toml): `computer_use.windows.always_allowed_app_ids` is ignored.
warning: Under-development features enabled: local_thread_store_compression. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in C:\Users\can02\.codex\config.toml.
warning: clamping SessionEnd hook timeout to 3s in C:\Users\can02\.codex\plugins\cache\openai-codex\codex\1.0.6\hooks\hooks.json
2026-11-03T10:01:29.511748Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when UnexpectedServerResponse("HTTP 403: <html>\n  <head>\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n    <style global>body{font-family:Arial,Helvetica,sans-serif}.container{align-items:center;display:flex;flex-direction:column;gap:2rem;height:100%;justify-content:center;width:100%}@keyframes enlarge-appear{0%{opacity:0;transform:scale(75%) rotate(-90deg)}to{opacity:1;transform:scale(100%) rotate(0deg)}}.logo{color:#8e8ea0}.scale-appear{animation:enlarge-appear .4s ease-out}@media (min-width:768px){.scale-appear{height:48px;width:48px}}.data:empty{display:none}.data{border-radius:5px;color:#8e8ea0;text-align:center}@media (prefers-color-scheme:dark){body{background-color:#343541}.logo{color:#acacbe}}</style>\n  <meta http-equiv=\"refresh\" content=\"360\"></head>\n  <body>\n    <div class=\"container\">\n      <div class=\"logo\">\n        <svg\n          width=\"41\"\n          height=\"41\"\n          viewBox=\"0 0 41 41\"\n          fill=\"none\"\n          xmlns=\"http://www.w3.org/2000/svg\"\n          strokeWidth=\"2\"\n          class=\"scale-appear\"\n        >\n          <path\n            d=\"M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z\"\n            fill=\"currentColor\"\n          />\n        </svg>\n      </div>\n      <div class=\"data\"><div class=\"main-wrapper\" role=\"main\"><div class=\"main-content\"><noscript><div class=\"h2\"><span id=\"challenge-error-text\">Enable JavaScript and cookies to continue</span></div></noscript></div></div><script>(function(){window._cf_chl_opt = {cFPWv: 'g',cH: 'NT3FDGM3MZpPr.lqR4kS361X_nz.zzg04kEp7uApP7E-1793700089-1.2.1.1-ucraDHE4RmcEdP3I2ZU6wzd64FwgzCIiUIWoM2hT7Pmgu6O0sB3HAgCmUktp3Ol_',cITimeS: '1793700089',cRay: 'a54a89ba0c1e49da',cTplC:1,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:\"/backend-api/product-account-links/mcp?__cf_chl_tk=3z5JkNO1zR12kAnvnutLE1zI1VNyUmNXAs65ugC0EV4-1793700089-1.0.1.1-6hyriRltJwC2SzyIo_kMdmK88nxqoRGAIKLR3aD8kvQ\",cvId: '3',cZone: 'chatgpt.com',fa:\"/backend-api/product-account-links/mcp?__cf_chl_f_tk=3z5JkNO1zR12kAnvnutLE1zI1VNyUmNXAs65ugC0EV4-1793700089-1.0.1.1-6hyriRltJwC2SzyIo_kMdmK88nxqoRGAIKLR3aD8kvQ\",md: 'C5cbxwuksYQZpyqhGktfrw.gol9nOsTKH7r0IbeeaUg-1793700089-1.2.1.1-CMoYua8teqFR5J8za0YNGIWrsiAEoGqaTqGRCFbiydOZWJmja96Rv_sIMbde9dfILdQhXrjC0W_bdX4yj_tKknHpbHnbrB9XzbnPEp8KXJsrweF9hb_rmrUfZXavO40FndVVYJRae_TBV0cSgUerKzTJkN_crLWZ2M698jvJ_ERqNiJcLS.t6kUjZDgG3RfQBr8ycNjFWONlBaiWuQnjwR_XmZrJ3pRm1NlPleCVuPG1_5RqFRpWqonpN8mxUn6Y2d0SWH.FN8nrzpTws1i3.onvY2a.B4Gv2ID5OL2BPLldJdd0TohmUcn7vYjgJ_9EwIKa3DY8XtOoUnDkPmy9bsYkS.Fv71hTS_Rf_f6xV_LcgYx6wv7TC3C0Jy.ACtUdzaYRvw3Bkvc2AnYy4hwt79enu8ABJamSsg04e46azj8rmk3IJQ0vgQUKqKvjamCcoM0Cy4qVTigYYlzwDg.6eKvZqFlo6hyC5fmVC6xdQDOJ6LPbocL.VtOyKQpkLr0e9wve9WwsEDoXlz9dskB37yAPeV1dN_xEnJmfrE7H7jxm.AbfRRuI5CyNQWZ2ezSvKaIhsDkPLol3grE1ssMkjhMMqpnZLcazDHUuknuw2bO4FBkiUnrKF8C7SMoCHqhaWSPAeBtDXj1CrbB1RYZ4gmL0fGr3hppH.obYA8r0vwWDQpqIst61EZbTY7QzMdeusPlwMU73EAS0FUPErI9WUGVgUe25AvfXpk4t9J8ntdgCuteCRar7Z3EtPExZNaiB4MrCYVTFaY0xQoZuHjWcwHXkrntlLupJPs9F1KLBdROe1su.NrpYFitotK5qPAU9JdoemTjjjRbckFcmxtUtAXDGZkhcxtvH7hrdzXDOPTCrVPeR3xu_wH8.jYS8d27JuY6lsR7e1CIeAzGfxg3_lvSbXanX1jL7x68Y.1ASeBsvhY0zE9Oa9mswprDfRTx1P7wzjlJYMstkQ_GQWQJU5HTWbL6_XW6ZcmBfWc9QDzjW7UnyrTt5Pb1t7fo2ntUuNgfCZsBURoNDuJeDp7PsjdBhricFiGFCWWOgNcM.oOdq4_oYwEfbjSOYPo0Cwcgf5lP__PbDBGg.qpHpG9_v5513yfwDl7WDa8tQSsQ6c4RzFrfEKa7eftJrwoKfTsDXwFvdThuGBglh2dApBn4OpA',mdrd: 'L9ZaIjOXFTprw4wKpWhfthhAXZZQhax42Jn8T9DUnxA-1793700089-1.2.1.1-NxcbUMDGHK5hHj2bs_tdvg_c746CvAOF9R_QJeMrl0n4N32EWTqSY1Nin8shHgHrHREhxPeSWM_if08aL3684bmhFuy4L_0MJ.YeBYrC7lSoAHCYgNgQJrRIh_JkkIcWjS1Dz_OPgU0MrxtfB1_6c78yeE1LrP4osn_QnCE7VOcp2lRMKh4OAiW9ueneHhUMG6JnkuL7QNC6oCiWCgaMqlVehqxeusPZlnf9YGX9gGndJPw0EMEoWiiICxu9hTbkckp1I0B_W_EmI5457K5z9VKLF0GDMHG_hCRgMesvrgarvZRRAGvOW8YLg1eOwOkbhlAz.aVgEbN.EIkLsx21khKI.Z9FqYgWCf2PYbj3C9JsBbXSssDy9wCxa8f1ABCtkw42rlvWMkk3yhqoJvTRGyoPOy_tSddq.lQiz3jdG8U2JfPe0TU14g7KWSXtN2lOMZX4FuqGQ50YUEY467GfWeGp1A_XnRbvA0ThZjBxXSXaHTt.stvcayaFMQKIJM0xQQ9oh7BuJV5HDLAaO_HplQ4092ImrX9WZcbRl3MtcRwo5YJ8RJLIKHJw_AcM6ja6yc.QOXEbC3s3cTRkNbL2Rjbp7cPAy64v6xUkwwyfZzRsL0QvQr2T2MzcXFXuLtRbuviw6rgBamkrjdJ6baQXKpHQ8u1tmWAuVw0ntozExj1_GEFxFI20hJ5MJ9PmLZ7AEoNgZeBX7esLbRnBoWJyAbahH.yrpE4PHEgbCL15hkMZHseJ1QyKECgC... (truncated 2376 bytes)")
2026-11-03T10:01:29.543933Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when AuthRequired(AuthRequiredError { www_authenticate_header: "Bearer resource_metadata=\"https://codex-app.tldraw.xyz/.well-known/oauth-protected-resource/mcp\", scope=\"openid profile email offline_access\"" })
2026-11-03T10:01:29.865824Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when AuthRequired(AuthRequiredError { www_authenticate_header: "Bearer resource_metadata=\"https://mcp.consensus.app/.well-known/oauth-protected-resource\", scope=\"search\"" })
2026-11-03T10:01:31.961330Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=OAuth tokens for server valency cannot be refreshed; authorization required
codex
Önceki NO-GO maddelerini düzeltilmiş kodla tek tek karşılaştırıp kanal sırasının sonuca etkisini inceleyeceğim. Dosya değiştirmeyeceğim.

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Location; rg -n \"k_asym|w1_design|AI driven Science\" C:\\Users\\can02\\.codex\\memories\\MEMORY.md" in C:\Users\can02\Projects\AI driven Science
 succeeded in 384ms:

77:# Task Group: AI driven Science alloy-energy and elasticity claim audit
79:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=read `.orchestra/LESSONS.md`, inspect the live ledger/data/scripts, keep `data/sealed/` unread unless the current workflow explicitly authorizes the arena, and treat all historical numerical claims as checkout-specific.
85:- rollout_summaries/2026-10-31T21-44-08-GISz-emix_random_vec_filling_candidate_and_sro_diagnostics.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8677-7d23-8736-9feecdd1a527.jsonl, updated_at=2026-10-31T11:15:16+00:00, thread_id=01a193eb-8677-7d23-8736-9feecdd1a527, strongest candidate not sealed-tested)
86:- rollout_summaries/2026-10-31T21-44-08-Qzmv-k_volume_transfer_anharmonicity_and_triplet_candidates.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-865c-74c3-b444-bb194b9c0aaf.jsonl, updated_at=2026-10-31T11:15:22+00:00, thread_id=01a193eb-865c-74c3-b444-bb194b9c0aaf, physical interpretation remains unresolved)
87:- rollout_summaries/2026-10-31T09-44-10-dWvd-emix_random_target_artifact_and_candidate_analysis.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\31\rollout-2026-10-31T12-44-10-01a19158-6021-7482-9551-9958d2b1cbff.jsonl, updated_at=2026-10-31T07:44:28+00:00, thread_id=01a19158-6021-7482-9551-9958d2b1cbff, establishes generator bookkeeping error)
97:- rollout_summaries/2026-10-31T21-44-08-N62j-l3_ci_gate_confidence_interval_defect.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8452-7b32-8fa5-dc42e5b07c5f.jsonl, updated_at=2026-10-31T20:51:16+00:00, thread_id=01a193eb-8452-7b32-8fa5-dc42e5b07c5f, latent L3 CI-gate defect)
98:- rollout_summaries/2026-10-31T21-44-08-ZwwK-alloy_regularity_audit_and_muggianu_baseline.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8488-7e21-ac6a-1e70f3f52ec6.jsonl, updated_at=2026-10-31T20:49:29+00:00, thread_id=01a193eb-8488-7e21-ac6a-1e70f3f52ec6, energy baseline demotion; K' survives)
99:- rollout_summaries/2026-10-31T21-44-08-KHDr-audit_shared_seed_leakage_pbe_shear_and_fixed_volume_excess.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8481-7b31-b53b-774b6fa2efa9.jsonl, updated_at=2026-10-31T20:15:15+00:00, thread_id=01a193eb-8481-7b31-b53b-774b6fa2efa9, shared-seed and validation-gate audit)
100:- rollout_summaries/2026-10-31T21-44-07-Uafy-audit_backfill_emix_structure_mismatch.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-83d0-7c91-a6e0-3820ae4da47c.jsonl, updated_at=2026-10-31T21:13:54+00:00, thread_id=01a193eb-83d0-7c91-a6e0-3820ae4da47c, structural reconstruction mismatch)
101:- rollout_summaries/2026-10-31T21-44-08-tMXk-audit_holdout_accounting_pbe_kmesh_and_l2_parent_errors.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8694-7b63-8ed9-478e5ea983e6.jsonl, updated_at=2026-10-31T11:13:12+00:00, thread_id=01a193eb-8694-7b63-8ed9-478e5ea983e6, three substantive issues)
102:- rollout_summaries/2026-10-31T21-44-08-bz70-audit_stale_derived_columns_composition_correction_zener_ani.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8606-7342-88b7-c496909afa26.jsonl, updated_at=2026-10-31T11:34:50+00:00, thread_id=01a193eb-8606-7342-88b7-c496909afa26, corrected-data audit)
103:- rollout_summaries/2026-10-31T21-44-08-3Ad3-silver_anomalies_mechanism_and_cutoff_error.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8654-7ab2-83f8-79124f513e41.jsonl, updated_at=2026-10-31T11:18:57+00:00, thread_id=01a193eb-8654-7ab2-83f8-79124f513e41, Ag mechanism partly unverified)
104:- rollout_summaries/2026-10-31T21-44-08-0sbZ-audit_ag_anomaly_claims_cutoff_kgrid_mechanism.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-85ea-7283-8340-585074438f97.jsonl, updated_at=2026-10-31T11:36:25+00:00, thread_id=01a193eb-85ea-7283-8340-585074438f97, controls corrected but reruns pending)
105:- rollout_summaries/2026-10-31T21-44-07-ik6S-cobalt_anomaly_mace_pbe_discriminator.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-835c-7861-9fb8-803628c6364a.jsonl, updated_at=2026-10-31T21:43:57+00:00, thread_id=01a193eb-835c-7861-9fb8-803628c6364a, diagnostic incomplete)
115:- rollout_summaries/2026-11-01T21-57-13-hXmh-audit_cobalt_anomaly_spin_mace_pbe_tests.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfb-72e3-85ce-9cf49c2550d9.jsonl, updated_at=2026-10-31T22:53:56+00:00, thread_id=01a1991d-dbfb-72e3-85ce-9cf49c2550d9, spin-control bug verified; experiments redesigned)
116:- rollout_summaries/2026-10-31T21-44-07-VJVR-validate_k44_shear_transfer_hypotheses.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-8431-7393-ae70-82453cb5df2f.jsonl, updated_at=2026-10-31T20:57:09+00:00, thread_id=01a193eb-8431-7393-ae70-82453cb5df2f, direction/seed averaging retained; composition asymmetry dropped)
126:- rollout_summaries/2026-11-01T21-57-13-BTwh-audit_astra_shared_shear_floor_claim.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfd-7a80-9f9b-7c31461ddc75.jsonl, updated_at=2026-10-31T22:53:45+00:00, thread_id=01a1991d-dbfd-7a80-9f9b-7c31461ddc75, reproduced exploratory fit; L0/UNCLEAR)
127:- rollout_summaries/2026-10-31T21-44-08-P24c-k44_transfer_shared_floor_anisotropy_diagnosis.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-84ac-7db1-98c3-4db467c575c4.jsonl, updated_at=2026-10-31T20:03:50+00:00, thread_id=01a193eb-84ac-7db1-98c3-4db467c575c4, shared-floor/anisotropy diagnosis)
159:# Task Group: AI driven Science stacking-fault volume-transfer test design
161:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=reuse the staged test design, but regenerate targets with current harness/model state and treat all numerical pilot values as model- and checkout-specific.
167:- rollout_summaries/2026-10-31T21-44-07-8WsC-mace_stacking_fault_volume_transfer_test.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-8361-7c41-9ab6-dcfb78c9c626.jsonl, updated_at=2026-10-31T21:43:49+00:00, thread_id=01a193eb-8361-7c41-9ab6-dcfb78c9c626, preregistered hypothesis; ternary test incomplete)
168:- rollout_summaries/2026-11-01T21-57-13-HRq6-audit_astra_1_sfe_volume_transfer.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfc-7ac3-b740-c2e60cf412ae.jsonl, updated_at=2026-10-31T22:51:53+00:00, thread_id=01a1991d-dbfc-7ac3-b740-c2e60cf412ae, KEEP/UNCLEAR design audit)
575:# Task Group: AI driven Science HEA mechanical-discovery harness and bcc L3 validation
577:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=checkout-specific: inspect the current harness, environment, ledger, logs, and benchmark state before rerunning or claiming L3 validation.
583:- rollout_summaries/2026-10-29T17-19-34-Vft1-hea_mechanical_harness_qe_bcc_l3_validation.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\29\rollout-2026-10-29T20-19-34-01a188ac-952b-78c0-9f69-56055f0d602b.jsonl, updated_at=2026-10-28T09:38:53+00:00, thread_id=01a188ac-952b-78c0-9f69-56055f0d602b, fcc harness calibrated; bcc benchmark incomplete)
1345:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=use for project direction and first-vertical-slice planning only; confirm scope, active environment, provider choice, and real-data access before implementation or scientific claims.
1351:- rollout_summaries/2026-10-26T03-00-46-pz1h-metalurji_ai_co_scientist_anomali_avciligi_ksenometalurji.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\26\rollout-2026-10-26T06-00-46-01a17627-4307-7952-bd84-33be35351bd3.jsonl, updated_at=2026-10-25T16:45:57+00:00, thread_id=01a17627-4307-7952-bd84-33be35351bd3, architecture/planning only)
Path                                     
----                                     
C:\Users\can02\Projects\AI driven Science



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Content C:\\Users\\can02\\.codex\\skills\\scientific-result-audit\\SKILL.md; "'$m=Get-Content C:'"\\Users\\can02\\.codex\\memories\\MEMORY.md; "'$m[108..136]' in C:\Users\can02\Projects\AI driven Science
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'git status --short; if (Test-Path CODEX_START.md) { Get-Content CODEX_START.md }; Get-Content .orchestra/audits/w1_design_astra.md; Get-Content .orchestra/LESSONS.md; Get-Content STATUS.md' in C:\Users\can02\Projects\AI driven Science
 succeeded in 416ms:
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
- 207 unseen alloys, h3_fresh_rows_fixed, hm_fresh_rows_fixed, fixed k-mesh, ecut_elements, l2_search.py, Zener anisotropy, shared-permutation leak, backfill_emix.py, L3 95% CI, own-volume Muggianu

## Task 3: Audit cobalt K44 controls, spin state, and matched MACE/PBE design, success/partial

### rollout_summary_files

- rollout_summaries/2026-11-01T21-57-13-hXmh-audit_cobalt_anomaly_spin_mace_pbe_tests.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfb-72e3-85ce-9cf49c2550d9.jsonl, updated_at=2026-10-31T22:53:56+00:00, thread_id=01a1991d-dbfb-72e3-85ce-9cf49c2550d9, spin-control bug verified; experiments redesigned)
- rollout_summaries/2026-10-31T21-44-07-VJVR-validate_k44_shear_transfer_hypotheses.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-8431-7393-ae70-82453cb5df2f.jsonl, updated_at=2026-10-31T20:57:09+00:00, thread_id=01a193eb-8431-7393-ae70-82453cb5df2f, direction/seed averaging retained; composition asymmetry dropped)

### keywords

- cobalt anomaly, Co K44, nspin, magnetize(), ASE espresso.py, MACE, PBE, disjoint seeds, same-site substitution, K44/Kp, seed permutation

## Task 4: Diagnose shared K44/K' residual floor and audit its energy-residual predictor, success/unclear

### rollout_summary_files

- rollout_summaries/2026-11-01T21-57-13-BTwh-audit_astra_shared_shear_floor_claim.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfd-7a80-9f9b-7c31461ddc75.jsonl, updated_at=2026-10-31T22:53:45+00:00, thread_id=01a1991d-dbfd-7a80-9f9b-7c31461ddc75, reproduced exploratory fit; L0/UNCLEAR)
- rollout_summaries/2026-10-31T21-44-08-P24c-k44_transfer_shared_floor_anisotropy_diagnosis.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-84ac-7db1-98c3-4db467c575c4.jsonl, updated_at=2026-10-31T20:03:50+00:00, thread_id=01a193eb-84ac-7db1-98c3-4db467c575c4, shared-floor/anisotropy diagnosis)

### keywords

- shared shear floor, K44, K', `R_E`, `q = 160.21766208 R_E/V0`, intercept-only baseline, disjoint seeds, Co-free, anisotropy, `data/k_floor_cells.csv`

## User preferences

- when auditing, the user required errors over new formulas and `file:line`, evidence, and numerical size -> lead with concrete reproducible defects quantified in meV/GPa; keep the investigation read-only and use concise structured proposals when requested. [Task 2]
- when proposing alloy rules, the user said �?oDo not edit files. Put your candidates in your answer�?? and prohibited `data/sealed/` access -> use only the `ctx` contract, at most the requested fitted coefficient count, a physical mechanism, numerical prediction, test, falsifier, and cost; do not present cross-source or synthetic estimates as sealed validation. [Task 1]


 succeeded in 748ms:
fatal: not a git repository (or any of the parent directories): .git
OpenAI Codex v0.160.0
--------
workdir: C:\Users\can02\Projects\AI driven Science
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a1a0d4-a137-7682-b1d6-70f06143ccd2
--------
user
G��rev: scripts/k_asym_w1.py test tasar��m��n��, hesap ba�Ylamadan ��nce ele�Ytir. Dosya de�Yi�Ytirme.

Ba�Ylam: Wu 2021 (NCSU tezi, Eq 5.1) ve Marker 2017, ikili verilerden ��ok bile�Yenli excess C' ve C44'Ǭ bile�Yim asimetrisiyle (Redlich-Kister, Muggianu) modelliyor ama her ikiliyi kendi denge hacminde tutuyor. Bizim kural (paper/draft_v5.md) yaln��z 50:50 ikilileri ala�Y��m��n Vegard hacminde okuyor. W1 ikisini ayn�� veride kar�Y��la�Yt��r��yor ve birle�Ytiriyor (H1, H2; beti�Yin docstring'i). Okuman gerekenler: scripts/k_asym_w1.py, scripts/k_shear_transfer.py, harness/context.py, harness/ledger.py, harness/power.py, .orchestra/LESSONS.md.

Sorular:
1. OV-asym kolu Wu/Marker yakla�Y��m��n��n adil bir temsilcisi mi? �-zellikle: Ǭ�� noktadan tam L0-L2, hacim olarak ikilinin Vegard hacmi (relakse denge hacmi de�Yil), clamped hedef. Adaletsizlik varsa nas��l dǬzeltilmeli?
2. H1 ve H2 gǬ�� hesab�� (gǬrǬltǬ = kural��n hm hedeflerindeki art��Y��) ger��ek��i mi, s��z��nt�� veya ��l��Ǭt kaymas�� var m��? Hedef SQS seed 100, ikililer 0-2.
3. Hedef bile�Yim ��ekimi, Co'nun 40/80 sat��rda olmas��, alpha 0.0025: sorun var m��?
4. k_shear_transfer'�� import etmek yan etki yarat��yor mu?
5. Kodda hata (RK ����zǬmǬ, Muggianu i�Yareti x_a - x_b, spline'��n ln V ekseni, grid kapsam��) var m��?

Sonunda: VERDICT GO / GO WITH FIXES / NO-GO ve gerekli dǬzeltmelerin listesi.

warning: Codex is ignoring 1 unrecognized configuration setting. Check for typos or deprecated settings.
  user (C:\Users\can02\.codex\config.toml): `computer_use.windows.always_allowed_app_ids` is ignored.
warning: Codex is ignoring 1 unrecognized configuration setting. Check for typos or deprecated settings.
  user (C:\Users\can02\.codex\config.toml): `computer_use.windows.always_allowed_app_ids` is ignored.
warning: Under-development features enabled: local_thread_store_compression. Under-development features are incomplete and may behave unpredictably. To suppress this warning, set `suppress_unstable_features_warning = true` in C:\Users\can02\.codex\config.toml.
warning: clamping SessionEnd hook timeout to 3s in C:\Users\can02\.codex\plugins\cache\openai-codex\codex\1.0.6\hooks\hooks.json
2026-11-03T09:54:14.983649Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when UnexpectedServerResponse("HTTP 403: <html>\n  <head>\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n    <style global>body{font-family:Arial,Helvetica,sans-serif}.container{align-items:center;display:flex;flex-direction:column;gap:2rem;height:100%;justify-content:center;width:100%}@keyframes enlarge-appear{0%{opacity:0;transform:scale(75%) rotate(-90deg)}to{opacity:1;transform:scale(100%) rotate(0deg)}}.logo{color:#8e8ea0}.scale-appear{animation:enlarge-appear .4s ease-out}@media (min-width:768px){.scale-appear{height:48px;width:48px}}.data:empty{display:none}.data{border-radius:5px;color:#8e8ea0;text-align:center}@media (prefers-color-scheme:dark){body{background-color:#343541}.logo{color:#acacbe}}</style>\n  <meta http-equiv=\"refresh\" content=\"360\"></head>\n  <body>\n    <div class=\"container\">\n      <div class=\"logo\">\n        <svg\n          width=\"41\"\n          height=\"41\"\n          viewBox=\"0 0 41 41\"\n          fill=\"none\"\n          xmlns=\"http://www.w3.org/2000/svg\"\n          strokeWidth=\"2\"\n          class=\"scale-appear\"\n        >\n          <path\n            d=\"M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z\"\n            fill=\"currentColor\"\n          />\n        </svg>\n      </div>\n      <div class=\"data\"><div class=\"main-wrapper\" role=\"main\"><div class=\"main-content\"><noscript><div class=\"h2\"><span id=\"challenge-error-text\">Enable JavaScript and cookies to continue</span></div></noscript></div></div><script>(function(){window._cf_chl_opt = {cFPWv: 'g',cH: 'iSfXoKmqpB6b.SjEETsJ1Y1HpOG0knx3h3U8FUaAM9k-1793699655-1.2.1.1-O32h9V1IZwvTR.nCIBCR9XEpTGWE7AiqNNO4T1xTRum5uPTilmhqYENt43egNfIn',cITimeS: '1793699655',cRay: 'a54a7f1d98d5d5f8',cTplC:1,cTplO:0,cTplV:5,cType: 'managed',cUPMDTk:\"/backend-api/product-account-links/mcp?__cf_chl_tk=16bfKtFW.2iBGoGJgMoISjUXseiRBVrhaMn3Lb4Zncg-1793699655-1.0.1.1-5vLyG8JSWCdq9TGMkr.SaMIM8FobAYIgP6RBZGbDKdM\",cvId: '3',cZone: 'chatgpt.com',fa:\"/backend-api/product-account-links/mcp?__cf_chl_f_tk=16bfKtFW.2iBGoGJgMoISjUXseiRBVrhaMn3Lb4Zncg-1793699655-1.0.1.1-5vLyG8JSWCdq9TGMkr.SaMIM8FobAYIgP6RBZGbDKdM\",md: 'vW3xdy8AIXxScodd4SAVzThUYRyhNgaqiWqu3w60x3k-1793699655-1.2.1.1-TsReX47Ma7rHI7lcCebH6OHdzKS6n7MstBtJRS75veeHBLwBEFJjnbwS5miZaSQNWo_RXZWPsjvMiLyRjtE8hUkC.w.3QDdiWb8xJr0QYhxtUCgNF8qPWFWCpMfBpK6flVT1CKq3cPwwdrbHwpnnb7NH1OctOTQWNrf2x4tZ4_8GVa9YCoQo98JUR6QAKobBSIFQhXz5tv8FLAtLE_Wu3OFIm5UakvMrsBaNJ9oSIfKFqyvreoNcrNUF.SX73vFOar3k9VP16lyrNPjHUPCrvpPVh8073m0GCdUw2d0yjMaaCKg9opTEALh4CXnWqbTvMLJXvLmyiLXkGECLvffZUkUiC4GlYXnVgF9z2QeJBbILoXGATQP4ED0xInSS.eQ9xM2.OXD.I0hAL.jbLviCG7bj874FB7h0BRqHm.rLL8jsG77G5UpaYZufJhsKlcRE1gOdpt86ZqYfNfLCtb4kQWIkgOQeDEU3H1HrMCD9s7gwM571Rx47nAUaYyClJgDlNSF1g91u9TUW_42_0ODa8qLrVw.oxwpMbXZwwPn90U82DS6i_Wi.C4OPEpNav6ih.pSbXz1JJCQoSsoLw7ePVzdxmjVFhJex1ec.TBlUjjeAS3QidR9v2qRSAEGOsDP7.K.tGTGkhjdO6k20AxMvwk7z_CvoDXcEnuRrH0SmdA1ShwV6AALkpU4cIkrtqvhSX2O0QTA0spg_WUg13ZGxDIhyEBXyknm4y3r7qN7Gwkh3uzRHZgUOm7qhpgH1017UhyKYjX0.YB_X44P9IlP_B22R38df.6yyaZZXKA4r8cKHeWKRxd071E0vIhZeV.uIe4JDY6ptoYLXlLa48k2yF9.IAX5_XDHcl38nmkO9hAm8upbT74bK0DyrdUnxIFojuW3ksVbw24.Kx7rqsL4RlqYAiHvECfYG5YK.oSXI88rGxAtE_vAjIJZiYm.N5WOdiuRK2NMiguqBwH_bPiMOlx2ZVgSgTvOegWRkWVoBNJB_6rKiZ77M7yxcIsakTfpiwZJlAFeWeNypLrAOsRqD9vppEPEcpwGMVFt6vaqGkNMDYCNuAX.rx3HCfiIH2fvd4eBVCcP9_7oBMY2xla9W3fKAH8mMl5s9holjVec82_wwTFtWZp9zYa7BvTgK7ndf7dem5pi2bQTdi.U9RnyXZg',mdrd: 'kCmmX2O0CvKNxIr._XO8Shqt9kYdLQk7w7Epe0Nzho4-1793699655-1.2.1.1-Wmq0qOexpiDZgC.ws0c3HCQui_Vhg_GJjOMcgZKueOD5Fly37jbPTvO8JnVvjdD6CDRHkJ5MvbC_zgxEqZYt7.ENc_BZKLrKl_HhzhQZRu9uUz0fJQHRBH9_oiVavoyhwKCvhmqd6JOOC45dI74CF.Ix5t8PZapQFy6wG3JwIcbMOUAqunu4z3PQwnhnQmg9BOPlOfregccetsMj8RuBdlHFWSKpsNQ1qUSuaCVr0rq.fUm6em6WCkqnZBzzIdGjKziUcggaQxH0r2keTQ5LoIajv.l6wiI5il7Kp0kk7W4ROlBEehZmYPCn00TsyfbLPu95d7A_LC9jLHDL1b1AjWpHLelxab33AA0z_ZGTb1r2FtwUjlvod1ggEw3nIB4Qcwe8MbHI_Bn0aCJauDY7bKg65PLN8hdMCx9jXFSvkSjACRA6AINw2f3at5GqS1q55c7duaMs.41p6akZCQ67qWoY.1zMUOXeeVL5bb5DpnVcuRBDq55TETrlMe6DsdtVx_raQvg7jhrm0yMmkuCEiEgDHedqx.xFZGhkmQ1peoC84L8FQB0_rscLHoBVDBJK3O8WhHyA7mu9Y_xyO.jnPYW3AqeZMbhhEfR7qbAcAbJoelr7sohaGPIduh2t9WIP8PQP6PWkLU54H2d44mTqgrhBgJVD.Au79VMHlmANHf2psPwqvCznA77GfLHkFdchwzF77odr3A44__SgiI9EAGVo4ker8Sw8uL55JHPpkusgdpRaBufWhq9x... (truncated 2376 bytes)")
2026-11-03T09:54:15.022303Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when AuthRequired(AuthRequiredError { www_authenticate_header: "Bearer resource_metadata=\"https://codex-app.tldraw.xyz/.well-known/oauth-protected-resource/mcp\", scope=\"openid profile email offline_access\"" })
2026-11-03T09:54:15.291433Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when AuthRequired(AuthRequiredError { www_authenticate_header: "Bearer resource_metadata=\"https://mcp.consensus.app/.well-known/oauth-protected-resource\", scope=\"search\"" })
2026-11-03T09:54:17.740382Z ERROR codex_rmcp_client::oauth::refresh_transaction: error=OAuth tokens for server valency cannot be refreshed; authorization required
codex
Belirtilen dosyalar�� salt okunur inceleyip testin adilli�Yini, gǬ�� hesab��n�� ve olas�� kod hatalar��n�� de�Yerlendirece�Yim; Wu/Marker kar�Y��la�Yt��rmas��n�� da kaynaklardan kontrol edece�Yim.

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "rg -n \"AI driven Science|k_asym|Wu|Marker|shear_transfer\" C:\\Users\\can02\\.codex\\memories\\MEMORY.md" in C:\Users\can02\Projects\AI driven Science
 succeeded in 711ms:
77:# Task Group: AI driven Science alloy-energy and elasticity claim audit
79:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=read `.orchestra/LESSONS.md`, inspect the live ledger/data/scripts, keep `data/sealed/` unread unless the current workflow explicitly authorizes the arena, and treat all historical numerical claims as checkout-specific.
85:- rollout_summaries/2026-10-31T21-44-08-GISz-emix_random_vec_filling_candidate_and_sro_diagnostics.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8677-7d23-8736-9feecdd1a527.jsonl, updated_at=2026-10-31T11:15:16+00:00, thread_id=01a193eb-8677-7d23-8736-9feecdd1a527, strongest candidate not sealed-tested)
86:- rollout_summaries/2026-10-31T21-44-08-Qzmv-k_volume_transfer_anharmonicity_and_triplet_candidates.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-865c-74c3-b444-bb194b9c0aaf.jsonl, updated_at=2026-10-31T11:15:22+00:00, thread_id=01a193eb-865c-74c3-b444-bb194b9c0aaf, physical interpretation remains unresolved)
87:- rollout_summaries/2026-10-31T09-44-10-dWvd-emix_random_target_artifact_and_candidate_analysis.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\31\rollout-2026-10-31T12-44-10-01a19158-6021-7482-9551-9958d2b1cbff.jsonl, updated_at=2026-10-31T07:44:28+00:00, thread_id=01a19158-6021-7482-9551-9958d2b1cbff, establishes generator bookkeeping error)
97:- rollout_summaries/2026-10-31T21-44-08-N62j-l3_ci_gate_confidence_interval_defect.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8452-7b32-8fa5-dc42e5b07c5f.jsonl, updated_at=2026-10-31T20:51:16+00:00, thread_id=01a193eb-8452-7b32-8fa5-dc42e5b07c5f, latent L3 CI-gate defect)
98:- rollout_summaries/2026-10-31T21-44-08-ZwwK-alloy_regularity_audit_and_muggianu_baseline.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8488-7e21-ac6a-1e70f3f52ec6.jsonl, updated_at=2026-10-31T20:49:29+00:00, thread_id=01a193eb-8488-7e21-ac6a-1e70f3f52ec6, energy baseline demotion; K' survives)
99:- rollout_summaries/2026-10-31T21-44-08-KHDr-audit_shared_seed_leakage_pbe_shear_and_fixed_volume_excess.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8481-7b31-b53b-774b6fa2efa9.jsonl, updated_at=2026-10-31T20:15:15+00:00, thread_id=01a193eb-8481-7b31-b53b-774b6fa2efa9, shared-seed and validation-gate audit)
100:- rollout_summaries/2026-10-31T21-44-07-Uafy-audit_backfill_emix_structure_mismatch.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-83d0-7c91-a6e0-3820ae4da47c.jsonl, updated_at=2026-10-31T21:13:54+00:00, thread_id=01a193eb-83d0-7c91-a6e0-3820ae4da47c, structural reconstruction mismatch)
101:- rollout_summaries/2026-10-31T21-44-08-tMXk-audit_holdout_accounting_pbe_kmesh_and_l2_parent_errors.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8694-7b63-8ed9-478e5ea983e6.jsonl, updated_at=2026-10-31T11:13:12+00:00, thread_id=01a193eb-8694-7b63-8ed9-478e5ea983e6, three substantive issues)
102:- rollout_summaries/2026-10-31T21-44-08-bz70-audit_stale_derived_columns_composition_correction_zener_ani.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8606-7342-88b7-c496909afa26.jsonl, updated_at=2026-10-31T11:34:50+00:00, thread_id=01a193eb-8606-7342-88b7-c496909afa26, corrected-data audit)
103:- rollout_summaries/2026-10-31T21-44-08-3Ad3-silver_anomalies_mechanism_and_cutoff_error.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-8654-7ab2-83f8-79124f513e41.jsonl, updated_at=2026-10-31T11:18:57+00:00, thread_id=01a193eb-8654-7ab2-83f8-79124f513e41, Ag mechanism partly unverified)
104:- rollout_summaries/2026-10-31T21-44-08-0sbZ-audit_ag_anomaly_claims_cutoff_kgrid_mechanism.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-85ea-7283-8340-585074438f97.jsonl, updated_at=2026-10-31T11:36:25+00:00, thread_id=01a193eb-85ea-7283-8340-585074438f97, controls corrected but reruns pending)
105:- rollout_summaries/2026-10-31T21-44-07-ik6S-cobalt_anomaly_mace_pbe_discriminator.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-835c-7861-9fb8-803628c6364a.jsonl, updated_at=2026-10-31T21:43:57+00:00, thread_id=01a193eb-835c-7861-9fb8-803628c6364a, diagnostic incomplete)
115:- rollout_summaries/2026-11-01T21-57-13-hXmh-audit_cobalt_anomaly_spin_mace_pbe_tests.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfb-72e3-85ce-9cf49c2550d9.jsonl, updated_at=2026-10-31T22:53:56+00:00, thread_id=01a1991d-dbfb-72e3-85ce-9cf49c2550d9, spin-control bug verified; experiments redesigned)
116:- rollout_summaries/2026-10-31T21-44-07-VJVR-validate_k44_shear_transfer_hypotheses.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-8431-7393-ae70-82453cb5df2f.jsonl, updated_at=2026-10-31T20:57:09+00:00, thread_id=01a193eb-8431-7393-ae70-82453cb5df2f, direction/seed averaging retained; composition asymmetry dropped)
126:- rollout_summaries/2026-11-01T21-57-13-BTwh-audit_astra_shared_shear_floor_claim.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfd-7a80-9f9b-7c31461ddc75.jsonl, updated_at=2026-10-31T22:53:45+00:00, thread_id=01a1991d-dbfd-7a80-9f9b-7c31461ddc75, reproduced exploratory fit; L0/UNCLEAR)
127:- rollout_summaries/2026-10-31T21-44-08-P24c-k44_transfer_shared_floor_anisotropy_diagnosis.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-08-01a193eb-84ac-7db1-98c3-4db467c575c4.jsonl, updated_at=2026-10-31T20:03:50+00:00, thread_id=01a193eb-84ac-7db1-98c3-4db467c575c4, shared-floor/anisotropy diagnosis)
156:- Do not import `scripts/k_shear_transfer.py` in a screening script: its top-level code computes and writes data. For the cobalt discriminator, use same-site Co��"Ni and Co��"Rh substitutions in seed>=100 cells, calibrate thresholds to the roughly 0.9 GPa Co/Co-free floor gap, and treat nonspin as an intervention rather than a paramagnetic phase. [Task 3]
159:# Task Group: AI driven Science stacking-fault volume-transfer test design
161:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=reuse the staged test design, but regenerate targets with current harness/model state and treat all numerical pilot values as model- and checkout-specific.
167:- rollout_summaries/2026-10-31T21-44-07-8WsC-mace_stacking_fault_volume_transfer_test.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-8361-7c41-9ab6-dcfb78c9c626.jsonl, updated_at=2026-10-31T21:43:49+00:00, thread_id=01a193eb-8361-7c41-9ab6-dcfb78c9c626, preregistered hypothesis; ternary test incomplete)
168:- rollout_summaries/2026-11-01T21-57-13-HRq6-audit_astra_1_sfe_volume_transfer.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfc-7ac3-b740-c2e60cf412ae.jsonl, updated_at=2026-10-31T22:51:53+00:00, thread_id=01a1991d-dbfc-7ac3-b740-c2e60cf412ae, KEEP/UNCLEAR design audit)
575:# Task Group: AI driven Science HEA mechanical-discovery harness and bcc L3 validation
577:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=checkout-specific: inspect the current harness, environment, ledger, logs, and benchmark state before rerunning or claiming L3 validation.
583:- rollout_summaries/2026-10-29T17-19-34-Vft1-hea_mechanical_harness_qe_bcc_l3_validation.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\29\rollout-2026-10-29T20-19-34-01a188ac-952b-78c0-9f69-56055f0d602b.jsonl, updated_at=2026-10-28T09:38:53+00:00, thread_id=01a188ac-952b-78c0-9f69-56055f0d602b, fcc harness calibrated; bcc benchmark incomplete)
1345:applies_to: cwd=C:\Users\can02\Projects\AI driven Science; reuse_rule=use for project direction and first-vertical-slice planning only; confirm scope, active environment, provider choice, and real-data access before implementation or scientific claims.
1351:- rollout_summaries/2026-10-26T03-00-46-pz1h-metalurji_ai_co_scientist_anomali_avciligi_ksenometalurji.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\10\26\rollout-2026-10-26T06-00-46-01a17627-4307-7952-bd84-33be35351bd3.jsonl, updated_at=2026-10-25T16:45:57+00:00, thread_id=01a17627-4307-7952-bd84-33be35351bd3, architecture/planning only)

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Item CODEX_START.md,STATUS.md,scripts/k_asym_w1.py,scripts/k_shear_transfer.py,harness/context.py,harness/ledger.py,harness/power.py,.orchestra/LESSONS.md,paper/draft_v5.md -ErrorAction SilentlyContinue | Select-Object FullName,Length; git status --short' in C:\Users\can02\Projects\AI driven Science
 exited 1 in 520ms:

fatal: not a git repository (or any of the parent directories): .git
FullName                                                              Length
--------                                                              ------
C:\Users\can02\Projects\AI driven Science\STATUS.md                     8650
C:\Users\can02\Projects\AI driven Science\scripts\k_asym_w1.py         10433
C:\Users\can02\Projects\AI driven Science\scripts\k_shear_transfer.py   9651
C:\Users\can02\Projects\AI driven Science\harness\context.py            2193
C:\Users\can02\Projects\AI driven Science\harness\ledger.py             3243
C:\Users\can02\Projects\AI driven Science\harness\power.py              1507
C:\Users\can02\Projects\AI driven Science\.orchestra\LESSONS.md         9323
C:\Users\can02\Projects\AI driven Science\paper\draft_v5.md            24237



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$p='"'scripts/k_asym_w1.py'; "'$i=0; Get-Content $p | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ }; $p='"'scripts/k_shear_transfer.py'; "'$i=0; Get-Content $p | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ }' in C:\Users\can02\Projects\AI driven Science
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$files=@('"'harness/context.py','harness/ledger.py','harness/power.py','.orchestra/LESSONS.md','STATUS.md'); foreach("'$p in $files) { Write-Output $p; $i=0; Get-Content $p | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ } }' in C:\Users\can02\Projects\AI driven Science
 succeeded in 418ms:
   1: """W1: where the binaries are read versus how their composition dependence is modelled (Wu 2021, Marker 2017 gap).
   2: 
   3: python scripts/k_asym_w1.py
   4: Prior binary-to-multicomponent elastic models (Marker 2017 CALPHAD; Wu 2021 Eq. 5.1, EMTO pair polynomials for excess
   5: C' and C44) keep each binary at its own equilibrium volume but model the composition dependence (Redlich-Kister,
   6: Muggianu). Our rule does the opposite: equiatomic binaries only, read at the alloy's Vegard volume. Neither literature
   7: nor our paper compared the two on the same data, or combined them. Arms, per channel (K' primary, K44 secondary):
   8:   OV-asym  binaries at x_A = 0.25, 0.5, 0.75, each at its own Vegard volume; exact L0, L1, L2 Redlich-Kister per pair;
   9:            Muggianu sum  K = sum x_a x_b [L0 + L1 (x_a - x_b) + L2 (x_a - x_b)^2]       (Wu/Marker class)
  10:   VV-sym   sum 4 x_a x_b K_ab(0.5; V0)                                                  (our rule, unchanged)
  11:   VV-asym  as OV-asym, but every binary curvature read at the alloy's Vegard volume V0   (the combination)
  12:   OV-sym   sum 4 x_a x_b K_ab(0.5; V_ab)                                                (reported only)
  13: Hypotheses, each registered on its own and only if power >= 0.8 and false pass <= 0.05 (two tests, alpha 0.0025):
  14:   H1  RMSE(VV-sym) <= 0.9 RMSE(OV-asym) on K' and paired sign-flip p < 0.0025
  15:   H2  RMSE(VV-asym) <= 0.9 RMSE(VV-sym) on K' and paired sign-flip p < 0.0025
  16: Order, so that the test is blind: 1. off-equiatomic binaries (seeds 0-2, as the 50:50 set), 2. fresh off-equiatomic
  17: target compositions drawn and predicted, power, registration, 3. targets (SQS seed 100, never computed), 4. test.
  18: Noise for the power check: the rule's residual on the seen hm targets (data/hm_shear_clamped.csv), arena convention.
  19: """
  20: 
  21: import datetime as dt
  22: import os
  23: import sys
  24: from pathlib import Path
  25: 
  26: ROOT = Path(__file__).resolve().parent.parent
  27: os.environ["HARNESS_MODEL"] = "medium-omat-0"
  28: sys.path.insert(0, str(ROOT))
  29: 
  30: import numpy as np  # noqa: E402
  31: import pandas as pd  # noqa: E402
  32: from scipy.interpolate import CubicSpline  # noqa: E402
  33: 
  34: from harness import compute, ledger  # noqa: E402
  35: from harness.context import context  # noqa: E402
  36: from harness.features import parse_comp  # noqa: E402
  37: 
  38: sys.argv = sys.argv[:1]  # k_shear_transfer reads no args; keep its import side-effect free of ours
  39: import k_shear_transfer as kst  # noqa: E402  (binary splines at 50:50, curvatures(), test helpers)
  40: 
  41: ctx = context()
  42: SCRIPT = str(Path(__file__))
  43: BIN = ROOT / "data" / "binary_kgrid_asym.csv"
  44: TGT = ROOT / "data" / "w1_shear_clamped.csv"
  45: COMPS = ROOT / "data" / "w1_compositions.csv"
  46: XS = (0.25, 0.75)
  47: ELS = ["Ag", "Au", "Co", "Cu", "Ir", "Ni", "Pd", "Pt", "Rh"]
  48: N_TGT, ALPHA = 80, 0.0025
  49: CH = ("Kp", "K44")
  50: 
  51: 
  52: def draw_targets():
  53:     """Fresh off-equiatomic compositions, 3-5 components, at least 1/12 each, rounded to the 108-atom cell."""
  54:     if COMPS.exists():
  55:         return [parse_comp(s) for s in pd.read_csv(COMPS).comp]
  56:     rng, out, seen = np.random.default_rng(2611), [], set()
  57:     quota = {3: 27, 4: 27, 5: 26}  # equal shares; a free draw gave 58/17/5 because the 1/12 floor rejects n = 5
  58:     while len(out) < N_TGT:
  59:         n = int(rng.integers(3, 6))
  60:         if sum(len(c) == n for c in out) >= quota[n]:
  61:             continue
  62:         els = sorted(rng.choice(ELS, n, replace=False))
  63:         x = rng.dirichlet([0.7] * n)
  64:         if x.min() < 1 / 12:
  65:             continue
  66:         cnt = np.round(x * 108).astype(int)
  67:         cnt[np.argmax(cnt)] += 108 - cnt.sum()
  68:         c = {e: k / 108 for e, k in zip(els, cnt)}
  69:         key = tuple(sorted(c.items()))
  70:         if key not in seen and max(c.values()) - min(c.values()) > 0.15:  # off-equiatomic by construction
  71:             seen.add(key)
  72:             out.append(c)
  73:     pd.DataFrame({"comp": [";".join(f"{e}:{v:.4f}" for e, v in c.items()) for c in out]}).to_csv(COMPS, index=False)
  74:     return out
  75: 
  76: 
  77: comps = draw_targets()
  78: lnv_need = {}
  79: for c in comps:
  80:     for a, b, _, _ in ctx.pairs(c):
  81:         for xa in XS:
  82:             lnv_need.setdefault((a, b, xa), []).append(np.log(ctx.vegard(c) / ctx.vegard({a: xa, b: 1 - xa})))
  83: 
  84: # 1. off-equiatomic binaries on the ln V grid around each binary's own Vegard volume, only as wide as the targets need
  85: done = set(map(tuple, pd.read_csv(BIN)[["pair", "xA", "seed", "dlnV"]].astype(str).values)) if BIN.exists() else set()
  86: for (a, b, xa), need in sorted(lnv_need.items()):
  87:     lo, hi = min(min(need), 0.0) - 0.1, max(max(need), 0.0) + 0.1
  88:     grid = [d for d in kst.GRID if lo <= d <= hi]
  89:     for seed in (0, 1, 2):
  90:         alloy = compute.solid_solution({a: xa, b: 1 - xa}, "fcc", reps=3, seed=seed)
  91:         x = compute.actual_fractions(alloy)
  92:         for d in grid:
  93:             if (f"{a}-{b}", str(xa), str(seed), str(d)) in done:
  94:                 continue
  95:             v = ctx.vegard({a: xa, b: 1 - xa}) * np.exp(d)
  96:             r = {"pair": f"{a}-{b}", "xA": xa, "xA_actual": x[a], "seed": seed, "dlnV": d, "V": v,
  97:                  **kst.curvatures(alloy, x, v)}
  98:             pd.DataFrame([r]).to_csv(BIN, mode="a", header=not BIN.exists(), index=False)
  99:     print("binary", a, b, xa, flush=True)
 100: 
 101: # splines in absolute ln V for x = 0.25, 0.75 (this file) and 0.5 (binary_kgrid.csv)
 102: g = pd.read_csv(BIN).groupby(["pair", "xA", "dlnV"])[["V", *CH]].mean().reset_index()
 103: SPL = {}
 104: for (pair, xa), s in g.groupby(["pair", "xA"]):
 105:     for ch in CH:
 106:         SPL[(tuple(pair.split("-")), xa, ch)] = CubicSpline(np.log(s.V.values), s[ch].values)
 107: g5 = pd.read_csv(kst.BIN).groupby(["pair", "dlnV"])[["V", *CH]].mean().reset_index()
 108: for pair, s in g5.groupby("pair"):
 109:     for ch in CH:
 110:         SPL[(tuple(pair.split("-")), 0.5, ch)] = CubicSpline(np.log(s.V.values), s[ch].values)
 111: 
 112: 
 113: def rk(k25, k50, k75):
 114:     """Exact L0, L1, L2 from K(x) = x(1-x)[L0 + L1 t + L2 t^2], t = 2x - 1, at x = 0.25, 0.5, 0.75."""
 115:     y = np.array([k25 / (3 / 16), k50 / 0.25, k75 / (3 / 16)])
 116:     T = np.array([[1, -0.5, 0.25], [1, 0, 0], [1, 0.5, 0.25]])
 117:     return np.linalg.solve(T, y)
 118: 
 119: 
 120: def predict(c, ch, arm):
 121:     v0, tot = ctx.vegard(c), 0.0
 122:     for a, b, xa, xb in ctx.pairs(c):
 123:         at = lambda x: np.log(v0) if arm.startswith("VV") else np.log(ctx.vegard({a: x, b: 1 - x}))  # noqa: E731
 124:         if arm.endswith("sym"):
 125:             tot += 4 * xa * xb * float(SPL[((a, b), 0.5, ch)](at(0.5)))
 126:         else:
 127:             L = rk(*(float(SPL[((a, b), x, ch)](at(x))) for x in (0.25, 0.5, 0.75)))
 128:             t = xa - xb
 129:             tot += xa * xb * (L[0] + L[1] * t + L[2] * t * t)
 130:     return tot
 131: 
 132: 
 133: ARMS = ("OV-asym", "VV-sym", "VV-asym", "OV-sym")
 134: P = {ch: {arm: np.array([predict(c, ch, arm) for c in comps]) for arm in ARMS} for ch in CH}
 135: 
 136: # 2. noise, power, registration
 137: hm = pd.read_csv(ROOT / "data" / "hm_shear_clamped.csv")
 138: hmc = [parse_comp(s) for s in hm.comp]
 139: SIG = {ch: float(np.sqrt(np.mean((hm[ch].values - [predict(c, ch, "VV-sym") for c in hmc]) ** 2))) for ch in CH}
 140: HYP = {"H1": ("VV-sym", "OV-asym"), "H2": ("VV-asym", "VV-sym")}
 141: 
 142: 
 143: def test(y, new, old, n_perm=4000, seed=0):
 144:     ok, gain, p = kst.test(y, new, old, n_perm, seed)
 145:     return gain >= 0.10 and p < ALPHA, gain, p
 146: 
 147: 
 148: regs = {}
 149: for h, (new, old) in HYP.items():
 150:     tag = f"W1 {h}:"
 151:     found = [e for e in ledger.entries() if e["claim"].startswith(tag) and "prereg" in e["notes"]]
 152:     if found:
 153:         regs[h] = found[-1]
 154:         continue
 155:     rng = np.random.default_rng(7)
 156:     sim = lambda truth: np.mean([test(P["Kp"][truth] + rng.normal(0, SIG["Kp"], len(comps)),  # noqa: E731
 157:                                       P["Kp"][new], P["Kp"][old], 1000, i)[0] for i in range(200)])
 158:     pw = {"power": round(float(sim(new)), 3), "false_pass": round(float(sim(old)), 3), "n_sims": 200}
 159:     d = P["Kp"][new] - P["Kp"][old]
 160:     print(f"{h}: n {len(comps)}, sigma {SIG['Kp']:.2f}, rms(new - old) {np.sqrt(np.mean(d**2)):.2f} GPa, {pw}",
 161:           flush=True)
 162:     claim = (f"{tag} on {len(comps)} fresh off-equiatomic fcc alloys (3-5 of {''.join(ELS)}), clamped mixing K' "
 163:              f"RMSE({new}) <= 0.9 RMSE({old}) and paired sign-flip p < {ALPHA}; MACE medium-omat-0, targets SQS seed "
 164:              f"100 computed after registration")
 165:     try:
 166:         regs[h] = ledger.register(claim, SCRIPT, pw, notes="literature gap: Wu 2021 / Marker 2017 own-volume RK vs "
 167:                                   "Vegard-volume rule; literature.jsonl line 65")
 168:         print("registered", h, regs[h]["id"], flush=True)
 169:     except ValueError as err:
 170:         ledger.record(f"Design note, {tag} not registered: {err}", "L0", [SCRIPT, str(BIN)],
 171:                       notes=f"design; sigma {SIG}; effect below detectability at n {len(comps)}")
 172:         print(h, "not registered:", err, flush=True)
 173: if not regs:
 174:     sys.exit("no hypothesis had enough power; no target computed")
 175: 
 176: # 3. targets
 177: done = set(pd.read_csv(TGT)["comp"]) if TGT.exists() else set()
 178: for c in comps:
 179:     s = ";".join(f"{e}:{v:.4f}" for e, v in c.items())
 180:     if s in done:
 181:         continue
 182:     alloy = compute.solid_solution(c, "fcc", reps=3, seed=100)
 183:     x = compute.actual_fractions(alloy)
 184:     assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
 185:     r = {"comp": s, "n_el": len(c), "V0": ctx.vegard(c), **kst.curvatures(alloy, x, ctx.vegard(c)),
 186:          "time": dt.datetime.now().isoformat(timespec="seconds")}
 187:     pd.DataFrame([r]).to_csv(TGT, mode="a", header=not TGT.exists(), index=False)
 188: print("targets done", flush=True)
 189: 
 190: # 4. test
 191: t = pd.read_csv(TGT)
 192: y = {ch: t[ch].values for ch in CH}
 193: rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
 194: for ch in CH:
 195:     print(ch, {arm: round(rm(y[ch] - P[ch][arm]), 2) for arm in ARMS}, flush=True)
 196: noco = np.array(["Co" not in c for c in comps])
 197: print("Kp, Co-free rows", int(noco.sum()), {arm: round(rm((y["Kp"] - P["Kp"][arm])[noco]), 2) for arm in ARMS})
 198: for h, reg in regs.items():
 199:     new, old = HYP[h]
 200:     ok, gain, p = test(y["Kp"], P["Kp"][new], P["Kp"][old])
 201:     k44 = test(y["K44"], P["K44"][new], P["K44"][old])
 202:     print(f"{h}: gain {gain:.3f}, p {p:.1e} -> {'PASS' if ok else 'FAIL'}; K44 (secondary) gain {k44[1]:.3f}, "
 203:           f"p {k44[2]:.1e}", flush=True)
 204:     ledger.record(f"W1 {h} result: {'PASS' if ok else 'FAIL'}, K' RMSE {new} {rm(y['Kp'] - P['Kp'][new]):.2f} vs "
 205:                   f"{old} {rm(y['Kp'] - P['Kp'][old]):.2f} GPa, gain {gain:.3f}, p {p:.1e}; K44 gain {k44[1]:.3f}",
 206:                   "L0", [str(BIN), str(TGT), str(COMPS), SCRIPT], notes=f"prereg {reg['id']}; audit pending")
   1: """Shear-curvature volume transfer (swarm S1, open front, Opus): a new observable for the champion's mechanism.
   2: 
   3: python scripts/k_shear_transfer.py
   4: Claim: the clamped mixing shear curvatures of random fcc alloys are pair sums of 50:50 binary curvatures taken at the
   5: alloy's own volume, K_alloy(V0) = sum 4 x_i x_j K_ij(V0), with no parameter. Baseline: the same pair sum at each
   6: binary's own Vegard volume V_ij.
   7: Order, so that the test is blind:
   8:  1. binaries: K44, K' of the 50:50 binaries (SQS seeds 0-2) on a ln(V/V_ij) grid -> data/binary_kgrid.csv
   9:  2. predictions on the h3_fresh compositions (comp_actual, n_el >= 3; K never computed there), power by simulation,
  10:     pre-registration in the ledger
  11:  3. targets: the same a2 protocol on those alloys, references at the cell's actual fractions -> data/h3_shear_clamped.csv
  12:  4. test: per channel RMSE(rule) <= 0.9 RMSE(pair at V_ij) and paired sign-flip p < 0.005 (two channels); PASS needs
  13:     both channels. Secondary (reported, not gated): Opus's prior on median dlnK/dlnV of binaries with |K| > 10 GPa,
  14:     K44 in [-5, -1.5], K' in [-6, -2].
  15: """
  16: 
  17: import datetime as dt
  18: import os
  19: import sys
  20: import time
  21: from pathlib import Path
  22: 
  23: ROOT = Path(__file__).resolve().parent.parent
  24: os.environ["HARNESS_MODEL"] = "medium-omat-0"
  25: sys.path.insert(0, str(ROOT))
  26: 
  27: import numpy as np  # noqa: E402
  28: import pandas as pd  # noqa: E402
  29: from ase.build import bulk  # noqa: E402
  30: from scipy.interpolate import CubicSpline  # noqa: E402
  31: 
  32: from harness import compute, ledger  # noqa: E402
  33: from harness.compute import GPA  # noqa: E402
  34: from harness.context import context  # noqa: E402
  35: from harness.features import parse_comp  # noqa: E402
  36: 
  37: AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
  38: GRID = [-0.40, -0.30, -0.20, -0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40]
  39: BIN, TGT = ROOT / "data" / "binary_kgrid.csv", ROOT / "data" / "h3_shear_clamped.csv"
  40: ctx = context()
  41: calc = compute.calculator()
  42: SCRIPT = str(Path(__file__))
  43: 
  44: 
  45: def e_strained(atoms, v_atom, F):
  46:     a = atoms.copy()
  47:     a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
  48:     a.set_cell(a.cell @ F.T, scale_atoms=True)
  49:     a.calc = calc
  50:     t = time.perf_counter()
  51:     e = a.get_potential_energy() / len(a)
  52:     time.sleep(time.perf_counter() - t)  # 50% duty cycle, keeps the laptop cool
  53:     return e
  54: 
  55: 
  56: def F_of(name, s):
  57:     if name == "K44":
  58:         F = np.eye(3)
  59:         F[0, 1] = s
  60:         return F
  61:     return np.diag([np.exp(s), np.exp(-s), 1.0])
  62: 
  63: 
  64: def curvatures(alloy, x, v):
  65:     """K44, Kp (GPa) of E_mix with references at fractions x, all at volume v and the same deformation."""
  66:     pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in x}
  67:     out = {}
  68:     for name in ("K44", "Kp"):
  69:         em = [e_strained(alloy, v, F_of(name, s)) - sum(xi * e_strained(pures[el], v, F_of(name, s))
  70:                                                          for el, xi in x.items()) for s in AMPS]
  71:         c2 = np.polyfit(AMPS, em, 2)[0]
  72:         out[name] = (2 * c2 if name == "K44" else c2 / 2) / v * GPA
  73:     return out
  74: 
  75: 
  76: # 1. binaries
  77: done = set(map(tuple, pd.read_csv(BIN)[["pair", "seed", "dlnV"]].astype(str).values)) if BIN.exists() else set()
  78: for (A, B), p in sorted(ctx.pair.items()):
  79:     for seed in (0, 1, 2):
  80:         alloy = compute.solid_solution({A: 0.5, B: 0.5}, "fcc", reps=3, seed=seed)
  81:         for d in GRID:
  82:             if (f"{A}-{B}", str(seed), str(d)) in done:
  83:                 continue
  84:             v = p["V"] * np.exp(d)
  85:             r = {"pair": f"{A}-{B}", "seed": seed, "dlnV": d, "V": v, **curvatures(alloy, {A: 0.5, B: 0.5}, v)}
  86:             pd.DataFrame([r]).to_csv(BIN, mode="a", header=not BIN.exists(), index=False)
  87:     print("binary", A, B, flush=True)
  88: 
  89: g = pd.read_csv(BIN).groupby(["pair", "dlnV"])[["K44", "Kp"]].mean().reset_index()
  90: spl = {(tuple(k.split("-")), ch): CubicSpline(s.dlnV, s[ch]) for k, s in g.groupby("pair") for ch in ("K44", "Kp")}
  91: 
  92: # 2. predictions, power, pre-registration
  93: h3 = pd.read_csv(ROOT / "data" / "h3_fresh_rows_fixed.csv")
  94: h3 = h3[h3.n_el >= 3].reset_index(drop=True)
  95: comps = [parse_comp(s) for s in h3.comp_actual]
  96: keep = [all(((a, b), "K44") in spl for a, b, _, _ in ctx.pairs(c)) for c in comps]
  97: h3, comps = h3[keep].reset_index(drop=True), [c for c, k in zip(comps, keep) if k]
  98: 
  99: 
 100: def predict(c, ch, at_alloy):
 101:     v0 = ctx.vegard(c)
 102:     return sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v0 / ctx.pair[(a, b)]["V"]) if at_alloy else 0.0))
 103:                for a, b, xa, xb in ctx.pairs(c))
 104: 
 105: 
 106: P = {ch: (np.array([predict(c, ch, True) for c in comps]), np.array([predict(c, ch, False) for c in comps]))
 107:      for ch in ("K44", "Kp")}
 108: 
 109: 
 110: def test(y, rule, pair, n_perm=4000, seed=0):
 111:     e_r, e_p = y - rule, y - pair
 112:     gain = 1 - np.sqrt(np.mean(e_r**2)) / np.sqrt(np.mean(e_p**2))
 113:     d = e_p**2 - e_r**2
 114:     rng = np.random.default_rng(seed)
 115:     null = np.array([(d * rng.choice([-1, 1], len(d))).mean() for _ in range(n_perm)])
 116:     p = (np.sum(null >= d.mean()) + 1) / (n_perm + 1)
 117:     return gain >= 0.10 and p < 0.005, float(gain), float(p)
 118: 
 119: 
 120: # Realistic scatter = the rule's residual on the exploratory a2 rows (h1 compositions, n_el >= 3), the arena's
 121: # convention. A first design used the pair sum's residual there (4 GPa, includes the transfer signal itself) and had
 122: # power 0.45, so it was not registered and no target was computed (ledger design note).
 123: a2 = pd.read_csv(ROOT / "data" / "a2_shear_clamped.csv")
 124: a2c = [parse_comp(s) for s in a2.comp]
 125: a2k = [len(c) >= 3 and all(((a, b), "K44") in spl for a, b, _, _ in ctx.pairs(c)) for c in a2c]
 126: a2, a2c = a2[a2k], [c for c, k in zip(a2c, a2k) if k]
 127: SIG = {ch: float(np.sqrt(np.mean((a2[ch].values - [sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v / ctx.pair[(a, b)]["V"])))
 128:                                                         for a, b, xa, xb in ctx.pairs(c)) for c, v in zip(a2c, a2.V0)])**2)))
 129:        for ch in ("K44", "Kp")}
 130: regs = [e for e in ledger.entries() if e["claim"].startswith("Shear-curvature volume transfer") and "prereg" in e["notes"]]
 131: if not regs:
 132:     if not any(e["claim"].startswith("Design note, shear-curvature transfer") for e in ledger.entries()):
 133:         ledger.record("Design note, shear-curvature transfer: first design (sigma 4 GPa = pair-sum residual on exploratory "
 134:                       "a2 rows) had power 0.45 and was not registered; no h3 target computed. Exploratory a2 (n 62, "
 135:                       "seen): K44 pair 3.56 -> rule 2.66 GPa, Kp 5.67 -> 1.80, refit k 0.90 / 1.05. Redesign: sigma = "
 136:                       f"rule residual on a2 {SIG}, the arena convention", "L0", [SCRIPT, str(BIN)],
 137:                       notes="design; before registration")
 138:     rng = np.random.default_rng(1)
 139:     sim = lambda truth: np.mean([all(test(P[ch][truth] + rng.normal(0, SIG[ch], len(comps)),  # noqa: E731
 140:                                           *P[ch], 1000, i)[0] for ch in P) for i in range(200)])
 141:     power, fp = sim(0), sim(1)
 142:     print(f"n {len(comps)}, power {power:.3f}, false pass {fp:.3f}", flush=True)
 143:     reg = ledger.register(f"Shear-curvature volume transfer: clamped mixing K44 and K' of random fcc alloys equal "
 144:                           f"sum 4 x_i x_j K_ij(V0) with binary curvatures at the alloy volume (no parameter); PASS if "
 145:                           f"in both channels RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005 on {len(comps)} h3_fresh "
 146:                           f"alloys whose K has never been computed", SCRIPT, {"power": power, "false_pass": fp},
 147:                           notes="proposed by Opus in swarm S1 (open front), critiqued by Astra; binaries computed first")
 148:     print("registered", reg["id"], flush=True)
 149:     regs = [reg]
 150: 
 151: # 3. targets
 152: done = set(pd.read_csv(TGT)["comp"]) if TGT.exists() else set()
 153: for s, c in zip(h3.comp_actual, comps):
 154:     if s in done:
 155:         continue
 156:     alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
 157:     x = compute.actual_fractions(alloy)
 158:     assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
 159:     r = {"comp": s, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
 160:          "time": dt.datetime.now().isoformat(timespec="seconds")}
 161:     pd.DataFrame([r]).to_csv(TGT, mode="a", header=not TGT.exists(), index=False)
 162: print("targets done", flush=True)
 163: 
 164: # 4. test
 165: t = pd.read_csv(TGT).set_index("comp").loc[h3.comp_actual]
 166: res = {}
 167: for ch in ("K44", "Kp"):
 168:     y = t[ch].values
 169:     ok, gain, p = test(y, *P[ch])
 170:     rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
 171:     T = P[ch][0] - P[ch][1]
 172:     k = float(T @ (y - P[ch][1]) / (T @ T))
 173:     res[ch] = ok
 174:     print(f"{ch}: raw {rm(y - y.mean()):.2f}, pair at V_ij {rm(y - P[ch][1]):.2f}, rule {rm(y - P[ch][0]):.2f} GPa, "
 175:           f"gain {gain:.2f}, p {p:.1e}, refit k {k:.2f} -> {'pass' if ok else 'fail'}", flush=True)
 176: sl = {}
 177: for ch in ("K44", "Kp"):
 178:     vals = [float(spl[((tuple(k.split('-'))), ch)](0, 1) / spl[((tuple(k.split('-'))), ch)](0))
 179:             for k in g.pair.unique() if abs(spl[((tuple(k.split('-'))), ch)](0)) > 10]
 180:     sl[ch] = (len(vals), float(np.median(vals)) if vals else float("nan"))
 181: print("secondary: median dlnK/dlnV of binaries with |K| > 10 GPa:", sl, flush=True)
 182: passed = all(res.values())
 183: if __name__ == "__main__":  # k_shear_kp_hm.py imports this file for its splines; the h3 result is recorded once
 184:     ledger.record(f"Shear-curvature volume transfer: {'PASS' if passed else 'FAIL'} on {len(comps)} unseen h3 alloys "
 185:               f"(K44 {'pass' if res['K44'] else 'fail'}, Kp {'pass' if res['Kp'] else 'fail'}); binary slope prior {sl}",
 186:               "L0", [str(BIN), str(TGT), SCRIPT], notes=f"prereg {regs[0]['id']}")

 succeeded in 504ms:
harness/context.py
   1: """What a candidate formula may use: per-element and per-binary inputs, never the alloy's own target.
   2: 
   3: ctx.pure[el]      dict: V (A^3/atom, MACE fcc), B, G, C11, C12, C44 (GPa), r, chi, vec, tm
   4: ctx.pair[(a, b)]  dict for sorted element pairs, 50:50 random clamped binary at its Vegard volume V_ij:
   5:                   E (eV/atom), D = dE/dlnV, D2 = d2E/dlnV2 (eV/atom), V (A^3/atom); mean over SQS seeds 0-2
   6: ctx.vegard(comp)  Vegard volume of a composition
   7: ctx.pairs(comp)   iterator over (a, b, x_a, x_b) for unlike pairs
   8: """
   9: 
  10: from __future__ import annotations
  11: 
  12: from functools import lru_cache
  13: from itertools import combinations
  14: from pathlib import Path
  15: 
  16: import pandas as pd
  17: 
  18: from harness.features import elem, parse_comp
  19: 
  20: ROOT = Path(__file__).resolve().parent.parent
  21: 
  22: 
  23: class Context:
  24:     def __init__(self):
  25:         p = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")
  26:         self.pure = {}
  27:         for el, r in p.iterrows():
  28:             self.pure[el] = {"V": r.vol_per_atom, "B": r.B, "G": r.G, "C11": r.C11, "C12": r.C12, "C44": r.C44,
  29:                              **elem(el)}
  30:         h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
  31:         h1["c"] = h1.comp.map(parse_comp)
  32:         eq = h1[(h1.n_el == 2) & h1.c.map(lambda c: all(abs(v - 0.5) < 1e-3 for v in c.values()))]
  33:         rows = [eq[["comp", "E_mix", "dE_dlnV", "d2E_dlnV2"]]]
  34:         seeds = ROOT / "data" / "binary_seeds.csv"
  35:         if seeds.exists():
  36:             rows.append(pd.read_csv(seeds)[["comp", "E_mix", "dE_dlnV", "d2E_dlnV2"]])
  37:         b = pd.concat(rows)
  38:         b["pair"] = b.comp.map(lambda s: tuple(sorted(parse_comp(s))))
  39:         m = b.groupby("pair")[["E_mix", "dE_dlnV", "d2E_dlnV2"]].mean()
  40:         self.pair = {k: {"E": r.E_mix, "D": r.dE_dlnV, "D2": r.d2E_dlnV2,
  41:                          "V": 0.5 * (self.pure[k[0]]["V"] + self.pure[k[1]]["V"])} for k, r in m.iterrows()}
  42: 
  43:     def vegard(self, comp: dict) -> float:
  44:         return sum(x * self.pure[e]["V"] for e, x in comp.items())
  45: 
  46:     def pairs(self, comp: dict):
  47:         for a, b in combinations(sorted(comp), 2):
  48:             yield a, b, comp[a], comp[b]
  49: 
  50: 
  51: @lru_cache(maxsize=1)
  52: def context() -> Context:
  53:     return Context()
harness/ledger.py
   1: """Append-only claim ledger. Nothing is called a discovery unless it is here at L2 or above.
   2: 
   3: Every entry above L1 names a parent entry one level below, so a claim's chain of evidence
   4: can be walked back to the calibration of the method that produced its data.
   5: """
   6: 
   7: from __future__ import annotations
   8: 
   9: import datetime as dt
  10: import hashlib
  11: import json
  12: from pathlib import Path
  13: 
  14: LEDGER = Path(__file__).resolve().parent.parent / "claims" / "claims.jsonl"
  15: LEVELS = ("L0", "L1", "L2", "L3", "L4")
  16: 
  17: 
  18: def file_hash(path: str | Path) -> str:
  19:     return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]
  20: 
  21: 
  22: def entries() -> list[dict]:
  23:     if not LEDGER.exists():
  24:         return []
  25:     return [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line]
  26: 
  27: 
  28: def record(claim: str, level: str, evidence: list[str], notes: str = "",
  29:            parent: str | None = None) -> dict:
  30:     assert level in LEVELS, level
  31:     if level in ("L2", "L3", "L4"):
  32:         below = LEVELS[LEVELS.index(level) - 1]
  33:         known = {e.get("id"): e["level"] for e in entries()}
  34:         if known.get(parent) != below:
  35:             raise ValueError(f"{level} claim needs a parent entry at {below}, got {parent!r}")
  36:     now = dt.datetime.now().isoformat(timespec="seconds")
  37:     entry = {"id": hashlib.sha256(f"{now}{claim}".encode()).hexdigest()[:10], "time": now,
  38:              "level": level, "claim": claim, "parent": parent,
  39:              "evidence": {str(p): file_hash(p) for p in evidence}, "notes": notes}
  40:     LEDGER.parent.mkdir(exist_ok=True)
  41:     with LEDGER.open("a", encoding="utf-8") as f:
  42:         f.write(json.dumps(entry, ensure_ascii=False) + "\n")
  43:     return entry
  44: 
  45: 
  46: # Pre-registration and verdicts. A test is registered with its measured power (harness/power.py): a design in which
  47: # a correct formula usually fails is not a test. A failed test is closed with a cause; only cause "hypothesis" retires
  48: # the candidate, "design" and "numerics" send it back to the queue.
  49: CAUSES = ("pass", "hypothesis", "design", "numerics")
  50: 
  51: 
  52: def register(claim: str, script: str, power: dict, notes: str = "") -> dict:
  53:     if power.get("power", 0) < 0.8 or power.get("false_pass", 1) > 0.05:
  54:         raise ValueError(f"underpowered or leaky test design, not registered: {power}")
  55:     return record(claim, "L0", [script], notes=f"prereg; power {power}; {notes}".strip("; "))
  56: 
  57: 
  58: def verdict(prereg: str, outcome: str, cause: str, audit: str, evidence: list[str]) -> dict:
  59:     assert cause in CAUSES, cause
  60:     if cause == "hypothesis" and not audit.strip():
  61:         raise ValueError("retiring a candidate needs a post-fail audit (what was checked, by whom)")
  62:     return record(f"verdict on {prereg}: {outcome}", "L0", evidence, notes=f"cause={cause}; audit: {audit}")
  63: 
  64: 
  65: def open_candidates() -> list[dict]:
  66:     """Registered candidates without a verdict, or whose last verdict was a design or numerics failure."""
  67:     es = entries()
  68:     last = {}
  69:     for e in es:
  70:         if e["claim"].startswith("verdict on "):
  71:             last[e["claim"].split()[2].rstrip(":")] = e["notes"]
  72:     return [e for e in es if e["notes"].startswith("prereg")
  73:             and ("cause=pass" not in last.get(e["id"], "") and "cause=hypothesis" not in last.get(e["id"], ""))]
harness/power.py
   1: """Power check for a pre-registered test, run before the test data exist.
   2: 
   3: A test is only informative if (a) data generated with the hypothesis TRUE, at realistic noise, pass it most of the
   4: time and (b) data with the hypothesis FALSE rarely pass. Both are estimated by simulation. Two failures this tool is
   5: meant to catch, from 2026-10-31: the L3 ordered-cell design (an intercept absorbed the rule's main signal) and R3
   6: (the observable compared relaxed with clamped volumes, so even the exact formula had slope 0.20).
   7: """
   8: 
   9: from __future__ import annotations
  10: 
  11: from typing import Callable
  12: 
  13: import numpy as np
  14: 
  15: 
  16: def power(test: Callable[[object], bool], simulate_true: Callable[[np.random.Generator], object],
  17:           simulate_null: Callable[[np.random.Generator], object], n: int = 300, seed: int = 0) -> dict:
  18:     rng = np.random.default_rng(seed)
  19:     p = np.mean([bool(test(simulate_true(rng))) for _ in range(n)])
  20:     f = np.mean([bool(test(simulate_null(rng))) for _ in range(n)])
  21:     return {"power": round(float(p), 3), "false_pass": round(float(f), 3), "n_sims": n}
  22: 
  23: 
  24: def near_zero_divisor(x, name: str, frac: float = 0.1) -> list[int]:
  25:     """Indices where a quantity used as a divisor is small relative to its spread (ratio predictions blow up there)."""
  26:     x = np.asarray(x, dtype=float)
  27:     bad = np.flatnonzero(np.abs(x) < frac * np.std(x))
  28:     if len(bad):
  29:         print(f"warning: {name} near zero at rows {bad.tolist()}; a ratio-based prediction is unstable there")
  30:     return bad.tolist()
.orchestra/LESSONS.md
   1: # Lessons for derivation agents (Astra, Opus)
   2: 
   3: Read before proposing. Each line is a way a candidate died or nearly died for the wrong reason. Updated 2026-10-31.
   4: 
   5: 1. Ratios of energies blow up where the denominator crosses zero (R3: n_eff = -3 b/a reached -102 for Cu-Ir). Prefer
   6:    predictions linear in measured quantities; if a ratio is essential, say where it is undefined.
   7: 2. Compare like with like: clamped with clamped, relaxed with relaxed, random with random. R3 compared a relaxed random
   8:    volume with a clamped L1_0 volume; even the exact formula then had slope 0.20.
   9: 3. Ordered cells are not random alloys. In PBE, 4-atom ordered cells carry a fixed-volume many-body term (~10 meV/atom)
  10:    that random alloys lack. A random-alloy rule must be tested on random (SQS) cells.
  11: 4. If your rule's main content is a common shift, a test with a free intercept cannot see it. State the test you expect
  12:    to pass, and check its power by simulation (harness/power.py) before data exist.
  13: 5. Results that survived so far: volume transfer of binary interactions (L2, refit k = 0.79 on both holdouts, not
  14:    input noise); isotropic chemical shear softening K44 ~ K' in Ir/Rh alloys (MACE, PBE pending). Build on these.
  15: 6. Results that died for real: A2 (shear from hydrostatic derivatives; even a free 2-term fit has r 0.37), H-sm
  16:    (predicted K44/K' = 4, measured 1.05), R3b (exponent sharing). Do not resubmit without a new mechanism.
  17: 7. PBE: pure references must share the alloy's cutoff (dft.Settings(ecut_elements=...)). Earlier PBE mixing numbers
  18:    carry a cutoff mismatch; its size is being measured (data/ecut_bias.csv).
  19: 8. Round R1 (Astra and Opus independently): 108-atom cells round atom counts, but references used nominal fractions,
  20:    so every non-integer composition carried up to ~60 meV/atom of bookkeeping error. Fixed in data/*_fixed.csv
  21:    (column comp_actual is the real composition) and in the generators. Always reference the composition the cell has.
  22: 9. PBE cutoff mismatch corrected (harness/ecutfix.py, validated to 0.002 meV/atom). MACE now PASSES L1 for the
  23:    ordered-cell beyond-pair Delta (sign 9/10, r 0.80); PBE quaternary Delta +12.9 meV is real. MACE data on ordered
  24:    multicomponent cells can be used.
  25: 10. Round R2 (Astra): the arena's permutation count capped the smallest reachable p at 1/501, so after five tests no
  26:     candidate could pass however good it was. Fixed: n_perm grows with m. Also open: generators set V0 from nominal
  27:     fractions while comp_actual differs (~0.5% in volume, ~0.06 meV RMSE effect, not the cause of k ~ 0.8).
  28: 11. k ~ 0.8 was mostly linearisation: E_ij(V) is strongly nonlinear over |ln(V0/V_ij)| up to 0.36. Exact binary
  29:     energies at the alloy volume give k 0.94 [0.90, 0.98] and RMSE 10.3 meV with no parameter (data/binary_vgrid.csv).
  30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
  31:     from the strained cell (18x18x18 vs 17x18x18), so 0.1 meV/atom of strain-dependent error moves K by 1.6 to 4.7
  32:     GPa. H-iso results before the fix are not evidence either way; the run is stopped. (b) fix_counts.py treated
  33:     0.3333 as the reference weight of equiatomic ternaries (36+36+36 atoms are exact): +0.3 to +0.7 meV added.
  34:     (c) B_chem and R in *_fixed.csv are stale. (d) K44 ~ K' is not Zener invariance.
  35: 13. k at fixed composition (h1/h3 E(V) curves vs exact binary response): 0.976 [0.956, 1.001]. No reduced volume
  36:     response; k ~ 0.8 is the curvature the linear transfer leaves out (94% of the shift).
  37: 
  38: 14. Shear-curvature volume transfer (prereg 4c29d9754c, result 6e0923b413), 113 unseen h3 alloys, binary curvatures
  39:     at the alloy volume, no parameter. Kp: 4.77 -> 2.03 GPa, gain 0.57, p 2.5e-4, refit k 1.08 (pass). K44: 3.29 -> 2.62,
  40:     gain 0.20, p 0.023, refit k 0.86 (fail at p < 0.005). Joint claim FAIL. The first design (sigma = pair-sum residual,
  41:     which contains the signal) had power 0.45 and was stopped before any target existed. K44's worst rule errors are
  42:     Co-rich (Co ~0.46 with Pt or Cu), where the rule is worse than no transfer; cause not yet audited (hypothesis,
  43:     design or numerics). Do not re-split the joint claim after the fact: a K44 or Kp claim needs its own fresh test.
  44: 
  45: 15. K' alone, fresh blind test (prereg 67a358fc59, result d92844787f, L2 entry recorded): 94 hm_fresh alloys, K' 4.22 ->
  46:     1.89 GPa, gain 0.55, p 2.5e-4, refit k 1.08, 75/94 better. Two independent blind sets now agree for K' (k 1.08 both).
  47:     K44 again weaker (gain 0.12, k 0.69, not gated). Why K44 transfers worse than K' is open: Co-rich outliers, or
  48:     internal (non-affine) relaxation channels that the clamped protocol suppresses differently for the two shears.
  49: 
  50: 16. Model swap of the K' rule (prereg 851aec6883, result 86767e478d): medium-mpa-0, same geometry, same 94 hm_fresh
  51:     alloys, binaries seed 0 only. K' 4.73 -> 2.28 GPa, gain 0.52, p 2.5e-4, but refit k 1.33 [1.11, 1.51]: the
  52:     pre-registered k-contains-1 condition FAILS. K44 gain 0.16, k 0.77. Reading: that the alloy's K' follows the binaries
  53:     at the alloy volume and cuts the error in half survives a model with a different shear bias; that the coefficient is
  54:     exactly 1 does not (omat 1.08 twice, mpa 1.33). Binary seed noise would pull k down, not up. The two models disagree
  55:     most at |dlnV| > 0.2 (K' corr 0.80 vs 0.96 within 0.1). Cause not yet audited. Do not claim "parameter-free" across
  56:     models; the PBE check decides which k is physical.
  57: 
  58: 17. K44 transfer fails only with Co (prereg e410c96a32, result d9460850ce). 120 fresh Co-free alloys: K44 pair 4.68 ->
  59:     rule 2.30 GPa, gain 0.51, p 2.5e-4, k 1.23 (PASS). 60 fresh alloys with Co >= 15%: gain 0.11, p 0.08, k 0.70. K'
  60:     passes in both. Open confound: the Co-free set has a larger volume signal (pair error 4.68 vs 3.36), so "Co breaks
  61:     K44" and "K44 needs a large signal" are not yet separated; match the two sets on |rule - pair| before claiming
  62:     a Co mechanism (magnetism is a guess, MACE has no spin).
  63:     Confound check (exploratory, same fresh rows, tertiles of |rule - pair|): at matched signal Co-free gain 0.37 / 0.58
  64:     vs Co 0.08 / 0.22 (mid / large), and Co alloys carry a larger floor at small signal (rule rms 2.61 vs 1.73 GPa).
  65:     The Co effect survives signal matching; not yet a registered claim.
  66: 
  67: 18. Why K44 looked broken (Opus, swarm S2, blind by file timestamp, confirmed on 60 Co alloys). The part the pair rule
  68:     misses is the same in both shears (corr 0.71, slope ~1). K44's volume signal is half of K''s, so the shared floor
  69:     swamps it; in Co alloys the floor anticorrelates with the signal and drags k to 0.7. Remove the floor (A = K44 - K'
  70:     or e' as covariate) and K44 transfers with k ~1. LESSONS 14-16 failure reason: design, not hypothesis.
  71: 
  72: 19. Shared SQS seed leak (Opus S2 audit, Astra confirmed). compute.py:56 draws the site permutation from (seed, n)
  73:     only, so every seed-0 cell thresholds one random field: seed-0 targets and seed-0 binaries share configuration
  74:     noise. K' is immune (gain 0.55-0.58, k 1.07-1.10 for every seed split). K44 is not: leak-free gain 0.06-0.14,
  75:     k 0.60-0.77. d9460850ce and the LESSONS 18 Co check used the leak; 9cfc8edaf0 was withdrawn before reading and
  76:     re-registered as c2eff007ad with target seed 100. Rule: targets and inputs never share a seed.
  77: 
  78: 20. Shared floor, disjoint seeds (c2eff007ad -> b86e0d8a40 PASS, 150 alloys): A = K44 - K' transfers (gain 0.49),
  79:     corr(e44, e') 0.77, joint k 0.91, b 0.94; plain K44 Co-free gain 0.47, Co 0.09. Astra audit: PLAUSIBLE, the
  80:     null could not separate a compositional floor from same-cell noise. A shared-channel claim needs targets for the
  81:     two channels from different cells. Test fd786169e3.
  82: 
  83: 21. The shared floor is compositional (fd786169e3 PASS, two cells per composition, unique seeds): cross-cell corr
  84:     0.75 vs same-cell 0.79, k 0.92, b 0.95; Astra audit PLAUSIBLE (cell noise ~5% of the shared covariance). Next
  85:     doubt is a known identity: clamped curvatures carry the initial stress, K44 = C44 + s_yy, K' = C' + (s_xx+s_yy)/2.
  86:     A floor claim must survive subtracting it (k_floor_stress.py). Pre-register every step; one audit, one test.
  87: 
  88: 22. The floor survives the known pre-stress identity (ede47f1d65 PASS; Astra PLAUSIBLE): corrected cross-cell r
  89:     0.67, k 0.99, b 0.79. Mixing pre-stress is 7 GPa rms but pair-additive (rule leaves 0.7 GPa), so it was never the
  90:     floor. Remaining doubt: error shared through the binary references (b drops to 0.4-0.5 with single disjoint
  91:     seeds). Shared-residual claims need two independent binary panels, as in k_mpa_equiv.py.
  92: 23. k = 1 is retired (88b9465108 FAIL, cause hypothesis; Astra found no coding error). Under mpa, 1200 alloys: k 1.14
  93:     [1.10, 1.18]; the rule still halves the error (4.81 to 2.21 GPa). k is not a model constant but composition
  94:     dependent: 3 elements 1.00, Cu-free 1.00, Cu 1.24, alloys with max|dlnV| > 0.25 1.41; omat shows the same pattern
  95:     (1.11). The pair transfer under-predicts at large size mismatch. A power sim that treats the target residual as
  96:     cell noise is optimistic: most of it is compositional and does not average out over cells.
STATUS.md
   1: # Durum (2 Kas������m 2026)
   2: 
   3: Tek giri���Y noktas������. Ayr������nt������ ve kan������t defterde (`claims/claims.jsonl`, kimlikler a���Ya���Y������da), dersler `.orchestra/LESSONS.md` i������inde. `.orchestra/NIGHT_REPORT.md` 31 Ekim sabah������na ait ve eskidir ("iki ba���Y������ms������z holdout" ifadesi d26bd71285 ile d��zeltildi).
   4: 
   5: ## Bulgular
   6: 
   7: | # | Bulgu | Seviye | Kan������t | A������������k olan |
   8: |---|---|---|---|---|
   9: | 1 | **K' hacim transferi.** Rastgele fcc ala���Y������m������n kar������Y������m K' de���Yeri = �o 4 x_i x_j K'_ij(V0), ikililer ala���Y������m hacminde. ������ki k������r sette hata yar������ya iniyor, k 1.08 ve 1.08. | L2 (697c2d6d75) | h3: 4c29d9754c ������' 6e0923b413 (ortak iddia K44 y��z��nden FAIL); hm_fresh: 67a358fc59 ������' d92844787f (PASS) | mpa modelinde k 1.33 [1.11, 1.51] (851aec6883 ������' 86767e478d), ama s������z������nt������s������z 150 ala���Y������mda 1.10 [0.94, 1.26] (kay������ts������z; 6bc0e190a8 FAIL, sebep design). Denklik testi 88b9465108 FAIL: 1200 ala���Y������m, k 1.14 [1.10, 1.18], kural yine hatay������ 4.81'den 2.21 GPa'ya indiriyor (43370bbb27, verdict 736bcac471, Astra: kod hatas������ yok). k kompozisyona ba���Yl������ (ke���Yifsel): 3 element 1.00, Cu'suz 1.00, Cu'lu 1.24, max|dlnV| > 0.25 iken 1.41. omat da benzer (1.11). k = 1 iddias������ d�����Yt��; b��y��k hacim fark������nda transfer eksik kal������yor. PBE yok. Literat��r (tam metin): k������smen biliniyor; hacim ad������m������, k������r test ve K'/K44 kar���Y������tl������Y������ bulunamad������. "Hacim transferli regular-solution / kesik tens������rel CE kural������" diye yaz������lmal������, Marker 2017 okunmadan yaz������lmamal������. |
  10: | 2 | **Enerji hacim transferi: D���o���?T���o.** Standart Muggianu (saf elementler kendi hacminde) ayn������ i���Yi yap������yor, 11.4 ile 11.5 meV, kural 13.3 (S2 denetimi, defterde d��zeltme). Eski metin: E_mix hatas������ 36.4 ������' 13.1 meV, yaln������z hm_fresh (n 94) ger������ekten k������rd��. Tam hesapta k 0.94 ile 0.98; 0.81 do���Yrusalla���Yt������rma etkisi. | L2 (05f01df6ec, d��zeltme d26bd71285) | 1708d0db77, k_direct | Fikrin ������z�� Zunger 1987-89'da biliniyor (`claims/literature.jsonl`). PBE d��zenli h��cre L3'�� FAIL (8541e914ea). |
  11: | 3 | **K44 Co'suz ala���Y������mlarda transfer oluyor** (������n kay������t e410c96a32 ������' d9460850ce, 120 taze ala���Y������m, kazan������ 0.51, p 2.5e-4, k 1.23); Co'lularda olmuyor (kazan������ 0.11). Eski g������zlem: Ayn������ kural K44'te zay������f: kazan������ 0.12 ile 0.20, k 0.69 ile 0.86. En k������t�� hatalar Co'ca zengin ala���Y������mlarda. | g������zlem | LESSONS 14 ile 16 | Neden a������������k; ba���Y������ms������z denetim yap������lmad������. Ke���Yif bak������Y������ (g������r��lm�����Y 269 sat������r, kay������t de���Yil): "E_F'de y��ksek DOS" a������������klamas������ desteklenmiyor, art������k Pd/Pt/Ni/Rh/Ir/Co oran������yla iki kanalda da benzer b��y��yor (K44/K' rms oran������ 1.15 ile 1.4). En b��y��k hatalar iki kanalda da Co'lu ala���Y������mlarda (|r44| ile Co r 0.33): s������radaki ���Y��pheli Co manyetizmas������. K44'��n hacim kaymas������ da k����������k, kazan������ i������in az yer var (a2: pair 3.56 ������' kural 2.66, K' 5.67 ������' 1.80). |
  12: | 3b | **Ortak kayma taban������.** Hacim kural������n������n K44 ve K''te ka������������rd������Y������ k������s������m ayn������ ve kompozisyona ait: K44 - K' kural������ ge������iyor (kazan������ 0.49), h��creler aras������ r 0.75, bilinen ������n gerilme ������zde���Yli���Yi ������������kar������l������nca r 0.67, k 0.99. K44'��n "tutmamas������" bu tabandan. | L0, �������� ������n kay������tl������ PASS (b86e0d8a40, fd786169e3, ede47f1d65), ���������� de Astra denetimi PLAUSIBLE | `data/k_aniso_s100_clamped.csv`, `k_floor_cells.csv`, `k_floor_stress_*.csv`; LESSONS 20-22 | ������kili referanslardan gelen ortak hata d������Ylanmad������ (iki ba���Y������ms������z ikili paneli gerekli). Fiziksel anlam������ a������������k; MACE only. |
  13: | 4 | **MACE kar������Y������m kayma e���Yrili���Yinde L1'den ge������miyor.** 8 d��zenli L1_2 h��crede K' i���Yareti 8/8 do���Yru, K44 i���Yareti 5/8 (Au3Ir PBE ���^'32.4, MACE +3.2 GPa); medyan sapma K' i������in %47, K44 i������in %56. K' kural������ yaln������z MACE i������inde g������sterilmi���Y say������l������r. | L1 FAIL (b3214734c2, Astra denetimli) | `data/hiso_l12_dft_v2.csv`, `data/hiso_l12_mace.csv` | dense-k ve ecutrho kontrolleri ko���Yuyor. |
  14: | 5 | **H-iso.** H��cre i������i i���Yaret okumas������yla PASS (n 6, medyan K44/K' 0.94), tek i���Yaret okumas������yla FAIL (Pt3Cu pozitif). Ag3Ir 0.54, Ag3Rh 0.39, Pt3Cu 2.61: h��cre baz������nda izotropi yok. | L0, PLAUSIBLE (b3214734c2, sebep numerics, a������������k) | `scripts/hiso_l12_v2.py` | 34/78 ko���Yuda negative rho; ecutrho ���-1.5 ve kspacing 0.08 kontrolleri bitince kapan������r. |
  15: 
  16: Yanl������Ylanan adaylar (A2, H-sm, R3, R3b, HM2-T4, Astra EOS kapan������Y������) ve gerek������eleri defterde `verdict on ...` kay������tlar������nda.
  17: 
  18: ## ������al������Yan i���Yler
  19: 
  20: - **H-iso kontrolleri (PBE, 2 ������ekirdek, s������ral������):** dense bitti (`data/hiso_l12_dft_v2_dense.csv`, kspacing 0.08). Cu3Ir de���Yi���Ymedi (K44 ���^'54.75 ������' ���^'54.71, K' ���^'57.39 ������' ���^'57.42). Ag3Rh K' kararl������ (���^'17.97 ������' ���^'17.44) ama K44 ���^'7.04 ������' ���^'3.64 GPa, oran 0.39 ������' 0.21: Ag3Rh K44 k-yak������nsak de���Yil. Medyan K44/K' 0.942 ������' 0.941, i���Yaretler ayn������, H-iso okumas������ de���Yi���Ymiyor. rho ko���Yusu 2 Kas������m 13:43'te reboot ile 8/18'de kesildi; 3 Kas������m 12:35'te devam ettirildi (log `data/hiso_l12_dft_v2_rho_resume1.log`, kalan Rh_t+ ve Pt3Cu, yakla���Y������k 3 saat).
  21: 
  22: ## S������radaki ad������mlar
  23: 
  24: 1. Dense ve rho bitince H-iso'yu kapat: oranlar ve MACE fark������ ������%10 i������inde kal������yorsa verdict b3214734c2'yi kesinle���Ytir, kalm������yorsa sebep numerics ve yeni ko���Yu.
  25: 2. K' kural������ i������in PBE (L3). **Tasar������m uyar������s������:** d��zenli 4 atomlu h��creler enerji kural������nda PBE'de +10 meV'lik sabit hacim ������ok cisim terimi ta���Y������d������Y������ i������in yanl������Y test ������������kt������ (d440b9eb7b, 8541e914ea). K' i������in de d��zenli h��cre kullan������lacaksa bu ������nce d�����Y��n��lmeli; do���Yru alan PBE SQS h��creleri (32 atom ve ��st��) ve bu laptopta g��nler s��rer, kiral������k sunucu se������ene���Yi var.
  26: 3. PBE h������zland������rma: Cu3Ir'de smearing ve k-a���Y������ gev���Yetmeyi referansa kar���Y������ test et.
  27: 4. ~~Veri d��zeltmesi~~ yap������ld������ (2 Kas������m): `scripts/fix_counts2.py` ������' `data/h1_ev_rows_fixed2.csv`, `h3_fresh_rows_fixed2.csv` (44 ��������l��de ���^'0.31 ile ���^'0.71 meV, R ve B_chem yeniden). hm3 ve di���Yerlerinde 1/3 yok, yeni m��h��r gerekmedi. Enerji analizleri bundan sonra `_fixed2` okumal������.
  28: 5. L4 (2 Kas������m): son tarama ve Astra denetimi yap������ld������ (`claims/literature.jsonl` sat������r 63 ve 64, `.orchestra/audits/L4_kprime_astra.md`). Karar PARTIALLY KNOWN, KEEP: kural ortak hacimli ikili regular-solution enerjisinin kayma t��revi, ������zg��l uygulama bulunmad������. Wu 2021 tezi okundu (sat������r 65): ikili EMTO'dan bcc ��������l��lere excess C' ve C44 aktar������m������ var, ama her bile���Yim kendi hacminde; Vegard hacmi ad������m������ yok. L4 taramas������ kapand������ (arama s������n������rl������), en yak������n ������nc��l olarak draft_v5'e eklendi. Yeni risk: Soyemi 2026 ve Chong 2026, kural������n MACE i������inde tutmas������n������n model yanl������l������Y������ olabilece���Yini d�����Y��nd��r��yor; PBE aktar������m testi bu y��zden daha ������nemli.
  29: 5b. Deney verisi (ajan taramas������ 1 Kas������m): bu dokuz elementte ������l��������lm�����Y tek kristal ala���Y������m sabitleri yaln������z kapal������ eri���Yimde (Cu-Ni Epstein-Carlson 1965, Schmunk-Smith 1960; Cu-Au Chiarodo 1972, dC/dP ile; Pd-Ag Hoare-Yates 1954; Co-Ni Weston-Granato 1975). 3+ bile���Yenli ������l��������m yok. K��t��phane PDF'i gerekli.
  30: 5c. ~~nspin hatas������~~ d��zeltildi (2 Kas������m): `extra={'system.nspin': 1}` art������k ba���Ylang������������ momenti koymuyor, Co girdisinde nspin 1 do���Yruland������.
  31: 6. Makale: `paper/draft_v5.md` (v4 art������ model yanl������l������Y������ s������n������r������, madde 6, ve Soyemi, Chong kaynaklar������; ar���Yiv hen��z v4 ile). v4: Astra v4 incelemesindeki (`.orchestra/audits/draft_v4_astra.md`) b��t��n kapsam ve say������ d��zeltmeleri uyguland������. Ar���Yiv `paper/repro_20261102_2.zip` (v4, requirements.txt, manifest do���Yru; ar���Yivden `chain.py` ve `fix_counts2.py` birebir ��retiyor). G������nderim i������in kalan: yazar������n son okumas������, Zenodo'ya ar���Yiv y��kleme ve DOI'yi metne yazma, ChemRxiv g������nderimi. Bunlar������ yazar yapar. Dense/rho sonucu gelince 5.1'deki "pending" c��mlesi g��ncellenir.
  32: 
  33: ## Harness haritas������
  34: 
  35: | Par������a | Yer |
  36: |---|---|
  37: | Hesap (MACE, SQS, curvature) | `harness/compute.py`, `harness/context.py` (ikili V_ij, Vegard) |
  38: | PBE | `harness/dft.py` (`Settings(kpts=..., ecut_elements=...)` zorunlu) |
  39: | Defter, ������n kay������t, g�������� | `harness/ledger.py`, `harness/power.py` |
  40: | Arena (m��h��rl�� holdout) | `harness/arena.py`, `data/sealed/`, `candidates/` |
  41: | Ajanlar | `scripts/discovery_round.py` (arena turu), `scripts/swarm.py` (cepheler `.orchestra/fronts/`) |
  42: | K' testleri | `scripts/k_shear_transfer.py` (h3), `k_shear_kp_hm.py` (hm_fresh), `k_shear_mpa.py` (model de���Yi���Yimi); veri `data/binary_kgrid*.csv`, `data/*_shear_clamped*.csv` |
  43: | Enerji kural������ | `scripts/hm_l2_fixed.py`, `scripts/k_direct.py`, `candidates/champion_volume_transfer.py` |
  44: 
  45: Veri k��meleri: h1 (ke���Yif, g������r��lm�����Y), h3 (model se������iminde kullan������ld������, K i������in k������rd��), hm_fresh (enerji ve K' i������in k������rd��, art������k g������r��ld��), hm3fix (m��h��rl��, ajanlar g������rmez).

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Content C:\\Users\\can02\\.codex\\skills\\scientific-result-audit\\SKILL.md; "'$p='"'C:\\Users\\can02\\.codex\\memories\\MEMORY.md'; "'$t=Get-Content $p; 147..156 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$t[$_] }; rg -n "Wu|Marker|Muggianu|Redlich|clamped|Vegard|asym" paper/draft_v5.md claims/literature.jsonl' in C:\Users\can02\Projects\AI driven Science
 succeeded in 410ms:
---
name: scientific-result-audit
description: "Bilimsel deney/sim��lasyon sonu������lar������n������n iddialarla, ham ������������kt������yla ve kabul ������l��������tleriyle tutarl������l������Y������n������ denetle; sonu������ kontrol��, deney raporu veya makaledeki say������sal iddialar������n do���Yrulanmas������ istendi���Yinde kullan. Genel literat��r ara���Yt������rmas������ i������in kullanma."
---

# Bilimsel sonu������ denetimi

����?���kt������: iddia, dayanak dosya/sat������r veya tablo, ������l��������t, ger������ek sonu������ ve karar. Yaln������z gerekli sat������rlar������ g������ster; PASS, FAIL, SKIPPED, UNAVAILABLE ve UNVALIDATED ayr������m������n������ koru.

1. ������lgili projenin kendi klas������r��nde AGENTS, aktif karar ve g��ncel sonu������ durumunu oku. AKOR'da freeze/telemetry/��cretli ������a���Yr������ s������n������rlar������; IsoShift'te START, DECISION, state/LEDGER ve tamamlanm������Y sonu������ JSON'u; Metalliksa'da STATUS, RULES ve ilgili fizik s������zle���Ymesi belirleyicidir.
2. Sonu������ dosyas������, girdi hash'i, kod/commit, y������ntem, birimler, ������rneklem, belirsizlik ve ������nceden tan������mlanm������Y kabul ������l��������t��n�� e���Yle���Ytir. Eksik olan������ a������������k b������rak. Logdaki ilerleme veya s��re������ ������������k������Y������ tek ba���Y������na bilimsel ba���Yar������ kan������t������ de���Yildir.
3. ������ddia edilen say������lar������ mevcut ham kaynaktan yeniden hesapla; ba���Y������ms������z beklenen de���Yer kullan. ���-l��������len, hesaplanan, tahmini, sentetik ve literat��rden al������nan de���Yerleri ay������r. Sentetik kontrol deneysel validasyon say������lmaz.
4. Ba���Yar������s������z ������nkay������tl������ testi sonradan ge������en test olarak sunma; de���Yi���Yen y������ntem/������l��������t i������in yeni s��r��m ve a������������k gerek������e gerekir. Tarihsel model sonu������lar������n������ farkl������ modelin g��ncel ������l��������m��yle birle���Ytirme. AKOR'da cache, reasoning, ba���Yar������s������z ������a���Yr������ ve retry t��ketimini bildir; batching etkisiyle format etkisini ay������r.
5. GPU/production ������al������Ymas������ veya model ������a���Yr������s������n������ yeniden ba���Ylatmak yerine ������nce var olan sonu������lar������ denetle. Ek ������al������Yt������rma gerekiyorsa proje yetkisini ve maliyet s������n������r������n������ kontrol et. IsoShift ��retim y������ntemini denetim s������ras������nda de���Yi���Ytirme.
6. Makale incelemesi istenmi���Yse mevcut ARS academic-research-suite ak������Y������n������ kullan; bu skill say������sal kan������t katman������n������ sa���Ylar. Al������nt������, denklem veya ���Yekli ������zg��n kaynakta do���Yrula; eksik at������f uydurma. Nitel ������nceki ������al������Ymayla projenin nicel katk������s������n������ ayr������ ifade et.

Sonu������ dosyas������n������ d��zeltme talebi yoksa audit salt okunurdur. Kapan������Yta do���Yrulanan������, iddiay������ s������n������rlayan hatay������ ve tek somut sonraki ad������m������ bildir.
148: - A nominal spin-off PBE run can remain spin-polarized because ASE forces `nspin=2` when `magnetize()` leaves nonzero moments, and the cache excludes spin/tag identity. Make spin/tag explicit, zero/skip moments for spin-off, assert `pw.in`, and validate cache/output state before Co spin comparisons. [Task 3]
149: - The energy-residual shared-floor predictor is reproducible but only an L0/UNCLEAR hypothesis: it loses much of its gain with disjoint energy/shear seeds and hm misses the 10% gate against an intercept-only baseline. Keep volume conventions consistent and report Co/Co-free strata separately. [Task 4]
150: 
151: ## Failures and how to do differently
152: 
153: - Strong training RMSE, source splits, power simulations, or clean-ternary diagnostics do not prove a candidate; submit the final answer-format candidate to the authorized sealed arena without inspecting sealed contents, or retain an explicit partial/uncertain status. [Task 1]
154: - Treat Ag shear/electronic mechanisms as hypotheses: cutoff mismatch and strain-dependent k-grid are real control failures but do not explain the anomaly; re-run corrected H-iso data before physical interpretation. Equal additive K44/K' corrections do not preserve Zener anisotropy. [Task 2]
155: - Interpolation or clamped/single-seed results are estimates, not direct pressure/ordering evidence. For small crossings such as Ni3Ir, compare signal to random-cell seed scatter and use enthalpy rather than fixed-volume energies. [Task 2]
156: - Do not import `scripts/k_shear_transfer.py` in a screening script: its top-level code computes and writes data. For the cobalt discriminator, use same-site Co������"Ni and Co������"Rh substitutions in seed>=100 cells, calibrate thresholds to the roughly 0.9 GPa Co/Co-free floor gap, and treat nonspin as an intervention rather than a paramagnetic phase. [Task 3]
157: - Do not present `-14/-7` as universal shared-floor coefficients or count overlapping seed patterns as independent evidence. Use disjoint binary energy/shear inputs and disjoint target E/K seeds, an intercept-only gate, and a preregistered test before promotion. [Task 4]
paper/draft_v5.md:14:one specific, fixed-coefficient prescription for the clamped mixing part of the tetragonal shear curvature K' of
paper/draft_v5.md:15:random fcc solid solutions: each equiatomic binary curvature is evaluated at the multicomponent alloy's Vegard volume
paper/draft_v5.md:23:across independent target cells and after removal of the clamped pre-stress, which supports a composition-dependent
paper/draft_v5.md:33:1. Liu et al. (2010) developed CALPHAD-style models for elastic coefficients, and Marker et al. (2017) applied this
paper/draft_v5.md:34:   approach to bcc Ti alloys using relaxed first-principles inputs, each at its own equilibrium volume. Marker
paper/draft_v5.md:38:   including binary and ternary data. Closest to the present test, Wu (2021, Sec. 5.2) fitted pair polynomials to
paper/draft_v5.md:45:   identify the specific fixed-coefficient transfer tested here: clamped multicomponent mixing K' estimated from
paper/draft_v5.md:46:   equiatomic binary curvatures at the alloy Vegard volume. This is a search-bounded statement, not proof that no
paper/draft_v5.md:48:3. Formally the rule is a pair-truncated tensorial cluster expansion or a zeroth-order Redlich-Kister sum with a
paper/draft_v5.md:59:the composition's Vegard volume V0 from the model's pure-element volumes.
paper/draft_v5.md:74:V_ij"), and two own-volume Muggianu analogues built from pure-element curvatures (Section 3.4).
paper/draft_v5.md:117:**3.4 Against own-volume Muggianu (exploratory, 270b2a4019).** A direct modulus-level own-volume Muggianu analogue
paper/draft_v5.md:122:full fitted CALPHAD model of Marker et al. For the mixing energy, the earlier linearised k = 1 transfer gives 13.3
paper/draft_v5.md:125:or h3. K' differs from the energy because the binary curvatures change steeply with volume: at the binary Vegard
paper/draft_v5.md:152:- The same cells after subtracting the clamped mixing pre-stress from targets and binaries alike (prereg ede47f1d65):
paper/draft_v5.md:182:   A preregistered eight-cell ordered L1_2 A3B check (6cb3c2a936, verdict b3214734c2, audited) compared clamped
paper/draft_v5.md:193:   binary Muggianu gives C' RMSE 3.08 GPa and a volume-transfer chain 2.52 GPa (gain 0.18, paired sign-flip p approximately 0.073). The chain
paper/draft_v5.md:254:- Marker, C., Shang, S.-L., Zhao, J.-C., Liu, Z.-K. (2017). Elastic knowledge base of bcc Ti alloys from
paper/draft_v5.md:263:- Wu, Y. (2021). Explorations of high-entropy alloys and perovskite ceramics from first principles based multiphysics
claims/literature.jsonl:2:{"time": "2026-10-30T23:10", "tool": "valency semantic_search_papers", "query": "volume change upon chemical ordering in alloys predicted from volume dependence of ordering or mixing energy, L1_0 versus random", "prior_art": ["cond-mat/9806093 volume changes in binary alloy ordering, classical DFT (Olmsted 1998)", "1203.0646 order-disorder effects on EOS in fcc Ni-Al (Geng, Sluiter, Chen)", "2004.12966 analytic binary alloy volume-concentration relations, deviation from Zen's law (Landa et al.)", "32901047 pressure effect on L1_0 FeNi ordering (Tian, Eriksson, Vitos)"], "implication": "ordering volume and mixing volume beyond Vegard are studied; R3 is new only in the specific claim n_ord = n_eff of the random clamped mixing energy. R1 overlaps Landa 2020, treat as baseline."}
claims/literature.jsonl:3:{"time": "2026-10-30T23:10", "tool": "valency semantic_search_papers", "query": "elastic shear constants of random alloys from volume derivatives of mixing energy, central force pair model, chemical contribution to C44 and C'", "prior_art": ["mtrl-th/9502005 static displacements and chemical correlations (Chakraborty)", "1410.5472 elastic energy of alloys, pitfalls of continuum treatments (Baskaran)", "26202339 elastic constants of random solid solutions by SQS and CPA (Tian, Vitos)"], "implication": "no direct hit for predicting clamped mixing shear curvatures from E_mix(V); A2 is a Born-Huang central-force closure, conceptually standard, specific application not found."}
claims/literature.jsonl:5:{"time":"2026-10-30T23:40","tool":"valency semantic_search_papers","query":"does chemical mixing in random fcc solid solutions change elastic anisotropy (Zener ratio)? isotropic contribution of alloying to C44 and Cprime","prior_art":["26202339 SQS vs CPA elastic constants fcc Ti-Al (Tian, Vitos)","11580714 anisotropic lattice distortions in random alloys (Vitos, Abrikosov)","1910.13210 elasticity of disordered binary crystals (Ras, Fuchs)","22181745 elastic anisotropy Fe-Cr random alloy vs T (Razumovskiy, Ruban)"],"implication":"no prior statement found that the clamped chemical mixing contribution to shear is isotropic (K44 = Kp); H-iso not known so far"}
claims/literature.jsonl:6:{"time":"2026-10-31T00:20","tool":"valency semantic_search_papers","query":"mixing enthalpy of multicomponent alloys deviates from binary pair-additive extrapolation; multicomponent destabilization beyond pair interactions","prior_art":["1907.10223 chemical complexity in HEAs: a pair-interaction perspective (Liu, Stocks, Eisenbach 2019)","2203.16002 phase stability of refractory CCAs from pairwise mixing enthalpy (Zhang, Mishra 2022)","40726175 decoupling of atomic interactions for thermodynamic prediction in FCC alloys (Fan et al. 2025)","1706.09282 first-principles prediction of HEA stability (Feng, Widom)","2211.13066 mixing thermodynamics of HEAs from random ordered configurations (Novick, Stevanovic)"],"implication":"pair additivity is widely used and defended; a systematic positive multicomponent excess in clamped fcc late-TM alloys would be a quantitative counterpoint. Must check Fan 2025 before any L4 claim."}
claims/literature.jsonl:7:{"time":"2026-10-31T02:30","tool":"valency semantic_search_papers","query":"extrapolating binary mixing enthalpies to multicomponent alloys with a volume correction (binary interaction at alloy volume via its volume derivative); volume-dependent ECIs, Connolly-Williams, transferability of binary interactions at different lattice constants","prior_art":["1409.3596 strain-induced interaction in concentrated size-mismatched alloys (Zhuravlev, Belashchenko 2014)","33266623 reliability of CALPHAD predictions in multicomponent systems (Gorsse, Senkov 2018)","1201.6284 composition-dependent interatomic potentials for multicomponent alloys (Sadigh et al.)","2203.16002 pairwise mixing enthalpy phase stability (Zhang, Mishra)","1907.10223 pair-interaction perspective in HEAs (Liu et al.)"],"implication":"volume dependence of pair interactions is known in CE practice; no hit found for the specific zero-parameter transfer of binary W to the multicomponent Vegard volume using binary dE/dlnV as a correction to pair-additive HEA mixing energies. Candidate for L4 after L3; must also read Fan 2025 (40726175) and Zhuravlev 2014 in full."}
claims/literature.jsonl:13:{"round": "R3", "candidate": "R3_opus_1.py", "prior": "UNCLEAR", "refs": ["[Redlich�?"Kister (1948)](https://doi.org/10.1021/ie50458a036)", "[Hillert (1980)](https://doi.org/10.1016/0364-5916(80)90016-4)", "[Hsieh et al. (1998), Ni�?"Cu elektronik yap��s��](https://doi.org/10.1103/PhysRevB.57.15204)"], "verdict": "DROP", "why": "�?ampiyonun trivial refiti de�Yil; D2 hacim dǬzeltmesi makul ve g farkl�� bir kompozisyon ba�Y��ml��l��Y�� getiriyor. Ancak mekanizma fiziksel olarak yeterince temellendirilmemi�Y: VEC ger��ek d-band dolulu�Yu de�Yildir; Ni�?"Cu spektroskopisi ayr�� d bantlar�� ve s��n��rl�� yǬk yeniden da�Y��l��m�� g��sterir. Buradan bǬtǬn Ni/Pd/Pt�?"Cu/Ag/Au ��iftlerine ortak bir ba�Y kuvvetlenmesi e�Yimi ����kar��lamaz. Ayr��ca cebirsel olarak, Xn ilgili VEC grubunun toplam fraksiyonu olmak Ǭzere, dǬzeltme tam olarak 2g X10 X11(X11�^'X10)�^'6g X9 X10 X11 olur: bilinen subregular ikili ve Ǭ��lǬ etkile�Yim polinomlar��n��n k��s��tl�� bi��imidir. Bu ��zel katsay�� ba�Ylama kural��n��n ��ncǬlǬnǬ do�Yrulayamad��m; bu nedenle UNCLEAR. Mevcut mekanizma iddias��yla DROP; olas�� tahmin kazanc�� da g=0 kontrolǬyle hacim e�Yrili�Yinin katk��s��ndan ayr��lmal��."}
claims/literature.jsonl:16:{"round": "S1/ag_anomaly", "candidate": "astra_3", "prior": "UNCLEAR", "refs": ["https://doi.org/10.1021/nn504746u (Garcia et al. 2014, immiscible Rh-Ag and Rh-Au nanoalloys, DFT)", "https://doi.org/10.1021/jz500496e (Seo et al. 2014, isoelectronic RhAg ~ Pd, IrAu ~ Pt)", "https://arxiv.org/abs/1308.4357 (Hart et al. 2013, ab initio PGM alloy review)", "https://doi.org/10.1021/ja908879y (Levy et al. 2010, Rh alloys)", "data/hm_ordered_dft_ecutfix.csv", "data/hiso_l12_dft.csv"], "verdict": "KEEP", "why": "Keep it as an L0 test design only, with changes, not as a mechanism. What holds: the volumes reproduce from scan_fcc_omat_pure.csv (14.9175, 14.7685, 16.9128), and the Delta definition matches hm_ordered.py:62-70. The crossed design is good. In the two large cells, Ir/Rh and Pd/Pt change together, and the bands exclude the swapped outcome (21 is outside [31,55], 43 is outside [11,31]). Problems: (1) The 'Ag d-state alignment' story produces none of the numbers. The predictions are copies of AgCuIrPd, AgCuPtRh and Au3Ir. (2) None of the three tests checks the 'one mechanism' link. The Delta cells never vary Ag and the shear cell has no Cu, so two unrelated effects would pass all three. Add AuCuIrPd, the 43 meV cell with Ag swapped for Au, with a band stated in advance. (3) It ignores data that cuts against Ag-specificity. IrPtAuAu has Delta +18 meV with no Ag and no Cu. AgPdRhRh has Ag-Rh bonds and only +2 meV. Pd3Ir has K44-Kp = +8.2 GPa with no Ag. (4) LESSONS #12 classes the shear premise as non-evidence until hiso_l12_v2 finishes, so register after v2 and use the v2 dense repeat as the noise input for harness/power.py. Prior work: the generic ideas are known (Ag-Rh and Ag-Ir immiscibility, the deep Ag d band versus relativistic Au, RhAg acting like Pd). I found nothing on beyond-pair Delta in Ag-Cu-Ir/Rh-Pd/Pt cells or on clamped K44 vs C' mixing anisotropy in Ag3Ir and Ag3Rh. The mechanism is too vague to search for directly."}
claims/literature.jsonl:17:{"round": "S1/ag_anomaly", "candidate": "opus_1", "prior": "UNCLEAR", "refs": ["scripts/hm_ordered.py:1", "scratchpad/delta_interp.py", "scratchpad/pbe_l12.py", "scratchpad/mace_l12.py:17", "scratchpad/rule_check.py:14", "[Berthier�?"Legrand, 2020](https://doi.org/10.1088/1361-648X/ab87ce)", "[Finnis�?"Sinclair, 1984](https://doi.org/10.1080/01418618408244210)"], "verdict": "KEEP", "why": "Yaln��z test edilecek ampirik hipotez olarak KEEP. Belirtilen scratchpad dosyalar�� mevcut; pw.out enerjileri ve cutoff tablosundan sekiz tahmini yeniden hesaplad��m: -66.3, -55.2, -57.9, -38.4, -27.4, -35.8, -57.6, -50.8 meV/atom; verilen de�Yerlerle uyumlu. Ancak rule_check her N3X terimini kendi Vegard hacminden al��yor; hedef hǬcrenin ortak hacmine transfer ayr��ca s��nanmal��. 28 MACE hǬcresi mevcut; r/slope/MAE de�Yerlerini yeniden Ǭretmedim. Toplam enerji art��Y��, katk��n��n TM sitesinde yerelle�Yti�Yini veya koordinasyon doygunlu�Yunu kan��tlamaz. Finnis�?"Sinclair'de tek site teriminin konveksli�Yi, farkl�� tǬrlerin katk��lar��n�� i��eren toplam D_L12'nin i�Yaretini tek ba�Y��na belirlemez; dolay��s��yla d-band a����klamas��n�� d��Ylama iddias�� fazla gǬ��lǬ. Site-energy yakla�Y��m�� biliniyor; ��nerilen ��zgǬl ��ok-bile�Yenli additivite kural��n��n do�Yrudan ��ncǬlǬnǬ bulamad��m, fakat yenilik kan��tlanm��Y de�Yil. Cephedeki pozitif 2+2 anomalilerini a����klam��yor."}
claims/literature.jsonl:22:{"round": "S1/audit", "candidate": "astra_3", "prior": "KNOWN", "refs": ["Zener, C. (1948) Elasticity and Anelasticity of Metals, Univ. Chicago Press (A = C44/C')", ".orchestra/BRAINSTORM.md:37", ".orchestra/astra_iso.md:1", "claims/claims.jsonl:20", "paper/outline.md:39"], "verdict": "KEEP", "why": "The algebra is right: A changes unless dC44/dC' = A_ref, so K44 = Kp keeps A only when A_ref = 1. I recomputed from the Cu, Ir and Cu3Ir pw.out files at v=12.571 and got Cu (63.04, 19.51), Ir (433.40, 254.39), reference (155.6279, 78.2314), alloy (100.9569, 22.4956), K (-54.671, -55.736) GPa, ratio 1.98933 -> 4.48785. That matches Astra to 1e-5. Caveats: these are finite-strain energy curvatures at Vegard volume with no pressure correction, which Astra states. They also come from the pre-fix H-iso PBE run, which LESSONS 12a says is not evidence because of the ecut and k-grid mismatch. So the size is illustrative and the logical point stands without it. The point itself is elementary and was already in project notes before this audit (BRAINSTORM.md:37, astra_iso.md). The literature check in claims/literature.jsonl:5 found no prior for K44 = Kp itself. Keep it anyway: claims.jsonl:20 still contains the false 'Zener unchanged' equivalence. paper/outline.md:39 already uses the narrower 'isotropic chemical shear softening' wording, so the remaining work is a ledger correction note."}
claims/literature.jsonl:25:{"round": "S1/audit", "candidate": "opus_3", "prior": "UNCLEAR", "refs": ["AGENTS.md:36", "scripts/l2_search.py:55-60", "claims/claims.jsonl:4,35-36", "harness/ledger.py:28-35", "data/l2_input_20261031_033518.csv", "data/l2_results_20261031_033518.csv", "claims/literature.jsonl", "[Denton ve Ashcroft (1991), Vegard's law](https://doi.org/10.1103/PhysRevA.43.3161)", "[Landa vd. (2020), ala�Y��m hacmi ve Zen yasas��ndan sapma](https://arxiv.org/abs/2004.12966)"], "verdict": "KEEP", "why": "Yanl��Y L1 ebeveyni kesin: iki hacim kayd�� elastik sabit kalibrasyonu e5ef5a57a3'e ba�Ylan��yor; se��ici ��zellik/kafes denetlemiyor ve defterde hacim kalibrasyonu yok. Veri 41 sat��r; sonu�� tablosunda RMSE 0.135085��'0.092529 ���/atom, kazan�� %31.50. 41'in 40'a yak��nl��Y�� veya etkinin kǬ��Ǭk olmas�� tek ba�Y��na ge��ersizlik de�Yildir. Boyut uyumsuzlu�Yu ile do�Yrusal hacim yasas��ndan sapma biliniyor; fakat bu, ��zel delta_r ve ��zellikle delta_r*S_mix regresyonlar��n��n ayn�� ��ncǬl sonucu tekrarlad��Y��n�� kan��tlamaz. Tam terimler i��in do�Yrulanm��Y ��ncǬl bulunamad��Y��ndan birle�Yik yenilik hǬkmǬ UNCLEAR. LiteratǬr defterinde genel hacim ��ncǬlleri bulunuyor, bu iki kayda ��zel kontrol g��rǬnmǬyor. KEEP kalibrasyon kap��s�� hatas�� i��indir; adaylar�� fiziksel olarak ��ǬrǬtǬlmǬ�Y diye emekliye ay��rmak gerekmez. Ayr��ca yaln��z L0 notu eklemek mevcut ledger.record i��inde eski L2 kay��tlar��n��n L3 ebeveyni olarak kullan��lmas��n�� engellemez; ge��ersizle�Ytirme durumunun kodda uygulanmas�� gerekir."}
claims/literature.jsonl:26:{"round": "S1/k_mechanism", "candidate": "S1_k_mechanism_opus_1.py", "prior": "KNOWN", "refs": ["harness/context.py", "data/binary_vgrid.csv", "data/h1_ev_rows_fixed.csv", "data/h3_fresh_rows_fixed.csv", "data/hm_fresh_rows_fixed.csv", ".orchestra/swarm/S1/k_mechanism/opus.md", "[Ferreira�?"Wei�?"Zunger, 1989](https://doi.org/10.1103/PhysRevB.40.3197)", "[Redlich�?"Kister�?"Muggianu uygulamas��, Denklem 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC4495026/)"], "verdict": "DROP", "why": "Say��sal dayanaklar do�Yruland��: 136 ikili sat��rda k=0.888814; D�?"D2 korelasyonu �^'0.953; 175 ��ok bile�Yenli sat��rda tǬrev e�Yimi 0.98568. E�Yitim RMSE=8.983 meV/atom. Ancak 0.89 mekanizmadan tǬretilmi�Y bir sabit de�Yil, bile�Yimler aras�� ampirik kalibrasyon; ��ok bile�Yenli ortama aktar��lmas�� ayr��ca s��nanmal��. D=V[לx_iP_i�^'P_alloy] oldu�Yundan kar��Y��m bas��nc��n�� yaln��z saf referanslarla ��zde�Yle�Ytirmek ek varsay��m gerektirir. Hacme ba�Yl�� etkile�Yimler ve Ǭ��lǬ bile�Yim terimi bilinen bi��imlerdir; 0.89 eklemek yeni fizik olu�Yturmaz. DROP yeni mekanizma aday�� olarak; ampirik kar�Y��la�Yt��rma modeli olarak saklanabilir. KNOWN s��n��flamas�� model ailesine aittir, bu say��sal katsay��n��n daha ��nce yay��mland��Y�� do�Yrulanmad��."}
claims/literature.jsonl:29:{"round": "S1/open", "candidate": "opus_1", "prior": "UNCLEAR", "refs": ["data/a2_shear_clamped.csv", "data/h1_ev_rows_fixed.csv", "data/binary_vgrid.csv", "scripts/a2_shear_clamped.py:53", "claims/claims.jsonl:29", "[Alling vd.: hacme ba�Yl�� cluster expansion](https://arxiv.org/abs/1012.3120)", "[van de Walle: tensorial cluster expansion](https://doi.org/10.1038/nmat2200)", "[Liu vd. 2021](https://pubmed.ncbi.nlm.nih.gov/34549360/)"], "verdict": "KEEP", "why": "Test edilebilir hipotez olarak KEEP. 62 sat��rda RMSE=3.971/5.631 GPa, r=-0.613/-0.665 ve LOO kazanc��=%21.2/%22.2 yeniden Ǭretildi; 19.999 within-n permǬtasyonda dǬzeltilmi�Y p=0.00005. Ortak hacimdeki binary enerji tǬrevleriyle P_mix RMSE�%^0.607 GPa da do�Yruland��. Fiziksel tǬretme, pair additivity'nin strain alt��nda da ge��erli olmas�� ko�Yuluyla do�Yru; hidrostatik enerji �Yampiyonu bu ko�Yulu kan��tlamaz. Ayr��ca K hedeflerinin Ǭretiminde nominal saf-element a�Y��rl��klar�� kullan��lm��Y: 7 be�Yli kompozisyonda ger��ek atom fraksiyonlar�� farkl��d��r; tahmin taraf��nda comp_actual kullanmak hedefi dǬzeltmez. Hacme ba�Yl�� etkile�Yimler ve elastisite i��in cluster expansion biliniyor; bu ��zel binary-only aktar��m��n nicel ge��erlili�Yine do�Yrudan ��ncǬl bulamad��m, dolay��s��yla NOVEL denemez. �-nce hedef referanslar�� dǬzeltilmeli, seed gǬrǬltǬsǬyle gǬ�� do�Yrulanmal��. Kesin ortak-hacim kural�� ile do�Yrusal slope yakla�Y��m�� ayr�� test edilmeli; do�Yrusal yakla�Y��m��n ba�Yar��s��zl��Y�� kesin kural�� ��ǬrǬtmez. Holdout kazanc��, binary shear slope'lar�� ve bildirilen gǬ�� de�Yerleri henǬz do�Yrulanm��Y sonu�� de�Yildir."}
claims/literature.jsonl:30:{"round": "S1/open", "candidate": "opus_2", "prior": "UNCLEAR", "refs": ["data/a2_shear_clamped.csv", "data/scan_fcc_omat_pure.csv", "data/hiso_l12_mace.csv", "data/hiso_l12_dft.csv", ".orchestra/LESSONS.md:30", "scripts/hiso_l12_v2.py:4", "[Castǭn ve Planes 1988: dǬzenlenmeye ba�Yl�� elastik sabitler](https://doi.org/10.1103/PhysRevB.38.7959)", "[Gornostyrev vd. 2000: Ir'de y��nlǬ ba�Ylanma ve shear](https://doi.org/10.1103/PhysRevB.62.7802)", "[Abbas ve Khawaja 1984: Ni�?"Ir/Ni�?"Rh k��sa menzilli dǬzen](https://doi.org/10.1016/0038-1098(84)90210-2)"], "verdict": "DROP", "why": "Mevcut mekanizma ve test yorumu i��in DROP; hipotez ��ǬrǬtǬlmǬ�Y say��lmamal��. Binary K de�Yerleri, Ir/Rh Cauchy bas��n��lar�� ve Cu3Rh ordered/random oranlar�� 1.145/1.243 dosyalardan do�Yrulan��yor. Ancak bunlar nearest-neighbour yerelli�Yini veya bǬtǬn alpha1 de�Yerlerinde izotropiyi g��stermiyor. K�^?1-alpha1, konfigǬrasyondan ba�Y��ms��z en yak��n kom�Yu etkile�Yimi varsay��l��rsa standart ba�Y say��m��ndan ����kar; K44�%^K' ayr��ca a����klanmas�� gereken bir ko�Yuldur. DǬ�YǬk Cauchy bas��nc�� bu mikroskobik mekanizmay�� tek ba�Y��na belirlemez. Elektronik/band mekanizmalar��n��n sabit kompozisyonda SRO'dan etkilenmeyece�Yi genellemesi de ge��ersizdir; ��l��Ǭlen e�Yim yerel ba�Y kayb��n�� benzersiz bi��imde te�Yhis edemez. �ostelik PBE uyumu ve Au3Ir i�Yaret hatas�� i��in kullan��lan eski hiso_l12 sonu��lar�� cutoff/k-grid sorunlar�� nedeniyle ge��ersiz k��l��nm��Y; dǬzeltilmi�Y sonu�� tablosu yok. SRO�?"elastisite ili�Ykisi ve Ir'nin y��nlǬ ba�Ylanmas�� biliniyor; d��rt ��iftte birim e�Yim ile korunan izotropinin ��zel birle�Yimi i��in ��ncǬl do�Yrulanamad��. Aday, y��nlere g��re ��ift korelasyonlar��n�� ve daha uzak kom�Yuluklar�� kontrol eden, mekanizmalar�� a�Y��r�� yorumlamayan bir SRO testi olarak yeniden sunulabilir."}
claims/literature.jsonl:31:{"time": "2026-10-31T20:22:41", "candidate": "energy volume transfer (champion, 05f01df6ec line)", "prior": "KNOWN (ingredient) / packaging new", "refs": ["Ferreira, Mbaye, Zunger PRB 1987-88 (c-G, energies at V(x))", "Asta et al. PRB 46 5055 (1992) doi:10.1103/physrevb.46.5055", "Ruban et al. SGPM arXiv cond-mat/0202370, 0202371", "Zhang, Li, Cavin, Flores, Mishra arXiv 2203.16002 (pairwise binaries, own volume = our baseline)", "Sanchez PRB 99 134206 (2019)"], "why": "evaluating interactions at the alloy volume is Zunger's renormalized-interaction idea; claim only the binary-at-Vegard pair-sum packaging and its blind accuracy", "queries": "valency 8 keyword + 6 semantic, web 4 (subagent 2026-10-31)"}
claims/literature.jsonl:33:{"time": "2026-10-31T22:30:17", "candidate": "energy volume transfer (05f01df6ec), full-text check", "prior": "PARTIALLY KNOWN", "refs": ["Ferreira, Mbaye, Zunger PRB 35 6475 (1987), full: binary only, alloy volume, pure refs at own volume (G(x) term)", "Ferreira, Mbaye, Zunger PRB 37 10547 (1988), pp 1-6: same, binary", "Ferreira, Wei, Zunger PRB 40 3197 (1989), pp 1-5: J(x,V), pseudobinary", "Ferreira, Ozolins, Zunger PRB 60 1687 (1999): volume-deformation term, our clamped refs remove it", "Bokas et al. Scripta 202 114000 (2021), full: 4 x_i x_j Omega_ij from 50:50 SQS, own volume, blind multicomponent RMSE ~16 meV", "Zhang, Li, Cavin, Flores, Mishra arXiv 2203.16002, full: same, bcc, relaxed binaries at own volume = our baseline", "Ruban et al. cond-mat/0202371, full: fixed common lattice constant, NiPt, no multicomponent"], "why": "pair-sum from 50:50 binaries known (Bokas, Zhang); alloy-volume interactions known for binaries (Zunger). Not found: binaries at the multicomponent Vegard volume with clamped refs, blind-tested vs own-volume pair sum. Not read in full: Sanchez 2019, Asta 1992, Chen Nat Commun 2023", "queries": "subagent full-text check 2026-11-01"}
claims/literature.jsonl:34:{"time": "2026-10-31T22:33:03", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), full-text check", "prior": "PARTIALLY KNOWN", "refs": ["Marker, Shang, Zhao, Liu CMS 140 121 (2017): Redlich-Kister c_ij from binaries/ternaries to Ti alloys; abstract only, closest algebraic precedent, READ BEFORE WRITING", "van de Walle Nat Mater 7 455 (2008) via arXiv 0906.1608 (full): tensorial CE, no volume dependence, no excess part", "Linton & Aidhy APL ML 1 016109 (2023), full: ML on binaries predicts HEA Cij, NiCuAuPdPt, no volume step", "Mirzaee ... Aidhy APL ML 2 046104 (2024), full: C44 transfers worst (R2 0.75), unexplained", "Huhn, Widom PRB 89 104103 (2014), full: binary averaging for moduli, shear transfers worse than bulk", "Asta et al PRB 46 5055 (1992), abstract: volume-dependent ECIs, bulk modulus only", "Geng, Sluiter, Chen PRB 72 014204 (2005), full: volume-dependent ECIs for EOS", "Behara, Van der Ven arXiv 2310.20085, full: strain-dependent CE formalism, Si-Ge only", "Li ... Vitos arXiv 1803.04178, full: volumetric vs electronic split of dC'/dc, dC44/dc, bcc dilute", "Malica & Dal Corso arXiv 2109.00459, full: Fermi-surface term affects C44 of Pd, Pt, not C'"], "verdict": "KEEP, wording restricted", "why": "Not found: excess clamped C' curvature as binary sum with binaries at the alloy Vegard volume, blind test, and the C' vs C44 contrast. Known: binary-to-HEA elastic extrapolation (Redlich-Kister, averaging, ML), volume-dependent interactions, C44 hardest to transfer. Write as pair-truncated tensorial CE / regular-solution rule with volume transfer, not a new law; k model-dependent (1.08 omat, 1.33 mpa). Lead for K44 failure: high DOS at E_F (Pd, Pt, Ni, Rh, Ir, Co) gives non-pair C44 term; test: does K44 additivity recover in Cu/Ag/Au-only alloys."}
claims/literature.jsonl:35:{"round": "S2/k44", "candidate": "astra_1", "prior": "KNOWN", "refs": ["Redlich & Kister 1948, Ind. Eng. Chem. 40:345, [doi:10.1021/ie50458a036](https://doi.org/10.1021/ie50458a036): the antisymmetric first term x(1-x)(1-2x)", "Wang et al. 2016, CALPHAD-type modelling of single-crystal elastic constants in Ti-Nb-Zr, [PMID 27235781](https://pubmed.ncbi.nlm.nih.gov/27235781/)", "Lin, Shang, ..., Liu 2024, CALPHAD modelling of shear properties of Ni alloys, [2404.19098](https://arxiv.org/abs/2404.19098)"], "verdict": "DROP", "why": "The citations and numbers check out. a2 lines 57 and 69 are Co0.75Ir0.25 and Co0.25Pt0.75, with r44/rp of -7.66/-6.33 and +4.44/+3.60 against the 3-seed binary_kgrid splines. All three fixed predictions reproduce exactly from 1.5*K50(V) - K(complement). But r(1-x) = -r(x) is the subregular first Redlich-Kister term, a known form. It also does not answer the front. (a) It does not single out one channel: the same rows carry nearly equal K44 and Kp residuals, and Kp still transfers with gain 0.55. (b) It is not specific to Co. The largest 25/75 binary residuals include Cu-Rh +6.7/+7.6, Cu-Ir -5.7, Au-Ir -5.2 and Au-Rh -4.6, while the K44 residual is under 1 GPa for Co-Ni, Co-Cu, Ag-Co and Au-Co. (c) Each fixed prediction inherits the seed-0 error of the old row. K44 seed SD at V_ij is 2.1 to 2.4 GPa for Co-Ir, Co-Pt and Cu-Pt (seed-0 Cu-Pt 50:50 alone sits -2.4 from the mean), the tolerances are 2.5 to 3, and no power was computed, so a true hypothesis would often fail. (d) The L1 term vanishes for any pair with x_i = x_j, so in multicomponent alloys it only matters for strongly off-equiatomic pairs. It could come back as a subregular extension of the rule covering both channels, but not as the explanation for K44."}
claims/literature.jsonl:36:{"round": "S2/k44", "candidate": "astra_2", "prior": "KNOWN", "refs": ["Tasnadi, Oden, Abrikosov 2012, PRB 85:144112, elastic constants vs supercell size and shape, cubic projection, [1111.0548](https://arxiv.org/abs/1111.0548)", "Tian et al. 2015, JPCM 27:315702, uncertainty from symmetry lowering in SQS elastic constants exceeds the SQS vs CPA difference, [PMID 26202339](https://pubmed.ncbi.nlm.nih.gov/26202339/)", "Moakher & Norris 2006, J. Elasticity 85:215, closest cubic tensor", "Caro 2014, projection onto higher symmetry, [1408.1219](https://arxiv.org/abs/1408.1219)"], "verdict": "KEEP", "why": "The file citations are correct. compute.py:49-58 shuffles without SQS, k_shear_transfer.py:56-60 uses only xy simple shear, and line 156 computes targets at seed 0. Seed SD at V_ij for the 4 pairs reproduces (K44 1.93, Kp 0.45). The 'whole grid' figures 1.93/1.17 are actually the all-36-pair values; the 4 named pairs over the grid give 2.67/1.25. I checked the physics with 108 MACE single points (36 pairs x 3 seeds). Deviatoric stress in the clamped cells is only 0.17 GPa RMS, so the sigma_yy term that simple shear adds through E_yy = g^2/2 is not the source. The K44 scatter follows cell anisotropy instead (dK44 vs dsigma_yy r = -0.54), and averaging over shear planes removes exactly that. Extra issue found: for a given seed and cell size, rng.shuffle applies the same permutation, so every seed-0 50:50 binary has identical sites and multicomponent seed-0 cells are nested in them (verified). Seed-0 K44 averages 0.50 GPa below the 3-seed mean over all 36 pairs. All h3, hm and cofree targets use seed 0, so their noise is correlated across rows, which the sign-flip test assumes away. Limits: the method is textbook, not a physics claim. If multicomponent targets carry binary-level noise of 1.4 to 1.9 GPa, removing it lifts the h3 K44 gain from 0.20 to about 0.3 at most, still below Kp's 0.55. Co pairs do not have larger seed SD than non-Co pairs (Cu-Ir 2.9, Ni-Pt 2.5, Ag-Ir 2.5), so this cannot explain the Co split in LESSONS 17. Keep it as a design/numerics fix to run before any new K44 test, with fresh seeds. At about 1 s per 108-atom single point on this machine, it costs roughly 1 to 2 hours, not 5 to 30 CPU-hours."}
claims/literature.jsonl:37:{"round": "S2/k44", "candidate": "opus_1", "prior": "UNCLEAR", "refs": ["data/binary_kgrid.csv", "data/{a2,h3,hm}_shear_clamped.csv", "data/hm_shear_clamped_mpa.csv", "data/k44_cofree_clamped.csv", ".orchestra/swarm/S2/k44/opus.md ve burada belirtilen scratchpad/a10.py, a12.py, stress_seen_dev.csv, pure_PV.csv", ".orchestra/LESSONS.md:14-16", "[Wallace 1967](https://doi.org/10.1103/PhysRev.162.776)"], "verdict": "KEEP", "why": "Ortak art��k hipotezi olarak KEEP; kan��tlanm��Y mekanizma veya ba�Yar��s��z testlerin design diye yeniden s��n��fland��r��lmas�� olarak de�Yil. Yeniden hesaplama: 269 sat��rda e�Yim 1.041, r=0.766; ikili hacim tǬrevlerinde e�Yim 0.489, r=0.879; g��rǬlen Co sat��rlar��nda ortak fit k=0.879, b=0.982. Art��k tamamlanm��Y 60 Co sat��r��nda k=1.002, b=1.050, r=0.706: ana ��ng��rǬ destekleniyor; dǬz fit k=0.705 ile <=0.70 tahmini az farkla ka����yor. Kar��Y��m bas��nc�� art��Y�� RMS=0.562 GPa ve ortak art��kla korelasyonu 0.626 do�Yruland��. Ancak korelasyon tam izotropi veya nedensellik g��stermez; e' ��l��ǬlmǬ�Y ala�Y��m hedefini i��erdi�Yinden ortak fit ba�Y��ms��z bir ikili-veri tahmin kural�� de�Yildir. 2.16/1.70 GPa de�Yerleri tǬm 72 ikili sat��r��n hatas��d��r; yaln��z 25/75 altkǬmesinde 2.83/2.38 GPa bulunuyor. Bas��n�� dǬzeltmelerinin teorisi Wallace'ta biliniyor; bu ala�Y��mlardaki ortak art��k ili�Ykisine do�Yrudan ��ncǬl bulamad��m. LESSONS 16'daki model ba�Y��ml��l��Y�� a����klanm��Y de�Yil."}
claims/literature.jsonl:38:{"round": "S2/k44", "candidate": "opus_2", "prior": "UNCLEAR", "refs": ["data/binary_kgrid.csv", "data/binary_kgrid_mpa.csv", "data/{a2,h3,hm}_shear_clamped.csv", "data/hm_shear_clamped_mpa.csv", "data/k44_cofree_clamped.csv", "scripts/k_shear_transfer.py", "claims/claims.jsonl:c75e865217", "[van de Walle 2008](https://www.nature.com/articles/nmat2200)", "[Marker ve di�Yerleri 2017](https://doi.org/10.1016/j.commatsci.2017.08.037)"], "verdict": "KEEP", "why": "Omat ile s��n��rl��, s��nanabilir ampirik aday olarak KEEP. G��rǬlen Ǭ�� sette kazan��lar 0.485/0.470/0.414 ve k=0.915/0.963/0.873 yeniden Ǭretildi. Tamamlanm��Y 60 Co sat��r��nda RMSE 3.400��'2.075 GPa, kazan�� 0.390, k=0.833; 100000 i�Yaret ��evirme ��rneklemesiyle p�%^0.0006. Ana ��ng��rǬler kar�Y��lan��yor. Mpa'da k=0.482 ve kazan��=-0.030: model-genel fizik yasas�� de�Yil. Ortak katk��n��n farkta iptali matematiksel olarak do�Yru, fakat kalan hatan��n yaln��z konfigǬrasyon gǬrǬltǬsǬ oldu�Yu g��sterilmedi; ikili seed sa����l��m�� ��ok bile�Yenli hedefin hata taban�� yerine ge��mez. GǬ�� hesab��ndaki 1.00/0.00, varsay��lan Gauss gǬrǬltǬsǬne ko�Yullu sonlu simǬlasyon oranlar��d��r. Defter kayd�� dosya zaman��na g��re k��r ��ng��rǬyǬ bildiriyor fakat ledger ��n kayd�� olmad��Y��n�� a����k��a s��ylǬyor; bu yǬzden kay��tl�� L2 ba�Yar��s�� say��lmaz. Tens��rel cluster expansion ve alt sistemlerden elastik ��zellik ekstrapolasyonu biliniyor; tam olarak bu hacim aktar��lm��Y K44�^'K' kural��n��n ��nceli�Yi do�Yrulanamad��."}
claims/literature.jsonl:41:{"round": "S2/open", "candidate": "opus_1", "prior": "KNOWN", "refs": ["harness/context.py", "candidates/champion_volume_transfer.py", ".orchestra/swarm/S2/open/opus.md �?" belirtilen scratchpad/ref_audit2.py, ref_audit_k.py, pure_ev.csv ve pure_k*.csv", "[Luo vd. 2019: CALPHAD interpolasyonu](https://doi.org/10.1016/j.jmst.2019.05.016)"], "verdict": "KEEP", "why": "Baseline denetimi olarak KEEP. CSV�?tlerden ba�Y��ms��z yeniden hesaplama enerji RMSE�?tlerini do�Yrulad��: h1/h3/hm_fresh i��in k=1: 13.74/13.31/13.26; alternatif baseline: 11.38/11.37/11.54 meV. Referans d��nǬ�YǬmǬnǬn i�Yareti do�Yru; regular-solution/Muggianu bi��imi biliniyor. Ancak F_ij, relakse ikilinin denge enerjisi de�Yil, ikilinin Vegard hacmindeki enerjisidir; bunu standart s��f��r-bas��n�� olu�Yum enerjisiyle ��zde�Yle�Ytirmemeli. K' i��in bildirilen 5.45/5.71 ��' 2.03/1.89 GPa da do�Yruland��. Bununla birlikte ref_audit_k.py modǬlleri do�Yrudan topluyor; enerji referans d��nǬ�YǬmǬnǬn tǬrevi ama��lan��yorsa V*K aktar��l��p hedef hacme b��lǬnmeli. Bu dǬzeltmeyle baseline 4.49/4.60 GPa oluyor ve K' ǬstǬnlǬ�YǬ sǬrǬyor. Yeni baseline eklenip kap�� yeniden de�Yerlendirilmeli; korelasyon tek ba�Y��na k�%^0.8 mekanizmas��n�� veya otomatik seviye dǬ�YǬrmeyi kan��tlamaz."}
claims/literature.jsonl:42:{"round": "S2/open", "candidate": "opus_2", "prior": "UNCLEAR", "refs": ["data/scan_fcc_omat.csv", "data/scan_fcc_omat_pure.csv", "harness/compute.py:77", ".orchestra/swarm/S2/open/opus.md �?" belirtilen scratchpad/chain.py, chain_vs_mug.csv ve relax_soft.py", "[Marker vd. 2017: elastik ��zelliklerin CALPHAD modellemesi](https://doi.org/10.1016/j.commatsci.2017.08.037)"], "verdict": "DROP", "why": "Mevcut mekanizma ve genelleme iddias��yla DROP; Muggianu kontrol modeli korunmal��. �o��lǬlerde C' i��in 2.525/3.075, C44 i��in 3.501/3.670 GPa chain/Muggianu hatalar��n�� do�Yrulad��m; ba�Y��ms��z Muggianu hesab�� dosyayla ��rtǬ�YǬyor. Fakat P=0 yaln��z hidrostatik enerji tǬrevini s��f��rlar; dC/dlnV veya dC/dP s��f��rlanmak zorunda de�Yildir. Dolay��s��yla hacim etkisinin yaln��z ikinci mertebeye kald��Y�� ����kar��m�� ge��ersiz. N_ij do�Yrudan ayn�� hǬcrede ��l��ǬlmǬ�Y iyonik yumu�Yama de�Yil, modellenmi�Y clamped de�Yer ile relakse hedefin fark��d��r; model ve konfigǬrasyon hatalar��n�� da i��erir. Chain ayr��ca ��l��ǬlmǬ�Y hedef hacmi kullan��yor. p�%^0.08/0.32, kazanc��n %20�?tden kǬ��Ǭk oldu�Yunu kan��tlayan e�Yde�Yerlik testi de�Yildir. Elastik CALPHAD modellemesi biliniyor; bu fcc kǬmesine ��zgǬ hata s��n��r�� ve s��f��r-bas��n�� genellemesi i��in do�Yrudan ��ncǬl do�Yrulanmad��Y��ndan UNCLEAR."}
claims/literature.jsonl:45:{"round": "S2/audit", "candidate": "opus_1", "prior": "KNOWN", "refs": ["harness/compute.py:56", "scripts/k_shear_transfer.py:79", "scripts/k_shear_transfer.py:156", "data/binary_kgrid.csv", "data/h3_shear_clamped.csv", "data/hm_shear_clamped.csv", ".orchestra/swarm/S2/audit/opus.md", "[Glasserman�?"Yao, 1992](https://doi.org/10.1287/mnsc.38.6.884)"], "verdict": "KEEP", "why": "Ortak permǬtasyon ve ba�Y��ms��z tahmin de�Yerlendirmesini etkileyen konfigǬrasyon korelasyonu do�Yruland��. Yeniden hesaplamada seed-1/2 ikilileriyle K44 kazan��/k de�Yerleri h3 i��in 0.144/0.771, hm i��in 0.060/0.598; seed-0 ile 0.303/1.038 ve 0.236/0.866. Ham crossed.csv dosyas��ndaki 40 ala�Y��m da e�Yle�Yen/e�Yle�Ymeyen seed RMSE fark��n�� do�Yruluyor: 2.61/2.91 GPa. Mekanizma literatǬrde common random numbers olarak biliniyor; burada hata ba�Y��ms��z genellemeyle kar��Yt��r��lmas��. DǬzeltmeler: power.py ba�Y��ms��z gǬrǬltǬyǬ zorunlu k��lm��yor, sorun ��a�Y��ran scriptlerin null simǬlasyonlar��nda. MPA i��in belirtilen 0.03 �Yi�Yme do�Yrudan seed kar�Y��la�Yt��rmas��yla do�Yrulanm��Y de�Yil. Co-free testi art��k tamamland��Y��ndan de�Yi�Yiklik geriye d��nǬk ��n kay��t say��lamaz; yeni analiz olarak kaydedilmeli."}
claims/literature.jsonl:48:{"time": "2026-11-01T00:32:50", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), Marker 2017 full text (accepted manuscript, 45 pp, read in full)", "prior": "DIFFERENT: Marker is our own-volume Muggianu baseline", "refs": ["Marker, Shang, Zhao, Liu, Comput Mater Sci 140 121 (2017), doi 10.1016/j.commatsci.2017.08.037", "Liu, Zhang, Ganeshan, Wang, Mathaudhu, Scr Mater 63 686 (2010): origin of CALPHAD modelling of c_ij (Marker ref 25)"], "verdict": "KEEP", "why": "Eq 14: c_ij(x) = sum x_A c_A + sum x_A x_B [L0 + L1 (x_A - x_B)] + sum x_A x_B x_C L2, fitted separately to C11, C12, C44 (not C') of fully relaxed PBE SQS (16-64 atoms), bcc Ti-X-Y (X,Y = Mo, Nb, Sn, Ta, Zr). Every input is at its own equilibrium volume; no volume or strain dependence of L anywhere; no excess/clamped decomposition. Only Ti-X binaries exist, so X0.5Y0.5 ends are off (e.g. Nb-Zr, Mo-Zr C11 and C44 by 20-40 GPa), which they attribute to missing non-Ti binaries; ternary L2 hardly helps (Janz-Schmid-Fetzer). Validation: Young's modulus of 13 multicomponent Ti alloys vs experiment, avg deviation 7 GPa binary-only, 5 GPa with L2; no blind or pre-registered test. Consequence for us: Marker's method is exactly the own-volume Muggianu baseline our rule beats (5.7 -> 1.9 GPa on hm_fresh); cite as the standard practice, not as prior art for the volume prescription."}
claims/literature.jsonl:49:{"round": "S3/floor", "candidate": "astra_1", "prior": "UNCLEAR", "refs": [".orchestra/swarm/S3/floor/astra.md", "data/h3_shear_clamped.csv", "data/hm_shear_clamped.csv", "data/h3_fresh_rows_fixed.csv", "data/hm_fresh_rows_fixed.csv", "data/binary_vgrid.csv", "data/binary_kgrid.csv", "data/k_floor_cells.csv", "scripts/k_shear_transfer.py:62", "scripts/h1_ev.py:49", "scripts/hm_fresh.py:59", "harness/compute.py:56", "[Temesi et al. 2023, G of HEAs from enthalpy of mixing (doi:10.3390/ma16062311)](https://pubmed.ncbi.nlm.nih.gov/36984190/)", "[van de Walle 2008, tensorial cluster expansion (doi:10.1038/nmat2200)](https://pubmed.ncbi.nlm.nih.gov/18488033/)", "[Tian et al. 2015, SQS vs CPA elastic constants of random alloys](https://pubmed.ncbi.nlm.nih.gov/26202339/)"], "verdict": "KEEP", "why": "Reproduced from repo data with binaries from seeds 1 and 2. Slopes: h3 (n 113) -13.75/-7.36, hm (n 94) -15.25/-6.06. Common-floor RMS: h3 2.25 -> 1.78, hm 2.21 -> 1.91. Permutation p is 2e-4 on both sets. q is not a Co proxy (corr with x_Co 0.04 and 0.10). The 2:1 split has a physical reading Astra did not give: with nearest-neighbour central forces in fcc, C11:C12:C44 = 2:1:1, so C' = C44/2. The size of -14 implies r^2 phi''/phi of about -168, i.e. a steep effective bond (around r^-12). This is plausible but not derived. Problems: (a) Input noise. The E and K binaries come from the same seed 1 and 2 cells, so their errors are correlated. With disjoint seeds (E from seed 2, K from seed 1) the gain falls to 8% on h3 and 4% on hm, and Co-free alloys get worse (1.83 -> 1.98 and 1.78 -> 1.97). Co alloys gain 10 to 37% in every seed split. (b) Shared cells. In h3, E and shear both come from the seed 0 cell. In hm, E averages seeds 0 to 2. Per-cell noise (E 3.4 meV median, common shear 0.70 GPa) can carry up to about 15 to 25% of the h3 covariance. The proposed main test measures E and shear on the same cell, so it cannot separate a composition term from cell noise. E and shear targets need disjoint seeds. (c) Baseline. Against an intercept-only correction (the validate.py convention), hm gains about 8%, below the 10% gate. (d) No universal coefficient. With Co: -19/-11. Co-free: -9/-4 (h3) and -11/-1.6 (hm). It explains 25 to 37% of the common-floor variance, so it is not the whole floor. (e) Both numeric predictions reproduce exactly, but they use the hm V0 11.959779, while the shear protocol uses ctx.vegard 11.949863 (a 0.17 GPa shift). Both compositions use seeds 1000 to 1009, so they share the (seed, n) random field; each needs its own seeds. Each test is at the 2 to 3 GPa noise level, so it cannot settle the claim. Prior work: the modulus vs mixing-enthalpy correlation is known (Temesi 2023), and tensorial CE expands Cij on the same cluster basis as the energy. I found no fixed-coefficient prediction of clamped shear residuals from the pair-rule energy residual with a 2:1 split. KEEP as L0 only if the pre-registration fixes (a) to (c): disjoint binary seeds for E and K, disjoint target seeds for E and shear, and an intercept-only baseline. Report and gate Co and Co-free separately."}
claims/literature.jsonl:53:{"round": "S3/sfe", "candidate": "astra_1", "prior": "UNCLEAR", "refs": ["https://arxiv.org/abs/2001.06912", "https://arxiv.org/abs/2202.12919", "https://arxiv.org/abs/2610.39495", "https://arxiv.org/abs/2004.06703", "https://arxiv.org/abs/1511.08634", "https://arxiv.org/abs/1806.00718", "https://doi.org/10.3390/e20090655", "https://doi.org/10.1038/s41467-021-23860-z", "https://arxiv.org/abs/2303.14872"], "verdict": "KEEP", "why": "Physically sound, and the file citations hold. calculator, site_counts and actual_fractions are at compute.py:29-47. solid_solution (compute.py:49) really has no SQS and no fault geometry. context.vegard and V_ij (mean of the two pure volumes) match the proposal. All five elements are in scan_fcc_omat_pure.csv. The ledger.register and power.power signatures match. The equiatomic coefficients are correct (4/9 and -1/9; 1/4 and -1/8). fcc111(3,4,18) gives 216 atoms, the 16021.766 conversion is right, and my recount of the cost (~3.7k evaluations) is the same order as theirs. Prior work: the closure is a one-parameter Muggianu (regular solution) extrapolation. For hcp-fcc it is the standard CALPHAD Olson-Cohen SFE model with binary interaction parameters. For gamma(u) it is the random-alloy average of a pair-truncated fault cluster expansion (Natarajan and Van der Ven 2020); Jagatramka 2022 gives similar mean statistics from EAM. The CoNiPt fault-layer control is known local-chemistry SFE physics (Ding 2018, Ikeda 2018, Shih 2021, Ma 2023). Tang 2026 (posted 3 days ago) predicts unstable fault energies from pure-element mu*b_p rule of mixtures. The only part I found nowhere is the volume transfer: pure and 50:50 references taken at the alloy's Vegard volume. Keep it as a cheap L0 test, but fix five things before ledger.register. (1) STATUS row 2 dropped volume transfer for energies because standard Muggianu, with each reference at its own volume, did as well (11.4 vs 13.3 meV). So the volume baseline must be that Muggianu, not the ambiguous 'excess at V_ij' variant, and linear rule of mixtures at V is a second null. Gate on gain over both nulls and a refit k near 1. Absolute RMSE caps alone could pass trivially if rule of mixtures already meets them. (2) K' transfers and E_mix does not, so preregister the split instead of a uniform 20%: volume transfer should help gamma_usf (shear-like, roughly mu*b_p) more than dE_hcp-fcc and gamma_isf. That split is the informative prediction. (3) Co is in 3 of the 8 targets, MACE has no spin, and K44 broke on Co (LESSONS 17). Put Co in a separate stratum. (4) AGENTS requires L1 for this property before any L2: add a MACE pure-element gamma_isf and gamma_usf check against sourced DFT values in reference.py. Elastic L1 does not count, as the proposal itself says. (5) Use target seeds of 100 or higher. The 24 fault-adjacent sites carry about 0.10 composition sd at x=0.5, so balance that layer or widen the cell; otherwise the noise sits near the 20 mJ/m2 tolerance. Scope: the targets are clamped at Vegard volume (no excess volume, no relaxation), so a pass says nothing yet about real twinning or TRIP."}
claims/literature.jsonl:60:{"round": "S3/cobalt", "candidate": "opus_1", "prior": "UNCLEAR", "refs": ["data/scan_fcc_omat_pure.csv", "data/k_aniso_s100.log:54", "scripts/k_aniso_fresh.py", "harness/compute.py:51", "[Gong vd., manyetizmay�� ��rtǬk ��Yrenen Ni potansiyeli](https://arxiv.org/html/2312.17596v2)"], "verdict": "DROP", "why": "Mevcut nedensel ����kar��m i��in DROP. E�Ylenmi�Y atom de�Yi�Yimi yararl�� bir tarama olabilir; fakat kimyay��, elektronik yap��y�� ve yeni Vegard hacmini birlikte de�Yi�Ytirir. Dolay��s��yla Ni kolunun ba�Yar��s��zl��Y�� boyutu, Rh kolunun ba�Yar��s��zl��Y�� valans�� kan��tlamaz; manyetizma ile model hatas��n�� da ay��rmaz. Dosyada Co/Ni hacimleri yak��n fakat e�Yit de�Yil: 10,874/10,921 ���; Cu 11,991 ��� ile yakla�Y��k %10 daha bǬyǬk. Ni de ferromanyetiktir. Tamamlanan 75 Co hǬcresinde k=0,6685; 0,35�?"0,65 aral��Y�� ger��ekle�Ymi�Y sonu�� de�Yildir. Birle�Ytirme sonras�� ikiliye dǬ�Yen hǬcrelerin elenmesi bǬtǬn kollarda ayn�� e�Ylenmi�Y ��rneklemi gerektirir. �-zgǬl swap sonucuna literatǬrde do�Yrudan ��ncǬl bulamad��m; bu, yenilik kan��t�� de�Yildir. Yeniden ��nerilecekse sabit-hacim kontrolǬ ve daha s��n��rl�� nedensel yorum gerekir."}
claims/literature.jsonl:61:{"round": "S3/cobalt", "candidate": "opus_2", "prior": "UNCLEAR", "refs": ["data/hm_shear_clamped_mpa.csv", "data/binary_kgrid_mpa.csv", "data/hm_shear_clamped.csv", "data/binary_kgrid.csv", "scripts/k_shear_mpa.py", "scripts/hm_ordered.py:22", "claims/claims.jsonl:64", "[Gong vd., manyetik durumun mekanik ��zelliklere etkisi](https://arxiv.org/html/2312.17596v2)"], "verdict": "KEEP", "why": "Ke�Yif olarak de�Yil, kapsam ve protokol denetimi olarak KEEP. Yeniden hesaplad��m: mpa K' tǬmǬnde 1,3345; Co�?tsuz 55 sat��rda 1,0474; Co�?tlu 39 sat��rda 1,4756. At��f yap��lan sekiz PBE CSV�?tsinin hi��birinde Co/Ni yok; beyond-pair enerji kalibrasyonunu bu elementlere ta�Y��mak desteklenmiyor. Ancak omat K44=1,21/0,49 ve K'=1,12/1,07 yaln��z seed-0 ikilileriyle yeniden Ǭretiliyor; orijinal Ǭ��-seed ortalamas��nda K44=1,004/0,405, K'=1,079/1,077. Protokoller a����k��a ayr��lmal�� ve seed-0 kar�Y��la�Yt��rmas��n��n bilinen s��z��nt��s�� belirtilmeli. PBE do�Yrulamas��n��n yoklu�Yu tek ba�Y��na failure cause=design sonucunu kan��tlamaz; ��nkay��tl�� FAIL korunmal��. Co ayr��m�� a����klay��c��, sonradan se��ilmi�Y bir bulgudur; ��zgǬl model fark��n��n fiziksel sebebi ve literatǬrdeki yenilik durumu belirsizdir."}
claims/literature.jsonl:63:{"time": "2026-11-02T13:48:50", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), L4 final search", "prior": "NOT FOUND as stated; ingredients known; new interpretive risk (MLIP binary-to-ternary interpolation)", "queries": ["semantic: predicting elastic constants or shear modulus of multicomponent HEAs from binary subsystem contributions evaluated at the alloy volume", "semantic: excess elastic constants of mixing, volume dependence of interaction parameters for shear modulus, CALPHAD elastic constants pressure", "semantic (2024+): MLIP elastic constants random solid solution transferability from binary to ternary/quaternary", "semantic: second derivative of mixing energy w.r.t. shear strain; deviation from linear interpolation", "semantic: ternary/higher-order elastic constants extrapolated from binary data, geometric extrapolation at fixed volume", "semantic (2017+): CALPHAD-type modelling of C11 C12 C44 of multicomponent alloys from binary/ternary parameters", "semantic (2023+): why universal MLIPs predict multicomponent properties from binary interactions; body order of MACE", "abstract FTS batch: Redlich-Kister elastic | CALPHAD elastic constants | excess elastic constants | binary interaction elastic constants ternary | elastic constants Muggianu | shear modulus binary subsystems (mostly off-topic hits)"], "refs": ["Soyemi, Barros, Germann, Nebgen, Hamilton, arXiv 2610.38876 (2026): MLIP trained on unary+binary data transfers to ternary/quaternary by interaction interpolation", "Chong et al. (Ceriotti), arXiv 2509.14146, J Chem Phys (2026): effective body order of MLIPs", "Behara, Thomas, Puchala, Van der Ven, arXiv 2310.20085 (2023): strain-dependent cluster expansion, binary Si-Ge, no multicomponent transfer", "Vazquez et al., Acta Mater (2022) doi 10.1016/j.actamat.2022.117924: SISSO descriptors trained on binary/ternary DFT Cij for Nb-Mo-Ta-W-V, no volume step", "Bijjala, Atlas, Kumar, arXiv 2501.00127: DFPT Cij of refractory binaries, data only", "Temesi et al., Materials 17 2728 (2024): G from valence and radius by rule of mixtures", "Lin et al., arXiv 2404.19098 (2024): CALPHAD of ideal shear strength in dilute Ni alloys (already DROP-checked, entry 34)", "Fan et al., Mater Horiz 12 9160 (2025): NN/LR decoupled CALPHAD energies, not elastic curvature", "Du et al., arXiv 2610.09837 (2026): uMLIP errors in multicomponent materials, compression-side errors larger", "Prior entries 31, 33, 47 (Marker 2017 full text, van de Walle 2008, Linton & Aidhy 2023, Asta 1992) still the closest precedents"], "verdict": "KEEP, wording restricted", "why": "No paper found that reads binary shear-mixing curvatures at the alloy's Vegard volume to predict multicomponent K'. Closest algebra remains Marker 2017 (own-volume Redlich-Kister on Cij = our baseline). New risk: Soyemi 2026 and Chong 2026 show MLIPs interpolate binary interactions into higher-order systems, so a binary-to-multicomponent rule that holds inside MACE may partly reflect the model's effective low body order. This strengthens the case for a PBE transfer test before any physical claim, and the discussion should cite it. Search was Valency only (arXiv, PubMed, ChemRxiv); Web of Science, Scopus and CALPHAD journal full texts not covered."}
claims/literature.jsonl:64:{"time": "2026-11-02T13:54:53", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), L4 audit of line 63", "prior": "PARTIALLY KNOWN (Astra): rule is the shear derivative of a common-volume binary regular-solution energy; specific application not found", "refs": [".orchestra/audits/L4_kprime_astra.md", "Wu, NC State dissertation (2021), repository.lib.ncsu.edu/items/c6af26ab-ea68-422e-bad0-c180581ad176, Sec 5.2 Eq 5.1: multicomponent excess C' and C44 from binary EMTO data. NOT YET READ: repository behind bot check; common-volume step unknown", "Ghosh & Olson, Acta Mater (2002) doi 10.1016/S1359-6454(02)00096-4 [Astra-cited]: superposition model for isotropic shear modulus of Fe-base solutions", "Myhill, Contrib Mineral Petrol (2017) doi 10.1007/s00410-017-1436-z: common-volume Helmholtz mixing model for elastic properties (minerals)", "Ferreira, Wei, Zunger PRB 40 3197 (1989); Behara et al. arXiv 2310.20085"], "verdict": "KEEP, wording restricted; L4 NOT closed", "why": "Corrections to line 63: (a) Soyemi uses HIP-NN, not MACE, and chemical component count is not atomic body order, so the line-63 wording 'MLIPs interpolate binary interactions' overgeneralises; the risk is a plausible alternative explanation, not a shown mechanism. (b) Line 63 cited entries 31, 33, 47 by 0-based index; the 1-based file lines are 32, 34, 48. (c) Marker 2017 relaxes structures to their own ground state; our own-volume baseline is an analogue, not a reproduction. L4 stays open until the Wu thesis Sec 5.2 is read in full. Paper draft_v5 limitation 6 added from the audit's suggested paragraph."}
claims/literature.jsonl:65:{"time": "2026-11-03T12:50:43", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), Wu 2021 thesis read (closes L4 open item from line 64)", "prior": "PARTIALLY KNOWN: binary-to-multicomponent excess C' and C44 known (Marker 2017, Wu 2021); Vegard-volume evaluation step not found", "refs": ["Wu, Yifeng, PhD dissertation, North Carolina State University (2021), Ch. 5, pp. 43-53, read in full from author-supplied PDF (C:/Users/can02/Downloads/etd.pdf, all rights reserved, not archived)"], "verdict": "KEEP, wording restricted; L4 search closed as search-bounded", "why": "Eq. 5.1 is a pair model (on-site polynomial c_ij^pq plus inter-site J_ij, many-body neglected) for excess properties relative to Hume-Rothery sums, explicitly applied to dC' and dC44. Coefficients fitted to EMTO-CPA binary bcc random solutions at x=0,0.1,...,1; each composition's B and Cij come from its own Vinet equilibrium with volume-conserving shears, so no common or Vegard volume step. Validated on arbitrary bcc ternaries: C' R2 0.983 sigma 4.9 GPa, C44 R2 0.938 sigma 5.3 GPa (Fig 5.4). Elements Al Cr Hf Mo Nb Ta Ti V W Zr; no overlap with our fcc set. It is an own-volume binary transfer, i.e. the same class as our baseline, and must be cited as the closest precedent. Our contribution narrows to the evaluation-volume prescription for clamped fcc K' and its preregistered test. Added to draft_v5 Introduction item 1 and references."}

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Content C:\\Users\\can02\\.codex\\skills\\scientific-result-audit\\SKILL.md; "'$files=@('"'harness/context.py','harness/ledger.py','harness/power.py'); foreach("'$p in $files) { Write-Output $p; $i=0; Get-Content $p | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ } }' in C:\Users\can02\Projects\AI driven Science
 succeeded in 445ms:
---
name: scientific-result-audit
description: "Bilimsel deney/sim��lasyon sonu������lar������n������n iddialarla, ham ������������kt������yla ve kabul ������l��������tleriyle tutarl������l������Y������n������ denetle; sonu������ kontrol��, deney raporu veya makaledeki say������sal iddialar������n do���Yrulanmas������ istendi���Yinde kullan. Genel literat��r ara���Yt������rmas������ i������in kullanma."
---

# Bilimsel sonu������ denetimi

����?���kt������: iddia, dayanak dosya/sat������r veya tablo, ������l��������t, ger������ek sonu������ ve karar. Yaln������z gerekli sat������rlar������ g������ster; PASS, FAIL, SKIPPED, UNAVAILABLE ve UNVALIDATED ayr������m������n������ koru.

1. ������lgili projenin kendi klas������r��nde AGENTS, aktif karar ve g��ncel sonu������ durumunu oku. AKOR'da freeze/telemetry/��cretli ������a���Yr������ s������n������rlar������; IsoShift'te START, DECISION, state/LEDGER ve tamamlanm������Y sonu������ JSON'u; Metalliksa'da STATUS, RULES ve ilgili fizik s������zle���Ymesi belirleyicidir.
2. Sonu������ dosyas������, girdi hash'i, kod/commit, y������ntem, birimler, ������rneklem, belirsizlik ve ������nceden tan������mlanm������Y kabul ������l��������t��n�� e���Yle���Ytir. Eksik olan������ a������������k b������rak. Logdaki ilerleme veya s��re������ ������������k������Y������ tek ba���Y������na bilimsel ba���Yar������ kan������t������ de���Yildir.
3. ������ddia edilen say������lar������ mevcut ham kaynaktan yeniden hesapla; ba���Y������ms������z beklenen de���Yer kullan. ���-l��������len, hesaplanan, tahmini, sentetik ve literat��rden al������nan de���Yerleri ay������r. Sentetik kontrol deneysel validasyon say������lmaz.
4. Ba���Yar������s������z ������nkay������tl������ testi sonradan ge������en test olarak sunma; de���Yi���Yen y������ntem/������l��������t i������in yeni s��r��m ve a������������k gerek������e gerekir. Tarihsel model sonu������lar������n������ farkl������ modelin g��ncel ������l��������m��yle birle���Ytirme. AKOR'da cache, reasoning, ba���Yar������s������z ������a���Yr������ ve retry t��ketimini bildir; batching etkisiyle format etkisini ay������r.
5. GPU/production ������al������Ymas������ veya model ������a���Yr������s������n������ yeniden ba���Ylatmak yerine ������nce var olan sonu������lar������ denetle. Ek ������al������Yt������rma gerekiyorsa proje yetkisini ve maliyet s������n������r������n������ kontrol et. IsoShift ��retim y������ntemini denetim s������ras������nda de���Yi���Ytirme.
6. Makale incelemesi istenmi���Yse mevcut ARS academic-research-suite ak������Y������n������ kullan; bu skill say������sal kan������t katman������n������ sa���Ylar. Al������nt������, denklem veya ���Yekli ������zg��n kaynakta do���Yrula; eksik at������f uydurma. Nitel ������nceki ������al������Ymayla projenin nicel katk������s������n������ ayr������ ifade et.

Sonu������ dosyas������n������ d��zeltme talebi yoksa audit salt okunurdur. Kapan������Yta do���Yrulanan������, iddiay������ s������n������rlayan hatay������ ve tek somut sonraki ad������m������ bildir.
harness/context.py
   1: """What a candidate formula may use: per-element and per-binary inputs, never the alloy's own target.
   2: 
   3: ctx.pure[el]      dict: V (A^3/atom, MACE fcc), B, G, C11, C12, C44 (GPa), r, chi, vec, tm
   4: ctx.pair[(a, b)]  dict for sorted element pairs, 50:50 random clamped binary at its Vegard volume V_ij:
   5:                   E (eV/atom), D = dE/dlnV, D2 = d2E/dlnV2 (eV/atom), V (A^3/atom); mean over SQS seeds 0-2
   6: ctx.vegard(comp)  Vegard volume of a composition
   7: ctx.pairs(comp)   iterator over (a, b, x_a, x_b) for unlike pairs
   8: """
   9: 
  10: from __future__ import annotations
  11: 
  12: from functools import lru_cache
  13: from itertools import combinations
  14: from pathlib import Path
  15: 
  16: import pandas as pd
  17: 
  18: from harness.features import elem, parse_comp
  19: 
  20: ROOT = Path(__file__).resolve().parent.parent
  21: 
  22: 
  23: class Context:
  24:     def __init__(self):
  25:         p = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")
  26:         self.pure = {}
  27:         for el, r in p.iterrows():
  28:             self.pure[el] = {"V": r.vol_per_atom, "B": r.B, "G": r.G, "C11": r.C11, "C12": r.C12, "C44": r.C44,
  29:                              **elem(el)}
  30:         h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
  31:         h1["c"] = h1.comp.map(parse_comp)
  32:         eq = h1[(h1.n_el == 2) & h1.c.map(lambda c: all(abs(v - 0.5) < 1e-3 for v in c.values()))]
  33:         rows = [eq[["comp", "E_mix", "dE_dlnV", "d2E_dlnV2"]]]
  34:         seeds = ROOT / "data" / "binary_seeds.csv"
  35:         if seeds.exists():
  36:             rows.append(pd.read_csv(seeds)[["comp", "E_mix", "dE_dlnV", "d2E_dlnV2"]])
  37:         b = pd.concat(rows)
  38:         b["pair"] = b.comp.map(lambda s: tuple(sorted(parse_comp(s))))
  39:         m = b.groupby("pair")[["E_mix", "dE_dlnV", "d2E_dlnV2"]].mean()
  40:         self.pair = {k: {"E": r.E_mix, "D": r.dE_dlnV, "D2": r.d2E_dlnV2,
  41:                          "V": 0.5 * (self.pure[k[0]]["V"] + self.pure[k[1]]["V"])} for k, r in m.iterrows()}
  42: 
  43:     def vegard(self, comp: dict) -> float:
  44:         return sum(x * self.pure[e]["V"] for e, x in comp.items())
  45: 
  46:     def pairs(self, comp: dict):
  47:         for a, b in combinations(sorted(comp), 2):
  48:             yield a, b, comp[a], comp[b]
  49: 
  50: 
  51: @lru_cache(maxsize=1)
  52: def context() -> Context:
  53:     return Context()
harness/ledger.py
   1: """Append-only claim ledger. Nothing is called a discovery unless it is here at L2 or above.
   2: 
   3: Every entry above L1 names a parent entry one level below, so a claim's chain of evidence
   4: can be walked back to the calibration of the method that produced its data.
   5: """
   6: 
   7: from __future__ import annotations
   8: 
   9: import datetime as dt
  10: import hashlib
  11: import json
  12: from pathlib import Path
  13: 
  14: LEDGER = Path(__file__).resolve().parent.parent / "claims" / "claims.jsonl"
  15: LEVELS = ("L0", "L1", "L2", "L3", "L4")
  16: 
  17: 
  18: def file_hash(path: str | Path) -> str:
  19:     return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]
  20: 
  21: 
  22: def entries() -> list[dict]:
  23:     if not LEDGER.exists():
  24:         return []
  25:     return [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line]
  26: 
  27: 
  28: def record(claim: str, level: str, evidence: list[str], notes: str = "",
  29:            parent: str | None = None) -> dict:
  30:     assert level in LEVELS, level
  31:     if level in ("L2", "L3", "L4"):
  32:         below = LEVELS[LEVELS.index(level) - 1]
  33:         known = {e.get("id"): e["level"] for e in entries()}
  34:         if known.get(parent) != below:
  35:             raise ValueError(f"{level} claim needs a parent entry at {below}, got {parent!r}")
  36:     now = dt.datetime.now().isoformat(timespec="seconds")
  37:     entry = {"id": hashlib.sha256(f"{now}{claim}".encode()).hexdigest()[:10], "time": now,
  38:              "level": level, "claim": claim, "parent": parent,
  39:              "evidence": {str(p): file_hash(p) for p in evidence}, "notes": notes}
  40:     LEDGER.parent.mkdir(exist_ok=True)
  41:     with LEDGER.open("a", encoding="utf-8") as f:
  42:         f.write(json.dumps(entry, ensure_ascii=False) + "\n")
  43:     return entry
  44: 
  45: 
  46: # Pre-registration and verdicts. A test is registered with its measured power (harness/power.py): a design in which
  47: # a correct formula usually fails is not a test. A failed test is closed with a cause; only cause "hypothesis" retires
  48: # the candidate, "design" and "numerics" send it back to the queue.
  49: CAUSES = ("pass", "hypothesis", "design", "numerics")
  50: 
  51: 
  52: def register(claim: str, script: str, power: dict, notes: str = "") -> dict:
  53:     if power.get("power", 0) < 0.8 or power.get("false_pass", 1) > 0.05:
  54:         raise ValueError(f"underpowered or leaky test design, not registered: {power}")
  55:     return record(claim, "L0", [script], notes=f"prereg; power {power}; {notes}".strip("; "))
  56: 
  57: 
  58: def verdict(prereg: str, outcome: str, cause: str, audit: str, evidence: list[str]) -> dict:
  59:     assert cause in CAUSES, cause
  60:     if cause == "hypothesis" and not audit.strip():
  61:         raise ValueError("retiring a candidate needs a post-fail audit (what was checked, by whom)")
  62:     return record(f"verdict on {prereg}: {outcome}", "L0", evidence, notes=f"cause={cause}; audit: {audit}")
  63: 
  64: 
  65: def open_candidates() -> list[dict]:
  66:     """Registered candidates without a verdict, or whose last verdict was a design or numerics failure."""
  67:     es = entries()
  68:     last = {}
  69:     for e in es:
  70:         if e["claim"].startswith("verdict on "):
  71:             last[e["claim"].split()[2].rstrip(":")] = e["notes"]
  72:     return [e for e in es if e["notes"].startswith("prereg")
  73:             and ("cause=pass" not in last.get(e["id"], "") and "cause=hypothesis" not in last.get(e["id"], ""))]
harness/power.py
   1: """Power check for a pre-registered test, run before the test data exist.
   2: 
   3: A test is only informative if (a) data generated with the hypothesis TRUE, at realistic noise, pass it most of the
   4: time and (b) data with the hypothesis FALSE rarely pass. Both are estimated by simulation. Two failures this tool is
   5: meant to catch, from 2026-10-31: the L3 ordered-cell design (an intercept absorbed the rule's main signal) and R3
   6: (the observable compared relaxed with clamped volumes, so even the exact formula had slope 0.20).
   7: """
   8: 
   9: from __future__ import annotations
  10: 
  11: from typing import Callable
  12: 
  13: import numpy as np
  14: 
  15: 
  16: def power(test: Callable[[object], bool], simulate_true: Callable[[np.random.Generator], object],
  17:           simulate_null: Callable[[np.random.Generator], object], n: int = 300, seed: int = 0) -> dict:
  18:     rng = np.random.default_rng(seed)
  19:     p = np.mean([bool(test(simulate_true(rng))) for _ in range(n)])
  20:     f = np.mean([bool(test(simulate_null(rng))) for _ in range(n)])
  21:     return {"power": round(float(p), 3), "false_pass": round(float(f), 3), "n_sims": n}
  22: 
  23: 
  24: def near_zero_divisor(x, name: str, frac: float = 0.1) -> list[int]:
  25:     """Indices where a quantity used as a divisor is small relative to its spread (ratio predictions blow up there)."""
  26:     x = np.asarray(x, dtype=float)
  27:     bad = np.flatnonzero(np.abs(x) < frac * np.std(x))
  28:     if len(bad):
  29:         print(f"warning: {name} near zero at rows {bad.tolist()}; a ratio-based prediction is unstable there")
  30:     return bad.tolist()

codex
Bilimsel sonu�� denetimi skill�?tini kullan��yorum. ��lk kritik hata bulundu: `"asym".endswith("sym")` do�Yru d��ndǬ�YǬ i��in iki asimetrik kol da simetrik dala giriyor; mevcut kod H2�?tde ayn�� tahmini kendisiyle kar�Y��la�Yt��r��yor. Ayr��ca `k_shear_transfer` import�?tu hesap ve dosya yaz��m�� ba�Ylat��yor; do�Yrulamalar�� bu modǬlǬ import etmeden yapaca�Y��m.

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$p='"'scripts/k_shear_transfer.py'; "'$t=Get-Content $p; 129..($t.Length-1) | ForEach-Object { '"'{0,4}: {1}' -f ("'$_+1),$t[$_] }; $p='"'harness/compute.py'; "'$t=Get-Content $p; 0..105 | ForEach-Object { '"'{0,4}: {1}' -f ("'$_+1),$t[$_] }; rg -n "Wu|Marker|clamped|reference|Hume|Redlich|Muggianu" paper/draft_v5.md; Get-Item C:/Users/can02/Downloads/etd.pdf -ErrorAction SilentlyContinue; rg --files paper .orchestra | rg "Wu|Marker|literature|L4"; rg -n "seed|V0|curvatures|shear_transfer" scripts/hm_shear* scripts/k_hm*' in C:\Users\can02\Projects\AI driven Science
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$files=@('"'.orchestra/LESSONS.md','STATUS.md'); foreach("'$p in $files) { Write-Output $p; $i=0; Get-Content -Encoding UTF8 $p | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ } }' in C:\Users\can02\Projects\AI driven Science
web search: 
 succeeded in 94ms:
.orchestra/LESSONS.md
   1: # Lessons for derivation agents (Astra, Opus)
   2: 
   3: Read before proposing. Each line is a way a candidate died or nearly died for the wrong reason. Updated 2026-10-31.
   4: 
   5: 1. Ratios of energies blow up where the denominator crosses zero (R3: n_eff = -3 b/a reached -102 for Cu-Ir). Prefer
   6:    predictions linear in measured quantities; if a ratio is essential, say where it is undefined.
   7: 2. Compare like with like: clamped with clamped, relaxed with relaxed, random with random. R3 compared a relaxed random
   8:    volume with a clamped L1_0 volume; even the exact formula then had slope 0.20.
   9: 3. Ordered cells are not random alloys. In PBE, 4-atom ordered cells carry a fixed-volume many-body term (~10 meV/atom)
  10:    that random alloys lack. A random-alloy rule must be tested on random (SQS) cells.
  11: 4. If your rule's main content is a common shift, a test with a free intercept cannot see it. State the test you expect
  12:    to pass, and check its power by simulation (harness/power.py) before data exist.
  13: 5. Results that survived so far: volume transfer of binary interactions (L2, refit k = 0.79 on both holdouts, not
  14:    input noise); isotropic chemical shear softening K44 ~ K' in Ir/Rh alloys (MACE, PBE pending). Build on these.
  15: 6. Results that died for real: A2 (shear from hydrostatic derivatives; even a free 2-term fit has r 0.37), H-sm
  16:    (predicted K44/K' = 4, measured 1.05), R3b (exponent sharing). Do not resubmit without a new mechanism.
  17: 7. PBE: pure references must share the alloy's cutoff (dft.Settings(ecut_elements=...)). Earlier PBE mixing numbers
  18:    carry a cutoff mismatch; its size is being measured (data/ecut_bias.csv).
  19: 8. Round R1 (Astra and Opus independently): 108-atom cells round atom counts, but references used nominal fractions,
  20:    so every non-integer composition carried up to ~60 meV/atom of bookkeeping error. Fixed in data/*_fixed.csv
  21:    (column comp_actual is the real composition) and in the generators. Always reference the composition the cell has.
  22: 9. PBE cutoff mismatch corrected (harness/ecutfix.py, validated to 0.002 meV/atom). MACE now PASSES L1 for the
  23:    ordered-cell beyond-pair Delta (sign 9/10, r 0.80); PBE quaternary Delta +12.9 meV is real. MACE data on ordered
  24:    multicomponent cells can be used.
  25: 10. Round R2 (Astra): the arena's permutation count capped the smallest reachable p at 1/501, so after five tests no
  26:     candidate could pass however good it was. Fixed: n_perm grows with m. Also open: generators set V0 from nominal
  27:     fractions while comp_actual differs (~0.5% in volume, ~0.06 meV RMSE effect, not the cause of k ~ 0.8).
  28: 11. k ~ 0.8 was mostly linearisation: E_ij(V) is strongly nonlinear over |ln(V0/V_ij)| up to 0.36. Exact binary
  29:     energies at the alloy volume give k 0.94 [0.90, 0.98] and RMSE 10.3 meV with no parameter (data/binary_vgrid.csv).
  30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
  31:     from the strained cell (18x18x18 vs 17x18x18), so 0.1 meV/atom of strain-dependent error moves K by 1.6 to 4.7
  32:     GPa. H-iso results before the fix are not evidence either way; the run is stopped. (b) fix_counts.py treated
  33:     0.3333 as the reference weight of equiatomic ternaries (36+36+36 atoms are exact): +0.3 to +0.7 meV added.
  34:     (c) B_chem and R in *_fixed.csv are stale. (d) K44 ~ K' is not Zener invariance.
  35: 13. k at fixed composition (h1/h3 E(V) curves vs exact binary response): 0.976 [0.956, 1.001]. No reduced volume
  36:     response; k ~ 0.8 is the curvature the linear transfer leaves out (94% of the shift).
  37: 
  38: 14. Shear-curvature volume transfer (prereg 4c29d9754c, result 6e0923b413), 113 unseen h3 alloys, binary curvatures
  39:     at the alloy volume, no parameter. Kp: 4.77 -> 2.03 GPa, gain 0.57, p 2.5e-4, refit k 1.08 (pass). K44: 3.29 -> 2.62,
  40:     gain 0.20, p 0.023, refit k 0.86 (fail at p < 0.005). Joint claim FAIL. The first design (sigma = pair-sum residual,
  41:     which contains the signal) had power 0.45 and was stopped before any target existed. K44's worst rule errors are
  42:     Co-rich (Co ~0.46 with Pt or Cu), where the rule is worse than no transfer; cause not yet audited (hypothesis,
  43:     design or numerics). Do not re-split the joint claim after the fact: a K44 or Kp claim needs its own fresh test.
  44: 
  45: 15. K' alone, fresh blind test (prereg 67a358fc59, result d92844787f, L2 entry recorded): 94 hm_fresh alloys, K' 4.22 ->
  46:     1.89 GPa, gain 0.55, p 2.5e-4, refit k 1.08, 75/94 better. Two independent blind sets now agree for K' (k 1.08 both).
  47:     K44 again weaker (gain 0.12, k 0.69, not gated). Why K44 transfers worse than K' is open: Co-rich outliers, or
  48:     internal (non-affine) relaxation channels that the clamped protocol suppresses differently for the two shears.
  49: 
  50: 16. Model swap of the K' rule (prereg 851aec6883, result 86767e478d): medium-mpa-0, same geometry, same 94 hm_fresh
  51:     alloys, binaries seed 0 only. K' 4.73 -> 2.28 GPa, gain 0.52, p 2.5e-4, but refit k 1.33 [1.11, 1.51]: the
  52:     pre-registered k-contains-1 condition FAILS. K44 gain 0.16, k 0.77. Reading: that the alloy's K' follows the binaries
  53:     at the alloy volume and cuts the error in half survives a model with a different shear bias; that the coefficient is
  54:     exactly 1 does not (omat 1.08 twice, mpa 1.33). Binary seed noise would pull k down, not up. The two models disagree
  55:     most at |dlnV| > 0.2 (K' corr 0.80 vs 0.96 within 0.1). Cause not yet audited. Do not claim "parameter-free" across
  56:     models; the PBE check decides which k is physical.
  57: 
  58: 17. K44 transfer fails only with Co (prereg e410c96a32, result d9460850ce). 120 fresh Co-free alloys: K44 pair 4.68 ->
  59:     rule 2.30 GPa, gain 0.51, p 2.5e-4, k 1.23 (PASS). 60 fresh alloys with Co >= 15%: gain 0.11, p 0.08, k 0.70. K'
  60:     passes in both. Open confound: the Co-free set has a larger volume signal (pair error 4.68 vs 3.36), so "Co breaks
  61:     K44" and "K44 needs a large signal" are not yet separated; match the two sets on |rule - pair| before claiming
  62:     a Co mechanism (magnetism is a guess, MACE has no spin).
  63:     Confound check (exploratory, same fresh rows, tertiles of |rule - pair|): at matched signal Co-free gain 0.37 / 0.58
  64:     vs Co 0.08 / 0.22 (mid / large), and Co alloys carry a larger floor at small signal (rule rms 2.61 vs 1.73 GPa).
  65:     The Co effect survives signal matching; not yet a registered claim.
  66: 
  67: 18. Why K44 looked broken (Opus, swarm S2, blind by file timestamp, confirmed on 60 Co alloys). The part the pair rule
  68:     misses is the same in both shears (corr 0.71, slope ~1). K44's volume signal is half of K''s, so the shared floor
  69:     swamps it; in Co alloys the floor anticorrelates with the signal and drags k to 0.7. Remove the floor (A = K44 - K'
  70:     or e' as covariate) and K44 transfers with k ~1. LESSONS 14-16 failure reason: design, not hypothesis.
  71: 
  72: 19. Shared SQS seed leak (Opus S2 audit, Astra confirmed). compute.py:56 draws the site permutation from (seed, n)
  73:     only, so every seed-0 cell thresholds one random field: seed-0 targets and seed-0 binaries share configuration
  74:     noise. K' is immune (gain 0.55-0.58, k 1.07-1.10 for every seed split). K44 is not: leak-free gain 0.06-0.14,
  75:     k 0.60-0.77. d9460850ce and the LESSONS 18 Co check used the leak; 9cfc8edaf0 was withdrawn before reading and
  76:     re-registered as c2eff007ad with target seed 100. Rule: targets and inputs never share a seed.
  77: 
  78: 20. Shared floor, disjoint seeds (c2eff007ad -> b86e0d8a40 PASS, 150 alloys): A = K44 - K' transfers (gain 0.49),
  79:     corr(e44, e') 0.77, joint k 0.91, b 0.94; plain K44 Co-free gain 0.47, Co 0.09. Astra audit: PLAUSIBLE, the
  80:     null could not separate a compositional floor from same-cell noise. A shared-channel claim needs targets for the
  81:     two channels from different cells. Test fd786169e3.
  82: 
  83: 21. The shared floor is compositional (fd786169e3 PASS, two cells per composition, unique seeds): cross-cell corr
  84:     0.75 vs same-cell 0.79, k 0.92, b 0.95; Astra audit PLAUSIBLE (cell noise ~5% of the shared covariance). Next
  85:     doubt is a known identity: clamped curvatures carry the initial stress, K44 = C44 + s_yy, K' = C' + (s_xx+s_yy)/2.
  86:     A floor claim must survive subtracting it (k_floor_stress.py). Pre-register every step; one audit, one test.
  87: 
  88: 22. The floor survives the known pre-stress identity (ede47f1d65 PASS; Astra PLAUSIBLE): corrected cross-cell r
  89:     0.67, k 0.99, b 0.79. Mixing pre-stress is 7 GPa rms but pair-additive (rule leaves 0.7 GPa), so it was never the
  90:     floor. Remaining doubt: error shared through the binary references (b drops to 0.4-0.5 with single disjoint
  91:     seeds). Shared-residual claims need two independent binary panels, as in k_mpa_equiv.py.
  92: 23. k = 1 is retired (88b9465108 FAIL, cause hypothesis; Astra found no coding error). Under mpa, 1200 alloys: k 1.14
  93:     [1.10, 1.18]; the rule still halves the error (4.81 to 2.21 GPa). k is not a model constant but composition
  94:     dependent: 3 elements 1.00, Cu-free 1.00, Cu 1.24, alloys with max|dlnV| > 0.25 1.41; omat shows the same pattern
  95:     (1.11). The pair transfer under-predicts at large size mismatch. A power sim that treats the target residual as
  96:     cell noise is optimistic: most of it is compositional and does not average out over cells.
STATUS.md
   1: # Durum (2 Kas���m 2026)
   2: 
   3: Tek giri��� noktas���. Ayr���nt��� ve kan���t defterde (`claims/claims.jsonl`, kimlikler a���a������da), dersler `.orchestra/LESSONS.md` i���inde. `.orchestra/NIGHT_REPORT.md` 31 Ekim sabah���na ait ve eskidir ("iki ba������ms���z holdout" ifadesi d26bd71285 ile d���zeltildi).
   4: 
   5: ## Bulgular
   6: 
   7: | # | Bulgu | Seviye | Kan���t | A������k olan |
   8: |---|---|---|---|---|
   9: | 1 | **K' hacim transferi.** Rastgele fcc ala������m���n kar���������m K' de���eri = ? 4 x_i x_j K'_ij(V0), ikililer ala������m hacminde. ���ki k���r sette hata yar���ya iniyor, k 1.08 ve 1.08. | L2 (697c2d6d75) | h3: 4c29d9754c  6e0923b413 (ortak iddia K44 y���z���nden FAIL); hm_fresh: 67a358fc59  d92844787f (PASS) | mpa modelinde k 1.33 [1.11, 1.51] (851aec6883  86767e478d), ama s���z���nt���s���z 150 ala������mda 1.10 [0.94, 1.26] (kay���ts���z; 6bc0e190a8 FAIL, sebep design). Denklik testi 88b9465108 FAIL: 1200 ala������m, k 1.14 [1.10, 1.18], kural yine hatay��� 4.81'den 2.21 GPa'ya indiriyor (43370bbb27, verdict 736bcac471, Astra: kod hatas��� yok). k kompozisyona ba���l��� (ke���ifsel): 3 element 1.00, Cu'suz 1.00, Cu'lu 1.24, max|dlnV| > 0.25 iken 1.41. omat da benzer (1.11). k = 1 iddias��� d������t���; b���y���k hacim fark���nda transfer eksik kal���yor. PBE yok. Literat���r (tam metin): k���smen biliniyor; hacim ad���m���, k���r test ve K'/K44 kar������tl��������� bulunamad���. "Hacim transferli regular-solution / kesik tens���rel CE kural���" diye yaz���lmal���, Marker 2017 okunmadan yaz���lmamal���. |
  10: | 2 | **Enerji hacim transferi: D������T���.** Standart Muggianu (saf elementler kendi hacminde) ayn��� i���i yap���yor, 11.4 ile 11.5 meV, kural 13.3 (S2 denetimi, defterde d���zeltme). Eski metin: E_mix hatas��� 36.4  13.1 meV, yaln���z hm_fresh (n 94) ger���ekten k���rd���. Tam hesapta k 0.94 ile 0.98; 0.81 do���rusalla���t���rma etkisi. | L2 (05f01df6ec, d���zeltme d26bd71285) | 1708d0db77, k_direct | Fikrin ���z��� Zunger 1987-89'da biliniyor (`claims/literature.jsonl`). PBE d���zenli h���cre L3'��� FAIL (8541e914ea). |
  11: | 3 | **K44 Co'suz ala������mlarda transfer oluyor** (���n kay���t e410c96a32  d9460850ce, 120 taze ala������m, kazan��� 0.51, p 2.5e-4, k 1.23); Co'lularda olmuyor (kazan��� 0.11). Eski g���zlem: Ayn��� kural K44'te zay���f: kazan��� 0.12 ile 0.20, k 0.69 ile 0.86. En k���t��� hatalar Co'ca zengin ala������mlarda. | g���zlem | LESSONS 14 ile 16 | Neden a������k; ba������ms���z denetim yap���lmad���. Ke���if bak��������� (g���r���lm������ 269 sat���r, kay���t de���il): "E_F'de y���ksek DOS" a������klamas��� desteklenmiyor, art���k Pd/Pt/Ni/Rh/Ir/Co oran���yla iki kanalda da benzer b���y���yor (K44/K' rms oran��� 1.15 ile 1.4). En b���y���k hatalar iki kanalda da Co'lu ala������mlarda (|r44| ile Co r 0.33): s���radaki ������pheli Co manyetizmas���. K44'���n hacim kaymas��� da k���������k, kazan��� i���in az yer var (a2: pair 3.56  kural 2.66, K' 5.67  1.80). |
  12: | 3b | **Ortak kayma taban���.** Hacim kural���n���n K44 ve K''te ka������rd��������� k���s���m ayn��� ve kompozisyona ait: K44 - K' kural��� ge���iyor (kazan��� 0.49), h���creler aras��� r 0.75, bilinen ���n gerilme ���zde���li���i ������kar���l���nca r 0.67, k 0.99. K44'���n "tutmamas���" bu tabandan. | L0, ������ ���n kay���tl��� PASS (b86e0d8a40, fd786169e3, ede47f1d65), ��������� de Astra denetimi PLAUSIBLE | `data/k_aniso_s100_clamped.csv`, `k_floor_cells.csv`, `k_floor_stress_*.csv`; LESSONS 20-22 | ���kili referanslardan gelen ortak hata d������lanmad��� (iki ba������ms���z ikili paneli gerekli). Fiziksel anlam��� a������k; MACE only. |
  13: | 4 | **MACE kar���������m kayma e���rili���inde L1'den ge���miyor.** 8 d���zenli L1_2 h���crede K' i���areti 8/8 do���ru, K44 i���areti 5/8 (Au3Ir PBE -32.4, MACE +3.2 GPa); medyan sapma K' i���in %47, K44 i���in %56. K' kural��� yaln���z MACE i���inde g���sterilmi��� say���l���r. | L1 FAIL (b3214734c2, Astra denetimli) | `data/hiso_l12_dft_v2.csv`, `data/hiso_l12_mace.csv` | dense-k ve ecutrho kontrolleri ko���uyor. |
  14: | 5 | **H-iso.** H���cre i���i i���aret okumas���yla PASS (n 6, medyan K44/K' 0.94), tek i���aret okumas���yla FAIL (Pt3Cu pozitif). Ag3Ir 0.54, Ag3Rh 0.39, Pt3Cu 2.61: h���cre baz���nda izotropi yok. | L0, PLAUSIBLE (b3214734c2, sebep numerics, a������k) | `scripts/hiso_l12_v2.py` | 34/78 ko���uda negative rho; ecutrho ���1.5 ve kspacing 0.08 kontrolleri bitince kapan���r. |
  15: 
  16: Yanl������lanan adaylar (A2, H-sm, R3, R3b, HM2-T4, Astra EOS kapan���������) ve gerek���eleri defterde `verdict on ...` kay���tlar���nda.
  17: 
  18: ## ���al������an i���ler
  19: 
  20: - **H-iso kontrolleri (PBE, 2 ���ekirdek, s���ral���):** dense bitti (`data/hiso_l12_dft_v2_dense.csv`, kspacing 0.08). Cu3Ir de���i���medi (K44 -54.75  -54.71, K' -57.39  -57.42). Ag3Rh K' kararl��� (-17.97  -17.44) ama K44 -7.04  -3.64 GPa, oran 0.39  0.21: Ag3Rh K44 k-yak���nsak de���il. Medyan K44/K' 0.942  0.941, i���aretler ayn���, H-iso okumas��� de���i���miyor. rho ko���usu 2 Kas���m 13:43'te reboot ile 8/18'de kesildi; 3 Kas���m 12:35'te devam ettirildi (log `data/hiso_l12_dft_v2_rho_resume1.log`, kalan Rh_t+ ve Pt3Cu, yakla������k 3 saat).
  21: 
  22: ## S���radaki ad���mlar
  23: 
  24: 1. Dense ve rho bitince H-iso'yu kapat: oranlar ve MACE fark��� ���%10 i���inde kal���yorsa verdict b3214734c2'yi kesinle���tir, kalm���yorsa sebep numerics ve yeni ko���u.
  25: 2. K' kural��� i���in PBE (L3). **Tasar���m uyar���s���:** d���zenli 4 atomlu h���creler enerji kural���nda PBE'de +10 meV'lik sabit hacim ���ok cisim terimi ta������d��������� i���in yanl������ test ������kt��� (d440b9eb7b, 8541e914ea). K' i���in de d���zenli h���cre kullan���lacaksa bu ���nce d���������n���lmeli; do���ru alan PBE SQS h���creleri (32 atom ve ���st���) ve bu laptopta g���nler s���rer, kiral���k sunucu se���ene���i var.
  26: 3. PBE h���zland���rma: Cu3Ir'de smearing ve k-a������ gev���etmeyi referansa kar������ test et.
  27: 4. ~~Veri d���zeltmesi~~ yap���ld��� (2 Kas���m): `scripts/fix_counts2.py`  `data/h1_ev_rows_fixed2.csv`, `h3_fresh_rows_fixed2.csv` (44 ������l���de -0.31 ile -0.71 meV, R ve B_chem yeniden). hm3 ve di���erlerinde 1/3 yok, yeni m���h���r gerekmedi. Enerji analizleri bundan sonra `_fixed2` okumal���.
  28: 5. L4 (2 Kas���m): son tarama ve Astra denetimi yap���ld��� (`claims/literature.jsonl` sat���r 63 ve 64, `.orchestra/audits/L4_kprime_astra.md`). Karar PARTIALLY KNOWN, KEEP: kural ortak hacimli ikili regular-solution enerjisinin kayma t���revi, ���zg���l uygulama bulunmad���. Wu 2021 tezi okundu (sat���r 65): ikili EMTO'dan bcc ������l���lere excess C' ve C44 aktar���m��� var, ama her bile���im kendi hacminde; Vegard hacmi ad���m��� yok. L4 taramas��� kapand��� (arama s���n���rl���), en yak���n ���nc���l olarak draft_v5'e eklendi. Yeni risk: Soyemi 2026 ve Chong 2026, kural���n MACE i���inde tutmas���n���n model yanl���l��������� olabilece���ini d���������nd���r���yor; PBE aktar���m testi bu y���zden daha ���nemli.
  29: 5b. Deney verisi (ajan taramas��� 1 Kas���m): bu dokuz elementte ���l������lm������ tek kristal ala������m sabitleri yaln���z kapal��� eri���imde (Cu-Ni Epstein-Carlson 1965, Schmunk-Smith 1960; Cu-Au Chiarodo 1972, dC/dP ile; Pd-Ag Hoare-Yates 1954; Co-Ni Weston-Granato 1975). 3+ bile���enli ���l������m yok. K���t���phane PDF'i gerekli.
  30: 5c. ~~nspin hatas���~~ d���zeltildi (2 Kas���m): `extra={'system.nspin': 1}` art���k ba���lang������ momenti koymuyor, Co girdisinde nspin 1 do���ruland���.
  31: 6. Makale: `paper/draft_v5.md` (v4 art��� model yanl���l��������� s���n���r���, madde 6, ve Soyemi, Chong kaynaklar���; ar���iv hen���z v4 ile). v4: Astra v4 incelemesindeki (`.orchestra/audits/draft_v4_astra.md`) b���t���n kapsam ve say��� d���zeltmeleri uyguland���. Ar���iv `paper/repro_20261102_2.zip` (v4, requirements.txt, manifest do���ru; ar���ivden `chain.py` ve `fix_counts2.py` birebir ���retiyor). G���nderim i���in kalan: yazar���n son okumas���, Zenodo'ya ar���iv y���kleme ve DOI'yi metne yazma, ChemRxiv g���nderimi. Bunlar��� yazar yapar. Dense/rho sonucu gelince 5.1'deki "pending" c���mlesi g���ncellenir.
  32: 
  33: ## Harness haritas���
  34: 
  35: | Par���a | Yer |
  36: |---|---|
  37: | Hesap (MACE, SQS, curvature) | `harness/compute.py`, `harness/context.py` (ikili V_ij, Vegard) |
  38: | PBE | `harness/dft.py` (`Settings(kpts=..., ecut_elements=...)` zorunlu) |
  39: | Defter, ���n kay���t, g������ | `harness/ledger.py`, `harness/power.py` |
  40: | Arena (m���h���rl��� holdout) | `harness/arena.py`, `data/sealed/`, `candidates/` |
  41: | Ajanlar | `scripts/discovery_round.py` (arena turu), `scripts/swarm.py` (cepheler `.orchestra/fronts/`) |
  42: | K' testleri | `scripts/k_shear_transfer.py` (h3), `k_shear_kp_hm.py` (hm_fresh), `k_shear_mpa.py` (model de���i���imi); veri `data/binary_kgrid*.csv`, `data/*_shear_clamped*.csv` |
  43: | Enerji kural��� | `scripts/hm_l2_fixed.py`, `scripts/k_direct.py`, `candidates/champion_volume_transfer.py` |
  44: 
  45: Veri k���meleri: h1 (ke���if, g���r���lm������), h3 (model se���iminde kullan���ld���, K i���in k���rd���), hm_fresh (enerji ve K' i���in k���rd���, art���k g���r���ld���), hm3fix (m���h���rl���, ajanlar g���rmez).

 exited 1 in 256ms:
 130: regs = [e for e in ledger.entries() if e["claim"].startswith("Shear-curvature volume transfer") and "prereg" in e["notes"]]
 131: if not regs:
 132:     if not any(e["claim"].startswith("Design note, shear-curvature transfer") for e in ledger.entries()):
 133:         ledger.record("Design note, shear-curvature transfer: first design (sigma 4 GPa = pair-sum residual on exploratory "
 134:                       "a2 rows) had power 0.45 and was not registered; no h3 target computed. Exploratory a2 (n 62, "
 135:                       "seen): K44 pair 3.56 -> rule 2.66 GPa, Kp 5.67 -> 1.80, refit k 0.90 / 1.05. Redesign: sigma = "
 136:                       f"rule residual on a2 {SIG}, the arena convention", "L0", [SCRIPT, str(BIN)],
 137:                       notes="design; before registration")
 138:     rng = np.random.default_rng(1)
 139:     sim = lambda truth: np.mean([all(test(P[ch][truth] + rng.normal(0, SIG[ch], len(comps)),  # noqa: E731
 140:                                           *P[ch], 1000, i)[0] for ch in P) for i in range(200)])
 141:     power, fp = sim(0), sim(1)
 142:     print(f"n {len(comps)}, power {power:.3f}, false pass {fp:.3f}", flush=True)
 143:     reg = ledger.register(f"Shear-curvature volume transfer: clamped mixing K44 and K' of random fcc alloys equal "
 144:                           f"sum 4 x_i x_j K_ij(V0) with binary curvatures at the alloy volume (no parameter); PASS if "
 145:                           f"in both channels RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005 on {len(comps)} h3_fresh "
 146:                           f"alloys whose K has never been computed", SCRIPT, {"power": power, "false_pass": fp},
 147:                           notes="proposed by Opus in swarm S1 (open front), critiqued by Astra; binaries computed first")
 148:     print("registered", reg["id"], flush=True)
 149:     regs = [reg]
 150: 
 151: # 3. targets
 152: done = set(pd.read_csv(TGT)["comp"]) if TGT.exists() else set()
 153: for s, c in zip(h3.comp_actual, comps):
 154:     if s in done:
 155:         continue
 156:     alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
 157:     x = compute.actual_fractions(alloy)
 158:     assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
 159:     r = {"comp": s, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
 160:          "time": dt.datetime.now().isoformat(timespec="seconds")}
 161:     pd.DataFrame([r]).to_csv(TGT, mode="a", header=not TGT.exists(), index=False)
 162: print("targets done", flush=True)
 163: 
 164: # 4. test
 165: t = pd.read_csv(TGT).set_index("comp").loc[h3.comp_actual]
 166: res = {}
 167: for ch in ("K44", "Kp"):
 168:     y = t[ch].values
 169:     ok, gain, p = test(y, *P[ch])
 170:     rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
 171:     T = P[ch][0] - P[ch][1]
 172:     k = float(T @ (y - P[ch][1]) / (T @ T))
 173:     res[ch] = ok
 174:     print(f"{ch}: raw {rm(y - y.mean()):.2f}, pair at V_ij {rm(y - P[ch][1]):.2f}, rule {rm(y - P[ch][0]):.2f} GPa, "
 175:           f"gain {gain:.2f}, p {p:.1e}, refit k {k:.2f} -> {'pass' if ok else 'fail'}", flush=True)
 176: sl = {}
 177: for ch in ("K44", "Kp"):
 178:     vals = [float(spl[((tuple(k.split('-'))), ch)](0, 1) / spl[((tuple(k.split('-'))), ch)](0))
 179:             for k in g.pair.unique() if abs(spl[((tuple(k.split('-'))), ch)](0)) > 10]
 180:     sl[ch] = (len(vals), float(np.median(vals)) if vals else float("nan"))
 181: print("secondary: median dlnK/dlnV of binaries with |K| > 10 GPa:", sl, flush=True)
 182: passed = all(res.values())
 183: if __name__ == "__main__":  # k_shear_kp_hm.py imports this file for its splines; the h3 result is recorded once
 184:     ledger.record(f"Shear-curvature volume transfer: {'PASS' if passed else 'FAIL'} on {len(comps)} unseen h3 alloys "
 185:               f"(K44 {'pass' if res['K44'] else 'fail'}, Kp {'pass' if res['Kp'] else 'fail'}); binary slope prior {sl}",
 186:               "L0", [str(BIN), str(TGT), SCRIPT], notes=f"prereg {regs[0]['id']}")
   1: """Structure generation, relaxation and elastic constants with a universal ML potential."""
   2: 
   3: from __future__ import annotations
   4: 
   5: import datetime as dt
   6: import os
   7: import time
   8: from functools import lru_cache
   9: 
  10: import numpy as np
  11: from ase import Atoms
  12: from ase.build import bulk
  13: from ase.filters import FrechetCellFilter
  14: from ase.optimize import FIRE
  15: 
  16: from harness.reference import ELASTIC_EXP
  17: 
  18: GPA = 160.21766208  # eV/A^3 -> GPa
  19: MODEL = os.environ.get("HARNESS_MODEL", "medium-omat-0")  # mace_mp foundation model name
  20: 
  21: # Rough lattice parameters (A) for the starting guess only; relaxation sets the real value.
  22: A0 = {"fcc": {"Al": 4.05, "Cu": 3.61, "Ni": 3.52, "Ag": 4.09, "Au": 4.08, "Pd": 3.89,
  23:               "Pt": 3.92, "Co": 3.54, "Fe": 3.59, "Cr": 3.60, "Mn": 3.60},
  24:       "bcc": {"Fe": 2.87, "Cr": 2.88, "Mo": 3.15, "W": 3.16, "V": 3.03, "Nb": 3.30,
  25:               "Ta": 3.30, "Ti": 3.28, "Zr": 3.57, "Hf": 3.50, "Al": 3.24}}
  26: 
  27: 
  28: @lru_cache(maxsize=1)
  29: def calculator():
  30:     from mace.calculators import mace_mp
  31:     import torch
  32:     device = "cuda" if torch.cuda.is_available() else "cpu"
  33:     return mace_mp(model=MODEL, device=device, default_dtype="float64")
  34: 
  35: 
  36: def site_counts(comp: dict[str, float], n: int) -> dict[str, int]:
  37:     counts = {el: int(round(x * n)) for el, x in comp.items()}
  38:     counts[max(counts, key=counts.get)] += n - sum(counts.values())
  39:     return counts
  40: 
  41: 
  42: def actual_fractions(atoms: Atoms) -> dict[str, float]:
  43:     """Composition the cell really has. Subtract pure references with these, not the nominal fractions (the
  44:     rounding to whole atoms shifted E_mix by up to ~57 meV/atom before 2026-10-31)."""
  45:     s = atoms.get_chemical_symbols()
  46:     return {el: s.count(el) / len(s) for el in sorted(set(s))}
  47: 
  48: 
  49: def solid_solution(comp: dict[str, float], lattice: str, reps: int, seed: int) -> Atoms:
  50:     """Random solid solution on a cubic conventional supercell (no SQS optimisation). Counts are rounded to whole
  51:     atoms; use actual_fractions() for references."""
  52:     a = sum(x * A0[lattice].get(el, 3.5 if lattice == "fcc" else 3.1) for el, x in comp.items())
  53:     atoms = bulk("X", lattice, a=a, cubic=True).repeat((reps, reps, reps))
  54:     counts = site_counts(comp, len(atoms))
  55:     symbols = [el for el, c in counts.items() for _ in range(c)]
  56:     np.random.default_rng(seed).shuffle(symbols)
  57:     atoms.set_chemical_symbols(symbols)
  58:     return atoms
  59: 
  60: 
  61: # GPU duty cycle in (0, 1]: after each relaxation sleep so the GPU is busy only this fraction
  62: # of the time. Keeps a laptop from overheating on long scans; results are unaffected.
  63: DUTY = float(os.environ.get("HARNESS_DUTY", "1.0"))
  64: 
  65: 
  66: def relax(atoms: Atoms, cell: bool, fmax: float = 1e-3, steps: int = 400) -> int:
  67:     atoms.calc = calculator()
  68:     target = FrechetCellFilter(atoms) if cell else atoms
  69:     opt = FIRE(target, logfile=None)
  70:     t = time.perf_counter()
  71:     opt.run(fmax=fmax, steps=steps)
  72:     if DUTY < 1:
  73:         time.sleep((time.perf_counter() - t) * (1 / DUTY - 1))
  74:     return opt.nsteps
  75: 
  76: 
  77: def elastic_tensor(atoms: Atoms, eps: float = 0.005, relax_ions: bool = True) -> np.ndarray:
  78:     """Full 6x6 Voigt tensor (GPa) from central differences of stress, ions relaxed at each strain."""
  79:     cell0 = atoms.get_cell().array.copy()
  80:     C = np.zeros((6, 6))
  81:     voigt = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
  82:     for j, (k, l) in enumerate(voigt):
  83:         sig = []
  84:         for s in (+eps, -eps):
  85:             e = np.zeros((3, 3))
  86:             if k == l:
  87:                 e[k, k] = s
  88:             else:
  89:                 e[k, l] = e[l, k] = s / 2  # engineering shear strain = s
  90:             strained = atoms.copy()
  91:             strained.set_cell(cell0 @ (np.eye(3) + e), scale_atoms=True)
  92:             strained.calc = calculator()
  93:             if relax_ions and len(strained) > 1:
  94:                 relax(strained, cell=False, fmax=5e-4)
  95:             sig.append(strained.get_stress(voigt=True) * GPA)  # ASE: tensile stress positive
  96:         C[:, j] = (sig[0] - sig[1]) / (2 * eps)
  97:     return 0.5 * (C + C.T)
  98: 
  99: 
 100: def cubic_average(C: np.ndarray) -> tuple[float, float, float]:
 101:     """Project a (noisy, random alloy) 6x6 tensor onto cubic symmetry."""
 102:     c11 = np.mean([C[0, 0], C[1, 1], C[2, 2]])
 103:     c12 = np.mean([C[0, 1], C[0, 2], C[1, 2]])
 104:     c44 = np.mean([C[3, 3], C[4, 4], C[5, 5]])
 105:     return float(c11), float(c12), float(c44)
 106: 
14:one specific, fixed-coefficient prescription for the clamped mixing part of the tetragonal shear curvature K' of
23:across independent target cells and after removal of the clamped pre-stress, which supports a composition-dependent
24:shared residual, but error shared through the binary references remains an unresolved alternative. Primary tests
33:1. Liu et al. (2010) developed CALPHAD-style models for elastic coefficients, and Marker et al. (2017) applied this
34:   approach to bcc Ti alloys using relaxed first-principles inputs, each at its own equilibrium volume. Marker
38:   including binary and ternary data. Closest to the present test, Wu (2021, Sec. 5.2) fitted pair polynomials to
45:   identify the specific fixed-coefficient transfer tested here: clamped multicomponent mixing K' estimated from
48:3. Formally the rule is a pair-truncated tensorial cluster expansion or a zeroth-order Redlich-Kister sum with a
61:**Observable.** E_mix(V, F) = E_alloy - sum x_i E_i per atom, every pure reference at the same volume and the same
64:the pure references; the historical exploratory a2 dataset is an exception (Section 3.1). With tensile-positive
74:V_ij"), and two own-volume Muggianu analogues built from pure-element curvatures (Section 3.4).
105:k 1.05 (b363c5a618). The quinary rows of this dataset keep nominal-fraction reference errors, so these values are
117:**3.4 Against own-volume Muggianu (exploratory, 270b2a4019).** A direct modulus-level own-volume Muggianu analogue
119:energy-consistent reference conversion that transfers V��K before dividing by the target volume; its errors are 4.49
122:full fitted CALPHAD model of Marker et al. For the mixing energy, the earlier linearised k = 1 transfer gives 13.3
152:- The same cells after subtracting the clamped mixing pre-stress from targets and binaries alike (prereg ede47f1d65):
159:residual may be error carried by the binary references. Independent binary panels for both channels and the stress
168:| Integer-count reference mismatch | R1 audits | up to 56.6 meV/atom in the Al-free set; 60.7 including Al | energy references corrected; historical a2 shear and some derived columns remain uncorrected |
169:| PBE cutoff mismatch | audit, 7e0ff785d1 | 30.7 meV/atom shift in the Pt reference; correction checked to 0.002 meV/atom | alloy-matched cutoffs; the ordered-cell beyond-pair mixing-energy �" calibration changed from FAIL to PASS; this was not a mixing-shear calibration |
176:| Equiatomic ternary reference weight 0.3333 instead of 1/3 in the count correction | Astra, S1 | +0.3 to +0.7 meV/atom on 44 energy rows; stale derived columns | corrected in *_fixed2 tables (scripts/fix_counts2.py); energy rows only, no shear result affected |
182:   A preregistered eight-cell ordered L1_2 A3B check (6cb3c2a936, verdict b3214734c2, audited) compared clamped
193:   binary Muggianu gives C' RMSE 3.08 GPa and a volume-transfer chain 2.52 GPa (gain 0.18, paired sign-flip p approximately 0.073). The chain
202:   different architecture (HIP-NN), and Chong et al. (2026) found a preference for low effective body order in MACE
207:   independently calculated binary and multicomponent DFT curvatures under matched geometric and reference conventions.
254:- Marker, C., Shang, S.-L., Zhao, J.-C., Liu, Z.-K. (2017). Elastic knowledge base of bcc Ti alloys from
263:- Wu, Y. (2021). Explorations of high-entropy alloys and perovskite ceramics from first principles based multiphysics


    Directory: C:\Users\can02\Downloads


Mode                 LastWriteTime         Length Name                                                                 
----                 -------------         ------ ----                                                                 
-a----         3.11.2026     12:49        5360688 etd.pdf                                                              
.orchestra\audits\L4_kprime_prompt.md
.orchestra\audits\L4_kprime_astra.md
rg: scripts/hm_shear*: Dosya ad��, dizin ad�� veya birim etiketi s��zdizimi hatal��. (os error 123)
rg: scripts/k_hm*: Dosya ad��, dizin ad�� veya birim etiketi s��zdizimi hatal��. (os error 123)



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$p='"'C:\\Users\\can02\\.codex\\memories\\MEMORY.md'; "'$t=Get-Content -Encoding UTF8 $p; 147..156 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$t[$_] }; rg --files scripts | rg "hm|shear|asym"; Get-Item .venv/Scripts/python.exe,data/w1_compositions.csv,data/w1_shear_clamped.csv,data/binary_kgrid_asym.csv -ErrorAction SilentlyContinue | Select-Object Name,Length' in C:\Users\can02\Projects\AI driven Science
 exited 1 in 489ms:
148: - A nominal spin-off PBE run can remain spin-polarized because ASE forces `nspin=2` when `magnetize()` leaves nonzero moments, and the cache excludes spin/tag identity. Make spin/tag explicit, zero/skip moments for spin-off, assert `pw.in`, and validate cache/output state before Co spin comparisons. [Task 3]
149: - The energy-residual shared-floor predictor is reproducible but only an L0/UNCLEAR hypothesis: it loses much of its gain with disjoint energy/shear seeds and hm misses the 10% gate against an intercept-only baseline. Keep volume conventions consistent and report Co/Co-free strata separately. [Task 4]
150: 
151: ## Failures and how to do differently
152: 
153: - Strong training RMSE, source splits, power simulations, or clean-ternary diagnostics do not prove a candidate; submit the final answer-format candidate to the authorized sealed arena without inspecting sealed contents, or retain an explicit partial/uncertain status. [Task 1]
154: - Treat Ag shear/electronic mechanisms as hypotheses: cutoff mismatch and strain-dependent k-grid are real control failures but do not explain the anomaly; re-run corrected H-iso data before physical interpretation. Equal additive K44/K' corrections do not preserve Zener anisotropy. [Task 2]
155: - Interpolation or clamped/single-seed results are estimates, not direct pressure/ordering evidence. For small crossings such as Ni3Ir, compare signal to random-cell seed scatter and use enthalpy rather than fixed-volume energies. [Task 2]
156: - Do not import `scripts/k_shear_transfer.py` in a screening script: its top-level code computes and writes data. For the cobalt discriminator, use same-site CoNi and CoRh substitutions in seed>=100 cells, calibrate thresholds to the roughly 0.9 GPa Co/Co-free floor gap, and treat nonspin as an intervention rather than a paramagnetic phase. [Task 3]
157: - Do not present `-14/-7` as universal shared-floor coefficients or count overlapping seed patterns as independent evidence. Use disjoint binary energy/shear inputs and disjoint target E/K seeds, an intercept-only gate, and a preregistered test before promotion. [Task 4]
scripts\a2_shear_clamped.py
scripts\k_shear_transfer.py
scripts\k_shear_mpa.py
scripts\k_shear_kp_hm.py
scripts\hm_l2_fixed.py
scripts\hm_l2.py
scripts\hm_fresh.py
scripts\hm3_holdout.py
scripts\hm2_test.py
scripts\dft_bcc_benchmark.py
scripts\hm_test.py
scripts\hm_ordered.py
scripts\k_asym_w1.py
scripts\__pycache__\k_shear_transfer.cpython-312.pyc
scripts\__pycache__\k_shear_mpa.cpython-312.pyc
scripts\__pycache__\k_shear_kp_hm.cpython-312.pyc

Name       Length
----       ------
python.exe 274424



web search: Yifeng Wu 2021 dissertation excess elastic constants NCSU 5.1 ...
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$p='"'scripts/k_shear_transfer.py'; "'$t=Get-Content $p; 129..($t.Length-1) | ForEach-Object { '"'{0,4}: {1}' -f ("'$_+1),$t[$_] }; $p='"'harness/compute.py'; "'$t=Get-Content $p; 0..90 | ForEach-Object { '"'{0,4}: {1}' -f ("'$_+1),$t[$_] }; $p='"'scripts/k_shear_kp_hm.py'; "'$t=Get-Content $p; 0..($t.Length-1) | ForEach-Object { '"'{0,4}: {1}' -f ("'$_+1),$t[$_] }' in C:\Users\can02\Projects\AI driven Science
 succeeded in 475ms:
 130: regs = [e for e in ledger.entries() if e["claim"].startswith("Shear-curvature volume transfer") and "prereg" in e["notes"]]
 131: if not regs:
 132:     if not any(e["claim"].startswith("Design note, shear-curvature transfer") for e in ledger.entries()):
 133:         ledger.record("Design note, shear-curvature transfer: first design (sigma 4 GPa = pair-sum residual on exploratory "
 134:                       "a2 rows) had power 0.45 and was not registered; no h3 target computed. Exploratory a2 (n 62, "
 135:                       "seen): K44 pair 3.56 -> rule 2.66 GPa, Kp 5.67 -> 1.80, refit k 0.90 / 1.05. Redesign: sigma = "
 136:                       f"rule residual on a2 {SIG}, the arena convention", "L0", [SCRIPT, str(BIN)],
 137:                       notes="design; before registration")
 138:     rng = np.random.default_rng(1)
 139:     sim = lambda truth: np.mean([all(test(P[ch][truth] + rng.normal(0, SIG[ch], len(comps)),  # noqa: E731
 140:                                           *P[ch], 1000, i)[0] for ch in P) for i in range(200)])
 141:     power, fp = sim(0), sim(1)
 142:     print(f"n {len(comps)}, power {power:.3f}, false pass {fp:.3f}", flush=True)
 143:     reg = ledger.register(f"Shear-curvature volume transfer: clamped mixing K44 and K' of random fcc alloys equal "
 144:                           f"sum 4 x_i x_j K_ij(V0) with binary curvatures at the alloy volume (no parameter); PASS if "
 145:                           f"in both channels RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005 on {len(comps)} h3_fresh "
 146:                           f"alloys whose K has never been computed", SCRIPT, {"power": power, "false_pass": fp},
 147:                           notes="proposed by Opus in swarm S1 (open front), critiqued by Astra; binaries computed first")
 148:     print("registered", reg["id"], flush=True)
 149:     regs = [reg]
 150: 
 151: # 3. targets
 152: done = set(pd.read_csv(TGT)["comp"]) if TGT.exists() else set()
 153: for s, c in zip(h3.comp_actual, comps):
 154:     if s in done:
 155:         continue
 156:     alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
 157:     x = compute.actual_fractions(alloy)
 158:     assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
 159:     r = {"comp": s, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
 160:          "time": dt.datetime.now().isoformat(timespec="seconds")}
 161:     pd.DataFrame([r]).to_csv(TGT, mode="a", header=not TGT.exists(), index=False)
 162: print("targets done", flush=True)
 163: 
 164: # 4. test
 165: t = pd.read_csv(TGT).set_index("comp").loc[h3.comp_actual]
 166: res = {}
 167: for ch in ("K44", "Kp"):
 168:     y = t[ch].values
 169:     ok, gain, p = test(y, *P[ch])
 170:     rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
 171:     T = P[ch][0] - P[ch][1]
 172:     k = float(T @ (y - P[ch][1]) / (T @ T))
 173:     res[ch] = ok
 174:     print(f"{ch}: raw {rm(y - y.mean()):.2f}, pair at V_ij {rm(y - P[ch][1]):.2f}, rule {rm(y - P[ch][0]):.2f} GPa, "
 175:           f"gain {gain:.2f}, p {p:.1e}, refit k {k:.2f} -> {'pass' if ok else 'fail'}", flush=True)
 176: sl = {}
 177: for ch in ("K44", "Kp"):
 178:     vals = [float(spl[((tuple(k.split('-'))), ch)](0, 1) / spl[((tuple(k.split('-'))), ch)](0))
 179:             for k in g.pair.unique() if abs(spl[((tuple(k.split('-'))), ch)](0)) > 10]
 180:     sl[ch] = (len(vals), float(np.median(vals)) if vals else float("nan"))
 181: print("secondary: median dlnK/dlnV of binaries with |K| > 10 GPa:", sl, flush=True)
 182: passed = all(res.values())
 183: if __name__ == "__main__":  # k_shear_kp_hm.py imports this file for its splines; the h3 result is recorded once
 184:     ledger.record(f"Shear-curvature volume transfer: {'PASS' if passed else 'FAIL'} on {len(comps)} unseen h3 alloys "
 185:               f"(K44 {'pass' if res['K44'] else 'fail'}, Kp {'pass' if res['Kp'] else 'fail'}); binary slope prior {sl}",
 186:               "L0", [str(BIN), str(TGT), SCRIPT], notes=f"prereg {regs[0]['id']}")
   1: """Structure generation, relaxation and elastic constants with a universal ML potential."""
   2: 
   3: from __future__ import annotations
   4: 
   5: import datetime as dt
   6: import os
   7: import time
   8: from functools import lru_cache
   9: 
  10: import numpy as np
  11: from ase import Atoms
  12: from ase.build import bulk
  13: from ase.filters import FrechetCellFilter
  14: from ase.optimize import FIRE
  15: 
  16: from harness.reference import ELASTIC_EXP
  17: 
  18: GPA = 160.21766208  # eV/A^3 -> GPa
  19: MODEL = os.environ.get("HARNESS_MODEL", "medium-omat-0")  # mace_mp foundation model name
  20: 
  21: # Rough lattice parameters (A) for the starting guess only; relaxation sets the real value.
  22: A0 = {"fcc": {"Al": 4.05, "Cu": 3.61, "Ni": 3.52, "Ag": 4.09, "Au": 4.08, "Pd": 3.89,
  23:               "Pt": 3.92, "Co": 3.54, "Fe": 3.59, "Cr": 3.60, "Mn": 3.60},
  24:       "bcc": {"Fe": 2.87, "Cr": 2.88, "Mo": 3.15, "W": 3.16, "V": 3.03, "Nb": 3.30,
  25:               "Ta": 3.30, "Ti": 3.28, "Zr": 3.57, "Hf": 3.50, "Al": 3.24}}
  26: 
  27: 
  28: @lru_cache(maxsize=1)
  29: def calculator():
  30:     from mace.calculators import mace_mp
  31:     import torch
  32:     device = "cuda" if torch.cuda.is_available() else "cpu"
  33:     return mace_mp(model=MODEL, device=device, default_dtype="float64")
  34: 
  35: 
  36: def site_counts(comp: dict[str, float], n: int) -> dict[str, int]:
  37:     counts = {el: int(round(x * n)) for el, x in comp.items()}
  38:     counts[max(counts, key=counts.get)] += n - sum(counts.values())
  39:     return counts
  40: 
  41: 
  42: def actual_fractions(atoms: Atoms) -> dict[str, float]:
  43:     """Composition the cell really has. Subtract pure references with these, not the nominal fractions (the
  44:     rounding to whole atoms shifted E_mix by up to ~57 meV/atom before 2026-10-31)."""
  45:     s = atoms.get_chemical_symbols()
  46:     return {el: s.count(el) / len(s) for el in sorted(set(s))}
  47: 
  48: 
  49: def solid_solution(comp: dict[str, float], lattice: str, reps: int, seed: int) -> Atoms:
  50:     """Random solid solution on a cubic conventional supercell (no SQS optimisation). Counts are rounded to whole
  51:     atoms; use actual_fractions() for references."""
  52:     a = sum(x * A0[lattice].get(el, 3.5 if lattice == "fcc" else 3.1) for el, x in comp.items())
  53:     atoms = bulk("X", lattice, a=a, cubic=True).repeat((reps, reps, reps))
  54:     counts = site_counts(comp, len(atoms))
  55:     symbols = [el for el, c in counts.items() for _ in range(c)]
  56:     np.random.default_rng(seed).shuffle(symbols)
  57:     atoms.set_chemical_symbols(symbols)
  58:     return atoms
  59: 
  60: 
  61: # GPU duty cycle in (0, 1]: after each relaxation sleep so the GPU is busy only this fraction
  62: # of the time. Keeps a laptop from overheating on long scans; results are unaffected.
  63: DUTY = float(os.environ.get("HARNESS_DUTY", "1.0"))
  64: 
  65: 
  66: def relax(atoms: Atoms, cell: bool, fmax: float = 1e-3, steps: int = 400) -> int:
  67:     atoms.calc = calculator()
  68:     target = FrechetCellFilter(atoms) if cell else atoms
  69:     opt = FIRE(target, logfile=None)
  70:     t = time.perf_counter()
  71:     opt.run(fmax=fmax, steps=steps)
  72:     if DUTY < 1:
  73:         time.sleep((time.perf_counter() - t) * (1 / DUTY - 1))
  74:     return opt.nsteps
  75: 
  76: 
  77: def elastic_tensor(atoms: Atoms, eps: float = 0.005, relax_ions: bool = True) -> np.ndarray:
  78:     """Full 6x6 Voigt tensor (GPa) from central differences of stress, ions relaxed at each strain."""
  79:     cell0 = atoms.get_cell().array.copy()
  80:     C = np.zeros((6, 6))
  81:     voigt = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
  82:     for j, (k, l) in enumerate(voigt):
  83:         sig = []
  84:         for s in (+eps, -eps):
  85:             e = np.zeros((3, 3))
  86:             if k == l:
  87:                 e[k, k] = s
  88:             else:
  89:                 e[k, l] = e[l, k] = s / 2  # engineering shear strain = s
  90:             strained = atoms.copy()
  91:             strained.set_cell(cell0 @ (np.eye(3) + e), scale_atoms=True)
   1: """Fresh blind test of the K' half of shear-curvature volume transfer (follow-up of prereg 4c29d9754c, result 6e0923b413).
   2: 
   3: python scripts/k_shear_kp_hm.py
   4: The joint K44 + K' claim failed on h3 (K' passed, K44 p 0.023). Splitting it after the fact is not allowed
   5: (.orchestra/LESSONS.md 14), so the K' claim gets its own test on alloys whose shear was never computed: hm_fresh rows
   6: with n_el >= 3, minus compositions already in h3 or a2. Same binaries (data/binary_kgrid.csv), same a2 protocol,
   7: references at the cell's actual fractions. PASS: RMSE(rule) <= 0.9 RMSE(pair at V_ij) and sign-flip p < 0.005.
   8: K44 is computed alongside and reported, not gated.
   9: """
  10: 
  11: import datetime as dt
  12: import sys
  13: from pathlib import Path
  14: 
  15: ROOT = Path(__file__).resolve().parent.parent
  16: sys.path.insert(0, str(ROOT))
  17: import importlib.util  # noqa: E402
  18: 
  19: import numpy as np  # noqa: E402
  20: import pandas as pd  # noqa: E402
  21: 
  22: from harness import ledger  # noqa: E402
  23: 
  24: # the binaries, curvature protocol and test come from the h3 script; its sections 1-4 are already done, so loading it
  25: # only rebuilds the splines and reprints the h3 result
  26: spec = importlib.util.spec_from_file_location("kst", ROOT / "scripts" / "k_shear_transfer.py")
  27: kst = importlib.util.module_from_spec(spec)
  28: spec.loader.exec_module(kst)
  29: from harness import compute  # noqa: E402
  30: from harness.features import parse_comp  # noqa: E402
  31: 
  32: ctx, spl, curvatures, test = kst.ctx, kst.spl, kst.curvatures, kst.test
  33: OUT = ROOT / "data" / "hm_shear_clamped.csv"
  34: SCRIPT = str(Path(__file__))
  35: CLAIM = "Shear-curvature volume transfer, K' channel"
  36: 
  37: hm = pd.read_csv(ROOT / "data" / "hm_fresh_rows_fixed.csv")
  38: seen = set(pd.read_csv(ROOT / "data" / "h3_fresh_rows_fixed.csv").comp_actual) | set(
  39:     pd.read_csv(ROOT / "data" / "a2_shear_clamped.csv").comp)
  40: hm = hm[(hm.n_el >= 3) & ~hm.comp_actual.isin(seen)].reset_index(drop=True)
  41: comps = [parse_comp(s) for s in hm.comp_actual]
  42: keep = [all(((a, b), "Kp") in spl for a, b, _, _ in ctx.pairs(c)) for c in comps]
  43: hm, comps = hm[keep].reset_index(drop=True), [c for c, k in zip(comps, keep) if k]
  44: 
  45: 
  46: def predict(c, ch, at_alloy):
  47:     v0 = ctx.vegard(c)
  48:     return sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v0 / ctx.pair[(a, b)]["V"]) if at_alloy else 0.0))
  49:                for a, b, xa, xb in ctx.pairs(c))
  50: 
  51: 
  52: P = {ch: (np.array([predict(c, ch, True) for c in comps]), np.array([predict(c, ch, False) for c in comps]))
  53:      for ch in ("K44", "Kp")}
  54: 
  55: # realistic scatter: the larger of the rule's K' residual on a2 (exploratory) and on h3 (now seen)
  56: h3 = pd.read_csv(kst.TGT).set_index("comp").loc[kst.h3.comp_actual]
  57: SIG = max(kst.SIG["Kp"], float(np.sqrt(np.mean((h3.Kp.values - kst.P["Kp"][0]) ** 2))))
  58: regs = [e for e in ledger.entries() if e["claim"].startswith(CLAIM) and "prereg" in e["notes"]]
  59: if not regs:
  60:     rng = np.random.default_rng(2)
  61:     sim = lambda truth: np.mean([test(P["Kp"][truth] + rng.normal(0, SIG, len(comps)), *P["Kp"], 1000, i)[0]  # noqa: E731
  62:                                  for i in range(300)])
  63:     power, fp = sim(0), sim(1)
  64:     print(f"n {len(comps)}, sigma {SIG:.2f}, power {power:.3f}, false pass {fp:.3f}", flush=True)
  65:     reg = ledger.register(f"{CLAIM}: clamped mixing K' of random fcc alloys equals sum 4 x_i x_j K'_ij(V0) with binary "
  66:                           f"curvatures at the alloy volume (no parameter); PASS if RMSE <= 0.9 x pair-at-V_ij and "
  67:                           f"sign-flip p < 0.005 on {len(comps)} hm_fresh alloys whose shear has never been computed",
  68:                           SCRIPT, {"power": power, "false_pass": fp},
  69:                           notes="fresh test after joint claim 4c29d9754c failed on K44 only (6e0923b413)")
  70:     print("registered", reg["id"], flush=True)
  71:     regs = [reg]
  72: 
  73: done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
  74: for s, c in zip(hm.comp_actual, comps):
  75:     if s in done:
  76:         continue
  77:     alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
  78:     x = compute.actual_fractions(alloy)
  79:     assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
  80:     r = {"comp": s, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
  81:          "time": dt.datetime.now().isoformat(timespec="seconds")}
  82:     pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
  83: print("targets done", flush=True)
  84: 
  85: t = pd.read_csv(OUT).set_index("comp").loc[hm.comp_actual]
  86: rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
  87: out = {}
  88: for ch in ("Kp", "K44"):
  89:     y = t[ch].values
  90:     ok, gain, p = test(y, *P[ch])
  91:     T = P[ch][0] - P[ch][1]
  92:     k = float(T @ (y - P[ch][1]) / (T @ T))
  93:     out[ch] = ok
  94:     print(f"{ch}{'' if ch == 'Kp' else ' (not gated)'}: raw {rm(y - y.mean()):.2f}, pair at V_ij {rm(y - P[ch][1]):.2f}, "
  95:           f"rule {rm(y - P[ch][0]):.2f} GPa, gain {gain:.2f}, p {p:.1e}, refit k {k:.2f}, rule better in "
  96:           f"{int(np.sum(abs(y - P[ch][0]) < abs(y - P[ch][1])))}/{len(y)} -> {'pass' if ok else 'fail'}", flush=True)
  97: ledger.record(f"{CLAIM}: {'PASS' if out['Kp'] else 'FAIL'} on {len(comps)} unseen hm_fresh alloys; K44 reported, "
  98:               f"not gated: {'pass' if out['K44'] else 'fail'}", "L0", [str(OUT), str(kst.BIN), SCRIPT],
  99:               notes=f"prereg {regs[0]['id']}")

web search: 
web search: https://repository.lib.ncsu.edu/bitstreams/0e1628d3-c575-4a34-abb0-dc0a3cfa741f/download
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-Item C:/Users/can02/Downloads/etd.pdf -ErrorAction SilentlyContinue | Select-Object FullName,Length; rg --files | rg -i 'marker|wu|etd|literature|\\.pdf"'$'"'; rg -n \"Marker|Wu|Hume|clamped|pre-stress|stress\" paper/draft_v5.md; ./.venv/Scripts/python -B -c \"import importlib.util; print({m:importlib.util.find_spec(m) is not None for m in ['numpy','scipy','pandas','pypdf','fitz']})\"" in C:\Users\can02\Projects\AI driven Science
 exited 1 in 533ms:

claims\literature.jsonl
14:one specific, fixed-coefficient prescription for the clamped mixing part of the tetragonal shear curvature K' of
23:across independent target cells and after removal of the clamped pre-stress, which supports a composition-dependent
33:1. Liu et al. (2010) developed CALPHAD-style models for elastic coefficients, and Marker et al. (2017) applied this
34:   approach to bcc Ti alloys using relaxed first-principles inputs, each at its own equilibrium volume. Marker
38:   including binary and ternary data. Closest to the present test, Wu (2021, Sec. 5.2) fitted pair polynomials to
45:   identify the specific fixed-coefficient transfer tested here: clamped multicomponent mixing K' estimated from
65:mixing stress and Green-Lagrange energy coefficients, K44 = C^L_xyxy + s_yy and K' = (C^L_xxxx + C^L_yyyy -
67:the stress terms does not give relaxed, zero-pressure elastic constants.
122:full fitted CALPHAD model of Marker et al. For the mixing energy, the earlier linearised k = 1 transfer gives 13.3
152:- The same cells after subtracting the clamped mixing pre-stress from targets and binaries alike (prereg ede47f1d65):
153:  cross-cell r 0.67, k 0.99, b 0.79. The pre-stress is about pair-additive (target rms 7.1 GPa, prediction residual
159:residual may be error carried by the binary references. Independent binary panels for both channels and the stress
182:   A preregistered eight-cell ordered L1_2 A3B check (6cb3c2a936, verdict b3214734c2, audited) compared clamped
254:- Marker, C., Shang, S.-L., Zhao, J.-C., Liu, Z.-K. (2017). Elastic knowledge base of bcc Ti alloys from
263:- Wu, Y. (2021). Explorations of high-entropy alloys and perovskite ceramics from first principles based multiphysics
Unable to create process using '"C:\Users\can02\AppData\Local\Programs\Python\Python312\python.exe" -B -c "import importlib.util; print({m:importlib.util.find_spec(m) is not None for m in ['numpy','scipy','pandas','pypdf','fitz']})"'
FullName                          Length
--------                          ------
C:\Users\can02\Downloads\etd.pdf 5360688



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Command python,python3,py,pdftotext -ErrorAction SilentlyContinue | Select-Object Name,Source; Get-Content .venv/pyvenv.cfg; Get-Item C:/Users/can02/AppData/Local/Programs/Python/Python312/python.exe -ErrorAction SilentlyContinue | Select-Object FullName,Length; $p='"'paper/draft_v5.md'; "'$t=Get-Content $p; 29..82 | ForEach-Object { '"'{0,4}: {1}' -f ("'$_+1),$t[$_] }; rg --files C:/Users/can02/Downloads | rg -i '"'marker|elastic|\\.pdf"'$'"'" in C:\Users\can02\Projects\AI driven Science
 exited 1 in 4977ms:

Name          Source                                        
----          ------                                        
pdftotext.exe C:\Program Files\Git\mingw64\bin\pdftotext.exe
home = C:\Users\can02\AppData\Local\Programs\Python\Python312
include-system-site-packages = false
version = 3.12.10
executable = C:\Users\can02\AppData\Local\Programs\Python\Python312\python.exe
command = C:\Users\can02\AppData\Local\Programs\Python\Python312\python.exe -m venv C:\Users\can02\Projects\AI driven Science\.venv
                                                            
  30: 
  31: ## 1. Introduction
  32: 
  33: 1. Liu et al. (2010) developed CALPHAD-style models for elastic coefficients, and Marker et al. (2017) applied this
  34:    approach to bcc Ti alloys using relaxed first-principles inputs, each at its own equilibrium volume. Marker
  35:    reported average Young's modulus deviations of about 7 GPa with binary parameters and 5 GPa with ternary terms for
  36:    13 multicomponent alloys. Huhn et al. (2014) compared alloy moduli with effective-medium estimates based on pure
  37:    elements. Linton and Aidhy (2023) trained ML models on binaries, and Mirzaee et al. (2024) a CNN on charge densities
  38:    including binary and ternary data. Closest to the present test, Wu (2021, Sec. 5.2) fitted pair polynomials to
  39:    EMTO-CPA binary random solutions and extrapolated the excess C' and C44 to arbitrary bcc refractory ternaries
  40:    (R^2 0.98 and 0.94 against direct calculations), each composition at its own equilibrium volume. These studies
  41:    motivate testing how shear transfers from simpler systems.
  42: 2. Volume-dependent effective cluster interactions (Asta et al. 1992; Geng et al. 2005), the alloy-volume formalism
  43:    for binaries (Ferreira et al. 1987, 1989) and tensorial or strain-dependent cluster expansions (van de
  44:    Walle 2008; Behara et al. 2023, which includes shear strain variables) are established. Our search did not
  45:    identify the specific fixed-coefficient transfer tested here: clamped multicomponent mixing K' estimated from
  46:    equiatomic binary curvatures at the alloy Vegard volume. This is a search-bounded statement, not proof that no
  47:    prior work exists.
  48: 3. Formally the rule is a pair-truncated tensorial cluster expansion or a zeroth-order Redlich-Kister sum with a
  49:    specified evaluation volume. The contribution is this prescription and its tested performance: (i) where the
  50:    binary terms are evaluated, (ii) a preregistered test of that choice, (iii) where it stops working, and (iv) how
  51:    the C44-type shear differs. In a different field, Hofgard et al. (2026) obtained large gains by changing the
  52:    target representation of an ML model while keeping the model. Here the target stays K'_mix; what changes is the
  53:    volume at which unchanged binary inputs are read.
  54: 
  55: ## 2. Methods
  56: 
  57: **Cells.** Random fcc solid solutions in 108-atom cubic supercells (3x3x3), built by randomly shuffling species over
  58: the sites without SQS optimisation. Atoms stay on ideal sites (no ionic or cell relaxation). The volume is fixed at
  59: the composition's Vegard volume V0 from the model's pure-element volumes.
  60: 
  61: **Observable.** E_mix(V, F) = E_alloy - sum x_i E_i per atom, every pure reference at the same volume and the same
  62: deformation F. K' from F = diag(e^t, e^-t, 1), K44 from F = I + g e_x e_y, five amplitudes in [-0.01, 0.01],
  63: quadratic fit, K' = c2/(2V), K44 = 2 c2/V. The target generators use the cell's actual integer-count fractions for
  64: the pure references; the historical exploratory a2 dataset is an exception (Section 3.1). With tensile-positive
  65: mixing stress and Green-Lagrange energy coefficients, K44 = C^L_xyxy + s_yy and K' = (C^L_xxxx + C^L_yyyy -
  66: 2 C^L_xxyy)/4 + (s_xx + s_yy)/2. The elastic part reduces to (C11 - C12)/2 only in the cubic limit, and subtracting
  67: the stress terms does not give relaxed, zero-pressure elastic constants.
  68: 
  69: **Binary inputs.** All 36 equiatomic pairs, 13 log-volume points ln(V/V_ij) in [-0.4, 0.4], cubic spline per pair.
  70: The omat grid uses seeds 0 to 2; the first mpa grid seed 0; the 1200-composition test two three-seed panels (20 to 22,
  71: 23 to 25).
  72: 
  73: **Rule.** K'_mix(alloy) = sum_{i<j} 4 x_i x_j K'_ij(ln V0/V_ij). Baselines: the same sum at ln V0/V_ij = 0 ("pair at
  74: V_ij"), and two own-volume Muggianu analogues built from pure-element curvatures (Section 3.4).
  75: 
  76: **Seeds.** The site permutation of a cell depends only on (seed, n), so cells with equal seed and size share a
  77: permutation field. The original h3 and hm_fresh shear tests used target seed 0 and binary seeds 0 to 2, and the first
  78: mpa model swap used seed 0 for both; these historical tests shared a permutation field between targets and inputs.
  79: After this was found (Section 4) target and binary seeds were separated: the floor tests use target seeds of 100 and
  80: above, and the 1200-composition test uses unique target seeds from 10000 with binary panels 20 to 25. Omat seed-split
  81: checks kept the K' improvement (gain 0.55 to 0.58, k 1.07 to 1.10) but showed sensitivity for K44.
  82: 
  83: **Models.** MACE medium-omat-0 (Batatia et al.), calibrated in this project on 14 cubic metals (fcc B, G MAE about



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "pdftotext -f 55 -l 66 -layout C:/Users/can02/Downloads/etd.pdf -; Get-ChildItem C:/Users/can02/AppData/Local/Programs/Python -ErrorAction SilentlyContinue | Select-Object Name; Get-Command uv,node -ErrorAction SilentlyContinue | Select-Object Name,Source; rg -n 'Marker' claims/literature.jsonl" in C:\Users\can02\Projects\AI driven Science
 succeeded in 3450ms:
ordered B2 crystal structures. A series of binary RSSs are then created with x Ai =x Bi =0, 0.1, 0.2, ��� ��� ��� , 1.
Subtracting the inter-site contributions from their total mixing enthalpies using the set of Ji j s leaves
us the on-site data. These are fed into the ML training processes for the ci jpq s with the constraint that
the mixing enthalpies of elemental phases are null, namely, x Ai =x Bi =0 and 1. The trained Eq. 5.1
is enrolled into the ML testing processes where the ML mixing enthalpies of thousands of ternary
systems are aligned with those from direct DFT calculations. To check the generality of Eq. 5.1, it
has been trained and tested among the palette of 10 commonly used elements in RHEAs, including
Al, Cr, Hf, Mo, Nb, Ta, Ti, V, W, and Zr. The R 2 value is found to be close to 1 for each of Hmix, ,
B , C , and C44 with a small standard deviation of errors. Such high accuracy reinforces the
rationality of assumptions made in the present approach. The results of testing and the values of
ci jk s and Ji j s are summarized in the supplemental materials.

     To obtain ci jpq s and Ji j s, the ML polynomial regression tool is used with the input from ex-
plicit EMTO-CPA calculations of binary alloys. We first calculate the Ji j s that are essentially the
mixing enthalpies of fully ordered B2 structures. A series of binary RSSs are then created with
x Ai =x Bi =0, 0.1, 0.2, ��� ��� ��� , 1. Subtracting the inter-site contributions from their total mixing enthalpies
using the set of Ji j s leaves us the on-site data. These are fed into the training processes for the ci jpq s
with the constraint that the mixing enthalpies of pure elemental phases are null, namely, x Ai =x Bi =0
and 1. The trained formula of Eq. 5.1 is used in the testing processes where the fitted mixing en-
thalpies of thousands of ternary systems are compared with those determined from direct DFT
calculations. To check the generality of Eq. 5.1, it has been trained and tested among the palette of 10
commonly used elements in RHEAs, including Al, Cr, Hf, Mo, Nb, Ta, Ti, V, W, and Zr. The R 2 value is
found to be close to 1 for each of Hmix, , B , C , and C44 with a small standard deviation of
errors. Such high accuracy reinforces the rationality of assumptions made in the present approach.
The results of testing and the values of ci jk s and Ji j s are given in the Supplemental Materials.

     For all the aforementioned EMTO calculations, the Green's functions in EMTO are solved for
16 complex energy points with the basis set including s, p, d, and f states. The screened impurity
model parameter is set to 0.9 for the electrostatic correction to the CPA. The RSS and B2 structures
are constructed with the 1-atom primitive cell and the 2-atom conventional cell of BCC, respectively.
Herein, a 27���27���27 k-point mesh and a 21���21���21 k-point mesh are used for RSS and B2, respectively,
to guarantee the numerical errors smaller than 1 meV/atom. The f electrons of Hf and Ta are counted
to be the valence electrons, and the soft core approximation is adopted. The ground-state total
energy, Wigner-Seitz radius, and bulk modulus are obtained through the fittings of Vinet equation
of state [Vin87; Vin89]. The single-crystal elastic constants are derived by the standard volume-
conserved shearing approach [Vit07b].

     To capture the influences of lattice vibrations on SRO and phase partitioning, the vibrational free
energies of an arbitrary RHEA system are determined by the Debye model, which is advantageous for
fast compositional screening as compared to explicit phonon dispersion calculations, and has been
used for phase stability [Ma15] and magnetoelastic effects [Wu19] in 3d transition metal-based HEAs.
The Debye temperature is physically correlated with the mean sound velocity vm [Vit07b], which

                                                                44
can be calculated through the full ab initio method [Wu19] as long as the elastic stability criteria
are fulfilled [Vit07b]. However, these criteria may be broken in practice as a result of elemental
redistribution. Therefore, without loss of generality, it was determined here using a semi-empirical

approach [Mor88]: vm=0.617 B / where  is the mass density.

The ultimate goal here is to minimize the total mixing free energy Gmix tot by tuning the sublattice

compositions                          and    phase  proportions.                                          Here,  Gmix tot  =H tot mix  -T  Sconf tot  +F tot       with  standard  meanings  of

                                                                                                                                                              vib

the variables at the right-hand side is a weighted sum of individual phases. Sconf tot obeys the Boltzmann

formula, and Fvibtot comes from the Debye model. A Python code that uses the NumPy module

[Har20] is developed to accelerate numerical computations of phase properties and self-organizing

elemental redistribution across sublattices and phases. Specifically, at a given set of temperature

and phase proportions, this code performs iterative intra-phase and inter-phase elemental swaps

until Gmix is minimized. For the AlMo0.5NbTa0.5TiZr RHES, two phases (phase  and phase  )

both with an initial uniform RSS composition are introduced, and the properties of the system are

determined for temperature between 0 K and 2000 K.

5.3 Results and Discussion

1.000 -0.06 500                          T [K]                                                                   Phase                                Sublattice A       Phase 
                                         1000 1500 2000
     -0.12                                                                                                                                                                         Al
                                                       ML 1.00 Sublattice A                                                                                                        Mo
0.75 -0.18                                                      0.75       Number Density Number Density                                                                           Nb
0.50                -0.14 -0.12                                                                                                                                                    Ta
f               -0.18                                           0.50                                                                                                               Ti
    -0.16                                                                                                                                                                          Zr
                       -0.04                                    0.25
0.25 -0.10 -0.08              -0.02
1.00 -0.10                                            DFT 1.00 Sublattice B
0.75                                                            0.75                                                                                  Sublattice B

0.25-0. 0.50 16 -0.08 0.50 0.25
f

             -0.14
                       -0.04

                              -0.02
0.00 -0.06 0.00
                -0.20 -0.16 -0.12 -0.08 -0.04 0.00 0                                                      500 1000 1500                    2000 500 1000 1500 2000
                G                     -  G      [eV/f.u.]                                                         T [K]                                       T [K]
                                 tot       RSS
                                 mix       mix

Figure 5.1 Left: the relative mixing free energy per formula unit as a function of phase  number density
and temperature (top: ML, bottom: DFT). Right: the equilibrium number densities of constituent elements
in the sublattices of each phase as a function of temperature.

     The total mixing free energy per formula unit (f.u.) as a function of the number density of
phase  ( f) and the temperature (T ) is illustrated in Fig. 5.1 (left). To highlight the extent of phase
partitioning, it is taken relative to that of single-phase RSS of the same composition. It can be seen
that there is an apparent convex hull at approximately f=0.6 and T =0 K, giving a reduction of
total mixing free energy by around 0.2 eV/f.u. This convex hull flattens out as the temperature

                                                                                                                 45
increases due to configurational entropy but it remains non-negligible up to 1000 K, suggesting a
strong phase partitioning behavior. The lattice vibrations play an insignificant role on the location
of convex hull with composition, but increase the rate of flattening with temperature. This can be
seen by comparing Fig. 5.1 with Fig. 5.5 where the lattice vibrations are absent.

     The underlying temperature-dependent sublattice compositions in phase  and phase  at the
optimized phase proportions are presented in Fig. 5.1 (right). As T decreases to 1550 K, phase
partitioning emerges, where phase  has exhibits B2 ordering of Al and Zr, and phase  remains
disordered. Based on the compositions of each phase, the predicted phase  and phase  correspond
to the matrix and the precipitate observed in the experiments [Sen16a; Sen18b], respectively. At
1400 K, there is an onset of Mo ordering with Nb and Ta that occurs in phase  . With further
reduction in temperature, ordering is enhanced within both of these phases, but ordering is weaker
in phase  relative to phase .

     The ground-state sublattice compositions in each phase will now be reviewed. Al and Zr fully
segregate into phase  and polarize their distributions. Ti also accumulates in phase  but is equally
distributed on both sublattices. Phase  only contains Mo, Nb, and Ta, where Mo and Ta are polarized
into different sublattices while Nb is evenly distributed across them.

Table 5.1 The experimental and simulational chemical composition, number density, and lattice parame-
ter [���] of each phase.

Al Mo Nb Ta Ti Zr vol. lat.

exp. [Sen16a]  25.9 5.5 14.2 4.0 24.1 25.9 61  3.7 15.6 31.8 21.9 17.2 9.5 39  3.304
                                                                               3.269

sim.  23.8 4.9 13.8 5.3 23.6 28.6 60 3.327
                      8.1 18.3 32.1 18.8 16.7 5.9 40 3.272

     Quantitative comparisons between the simulated results and experimental measurements are
a challenging task, primarily due to the potential sluggish diffusion. This is especially the case for
low temperature alloys as cooling the as-annealed material to room temperature would likely pin
the system at an unknown high-temperature state. To pinpoint the temperature that such a state
corresponds to, standard deviations between the calculated and the measured phase compositions
are minimized, yielding a value of 1330 K. The experimental and simulated chemical composition,
number density, and lattice parameter of each phase are tabulated in Table 5.1. Impressively, these
quantities exhibit little or negligible discrepancies between the simulation and the experiment.
Furthermore, it is worth mentioning that the present RHES was observed to be a single phase at an
annealing temperature of 1673 K [Sen16a], which is also true from Fig. 5.1.

     The coherent B2 matrix and BCC precipitate has an orientation relationship 100BCC//100B2,
{001}BCC//{001}B2. [Jen16] Such sharp coherency would create a strong stress field along specific

                                                                46
Figure 5.2 The full directional dependencies of single-crystal Young's and shear moduli of each phase at
different temperatures.

crystallographic directions due to lattice mismatch or modulus difference, which interacts with the
dislocations and in turn influences the precipitate strengthening. Here, the directional dependencies
of the single-crystal elastic moduli of each phase are calculated according to Grimvall [Gri99b],
and their values at different temperatures are demonstrated in Fig. 5.2. In general, it is found that
phase  is extremely anisotropic while phase  is nearly isotropic. At room temperature (300 K), the
minimum (28.1) and maximum (210.8) Young's modulus of phase  are in parallel with [100] and
[111] directions, respectively, but an opposite trend exists in its shear modulus whose minimum
(13.8) and maximum (90.5) are along [111] and [100], respectively. Phase  is opposite to phase
 for both Y and G : Ymin=217.0 along [111], Ymax=297.1 along [100], Gmin=82.9 along [100], and
Gmax=104.5 along [111]. At 1000 K, the elastic anisotropy of phase  and the elastic isotropy of phase
 persist. Above 1550 K, these phases lose their identities by turning into a uniform single-phase
RSS and the whole alloy becomes moderately anisotropic as a result.

     Polycrystalline elastic moduli are calculated by averaging over the single-crystal values, e.g. the
Hill average [Hil52] where the effective G is calculated as an arithmetic average of the Voigt bound
GV and the Reuss bound GR. The mathematical expressions of these bounds for cubic systems
are given by [Gri99b] GV=(2C +3C44)/5 and GR=5C C44/(2C44+3C ). The Young's modulus of the
polycrystalline material can be calculated as Y =9B G /(3B + G ). The temperature-dependent bulk
modulus, polycrystalline Young's modulus, and shear modulus of phase  and those of phase 
are shown in Fig. 5.3. Clearly, there are dramatic differences between the elastic moduli of  and  ,
which are 80 GPa for B , 140 GPa for Y , and 60 GPa for G at 0 K. All of these difference reduce as T
approaches 1550 K. The difference between the lattice parameters of these phases is insignificant,
consistent with the data in Table 5.1.

     Based on the above, insights into the AlMo0.5NbTa0.5TiZr RHES will now be discussed. The
cuboidal precipitate was observed to be disordered BCC with the scanning transmission electron
microscopy (STEM) technique [Sen16a; Jen16], which instead contains weak ordering of Mo with Nb

                                                                47
200 B [GPa] 110 G [GPa] 270 Y [GPa]

                     
180  95 235

160   80                                      200

140   65                                      165

120   50                                      130

1000                                  35                                  95  500 1000 1500 2000
      500 1000 1500 2000 0                500 1000 1500 2000 0
                                                                                  T [K]
          T [K]                               T [K]

Figure 5.3 The polycrystalline bulk, Young's, and shear moduli of each phase as a function of temperature.
For each quantity, the difference between the two phases is highlighted by a shaded area.

and Ta from the simulation. Since Mo and Nb possess similar atomic masses as tabulated in Table
5.2, further studies with extra sensitivity to these elements are required to confirm this prediction.
The number density of B2 matrix is as large as 60%, which may be the reason for the opposite
superalloy microstructure observed in the RHES as compared to conventional superalloys. Based
on the present simulation, the B2 matrix are elastically much weaker and more anisotropic relative
to those of the precipitates, causing limited ductility at room temperature. Therefore, to address this
issue, the inherent microstructure must be reversed [Mir20] and the elastic properties of the Al and
Zr-enriched phase must be modified. Senkov et al. [Sen18b] studied the compositional variation
effects on the mechanical behaviors of derivative systems, but the parent RHES was still the best
among them. According to the simulated single-crystal and polycrystalline elastic moduli of each
phase, the precipitation hardening in the RHES is likely to be from modulus hardening [Ard85] due
to their substantial differences between the two phases, while the lattice mismatch contribution is
insignificant.

5.4 Conclusions

In summary, an advanced approach combining the mean-field DFT with the ML fitting has been
presented that includes the SRO, phase partitioning, lattice vibrations, and their couplings. Exploit-
ing this approach for the AlMo0.5NbTa0.5TiZr RHES, excellent agreement with the experiment was
found in terms of the chemical compositions, number densities, and lattice parameters of both
matrix and precipitate. The Al and Zr ordering was confirmed to be responsible for the formation
of B2 matrix. Different from the argument made in the experiment, the BCC precipitate contains
weak ordering of Mo with Nb and Ta. The matrix and the precipitate have substantially different
elastic properties, the former of which has small elastic moduli and large anisotropy, while the latter
is elastically strong and nearly isotropic.

                                          48
5.5 Acknowledgements

The authors gratefully acknowledge the University Faculty Scholar program at NCSU and Jonathon
N. Baker for his constructive feedback on the manuscript. The Supplemental Materials present fitted
parameters, specific details on the fitting procedure, and data without vibrational contributions.

                                                                49
5.6 Supplementary Materials

        H  mix [eV/f.u.]                        [a.u.]                                         B [GPa]             C [GPa]    160 R2 = 0C.938 44 [GPa]

    0.8 R 2 = 0.980                     3.4 R 2 = 0.998                                 285 R 2 = 0.997     210 R 2 = 0.983   125
    0.4                                 3.2                                             230                 150

ML  0.0                                 3.0                                             175                 90                90

    -0.4                                2.8                          120                                    30                55
                                                   2.8 3.0  3.2 3.4 = 0.005 6565
    -0.-80.8 -0.4 0.0  0.4 0.8 = 0.031 2.62.6                                                     = .2 029       = .4 909                     = .5 279
                 DFT                                   DFT                                   120 175 230 285-3-030 30 90 150 2102020  55 90 125 160
                                                                                             DFT                DFT
                                                                                                                                          DFT

Figure 5.4 Cross-validations for Hmix [eV],  [a.u.], B [GPa], C [GPa], and C44 [GPa] of arbitrary ternary
systems in the BCC structure.

                       T [K]                                                                 Phase                            Phase 
          0 500 1000 1500 2000
    1.00 -0.08                                     ML 1.00 Sublattice A
                                                                                                                Sublattice A                            Al
       -0.14                                                                                                                                            Mo
                -0                                 Number Density Number Density
    0.75 -0.18 .12 0.75                                                                                                                                 Nb
                                                                                                                                                        Ta
f   0.50                                                                          0.50                                                                  Ti
        -0.16
    0.25 -0.10 0.06                                                               0.25                                                                  Zr

                      -  -0.04   -0.02

    1.00 -0.08 -0.04                               DFT 1.00 Sublattice B                                        Sublattice B
    0.75                                                    0.75
                  -0.12
          -0.16 -0.20
f   -0 0.50 .18 0.50
               -0.14

    0.25 -0.10                   -0.02                                            0.25
    0.00 -0. -0.20 -0.16 -0.12 -0.08 -0.04 0.00 0.00 06 0
               G              -  G      [eV/f.u.]                                       500 1000 1500           2000 500 1000 1500 2000
                         tot       RSS                                                          T [K]                              T [K]
                         mix       mix

Figure 5.5 Left: the relative mixing free energy per formula unit as a function of phase  number density
and temperature (top: ML, bottom: DFT). Right: the equilibrium number densities of constituent elements
in the sublattices of each phase as a function of temperature. The contributions from lattice vibrations are
absent.

                                                                                             50
Table 5.2 Ar [Da] (atomic mass),  [a.u.], B [GPa], C [GPa], and C44 [GPa] of pure Al, Mo, Nb, Ta, Ti, and Zr
in the BCC structure.

                                           Ar                      B  C           C44

                               Al 26.982 3.009 69.3 -6.2 42.7
                               Cr 51.996 2.652 253.6 196.5 108.9
                               Hf 178.49 3.303 97.7 -6.5 87.9
                               Mo 95.95 2.944 248.7 173.9 118.6
                               Nb 92.906 3.080 159.9 74.2 35.8
                               Ta 180.95 3.095 186.9 71.3 99.8
                               Ti 47.867 3.030 103.7 1.2 65.6
                               V 50.942 2.789 177.1 80.6 37.2
                               W 183.84 2.970 294.2 179.7 153.9
                               Zr 91.224 3.325 81.8 8.8 64.1

Table 5.3 The ci jpq s and Ji j of Hmix [eV/atom] for each pair between Al, Mo, Nb, Ta, Ti, and Zr in the BCC
structure.

Al-Mo      ci j11      ci j12      ci j13      ci j21      ci j22         ci j23      ci j31      ci j32      ci j33      Ji j
Al-Nb
Al-Ta  -0.307      -0.216      -0.001      -0.091      -0.215          1.041       0.123      -1.256       0.921       0.069
Al-Ti  -0.247      -0.114       0.025      -0.133      -0.139          0.547       0.005      -0.686       0.741      -0.059
Al-Zr  -0.183      -0.080       0.074      -0.103      -0.154          0.089       0.052      -0.244       0.549       0.044
Mo-Nb  -0.363      -0.165       0.243      -0.198      -0.408         -0.062       0.210      -0.346       1.088      -0.351
Mo-Ta  -0.115       0.015       0.133      -0.130      -0.118         -0.041      -0.012      -0.076       0.345      -0.364
Mo-Ti  -0.055       0.008       0.099      -0.063      -0.091          0.216       0.029      -0.307       0.166      -0.121
Mo-Zr  -0.029       0.030       0.074      -0.059      -0.043          0.444      -0.016      -0.487       0.087      -0.181
Nb-Ta  -0.117       0.156      -0.108      -0.273       0.264         -0.440      -0.537       0.704       0.351      -0.083
Nb-Ti   0.059       0.164      -0.067      -0.105       0.230         -0.212      -0.335       0.443      -0.176       0.039
Nb-Zr   0.000      -0.001      -0.002       0.001       0.001          0.017       0.000      -0.016      -0.001       0.004
Ta-Ti   0.002      -0.015      -0.011       0.018      -0.004          0.043       0.021      -0.046      -0.007       0.022
Ta-Zr   0.027      -0.005      -0.015       0.032       0.010          0.034       0.022      -0.024      -0.080       0.092
Ti-Zr   0.060       0.023      -0.012       0.037       0.036          0.013       0.001       0.022      -0.180       0.051
        0.032      -0.008      -0.026       0.039       0.018          0.025       0.021      -0.006      -0.095       0.163
        0.097       0.053      -0.019       0.044       0.072          0.035      -0.027       0.037      -0.292       0.017

                                                         51
Table 5.4 The ci jpq s and Ji j of  [a.u.] for each pair between Al, Mo, Nb, Ta, Ti, and Zr in the BCC structure.

Al-Mo      ci j11      ci j12      ci j13      ci j21      ci j22      ci j23      ci j31      ci j32      ci j33      Ji j
Al-Nb
Al-Ta  -0.032       0.071      -0.070      -0.103       0.141      -0.088      -0.244       0.229       0.096      -0.062
Al-Ti   0.013       0.070      -0.033      -0.057       0.103      -0.046      -0.161       0.149      -0.039      -0.030
Al-Zr   0.023       0.082      -0.022      -0.059       0.104      -0.045      -0.162       0.148      -0.068      -0.046
Mo-Nb  -0.021       0.048       0.010      -0.069       0.038       0.046      -0.107      -0.008       0.063      -0.050
Mo-Ta   0.034       0.016       0.010       0.018       0.006       0.077       0.012      -0.071      -0.101      -0.006
Mo-Ti  -0.014       0.006       0.035      -0.020      -0.029      -0.209       0.009       0.180       0.041      -0.007
Mo-Zr  -0.006      -0.002       0.018      -0.004      -0.020      -0.030       0.016       0.010       0.019      -0.012
Nb-Ta  -0.016      -0.008      -0.017      -0.008       0.010       0.058      -0.018      -0.049       0.048      -0.042
Nb-Ti  -0.057      -0.034       0.001      -0.023      -0.035       0.043       0.012      -0.078       0.171      -0.025
Nb-Zr   0.002      -0.004       0.006       0.006      -0.010       0.043       0.016      -0.053      -0.005       0.001
Ta-Ti   0.011      -0.005      -0.005       0.017      -0.000       0.061       0.017      -0.061      -0.034      -0.015
Ta-Zr  -0.017      -0.019      -0.011       0.003      -0.008       0.108       0.011      -0.117       0.051      -0.006
Ti-Zr   0.018       0.001      -0.011       0.016       0.012       0.046       0.004      -0.034      -0.053      -0.014
       -0.031      -0.024      -0.001      -0.007      -0.023       0.029       0.016      -0.052       0.094      -0.003
        0.006       0.004      -0.003       0.002       0.007       0.007      -0.005      -0.001      -0.017       0.005

Table 5.5 The ci jpq s and Ji j of B [GPa] for each pair between Al, Mo, Nb, Ta, Ti, and Zr in the BCC structure.

Al-Mo    ci j11      ci j12      ci j13      ci j21      ci j22        ci j23    ci j31        ci j32    ci j33     Ji j
Al-Nb
Al-Ta   14.8        -5.8       -18.6        20.6        12.8        -70.7        7.8         83.5      -44.4      11.8
Al-Ti   11.7        -7.9        -6.9        19.6        -1.0        -59.5       20.6         58.5      -35.2      25.9
Al-Zr   -0.8       -21.2                    20.4         1.0                    19.4          -1.6                31.5
Mo-Nb   18.4        -2.4       -22.2        20.8        23.6           2.6      -2.8                     2.4      25.6
Mo-Ta               -4.4       -26.0                   -18.6         18.0       24.5           5.6     -55.1      26.0
Mo-Ti    1.5       -10.1        14.2         5.9        -9.0        -63.6       13.5         45.0
Mo-Zr   -5.6         8.6                     4.5        -2.7         27.4       -8.8        -36.4       -4.5       0.8
Nb-Ta   -2.9       -28.5        -1.1       -11.4       -36.5       -198.0       54.7        195.4       16.7       1.8
Nb-Ti  -10.4       -12.9        11.2        18.2       -38.7        151.9       22.5       -188.4                -10.5
Nb-Zr  -29.1        12.2                   -16.2       -20.1         21.0                   -59.6        8.6     -24.6
Ta-Ti   -3.3         2.0         8.0       -15.5         7.3       -140.3        4.6        120.2       31.1       0.5
Ta-Zr   -1.3        11.8        25.8        -3.3        -5.0        -25.7      -10.6         33.1       87.4      -2.2
Ti-Zr   -7.3         1.3        32.3       -19.1        13.2       -155.5      -14.2        150.5       10.0      -7.6
        -0.2         3.8        -5.3        -1.5       -11.9        -10.2      -14.7         23.4                 -3.7
       -10.2         2.1        16.8       -14.0        -3.9        -76.4                    64.4        3.8      -9.4
        -4.8                   -11.9        -6.9                    -18.3       -2.1         14.4       21.9      -2.6
                                15.7                                            -3.0
                                                                                                         0.6
                                 6.0                                                                    30.5
                                                                                                        14.5

                                                       52
Table 5.6 The ci jpq s and Ji j of C [GPa] for each pair between Al, Mo, Nb, Ta, Ti, and Zr in the BCC struc-
ture.

Al-Mo      ci j11    ci j12      ci j13    ci j21      ci j22      ci j23    ci j31      ci j32      ci j33     Ji j
Al-Nb
Al-Ta   -59.9      -33.2      -54.4      -26.8       21.2      -238.9      -48.0      260.2       179.8      -19.9
Al-Ti    39.0       22.7        -4.9      16.3       27.6      -123.5      -11.3      151.2      -117.1      -38.7
Al-Zr    39.8       -2.3                  42.1       71.5                  -29.3                 -119.5      -40.1
Mo-Nb    62.5       17.9      -73.8       44.6      107.8        71.4      -63.2         0.1     -187.5
Mo-Ta    44.1       -2.2      -89.9       46.3       51.9       127.7                 -19.9      -132.3       -4.5
Mo-Ti   -64.4      -80.0      -54.1       15.6       20.3                    -5.5                 193.1      -10.3
Mo-Zr   -93.0      -55.2     -100.3      -37.8     -104.4        58.6        -4.7       -6.8      279.0       71.2
Nb-Ta   -65.4      -84.7       49.2       19.3     -170.1        59.5       66.6      -39.2       196.3       66.6
Nb-Ti  -100.6      -89.9       85.4      -10.7     -158.4      -501.2      189.4      396.8       301.7       28.0
Nb-Zr   -49.3      -24.7       68.5      -24.7      -29.6       336.5      147.7     -506.6       148.0       28.0
Ta-Ti   -14.7       -3.2                 -11.5      -16.5       197.1         4.9    -355.5                   36.8
Ta-Zr   -34.9      -13.7         4.9     -21.2      -31.7       -14.8         5.0     -14.8        44.1       18.3
Ti-Zr   -22.3      -11.1       13.2      -11.1      -13.4       -14.2       10.5                  104.6       17.2
        -34.9      -10.5       18.0      -24.4      -25.9       -20.3         2.2       -2.3                  16.6
          -9.5      -4.7                  -4.7        -5.7        -6.7        1.5     -11.3        66.8       13.4
                                 2.2                            -27.5         0.9                 104.6
                               15.5                               -2.8                  -6.7                   7.1
                                                                                         1.5       28.5
                                 0.9                                                    -2.8

Table 5.7 The ci jpq s and Ji j of C44 [GPa] for each pair between Al, Mo, Nb, Ta, Ti, and Zr in the BCC struc-
ture.

       ci j11 ci j12 ci j13 ci j21 ci j22 ci j23 ci j31 ci j32 ci j33 Ji j

Al-Mo  2.5 -47.6 -124.7 50.2 77.1 -129.9 -26.9 207.0 -7.6 64.5

Al-Nb  96.8 38.7 -10.8 58.1 49.5 -117.9 8.7 167.4 -290.4 30.4

Al-Ta  64.1 -41.7 -185.9 105.8 144.2 241.0 -38.4 -96.8 -192.4 30.4

Al-Ti  56.1 2.9 -102.0 53.2 104.8 68.3 -51.6 36.5 -168.3 44.3

Al-Zr  14.5 -30.0 -48.1 44.5 18.1 -53.4 26.4 71.5 -43.4 27.6

Mo-Nb -63.5 -62.0 -30.8 -1.5 -31.2 -24.1 29.7 -7.1 190.4 37.9

Mo-Ta -127.9 -71.4 90.7 -56.4 -162.2 -390.1 105.7 228.0 383.7 42.3

Mo-Ti -97.8 -68.8 29.0 -28.9 -97.8 292.9 68.8 -390.7 293.3 10.6

Mo-Zr -130.0 -87.5 37.0 -42.5 -124.4 203.9 81.9 -328.3 390.0 14.6

Nb-Ta -36.8 -20.4            4.4 -16.4 -24.8 -16.3 8.4 -8.6 110.4 33.6

Nb-Ti  -7.7 -6.6 12.0 -1.2 -18.6 23.9 17.5 -42.5 23.2 19.5

Nb-Zr -45.9 -32.5            9.8 -13.4 -42.3 14.8 28.9 -57.1 137.7 25.4

Ta-Ti  -45.1 -19.2 13.3 -25.9 -32.5 13.7 6.6 -46.2 135.2 34.3

Ta-Zr  -79.7 -36.0           6.1 -43.8 -42.1 -15.0 -1.7 -27.1 239.2 32.5

Ti-Zr  -31.6 -23.7 -0.4 -7.9 -23.3 -33.6 15.3 10.4 94.8 30.9

                                                   53
                                           CHAPTER

                            6

    INFLUENCE OF SPACE CHARGE ON
CONDUCTIVITY OF NANOCRYSTALLINE

                        SRTIO3

Reproduced with minor edits from Journal of Applied Physics 128, 014101, 2020. [Wu19] Contribut-
ing authors: Yifeng Wu, Preston C. Bowes, Jonathon N. Baker, and Douglas L. Irving.

     A grand canonical multiscale space-charge model has been developed to study and predict the
electrical properties of polycrystalline perovskites with complex defect chemistries. This model
combines accurate data from hybrid exchange-correlation functional density functional theory
calculations (defect formation energies, resultant grand canonical calculations of defect concentra-
tions, and ionization states) with finite-element simulation of the electric field and its coupling to
defect redistribution and reionization throughout the grain. This model was used to simulate the
evolution of the oxygen partial pressure-dependent conductivity of polycrystalline acceptor-doped
strontium titanate as grain size decreases, and the results were compared to previous experiments.
These results demonstrate that as the grain size is reduced from microscale to nanoscale, the ex-
perimentally observed disappearance of ionic conductivity and forward shift of the oxygen partial
pressure of the n-p crossover are successfully reproduced and explained by the model. Mechanisti-
cally, the changes to conductivity stem from the charge transfer from the grain boundary core into
the grain interior, forming a space charge layer near the grain boundary core that perturbs the local
defect chemistry. The impact of grain size on the electrical conductivity and the underlying defect

                                                                54
chemistry across the grain are discussed. In addition to the findings herein, the model itself enables
exploration of the electrical response of polycrystalline semiconductor systems with complex defect
chemistries, which is critical to the design of future electronic components.

6.1 Introduction

Strontium titanate, or STO, is a prototypical perovskite material that has a wide indirect bandgap of
3.25 eV [VB01] and a high room-temperature dielectric constant of 300 [Sam66]. STO and its alloys
have a wide range of current commercial uses (substrates for thin-film growth [Low96; Izy07; Hui09],
varistors [Kub15; Uen03; Wan08], and capacitors [Bur72; Kis03; Was89]) and also exhibit promise
in a number of next-generation applications (sensors [Ger91; Fer07; Men99; Hu04], memristors
[Szo06; Fle16], and fuel cells [Mar02; Tao03; RM06]). There has been much work recently to refine
the models for the property-processing relationships in single crystal STO so as to understand the
roles of doping strategies and processing environment on the emergent properties of the point
defect ensemble. [Bak17; Bow18; Bak18a; Bak18b; Bow20b] However, STO polycrystals are typically
used instead of single crystals in many applications, due to cost and partial mitigation of long-term
degradation behavior, among other factors. Therefore, it is critical that models capture the influence
of microstructure to facilitate understanding and exploitation of structure-property-processing
relationships when engineering the electrical response of this material system.

     Previous models have been used to explore the development of space charge (SC) in the vicinity of
grain boundaries (GBs) in electroceramics [Vol94; Mai95; Vol97; Hag98; Kna00; Tul00; Tsc01; Guo01b;
Guo03; Bal07; DS09; Lup10; Cao19; DS19] but explicit simulation of the grain size dependency of
the electrical conductivity has been limited, especially for nanocrystals. [Tul00; Tsc01; Guo01b;
Guo03; Lup10] Addressing these issues requires the combination of the emerging paradigm of
coupled grand canonical thermodynamics and high fidelity hybrid exchange-correlation functional
density functional theory (DFT) calculations with multiscale simulations. Such a model would
self-consistently capture the behavior changes with space when the ensemble of defects interacts
with the electric field and extended defects within the polycrystalline materials. Assessing the results
from and the validity of approximations made in such a model is also a challenge without the
available experimental measurements. Fortunately, a recent article by Lupetin, Gregori, and Maier
[Lup10] collected relevant measurements across grain size and processing conditions, against which
such a model can be tested. In doing so, new mechanistic insights have been obtained into how the
SC layer near the GB core behaves as grain size is altered, how it interacts with the defect ensemble
in the grain interior, and how dopant segregation can change the effective doping level in some
conditions. The elemental segregation predicted from the present model is consistent with a series
of experiments, such as the Al and Sr vacancy segregation examined by Chiang & Takagi [Chi90] and
Mizoguchi et al. [Miz05], respectively.

     This paper is organized as follows: The details of the multiscale SC model developed for this
study are described first. Then the evolution of electrical conductivity of a simulated acceptor-

                                                                55

34:{"time": "2026-10-31T22:33:03", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), full-text check", "prior": "PARTIALLY KNOWN", "refs": ["Marker, Shang, Zhao, Liu CMS 140 121 (2017): Redlich-Kister c_ij from binaries/ternaries to Ti alloys; abstract only, closest algebraic precedent, READ BEFORE WRITING", "van de Walle Nat Mater 7 455 (2008) via arXiv 0906.1608 (full): tensorial CE, no volume dependence, no excess part", "Linton & Aidhy APL ML 1 016109 (2023), full: ML on binaries predicts HEA Cij, NiCuAuPdPt, no volume step", "Mirzaee ... Aidhy APL ML 2 046104 (2024), full: C44 transfers worst (R2 0.75), unexplained", "Huhn, Widom PRB 89 104103 (2014), full: binary averaging for moduli, shear transfers worse than bulk", "Asta et al PRB 46 5055 (1992), abstract: volume-dependent ECIs, bulk modulus only", "Geng, Sluiter, Chen PRB 72 014204 (2005), full: volume-dependent ECIs for EOS", "Behara, Van der Ven arXiv 2310.20085, full: strain-dependent CE formalism, Si-Ge only", "Li ... Vitos arXiv 1803.04178, full: volumetric vs electronic split of dC'/dc, dC44/dc, bcc dilute", "Malica & Dal Corso arXiv 2109.00459, full: Fermi-surface term affects C44 of Pd, Pt, not C'"], "verdict": "KEEP, wording restricted", "why": "Not found: excess clamped C' curvature as binary sum with binaries at the alloy Vegard volume, blind test, and the C' vs C44 contrast. Known: binary-to-HEA elastic extrapolation (Redlich-Kister, averaging, ML), volume-dependent interactions, C44 hardest to transfer. Write as pair-truncated tensorial CE / regular-solution rule with volume transfer, not a new law; k model-dependent (1.08 omat, 1.33 mpa). Lead for K44 failure: high DOS at E_F (Pd, Pt, Ni, Rh, Ir, Co) gives non-pair C44 term; test: does K44 additivity recover in Cu/Ag/Au-only alloys."}
38:{"round": "S2/k44", "candidate": "opus_2", "prior": "UNCLEAR", "refs": ["data/binary_kgrid.csv", "data/binary_kgrid_mpa.csv", "data/{a2,h3,hm}_shear_clamped.csv", "data/hm_shear_clamped_mpa.csv", "data/k44_cofree_clamped.csv", "scripts/k_shear_transfer.py", "claims/claims.jsonl:c75e865217", "[van de Walle 2008](https://www.nature.com/articles/nmat2200)", "[Marker ve di�Yerleri 2017](https://doi.org/10.1016/j.commatsci.2017.08.037)"], "verdict": "KEEP", "why": "Omat ile s��n��rl��, s��nanabilir ampirik aday olarak KEEP. G��rǬlen Ǭ�� sette kazan��lar 0.485/0.470/0.414 ve k=0.915/0.963/0.873 yeniden Ǭretildi. Tamamlanm��Y 60 Co sat��r��nda RMSE 3.400��'2.075 GPa, kazan�� 0.390, k=0.833; 100000 i�Yaret ��evirme ��rneklemesiyle p�%^0.0006. Ana ��ng��rǬler kar�Y��lan��yor. Mpa'da k=0.482 ve kazan��=-0.030: model-genel fizik yasas�� de�Yil. Ortak katk��n��n farkta iptali matematiksel olarak do�Yru, fakat kalan hatan��n yaln��z konfigǬrasyon gǬrǬltǬsǬ oldu�Yu g��sterilmedi; ikili seed sa����l��m�� ��ok bile�Yenli hedefin hata taban�� yerine ge��mez. GǬ�� hesab��ndaki 1.00/0.00, varsay��lan Gauss gǬrǬltǬsǬne ko�Yullu sonlu simǬlasyon oranlar��d��r. Defter kayd�� dosya zaman��na g��re k��r ��ng��rǬyǬ bildiriyor fakat ledger ��n kayd�� olmad��Y��n�� a����k��a s��ylǬyor; bu yǬzden kay��tl�� L2 ba�Yar��s�� say��lmaz. Tens��rel cluster expansion ve alt sistemlerden elastik ��zellik ekstrapolasyonu biliniyor; tam olarak bu hacim aktar��lm��Y K44�^'K' kural��n��n ��nceli�Yi do�Yrulanamad��."}
42:{"round": "S2/open", "candidate": "opus_2", "prior": "UNCLEAR", "refs": ["data/scan_fcc_omat.csv", "data/scan_fcc_omat_pure.csv", "harness/compute.py:77", ".orchestra/swarm/S2/open/opus.md �?" belirtilen scratchpad/chain.py, chain_vs_mug.csv ve relax_soft.py", "[Marker vd. 2017: elastik ��zelliklerin CALPHAD modellemesi](https://doi.org/10.1016/j.commatsci.2017.08.037)"], "verdict": "DROP", "why": "Mevcut mekanizma ve genelleme iddias��yla DROP; Muggianu kontrol modeli korunmal��. �o��lǬlerde C' i��in 2.525/3.075, C44 i��in 3.501/3.670 GPa chain/Muggianu hatalar��n�� do�Yrulad��m; ba�Y��ms��z Muggianu hesab�� dosyayla ��rtǬ�YǬyor. Fakat P=0 yaln��z hidrostatik enerji tǬrevini s��f��rlar; dC/dlnV veya dC/dP s��f��rlanmak zorunda de�Yildir. Dolay��s��yla hacim etkisinin yaln��z ikinci mertebeye kald��Y�� ����kar��m�� ge��ersiz. N_ij do�Yrudan ayn�� hǬcrede ��l��ǬlmǬ�Y iyonik yumu�Yama de�Yil, modellenmi�Y clamped de�Yer ile relakse hedefin fark��d��r; model ve konfigǬrasyon hatalar��n�� da i��erir. Chain ayr��ca ��l��ǬlmǬ�Y hedef hacmi kullan��yor. p�%^0.08/0.32, kazanc��n %20�?tden kǬ��Ǭk oldu�Yunu kan��tlayan e�Yde�Yerlik testi de�Yildir. Elastik CALPHAD modellemesi biliniyor; bu fcc kǬmesine ��zgǬ hata s��n��r�� ve s��f��r-bas��n�� genellemesi i��in do�Yrudan ��ncǬl do�Yrulanmad��Y��ndan UNCLEAR."}
48:{"time": "2026-11-01T00:32:50", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), Marker 2017 full text (accepted manuscript, 45 pp, read in full)", "prior": "DIFFERENT: Marker is our own-volume Muggianu baseline", "refs": ["Marker, Shang, Zhao, Liu, Comput Mater Sci 140 121 (2017), doi 10.1016/j.commatsci.2017.08.037", "Liu, Zhang, Ganeshan, Wang, Mathaudhu, Scr Mater 63 686 (2010): origin of CALPHAD modelling of c_ij (Marker ref 25)"], "verdict": "KEEP", "why": "Eq 14: c_ij(x) = sum x_A c_A + sum x_A x_B [L0 + L1 (x_A - x_B)] + sum x_A x_B x_C L2, fitted separately to C11, C12, C44 (not C') of fully relaxed PBE SQS (16-64 atoms), bcc Ti-X-Y (X,Y = Mo, Nb, Sn, Ta, Zr). Every input is at its own equilibrium volume; no volume or strain dependence of L anywhere; no excess/clamped decomposition. Only Ti-X binaries exist, so X0.5Y0.5 ends are off (e.g. Nb-Zr, Mo-Zr C11 and C44 by 20-40 GPa), which they attribute to missing non-Ti binaries; ternary L2 hardly helps (Janz-Schmid-Fetzer). Validation: Young's modulus of 13 multicomponent Ti alloys vs experiment, avg deviation 7 GPa binary-only, 5 GPa with L2; no blind or pre-registered test. Consequence for us: Marker's method is exactly the own-volume Muggianu baseline our rule beats (5.7 -> 1.9 GPa on hm_fresh); cite as the standard practice, not as prior art for the volume prescription."}
63:{"time": "2026-11-02T13:48:50", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), L4 final search", "prior": "NOT FOUND as stated; ingredients known; new interpretive risk (MLIP binary-to-ternary interpolation)", "queries": ["semantic: predicting elastic constants or shear modulus of multicomponent HEAs from binary subsystem contributions evaluated at the alloy volume", "semantic: excess elastic constants of mixing, volume dependence of interaction parameters for shear modulus, CALPHAD elastic constants pressure", "semantic (2024+): MLIP elastic constants random solid solution transferability from binary to ternary/quaternary", "semantic: second derivative of mixing energy w.r.t. shear strain; deviation from linear interpolation", "semantic: ternary/higher-order elastic constants extrapolated from binary data, geometric extrapolation at fixed volume", "semantic (2017+): CALPHAD-type modelling of C11 C12 C44 of multicomponent alloys from binary/ternary parameters", "semantic (2023+): why universal MLIPs predict multicomponent properties from binary interactions; body order of MACE", "abstract FTS batch: Redlich-Kister elastic | CALPHAD elastic constants | excess elastic constants | binary interaction elastic constants ternary | elastic constants Muggianu | shear modulus binary subsystems (mostly off-topic hits)"], "refs": ["Soyemi, Barros, Germann, Nebgen, Hamilton, arXiv 2610.38876 (2026): MLIP trained on unary+binary data transfers to ternary/quaternary by interaction interpolation", "Chong et al. (Ceriotti), arXiv 2509.14146, J Chem Phys (2026): effective body order of MLIPs", "Behara, Thomas, Puchala, Van der Ven, arXiv 2310.20085 (2023): strain-dependent cluster expansion, binary Si-Ge, no multicomponent transfer", "Vazquez et al., Acta Mater (2022) doi 10.1016/j.actamat.2022.117924: SISSO descriptors trained on binary/ternary DFT Cij for Nb-Mo-Ta-W-V, no volume step", "Bijjala, Atlas, Kumar, arXiv 2501.00127: DFPT Cij of refractory binaries, data only", "Temesi et al., Materials 17 2728 (2024): G from valence and radius by rule of mixtures", "Lin et al., arXiv 2404.19098 (2024): CALPHAD of ideal shear strength in dilute Ni alloys (already DROP-checked, entry 34)", "Fan et al., Mater Horiz 12 9160 (2025): NN/LR decoupled CALPHAD energies, not elastic curvature", "Du et al., arXiv 2610.09837 (2026): uMLIP errors in multicomponent materials, compression-side errors larger", "Prior entries 31, 33, 47 (Marker 2017 full text, van de Walle 2008, Linton & Aidhy 2023, Asta 1992) still the closest precedents"], "verdict": "KEEP, wording restricted", "why": "No paper found that reads binary shear-mixing curvatures at the alloy's Vegard volume to predict multicomponent K'. Closest algebra remains Marker 2017 (own-volume Redlich-Kister on Cij = our baseline). New risk: Soyemi 2026 and Chong 2026 show MLIPs interpolate binary interactions into higher-order systems, so a binary-to-multicomponent rule that holds inside MACE may partly reflect the model's effective low body order. This strengthens the case for a PBE transfer test before any physical claim, and the discussion should cite it. Search was Valency only (arXiv, PubMed, ChemRxiv); Web of Science, Scopus and CALPHAD journal full texts not covered."}
64:{"time": "2026-11-02T13:54:53", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), L4 audit of line 63", "prior": "PARTIALLY KNOWN (Astra): rule is the shear derivative of a common-volume binary regular-solution energy; specific application not found", "refs": [".orchestra/audits/L4_kprime_astra.md", "Wu, NC State dissertation (2021), repository.lib.ncsu.edu/items/c6af26ab-ea68-422e-bad0-c180581ad176, Sec 5.2 Eq 5.1: multicomponent excess C' and C44 from binary EMTO data. NOT YET READ: repository behind bot check; common-volume step unknown", "Ghosh & Olson, Acta Mater (2002) doi 10.1016/S1359-6454(02)00096-4 [Astra-cited]: superposition model for isotropic shear modulus of Fe-base solutions", "Myhill, Contrib Mineral Petrol (2017) doi 10.1007/s00410-017-1436-z: common-volume Helmholtz mixing model for elastic properties (minerals)", "Ferreira, Wei, Zunger PRB 40 3197 (1989); Behara et al. arXiv 2310.20085"], "verdict": "KEEP, wording restricted; L4 NOT closed", "why": "Corrections to line 63: (a) Soyemi uses HIP-NN, not MACE, and chemical component count is not atomic body order, so the line-63 wording 'MLIPs interpolate binary interactions' overgeneralises; the risk is a plausible alternative explanation, not a shown mechanism. (b) Line 63 cited entries 31, 33, 47 by 0-based index; the 1-based file lines are 32, 34, 48. (c) Marker 2017 relaxes structures to their own ground state; our own-volume baseline is an analogue, not a reproduction. L4 stays open until the Wu thesis Sec 5.2 is read in full. Paper draft_v5 limitation 6 added from the audit's suggested paragraph."}
65:{"time": "2026-11-03T12:50:43", "candidate": "K' shear-curvature volume transfer (L2 697c2d6d75), Wu 2021 thesis read (closes L4 open item from line 64)", "prior": "PARTIALLY KNOWN: binary-to-multicomponent excess C' and C44 known (Marker 2017, Wu 2021); Vegard-volume evaluation step not found", "refs": ["Wu, Yifeng, PhD dissertation, North Carolina State University (2021), Ch. 5, pp. 43-53, read in full from author-supplied PDF (C:/Users/can02/Downloads/etd.pdf, all rights reserved, not archived)"], "verdict": "KEEP, wording restricted; L4 search closed as search-bounded", "why": "Eq. 5.1 is a pair model (on-site polynomial c_ij^pq plus inter-site J_ij, many-body neglected) for excess properties relative to Hume-Rothery sums, explicitly applied to dC' and dC44. Coefficients fitted to EMTO-CPA binary bcc random solutions at x=0,0.1,...,1; each composition's B and Cij come from its own Vinet equilibrium with volume-conserving shears, so no common or Vegard volume step. Validated on arbitrary bcc ternaries: C' R2 0.983 sigma 4.9 GPa, C44 R2 0.938 sigma 5.3 GPa (Fig 5.4). Elements Al Cr Hf Mo Nb Ta Ti V W Zr; no overlap with our fcc set. It is an own-volume binary transfer, i.e. the same class as our baseline, and must be cited as the closest precedent. Our contribution narrows to the evaluation-volume prescription for clamped fcc K' and its preregistered test. Added to draft_v5 Introduction item 1 and references."}
Name     Source                          
----     ------                          
node.exe C:\Program Files\nodejs\node.exe



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-ChildItem C:/Users/can02/AppData/Local, C:/ProgramData, C:/Users/can02/.local -Directory -ErrorAction SilentlyContinue | Where-Object Name -Match 'python|uv|conda|program|share' | Select-Object FullName; rg --files C:/Users/can02/.local C:/Users/can02/AppData/Roaming/uv C:/Users/can02/AppData/Local/uv C:/ProgramData/miniconda3 -g python.exe -g uv.exe 2>"'$null; pdftotext -f 54 -l 55 -layout C:/Users/can02/Downloads/etd.pdf -' in C:\Users\can02\Projects\AI driven Science
 succeeded in 532ms:

been a systematic and efficient way to adding the couplings of vibrational free energies. A previous
study [Wid14] implemented ab initio molecular dynamics combined with the Monte Carlo. While it
is a comprehensive approach, it comes with a more significant computational cost that may limit
its use in rapid compositional screening.

     In this work, we introduce an approach that utilizes explicit EMTO-CPA calculations and condi-
tional polynomial regressions (a standard machine learning (ML) tool) to train mean-field expres-
sions for mixing enthalpies, Wigner-Seitz radius, and elastic constants of all possible binary alloys
of elements common to RHEAs. Approximate mean-field expressions for higher order systems with
arbitrary compositions are extrapolated using the trained coefficients. This approach is adopted
here to predict the phase (BCC or B2) proportions, SRO in each phase, and resultant properties
of AlMo0.5NbTa0.5TiZr. Excellent agreement with the experiments was found regarding the com-
positions, phase proportions, and lattice parameters of both phases. Several insights beyond the
experimental observations were also found. First, it is confirmed that Al and Zr ordering is critical
to form the B2 matrix. Second, the BCC precipitate shows weak Mo ordering with Nb and Ta. Last
but not least, the B2 matrix has not only smaller elastic constants but it also has substantially larger
elastic anisotropy with respect to the precipitate.

5.2 Methods

In a mean-field crystal, a given lattice site can be occupied by more than one element with different
probabilities of occurrence, i.e. number densities. Therfore, elemental site probabilities are not only
influenced by neighboring lattice sites but also on-site contributions. Assuming that the many-body
interactions are minor contributions, the mixing enthalpy of the system would consist of an on-site
and inter-site component, each of which involves contributions from all possible chemical pair
interactions. In order to quantify the on-site and inter-site components, the inter-site component is
presumed to follow the semi-empirical Miedema's macroscopic model [Mie81], while the on-site
component is described by a polynomial regression model. Moving along this logic, the mixing
enthalpy per atom of the conventional 2-atom BCC crystal can be expressed ash shown in Eq. 5.1.

             2Hmix       (���  ���  ���  ,  xiA  ,  ���  ���  ���  ,  x  A  ,  ���  ���  ���  ,  xiB  ,  ���  ���  ���  ,  x  B  ,  ���  ���  ���  )  =
                                                             j                                        j

                                ci jp q (xiA )p (x jA )q + ci jp q (xiB )p (x jB )q + 2 Ji j xiA x jB                      (5.1)

             i j ,i > j  pq                                                    pq

In Eq. 5.1, x Ai is the number density of element i in sublattice A. x Aj , x Bi , and x Bj have similar
meanings. ci jpq s are the on-site interaction coefficients and Ji j is the inter-site interaction coefficient
between i and j . In fact, Eq. 5.1 is valid for all properties that rely on chemical interactions, e.g. the

excessive Wigner-Seitz radius , bulk modulus B , single-crystal elastic constants C and C44,

etc. relative to the Hume-Rothery sums.
     To obtain ci jpq s and Ji j s, the ML polynomial regression toolbox is invoked with the input from

EMTO-CPA calculations. We first calculate the Ji j s which are essentially the mixing enthalpies of fully

                                                                               43
ordered B2 crystal structures. A series of binary RSSs are then created with x Ai =x Bi =0, 0.1, 0.2, ��� ��� ��� , 1.
Subtracting the inter-site contributions from their total mixing enthalpies using the set of Ji j s leaves
us the on-site data. These are fed into the ML training processes for the ci jpq s with the constraint that
the mixing enthalpies of elemental phases are null, namely, x Ai =x Bi =0 and 1. The trained Eq. 5.1
is enrolled into the ML testing processes where the ML mixing enthalpies of thousands of ternary
systems are aligned with those from direct DFT calculations. To check the generality of Eq. 5.1, it
has been trained and tested among the palette of 10 commonly used elements in RHEAs, including
Al, Cr, Hf, Mo, Nb, Ta, Ti, V, W, and Zr. The R 2 value is found to be close to 1 for each of Hmix, ,
B , C , and C44 with a small standard deviation of errors. Such high accuracy reinforces the
rationality of assumptions made in the present approach. The results of testing and the values of
ci jk s and Ji j s are summarized in the supplemental materials.

     To obtain ci jpq s and Ji j s, the ML polynomial regression tool is used with the input from ex-
plicit EMTO-CPA calculations of binary alloys. We first calculate the Ji j s that are essentially the
mixing enthalpies of fully ordered B2 structures. A series of binary RSSs are then created with
x Ai =x Bi =0, 0.1, 0.2, ��� ��� ��� , 1. Subtracting the inter-site contributions from their total mixing enthalpies
using the set of Ji j s leaves us the on-site data. These are fed into the training processes for the ci jpq s
with the constraint that the mixing enthalpies of pure elemental phases are null, namely, x Ai =x Bi =0
and 1. The trained formula of Eq. 5.1 is used in the testing processes where the fitted mixing en-
thalpies of thousands of ternary systems are compared with those determined from direct DFT
calculations. To check the generality of Eq. 5.1, it has been trained and tested among the palette of 10
commonly used elements in RHEAs, including Al, Cr, Hf, Mo, Nb, Ta, Ti, V, W, and Zr. The R 2 value is
found to be close to 1 for each of Hmix, , B , C , and C44 with a small standard deviation of
errors. Such high accuracy reinforces the rationality of assumptions made in the present approach.
The results of testing and the values of ci jk s and Ji j s are given in the Supplemental Materials.

     For all the aforementioned EMTO calculations, the Green's functions in EMTO are solved for
16 complex energy points with the basis set including s, p, d, and f states. The screened impurity
model parameter is set to 0.9 for the electrostatic correction to the CPA. The RSS and B2 structures
are constructed with the 1-atom primitive cell and the 2-atom conventional cell of BCC, respectively.
Herein, a 27���27���27 k-point mesh and a 21���21���21 k-point mesh are used for RSS and B2, respectively,
to guarantee the numerical errors smaller than 1 meV/atom. The f electrons of Hf and Ta are counted
to be the valence electrons, and the soft core approximation is adopted. The ground-state total
energy, Wigner-Seitz radius, and bulk modulus are obtained through the fittings of Vinet equation
of state [Vin87; Vin89]. The single-crystal elastic constants are derived by the standard volume-
conserved shearing approach [Vit07b].

     To capture the influences of lattice vibrations on SRO and phase partitioning, the vibrational free
energies of an arbitrary RHEA system are determined by the Debye model, which is advantageous for
fast compositional screening as compared to explicit phonon dispersion calculations, and has been
used for phase stability [Ma15] and magnetoelastic effects [Wu19] in 3d transition metal-based HEAs.
The Debye temperature is physically correlated with the mean sound velocity vm [Vit07b], which

                                                                44
FullName                                       
--------                                       
C:\Users\can02\AppData\Local\conda             
C:\Users\can02\AppData\Local\conda-anaconda-tos
C:\Users\can02\AppData\Local\Programs          
C:\Users\can02\AppData\Local\uv                
C:\ProgramData\USOShared                       
C:\Users\can02\.local\share                    



web search: 
web search: "Elastic knowledge base" Marker pdf ...
codex
GǬ�� hesab��nda da ��nemli bir uyumsuzluk var: hm hedefleri seed 0 ile Ǭretilmi�Y, dolay��s��yla gǬrǬltǬ tahmini ikili girdilerle ortak seed kullanan eski testten geliyor. W1�?tin seed 100 se��imi bu s��z��nt��y�� gideriyor, fakat 80 hedefin hepsinde ayn�� seed�?tin kullan��lmas�� sat��rlar aras��nda ba�Y��ml��l��k riski b��rak��yor. Wu�?tnun ��zgǬn tezindeki y��ntemi de okudum; Ǭ�� noktal�� RK modeli ancak s��n��rl�� bir analog olarak sunulabilir.

web search: 
web search: https://www.osti.gov/servlets/purl/1462702
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command "Get-ChildItem C:/Users/can02 -Directory -Force | Where-Object Name -Match 'conda|python|uv'; Get-ChildItem C:/Users/can02/AppData/Local/uv -Force -ErrorAction SilentlyContinue | Select-Object Name; Get-Content data/scan_fcc_omat_pure.csv -TotalCount 15; Get-Content data/binary_kgrid.csv -TotalCount 4; Get-Item data/binary_kgrid.csv,data/hm_shear_clamped.csv | Select-Object Name,Length" in C:\Users\can02\Projects\AI driven Science
 succeeded in 491ms:
Get-ChildItem : 'C:\Users\can02' yoluna eri���im reddedildi.
At line:2 char:1
+ Get-ChildItem C:/Users/can02 -Directory -Force | Where-Object Name -M ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\Users\can02:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand
 
formula,comp,lattice,natoms,seed,model,vol_per_atom,a_eff,relax_steps,cubic_spread,C11,C12,C44,time,B,G,E,nu,pugh,cauchy,zener,el
Ni4,Ni:1.0000,fcc,4,0,medium-omat-0,10.92074197468201,3.5218488452326864,13,1.095569688286899e-13,280.61433282249305,168.77756976661377,124.78295431302875,2026-10-30T14:34:31,206.0564907852402,90.41887912911963,236.64313992087708,0.308593637745425,2.278910032615956,43.99461545358501,2.2315194199724986,Ni
Cu4,Cu:1.0000,fcc,4,0,medium-omat-0,11.991099263282468,3.6333424238608667,30,1.405838335779906e-13,168.0025358218953,121.01239153357562,75.09695925217237,2026-10-30T14:34:34,136.67577296301553,47.216494808319254,127.02229441035695,0.34510508378500365,2.894661569391511,45.915432281403255,3.1962855355964166,Cu
Pd4,Pd:1.0000,fcc,4,0,medium-omat-0,15.351033412517511,3.94517133938984,13,4.9699739028243254e-14,185.90109911600925,144.2946384415743,70.91167958381673,2026-10-30T14:34:37,158.16345866638596,43.49185415214353,119.52031379642071,0.3740540168546718,3.6366225756459443,73.38295885775757,3.408685979742005,Pd
Pt4,Pt:1.0000,fcc,4,0,medium-omat-0,15.527451675555266,3.9602268070240547,21,1.118214085183768e-13,288.6719725837192,228.7753835412926,67.73645282743767,2026-10-30T14:34:40,248.74091322210145,48.81870702951912,137.4631327383066,0.4078940338914241,5.095196664501904,161.03893071385494,2.2617799747981597,Pt
Ag4,Ag:1.0000,fcc,4,0,medium-omat-0,17.840925109818457,4.147876214129697,5,1.616166448731835e-13,112.1099858006578,81.97999793145748,43.303228214372375,2026-10-30T14:34:41,92.02332722119093,28.377938262972968,77.1983946988286,0.3601832871621209,3.242777060420254,38.6767697170851,2.8744271920957587,Ag
Au4,Au:1.0000,fcc,4,0,medium-omat-0,17.920056075815886,4.153999614413019,25,2.2314773485250702e-13,160.30671151377345,131.011185033473,29.310384382771343,2026-10-30T14:34:45,140.77636052690647,22.18762950139258,63.24046513548601,0.42512892446479694,6.3448130192579075,101.70080065070165,2.001014346165165,Au
Al4,Al:1.0000,fcc,4,0,medium-omat-0,16.410446749313255,4.033915517450497,19,7.267221779888226e-13,105.72994761150709,50.51149588166774,32.66617356778958,2026-10-30T14:34:47,68.91764645828086,30.53983327254447,79.82797233987796,0.3069483979738009,2.2566477637007374,17.845322313878164,1.183161517371455,Al
Rh4,Rh:1.0000,fcc,4,0,medium-omat-0,13.890889916682202,3.8158973814458803,51,9.54002095479854e-14,429.5549984236652,201.73384991911846,202.88408394291477,2026-10-30T14:34:52,277.6742327539674,160.94047009892313,404.643961453133,0.25712308782376475,1.7253226151464145,-1.1502340237963153,1.781082092463121,Rh
Ir4,Ir:1.0000,fcc,4,0,medium-omat-0,14.310425195523056,3.853933143243623,28,1.0786645757558362e-13,630.1291989891391,269.6652516767145,277.71823060616293,2026-10-30T14:34:56,389.819900780856,233.52167169759574,583.9582543157651,0.25032989458891713,1.6693093105536787,-8.052978929448443,1.5408932442581085,Ir
Co4,Co:1.0000,fcc,4,0,medium-omat-0,10.874016237580149,3.5168187767249437,25,2.604108491574032e-14,292.5000303172557,169.2120751038531,148.09668059613875,2026-10-30T14:34:59,210.3080601749873,104.19486326714247,268.2792369897726,0.28739185684201374,2.018411019320444,21.115394507714342,2.402451729202484,Co
pair,seed,dlnV,V,K44,Kp
Ag-Au,0,-0.4,11.985651277317022,8.523430390840046,1.9362738616052462
Ag-Au,0,-0.3,13.246193225887012,6.83273983768061,0.09415509585070463
Ag-Au,0,-0.2,14.639307528460971,5.9475727374990885,2.6990438579393303

Name                 Length
----                 ------
binary_kgrid.csv      98994
hm_shear_clamped.csv  10814



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$grid=Import-Csv data/binary_kgrid.csv; $grid | Group-Object pair | ForEach-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Group.seed | Select-Object -Unique) -join '"',');min=("'$_.Group.dlnV | ForEach-Object {[double]$_} | Measure-Object -Minimum).Minimum;max=($_.Group.dlnV | ForEach-Object {[double]$_} | Measure-Object -Maximum).Maximum} } | Format-Table -AutoSize; Get-Content harness/features.py -TotalCount 50; rg -n '"'W1|w1' claims/claims.jsonl" in C:\Users\can02\Projects\AI driven Science
 exited 1 in 925ms:
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
Cannot convert value to type "System.Management.Automation.LanguagePrimitives+InternalPSCustomObject". Only core types 
are supported in this language mode.
At line:2 char:86
+ ... ch-Object { [pscustomobject]@{pair=$_.Name;n=$_.Count;seeds=(($_.Grou ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : ConversionSupportedOnlyToCoreTypes
 
"""Composition descriptors used by baselines and by the discovery search."""

from __future__ import annotations

import numpy as np
from pymatgen.core import Element

R = 8.314462618  # J/(mol K)


def parse_comp(s: str) -> dict[str, float]:
    return {el: float(x) for el, x in (p.split(":") for p in s.split(";"))}


def elem(el: str) -> dict[str, float]:
    e = Element(el)
    vec = e.group if e.group <= 12 else e.group - 10  # valence electron count, transition metal convention
    return {"r": float(e.atomic_radius_calculated or e.atomic_radius),
            "chi": float(e.X), "vec": float(vec), "mass": float(e.atomic_mass),
            "tm": float(e.melting_point)}


def descriptors(comp: dict[str, float]) -> dict[str, float]:
    els = list(comp)
    c = np.array([comp[e] for e in els])
    p = {k: np.array([elem(e)[k] for e in els]) for k in ("r", "chi", "vec", "tm")}
    rbar = c @ p["r"]
    return {"n_el": len(els),
            "S_mix": -R * float(c @ np.log(c)),
            "delta_r": float(np.sqrt(c @ (1 - p["r"] / rbar) ** 2)),
            "d_chi": float(np.sqrt(c @ (p["chi"] - c @ p["chi"]) ** 2)),
            "vec": float(c @ p["vec"]),
            "tm_mix": float(c @ p["tm"])}


def misfit(comp: dict[str, float], vols: dict[str, float], v_alloy: float) -> dict[str, float]:
    """Vegard deviation and the volume misfit sum used by Varvenne-Curtin.

    vols: per-atom volume of each pure element in the alloy's lattice, from the same potential.
    Apparent misfit volume uses the Vegard approximation dV_n = V_n - V_alloy.
    """
    c = np.array([comp[e] for e in comp])
    v = np.array([vols[e] for e in comp])
    dv = v - v_alloy
    return {"vegard_dev": float(v_alloy - c @ v) / v_alloy,
            "misfit_sum": float(c @ dv**2) / v_alloy**2}


def mismatch(comp: dict[str, float], pure: dict[str, float]) -> float:
    """Concentration weighted RMS mismatch of a pure element property, e.g. shear modulus.

web search: 
web search: https://www.osti.gov/servlets/purl/1462702
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content data/scan_fcc_omat_pure.csv -Raw' in C:\Users\can02\Projects\AI driven Science
 succeeded in 371ms:
formula,comp,lattice,natoms,seed,model,vol_per_atom,a_eff,relax_steps,cubic_spread,C11,C12,C44,time,B,G,E,nu,pugh,cauchy,zener,el
Ni4,Ni:1.0000,fcc,4,0,medium-omat-0,10.92074197468201,3.5218488452326864,13,1.095569688286899e-13,280.61433282249305,168.77756976661377,124.78295431302875,2026-10-30T14:34:31,206.0564907852402,90.41887912911963,236.64313992087708,0.308593637745425,2.278910032615956,43.99461545358501,2.2315194199724986,Ni
Cu4,Cu:1.0000,fcc,4,0,medium-omat-0,11.991099263282468,3.6333424238608667,30,1.405838335779906e-13,168.0025358218953,121.01239153357562,75.09695925217237,2026-10-30T14:34:34,136.67577296301553,47.216494808319254,127.02229441035695,0.34510508378500365,2.894661569391511,45.915432281403255,3.1962855355964166,Cu
Pd4,Pd:1.0000,fcc,4,0,medium-omat-0,15.351033412517511,3.94517133938984,13,4.9699739028243254e-14,185.90109911600925,144.2946384415743,70.91167958381673,2026-10-30T14:34:37,158.16345866638596,43.49185415214353,119.52031379642071,0.3740540168546718,3.6366225756459443,73.38295885775757,3.408685979742005,Pd
Pt4,Pt:1.0000,fcc,4,0,medium-omat-0,15.527451675555266,3.9602268070240547,21,1.118214085183768e-13,288.6719725837192,228.7753835412926,67.73645282743767,2026-10-30T14:34:40,248.74091322210145,48.81870702951912,137.4631327383066,0.4078940338914241,5.095196664501904,161.03893071385494,2.2617799747981597,Pt
Ag4,Ag:1.0000,fcc,4,0,medium-omat-0,17.840925109818457,4.147876214129697,5,1.616166448731835e-13,112.1099858006578,81.97999793145748,43.303228214372375,2026-10-30T14:34:41,92.02332722119093,28.377938262972968,77.1983946988286,0.3601832871621209,3.242777060420254,38.6767697170851,2.8744271920957587,Ag
Au4,Au:1.0000,fcc,4,0,medium-omat-0,17.920056075815886,4.153999614413019,25,2.2314773485250702e-13,160.30671151377345,131.011185033473,29.310384382771343,2026-10-30T14:34:45,140.77636052690647,22.18762950139258,63.24046513548601,0.42512892446479694,6.3448130192579075,101.70080065070165,2.001014346165165,Au
Al4,Al:1.0000,fcc,4,0,medium-omat-0,16.410446749313255,4.033915517450497,19,7.267221779888226e-13,105.72994761150709,50.51149588166774,32.66617356778958,2026-10-30T14:34:47,68.91764645828086,30.53983327254447,79.82797233987796,0.3069483979738009,2.2566477637007374,17.845322313878164,1.183161517371455,Al
Rh4,Rh:1.0000,fcc,4,0,medium-omat-0,13.890889916682202,3.8158973814458803,51,9.54002095479854e-14,429.5549984236652,201.73384991911846,202.88408394291477,2026-10-30T14:34:52,277.6742327539674,160.94047009892313,404.643961453133,0.25712308782376475,1.7253226151464145,-1.1502340237963153,1.781082092463121,Rh
Ir4,Ir:1.0000,fcc,4,0,medium-omat-0,14.310425195523056,3.853933143243623,28,1.0786645757558362e-13,630.1291989891391,269.6652516767145,277.71823060616293,2026-10-30T14:34:56,389.819900780856,233.52167169759574,583.9582543157651,0.25032989458891713,1.6693093105536787,-8.052978929448443,1.5408932442581085,Ir
Co4,Co:1.0000,fcc,4,0,medium-omat-0,10.874016237580149,3.5168187767249437,25,2.604108491574032e-14,292.5000303172557,169.2120751038531,148.09668059613875,2026-10-30T14:34:59,210.3080601749873,104.19486326714247,268.2792369897726,0.28739185684201374,2.018411019320444,21.115394507714342,2.402451729202484,Co


exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content data/binary_kgrid.csv -Raw' in C:\Users\can02\Projects\AI driven Science
 succeeded in 395ms:
pair,seed,dlnV,V,K44,Kp
Ag-Au,0,-0.4,11.985651277317022,8.523430390840046,1.9362738616052462
Ag-Au,0,-0.3,13.246193225887012,6.83273983768061,0.09415509585070463
Ag-Au,0,-0.2,14.639307528460971,5.9475727374990885,2.6990438579393303
Ag-Au,0,-0.15,15.38988087563095,4.791744756031039,2.1356376618991746
Ag-Au,0,-0.1,16.178936941220954,4.254463373403438,1.9898373827310942
Ag-Au,0,-0.05,17.00844877639591,3.9884879789138323,1.946720865512062
Ag-Au,0,0.0,17.88049059281717,3.42055706783792,1.7798757634797238
Ag-Au,0,0.05,18.797242949252094,3.228817304417029,1.7808857592210035
Ag-Au,0,0.1,19.760998204106734,2.877696119420343,1.5734154289391575
Ag-Au,0,0.15,20.77416624751593,2.6919316802443474,1.3973225282539112
Ag-Au,0,0.2,21.839280527323865,2.43514854318634,1.15149137106347
Ag-Au,0,0.3,24.13613771049413,2.4002578445380953,0.8575641169194845
Ag-Au,0,0.4,26.674557472307054,2.03302977238677,0.7134472384184474
Ag-Au,1,-0.4,11.985651277317022,8.400044223952468,2.254808545871703
Ag-Au,1,-0.3,13.246193225887012,6.67588624484624,0.4482872038349287
Ag-Au,1,-0.2,14.639307528460971,5.776282597009905,2.8583455691456847
Ag-Au,1,-0.15,15.38988087563095,4.6588740904951935,2.2767500291228955
Ag-Au,1,-0.1,16.178936941220954,4.147745122537342,2.123048028973297
Ag-Au,1,-0.05,17.00844877639591,3.837120823045628,2.0792319986674554
Ag-Au,1,0.0,17.88049059281717,3.3005899046626475,1.8842681922670375
Ag-Au,1,0.05,18.797242949252094,3.042102562177649,1.8797155515969928
Ag-Au,1,0.1,19.760998204106734,2.6213645166713233,1.6579547611232113
Ag-Au,1,0.15,20.77416624751593,2.4046190300636563,1.462407068358507
Ag-Au,1,0.2,21.839280527323865,2.1229079355670546,1.195528043137594
Ag-Au,1,0.3,24.13613771049413,2.0603151139911575,0.8502807958698667
Ag-Au,1,0.4,26.674557472307054,1.7372460713693954,0.6547912724291621
Ag-Au,2,-0.4,11.985651277317022,8.432522766019936,1.7866460866998817
Ag-Au,2,-0.3,13.246193225887012,6.798132532539081,0.24997877366951796
Ag-Au,2,-0.2,14.639307528460971,5.811881754187509,2.570481968250618
Ag-Au,2,-0.15,15.38988087563095,4.703967219361489,2.0085070659370072
Ag-Au,2,-0.1,16.178936941220954,4.177497277955075,1.8517790175740367
Ag-Au,2,-0.05,17.00844877639591,3.8630474172011047,1.7930632706069423
Ag-Au,2,0.0,17.88049059281717,3.3989556933766827,1.6436061615487179
Ag-Au,2,0.05,18.797242949252094,3.1841670364982764,1.6442031984365513
Ag-Au,2,0.1,19.760998204106734,2.813834128381473,1.4372416422893122
Ag-Au,2,0.15,20.77416624751593,2.636636727584986,1.2631924605535443
Ag-Au,2,0.2,21.839280527323865,2.3770151910003343,1.017062411331121
Ag-Au,2,0.3,24.13613771049413,2.303486419212112,0.7153120668527495
Ag-Au,2,0.4,26.674557472307054,1.9256470913804766,0.5845910707241538
Ag-Co,0,-0.4,9.624100402949459,-1.2348872865041092,0.695990676526331
Ag-Co,0,-0.3,10.636275877979863,-7.099053787229075,-8.749758128700783
Ag-Co,0,-0.2,11.75490277697287,-1.5248992809963355,-2.4291001114429602
Ag-Co,0,-0.15,12.357589530141839,0.8563728457004546,0.55266699231023
Ag-Co,0,-0.1,12.991176693917087,2.0021018844997314,4.501391514338048
Ag-Co,0,-0.05,13.657248566228867,0.5069792658716432,0.9232744392182411
Ag-Co,0,0.0,14.357470673699304,-0.3584774922270004,-0.002739685202876314
Ag-Co,0,0.05,15.09359393632648,-0.9867453981739474,-0.4348806738875199
Ag-Co,0,0.1,15.867459045696448,-1.0854934355940258,-0.5658879790730131
Ag-Co,0,0.15,16.681001067670962,-0.7910585508159174,-0.4122075001993553
Ag-Co,0,0.2,17.53625428106008,-0.15874931951148216,0.06411785923362738
Ag-Co,0,0.3,19.380558243407176,0.47362688136345155,0.43129565248635576
Ag-Co,0,0.4,21.41882934668487,0.45023252236515143,0.453160576432347
Ag-Co,1,-0.4,9.624100402949459,-1.8355849674869225,-0.9721603196609429
Ag-Co,1,-0.3,10.636275877979863,-8.713853481108579,-9.194404946867175
Ag-Co,1,-0.2,11.75490277697287,-3.5091033801855307,-2.0666227962679966
Ag-Co,1,-0.15,12.357589530141839,-1.11443892261523,0.9667515983584143
Ag-Co,1,-0.1,12.991176693917087,0.10682641744776827,4.801130098849259
Ag-Co,1,-0.05,13.657248566228867,-1.1819886852178954,1.2655852757261943
Ag-Co,1,0.0,14.357470673699304,-1.8315549791556227,0.32719767107938547
Ag-Co,1,0.05,15.09359393632648,-2.2960380208724196,-0.11505376491551365
Ag-Co,1,0.1,15.867459045696448,-2.270806188481157,-0.23998752320960237
Ag-Co,1,0.15,16.681001067670962,-1.875234793909349,-0.07634992843063443
Ag-Co,1,0.2,17.53625428106008,-1.0612035545796876,0.4092764606165694
Ag-Co,1,0.3,19.380558243407176,-0.27354535824943504,0.7892889823223943
Ag-Co,1,0.4,21.41882934668487,-0.24186616490706075,0.7755958979005785
Ag-Co,2,-0.4,9.624100402949459,-0.019836328134875153,0.8455636951130344
Ag-Co,2,-0.3,10.636275877979863,-6.721982469027142,-8.55584251123511
Ag-Co,2,-0.2,11.75490277697287,-1.8025441859764462,-2.31247144245902
Ag-Co,2,-0.15,12.357589530141839,0.4518625377838452,0.5205096925773093
Ag-Co,2,-0.1,12.991176693917087,1.5360369294906824,4.354091574645194
Ag-Co,2,-0.05,13.657248566228867,0.08477084595863547,0.7942919865260074
Ag-Co,2,0.0,14.357470673699304,-0.700217058116415,-0.17412081412144348
Ag-Co,2,0.05,15.09359393632648,-1.2961995125699006,-0.6168873584132318
Ag-Co,2,0.1,15.867459045696448,-1.3842538897692407,-0.7439946749495603
Ag-Co,2,0.15,16.681001067670962,-1.003524384521839,-0.5265353588768928
Ag-Co,2,0.2,17.53625428106008,-0.3360741530104532,-0.050157827968965486
Ag-Co,2,0.3,19.380558243407176,0.3702524789321282,0.42828522666798463
Ag-Co,2,0.4,21.41882934668487,0.40720312544792664,0.5145229499922556
Ag-Cu,0,-0.4,9.998501975556664,-23.570504396624287,-1.8785985624049022
Ag-Cu,0,-0.3,11.050053607707135,-17.194870659436504,-1.716668595725932
Ag-Cu,0,-0.2,12.212197890414814,-11.72826729892468,-0.9934222981686766
Ag-Cu,0,-0.15,12.83833066541735,-9.796101898593651,-1.25452857776691
Ag-Cu,0,-0.1,13.496565954271228,-8.006809409829113,-1.3448196194779223
Ag-Cu,0,-0.05,14.188549688058034,-6.43564336178323,-1.1399896224421098
Ag-Cu,0,0.0,14.916012186550462,-5.220488921678495,-0.9247395764669046
Ag-Cu,0,0.05,15.680772484913042,-4.220843079019845,-0.7677165455991796
Ag-Cu,0,0.1,16.484742882237523,-3.53346501147476,-0.7337263213200531
Ag-Cu,0,0.15,17.329933723286697,-3.0666460857967373,-0.7180736994348027
Ag-Cu,0,0.2,18.21845842540344,-2.445927938830241,-0.621397744797998
Ag-Cu,0,0.3,20.134510423926137,-1.465218162877091,-0.397169847247745
Ag-Cu,0,0.4,22.252075370214147,-0.8861131643022453,-0.22353881045545396
Ag-Cu,1,-0.4,9.998501975556664,-19.584466230337434,-3.540700568701248
Ag-Cu,1,-0.3,11.050053607707135,-14.128374063871684,-2.969717652402929
Ag-Cu,1,-0.2,12.212197890414814,-9.432886176311161,-2.0350967249785397
Ag-Cu,1,-0.15,12.83833066541735,-7.793913376449128,-2.129663346201434
Ag-Cu,1,-0.1,13.496565954271228,-6.291202603525214,-2.068332839787424
Ag-Cu,1,-0.05,14.188549688058034,-4.991703815858694,-1.7421883252494015
Ag-Cu,1,0.0,14.916012186550462,-4.021255432350839,-1.4228030104241767
Ag-Cu,1,0.05,15.680772484913042,-3.207186023295256,-1.179885483203537
Ag-Cu,1,0.1,16.484742882237523,-2.7407979590264278,-1.0602996995688914
Ag-Cu,1,0.15,17.329933723286697,-2.411302641487463,-0.9808094698373722
Ag-Cu,1,0.2,18.21845842540344,-1.8674667012569581,-0.8316479522128154
Ag-Cu,1,0.3,20.134510423926137,-1.1534017161353827,-0.5097807816336474
Ag-Cu,1,0.4,22.252075370214147,-0.7125205947025693,-0.2759718140498414
Ag-Cu,2,-0.4,9.998501975556664,-21.717580644358225,-1.8925025374487086
Ag-Cu,2,-0.3,11.050053607707135,-15.9023048362885,-1.7582498835982252
Ag-Cu,2,-0.2,12.212197890414814,-10.84295010167594,-1.0974960787386672
Ag-Cu,2,-0.15,12.83833066541735,-9.022338842991783,-1.2316493119292207
Ag-Cu,2,-0.1,13.496565954271228,-7.360873122667109,-1.318055224123552
Ag-Cu,2,-0.05,14.188549688058034,-5.905519146443098,-1.1291837022689013
Ag-Cu,2,0.0,14.916012186550462,-4.785344613872991,-0.9162193001005803
Ag-Cu,2,0.05,15.680772484913042,-3.8370050648619607,-0.7623131450308139
Ag-Cu,2,0.1,16.484742882237523,-3.242223731884482,-0.7269909650919292
Ag-Cu,2,0.15,17.329933723286697,-2.819628951084557,-0.7143121715569248
Ag-Cu,2,0.2,18.21845842540344,-2.195480597957874,-0.6212628054680411
Ag-Cu,2,0.3,20.134510423926137,-1.3424669668268885,-0.39170309545559645
Ag-Cu,2,0.4,22.252075370214147,-0.8132251502214757,-0.21499576284753671
Ag-Ir,0,-0.4,10.775847308392244,-23.133259135293393,-83.00760164836812
Ag-Ir,0,-0.3,11.909153062858852,-53.93615964992658,-89.28934706036709
Ag-Ir,0,-0.2,13.161649623983127,-48.44068249882412,-67.54417123438357
Ag-Ir,0,-0.15,13.836461830321827,-36.6431228963861,-41.41174988266926
Ag-Ir,0,-0.1,14.545872398327434,-29.950775921544167,-34.98825987022931
Ag-Ir,0,-0.05,15.29165522393543,-24.54940845861334,-29.200955996377015
Ag-Ir,0,0.0,16.075675152670755,-18.36866077034112,-23.191055529509736
Ag-Ir,0,0.05,16.899892642732993,-10.793685861429744,-16.447465108277974
Ag-Ir,0,0.1,17.766368667163015,-9.541215557484003,-12.972048037499507
Ag-Ir,0,0.15,18.677269867349104,-7.759055366824196,-9.226436347200176
Ag-Ir,0,0.2,19.63487397075897,-4.236535153886224,-5.635005034174954
Ag-Ir,0,0.3,21.699891692563327,1.7741127302274196,-2.387675611194178
Ag-Ir,0,0.4,23.98208922401233,6.474143620517902,-0.9639711207422199
Ag-Ir,1,-0.4,10.775847308392244,-25.75702346123681,-83.19136096581725
Ag-Ir,1,-0.3,11.909153062858852,-57.23590740939006,-88.19621306175718
Ag-Ir,1,-0.2,13.161649623983127,-53.135372289925705,-66.71258989463634
Ag-Ir,1,-0.15,13.836461830321827,-41.317597815401044,-39.798434867999255
Ag-Ir,1,-0.1,14.545872398327434,-34.291188723606034,-33.42911065468347
Ag-Ir,1,-0.05,15.29165522393543,-28.691015535172543,-27.811157964314514
Ag-Ir,1,0.0,16.075675152670755,-22.270311599502108,-21.97471940421335
Ag-Ir,1,0.05,16.899892642732993,-14.110468859509622,-15.22717437411702
Ag-Ir,1,0.1,17.766368667163015,-12.702823525135441,-11.889783571803283
Ag-Ir,1,0.15,18.677269867349104,-10.338698965928753,-8.084807345294504
Ag-Ir,1,0.2,19.63487397075897,-6.318230247698291,-4.404170921809648
Ag-Ir,1,0.3,21.699891692563327,-0.1023433516928308,-1.2543150324655803
Ag-Ir,1,0.4,23.98208922401233,4.940693867286478,0.03075387601353437
Ag-Ir,2,-0.4,10.775847308392244,-17.459292337643088,-80.88933954063404
Ag-Ir,2,-0.3,11.909153062858852,-49.693392519636234,-86.85238028245537
Ag-Ir,2,-0.2,13.161649623983127,-46.321570653004564,-66.01003644581056
Ag-Ir,2,-0.15,13.836461830321827,-34.96762116517772,-39.07312448498367
Ag-Ir,2,-0.1,14.545872398327434,-28.487716863047982,-32.94163376718516
Ag-Ir,2,-0.05,15.29165522393543,-23.42891837112894,-27.483447167118104
Ag-Ir,2,0.0,16.075675152670755,-17.647949476072043,-21.848214574053426
Ag-Ir,2,0.05,16.899892642732993,-10.320289316647107,-15.390632999521463
Ag-Ir,2,0.1,17.766368667163015,-9.282615497965157,-12.126371816987497
Ag-Ir,2,0.15,18.677269867349104,-7.526948058885239,-8.534755291926526
Ag-Ir,2,0.2,19.63487397075897,-4.118382961525831,-5.10015189071934
Ag-Ir,2,0.3,21.699891692563327,1.4648388988619108,-2.1676192302219053
Ag-Ir,2,0.4,23.98208922401233,5.881106070677121,-0.8501509292077886
Ag-Ni,0,-0.4,9.639761002072042,-8.899895514907367,-5.52665088262394
Ag-Ni,0,-0.3,10.653583516689784,-11.389170937581662,-10.944370812602362
Ag-Ni,0,-0.2,11.774030675935634,-6.240337258400163,-7.211611906453585
Ag-Ni,0,-0.15,12.377698137455795,-3.9578208063303215,-2.6616551483353663
Ag-Ni,0,-0.1,13.012316291574622,-0.4219267689615423,7.688251059638802
Ag-Ni,0,-0.05,13.679472014235253,-2.4052255620209917,-0.7182104068562775
Ag-Ni,0,0.0,14.380833542250233,-3.197403835753923,-2.0071503212726465
Ag-Ni,0,0.05,15.118154644762505,-2.886767416363338,-1.6582353903360834
Ag-Ni,0,0.1,15.893279008581759,-1.4737862553174912,-0.7408230829486399
Ag-Ni,0,0.15,16.70814484836179,-1.5096506798320874,-0.6133971474030392
Ag-Ni,0,0.2,17.56478975314672,-0.11187566116705065,0.33203991321327014
Ag-Ni,0,0.3,19.41209481729089,-0.4789378394751549,0.16634123442337448
Ag-Ni,0,0.4,21.453682650996893,0.046714332746797725,0.1295544333484683
Ag-Ni,1,-0.4,9.639761002072042,-5.188029321080746,-7.509795928133263
Ag-Ni,1,-0.3,10.653583516689784,-8.918860281283544,-12.396606801634944
Ag-Ni,1,-0.2,11.774030675935634,-4.65221591250319,-8.08050936199243
Ag-Ni,1,-0.15,12.377698137455795,-2.668051215371412,-3.399715777526191
Ag-Ni,1,-0.1,13.012316291574622,0.6807099463325457,7.270585505761568
Ag-Ni,1,-0.05,13.679472014235253,-1.5542134573122754,-1.0840973965196494
Ag-Ni,1,0.0,14.380833542250233,-2.6173530929820035,-2.2834549615798627
Ag-Ni,1,0.05,15.118154644762505,-2.4829411324018515,-1.8429917380016554
Ag-Ni,1,0.1,15.893279008581759,-1.2065680155691851,-0.832534651285223
Ag-Ni,1,0.15,16.70814484836179,-1.5460475027421419,-0.623334950803632
Ag-Ni,1,0.2,17.56478975314672,-0.1838359295053217,0.35817837313497075
Ag-Ni,1,0.3,19.41209481729089,-0.6472523135494259,0.22332935370928264
Ag-Ni,1,0.4,21.453682650996893,-0.16791361529877766,0.18178461556514325
Ag-Ni,2,-0.4,9.639761002072042,-7.233045893622561,-5.750902984873687
Ag-Ni,2,-0.3,10.653583516689784,-10.178928607061406,-10.896137350074746
Ag-Ni,2,-0.2,11.774030675935634,-5.449540775211011,-7.0484831956245815
Ag-Ni,2,-0.15,12.377698137455795,-3.286269779998056,-2.592178563271748
Ag-Ni,2,-0.1,13.012316291574622,0.10140026477336361,7.450963240848004
Ag-Ni,2,-0.05,13.679472014235253,-1.9051966158029363,-0.6669801717838623
Ag-Ni,2,0.0,14.380833542250233,-2.7566407806079276,-1.9124820379264862
Ag-Ni,2,0.05,15.118154644762505,-2.5230987176674606,-1.5744186891477236
Ag-Ni,2,0.1,15.893279008581759,-1.21715913196453,-0.6793100502011661
Ag-Ni,2,0.15,16.70814484836179,-1.3428414086464595,-0.5261531600014377
Ag-Ni,2,0.2,17.56478975314672,-0.10620051168441509,0.3684036012388182
Ag-Ni,2,0.3,19.41209481729089,-0.5153730287847389,0.15569800558238953
Ag-Ni,2,0.4,21.453682650996893,-0.0829985811905452,0.08632562736220628
Ag-Pd,0,-0.4,11.124617582352638,28.238697943867727,-3.553062827195927
Ag-Pd,0,-0.3,12.294603826729157,19.20395899268179,2.51836811366293
Ag-Pd,0,-0.2,13.58763859856263,12.074269174896575,2.3441755596083627
Ag-Pd,0,-0.15,14.284291726672121,10.953937735863388,4.866976883725856
Ag-Pd,0,-0.1,15.01666302445357,10.095369935369893,5.501095374350757
Ag-Pd,0,-0.05,15.786583801626605,7.519417771326523,5.093010822406915
Ag-Pd,0,0.0,16.595979261167983,8.493455767966319,6.288358355472664
Ag-Pd,0,0.05,17.446873313321824,4.473330863692006,5.007086391212225
Ag-Pd,0,0.1,18.34139363642943,0.5541578872889907,3.31607938721704
Ag-Pd,0,0.15,19.281776997233393,1.5834639020945407,3.7491266482418584
Ag-Pd,0,0.2,20.27037484395955,-0.3363126774470664,2.444435923665261
Ag-Pd,0,0.3,22.402228776036292,0.44146464271704866,1.0528554618623696
Ag-Pd,0,0.4,24.758291743352718,3.838062467424429,1.0036102966982525
Ag-Pd,1,-0.4,11.124617582352638,28.48206351646288,-3.553289447512142
Ag-Pd,1,-0.3,12.294603826729157,19.256273657770105,2.8931371339332044
Ag-Pd,1,-0.2,13.58763859856263,12.066572559065648,2.818765458787873
Ag-Pd,1,-0.15,14.284291726672121,10.88251863368465,5.224697854877776
Ag-Pd,1,-0.1,15.01666302445357,9.942658639603136,5.762344994984988
Ag-Pd,1,-0.05,15.786583801626605,7.395939918353878,5.27141408575929
Ag-Pd,1,0.0,16.595979261167983,8.223306439377208,6.407968742767025
Ag-Pd,1,0.05,17.446873313321824,4.367026563641588,5.0726406542167135
Ag-Pd,1,0.1,18.34139363642943,0.6753966299344035,3.335976089950893
Ag-Pd,1,0.15,19.281776997233393,1.588683321227649,3.7512732248080316
Ag-Pd,1,0.2,20.27037484395955,-0.37011068259644725,2.4076558649541253
Ag-Pd,1,0.3,22.402228776036292,0.4017244736770799,0.9393234213921073
Ag-Pd,1,0.4,24.758291743352718,3.9103803888508075,0.8677842860407637
Ag-Pd,2,-0.4,11.124617582352638,28.477502955470694,-3.221695901747962
Ag-Pd,2,-0.3,12.294603826729157,19.22794568288193,2.463690295945853
Ag-Pd,2,-0.2,13.58763859856263,12.244205595673298,2.779654144665604
Ag-Pd,2,-0.15,14.284291726672121,11.028955116709168,5.067624942805699
Ag-Pd,2,-0.1,15.01666302445357,10.101842872377757,5.63247382077092
Ag-Pd,2,-0.05,15.786583801626605,7.615636045611147,5.1935837254255155
Ag-Pd,2,0.0,16.595979261167983,8.431942813207607,6.332146792774403
Ag-Pd,2,0.05,17.446873313321824,4.622347975138792,5.050518166920367
Ag-Pd,2,0.1,18.34139363642943,0.8837820869999484,3.3523591143108327
Ag-Pd,2,0.15,19.281776997233393,1.7396765455016268,3.770614530857385
Ag-Pd,2,0.2,20.27037484395955,-0.20438192299505295,2.4509531993111326
Ag-Pd,2,0.3,22.402228776036292,0.4822266242675019,1.0329533972659775
Ag-Pd,2,0.4,24.758291743352718,3.6464697170082454,0.896698761558132
Ag-Pt,0,-0.4,11.183745931453137,45.7976043426572,-7.115627615054192
Ag-Pt,0,-0.3,12.359950758588852,23.493375240726934,-3.467526154737155
Ag-Pt,0,-0.2,13.659858127239438,20.217920584530876,7.872540782684801
Ag-Pt,0,-0.15,14.360214029763949,18.495097002023915,8.227675454441362
Ag-Pt,0,-0.1,15.096477947264306,17.651886440631902,8.682711721996506
Ag-Pt,0,-0.05,15.870490923037018,16.23636640211542,8.463931876528736
Ag-Pt,0,0.0,16.684188392686863,15.514441735810207,8.487554607306745
Ag-Pt,0,0.05,17.539605023724054,13.306338790737303,7.202396408165608
Ag-Pt,0,0.1,18.438879803292807,12.01287333538722,6.208942811497761
Ag-Pt,0,0.15,19.38426138675335,10.227552736220185,4.9790101716738215
Ag-Pt,0,0.2,20.378113720491626,9.349357628391246,3.9494617575626996
Ag-Pt,0,0.3,22.521298649125683,7.352400817164054,2.1107828688100523
Ag-Pt,0,0.4,24.889884304310073,7.3280529371784775,2.2605253735206547
Ag-Pt,1,-0.4,11.183745931453137,47.632956016612866,-6.375608941490749
Ag-Pt,1,-0.3,12.359950758588852,24.487029490807362,-2.2067742478348595
Ag-Pt,1,-0.2,13.659858127239438,19.83881537140963,8.949152751109528
Ag-Pt,1,-0.15,14.360214029763949,17.955643642677092,9.282162992461256
Ag-Pt,1,-0.1,15.096477947264306,16.92393196775094,9.650221909714118
Ag-Pt,1,-0.05,15.870490923037018,15.33807933631423,9.342613130775058
Ag-Pt,1,0.0,16.684188392686863,14.853220572363785,9.249790549454161
Ag-Pt,1,0.05,17.539605023724054,12.514502085730735,7.94437387723498
Ag-Pt,1,0.1,18.438879803292807,11.275490190732706,6.896090909193165
Ag-Pt,1,0.15,19.38426138675335,9.796009354867012,5.58555256798956
Ag-Pt,1,0.2,20.378113720491626,8.865210174339088,4.478033317500866
Ag-Pt,1,0.3,22.521298649125683,6.893659940002844,2.549784561386002
Ag-Pt,1,0.4,24.889884304310073,7.077585246019886,2.644386556986444
Ag-Pt,2,-0.4,11.183745931453137,47.05833505498648,-6.818669318214101
Ag-Pt,2,-0.3,12.359950758588852,24.138989020066095,-3.413099172608392
Ag-Pt,2,-0.2,13.659858127239438,20.37092246430537,8.811339570342517
Ag-Pt,2,-0.15,14.360214029763949,18.408412235445716,8.914222818778207
Ag-Pt,2,-0.1,15.096477947264306,17.43919431219203,9.236951996455028
Ag-Pt,2,-0.05,15.870490923037018,16.018690798143535,8.92034840492265
Ag-Pt,2,0.0,16.684188392686863,15.130101189514354,8.771094621808137
Ag-Pt,2,0.05,17.539605023724054,13.065190959847568,7.476124009055109
Ag-Pt,2,0.1,18.438879803292807,11.81852724797202,6.410647702340642
Ag-Pt,2,0.15,19.38426138675335,9.951410901798678,5.112107301908095
Ag-Pt,2,0.2,20.378113720491626,9.020981835242615,4.035031302875107
Ag-Pt,2,0.3,22.521298649125683,6.99009998245125,2.160495526684136
Ag-Pt,2,0.4,24.889884304310073,6.912670490175347,2.2674836140351164
Ag-Rh,0,-0.4,10.635235854679157,-17.60088775604701,-50.674350406120205
Ag-Rh,0,-0.3,11.753753373466807,-26.99517381501737,-55.339334237569254
Ag-Rh,0,-0.2,12.989906406589052,-19.221887993421973,-25.63845799203684
Ag-Rh,0,-0.15,13.655913149876811,-16.93531141011994,-22.179672159209005
Ag-Rh,0,-0.1,14.356066789086759,-14.504885198657165,-18.05700235713572
Ag-Rh,0,-0.05,15.092118073010665,-10.733342362392907,-13.891283611968092
Ag-Rh,0,0.0,15.86590751325033,-7.385014037130605,-10.367103815260949
Ag-Rh,0,0.05,16.67936998645527,-2.661749787317508,-6.368445993718866
Ag-Rh,0,0.1,17.534539572522185,-1.3481483885579708,-3.9899148006140734
Ag-Rh,0,0.15,18.433554640854172,-1.3188710074105543,-2.0368295086640718
Ag-Rh,0,0.2,19.378663197398115,1.0187636632547499,0.5835815195657124
Ag-Rh,0,0.3,21.41673499694724,-0.11096724653848994,0.8525665646995836
Ag-Rh,0,0.4,23.669152678759033,2.8346494013555614,0.9965167471015663
Ag-Rh,1,-0.4,10.635235854679157,-21.854715698762103,-49.71352039884912
Ag-Rh,1,-0.3,11.753753373466807,-30.701526397784257,-53.97868718903312
Ag-Rh,1,-0.2,12.989906406589052,-22.892499873807793,-24.93985963715416
Ag-Rh,1,-0.15,13.655913149876811,-20.28793732535736,-21.00712076327114
Ag-Rh,1,-0.1,14.356066789086759,-17.468607929423953,-16.88894775363446
Ag-Rh,1,-0.05,15.092118073010665,-13.468022878512686,-12.846394967984361
Ag-Rh,1,0.0,15.86590751325033,-10.012629582386753,-9.474625556506137
Ag-Rh,1,0.05,16.67936998645527,-4.918509466057118,-5.518184434318221
Ag-Rh,1,0.1,17.534539572522185,-3.415914760451331,-3.2554805152187045
Ag-Rh,1,0.15,18.433554640854172,-3.1412743676112496,-1.374943676146134
Ag-Rh,1,0.2,19.378663197398115,-0.4565800664654494,1.2701287728284754
Ag-Rh,1,0.3,21.41673499694724,-1.5362812052735362,1.3677020328569829
Ag-Rh,1,0.4,23.669152678759033,1.6509879861794752,1.367550200970614
Ag-Rh,2,-0.4,10.635235854679157,-14.683096937757611,-49.27753964951638
Ag-Rh,2,-0.3,11.753753373466807,-24.797017297676618,-53.97936417425305
Ag-Rh,2,-0.2,12.989906406589052,-17.903311406540794,-24.697047789706218
Ag-Rh,2,-0.15,13.655913149876811,-16.045434871356434,-21.03942805098529
Ag-Rh,2,-0.1,14.356066789086759,-13.775989389438836,-17.037775412736334
Ag-Rh,2,-0.05,15.092118073010665,-10.196419889826279,-13.081367590933365
Ag-Rh,2,0.0,15.86590751325033,-7.08331573525587,-9.765425305564975
Ag-Rh,2,0.05,16.67936998645527,-2.441409234540054,-5.9024460863159485
Ag-Rh,2,0.1,17.534539572522185,-1.155053212274855,-3.6453723412739567
Ag-Rh,2,0.15,18.433554640854172,-1.1589273873116526,-1.7823144533955797
Ag-Rh,2,0.2,19.378663197398115,1.1338587580712534,0.8076031405838985
Ag-Rh,2,0.3,21.41673499694724,-0.06341663615600365,0.9465448518889864
Ag-Rh,2,0.4,23.669152678759033,2.745758143496995,1.0375513108780905
Au-Co,0,-0.4,9.65062193933458,-30.444833148080356,-1.1779677511689095
Au-Co,0,-0.3,10.665586708695384,-7.461248531650858,0.5496766495752997
Au-Co,0,-0.2,11.787296254664302,7.585499722856023,10.189577174720732
Au-Co,0,-0.15,12.391643856949942,9.825020066030564,12.444647409878172
Au-Co,0,-0.1,13.026977023396988,10.18735660873729,16.72644574898928
Au-Co,0,-0.05,13.694884417851828,5.993294406912391,9.360089448359432
Au-Co,0,0.0,14.397036156698018,3.016569451439444,6.1068010106242285
Au-Co,0,0.05,15.135187985017186,1.4063843257825894,4.167443623448709
Au-Co,0,0.1,15.911185666866244,0.8826751922919382,3.2334394946695277
Au-Co,0,0.15,16.726969600648953,-0.2784075554887977,2.372939719418844
Au-Co,0,0.2,17.58457967112265,1.1099103370186711,2.571366743426348
Au-Co,0,0.3,19.43396605910899,0.15521395918309064,1.8292149934186845
Au-Co,0,0.4,21.477854111396457,1.7702384256828938,1.7660360479500952
Au-Co,1,-0.4,9.65062193933458,-22.198779574042163,-6.740551615941894
Au-Co,1,-0.3,10.665586708695384,-2.6429357896856396,-2.254669148130843
Au-Co,1,-0.2,11.787296254664302,10.182606013723854,9.354171871986967
Au-Co,1,-0.15,12.391643856949942,11.553155188963018,11.913025653671138
Au-Co,1,-0.1,13.026977023396988,10.82394083283475,15.763835136657184
Au-Co,1,-0.05,13.694884417851828,6.4818339198979835,8.841119333422528
Au-Co,1,0.0,14.397036156698018,3.3539383166987244,5.739747345299876
Au-Co,1,0.05,15.135187985017186,1.4037121076182628,3.9865414255297957
Au-Co,1,0.1,15.911185666866244,0.5347352053051542,3.2426940232369956
Au-Co,1,0.15,16.726969600648953,-0.5540350881148072,2.3591819361313004
Au-Co,1,0.2,17.58457967112265,0.43580127449742584,2.7976412408382965
Au-Co,1,0.3,19.43396605910899,-0.4121653962579781,1.9991119492143092
Au-Co,1,0.4,21.477854111396457,1.1806441307466025,1.9367138227098735
Au-Co,2,-0.4,9.65062193933458,-26.43436160194152,-2.284459373806714
Au-Co,2,-0.3,10.665586708695384,-5.877152520638706,-1.2436227631003012
Au-Co,2,-0.2,11.787296254664302,8.016198359551046,9.099523044340167
Au-Co,2,-0.15,12.391643856949942,9.968484362516676,11.706663498562111
Au-Co,2,-0.1,13.026977023396988,10.160426002828636,16.960966734393256
Au-Co,2,-0.05,13.694884417851828,5.884079843962178,8.811179654057165
Au-Co,2,0.0,14.397036156698018,2.8960098167685056,5.468514852212455
Au-Co,2,0.05,15.135187985017186,1.2841165866284407,3.6004589888774223
Au-Co,2,0.1,15.911185666866244,0.7780685985435617,2.7738013069429903
Au-Co,2,0.15,16.726969600648953,-0.45683431610341274,1.926489043691946
Au-Co,2,0.2,17.58457967112265,1.009562116012139,2.272417895779954
Au-Co,2,0.3,19.43396605910899,0.0247145633453297,1.6224775072656836
Au-Co,2,0.4,21.477854111396457,1.730837789598343,1.7152358582807499
Au-Cu,0,-0.4,10.025023511941784,-53.64922020333278,-11.224419312821116
Au-Cu,0,-0.3,11.079364438422655,-24.7245210961553,-5.8629979369887595
Au-Cu,0,-0.2,12.244591368106246,-12.721941593066314,-2.055748079171486
Au-Cu,0,-0.15,12.872384992225454,-10.530127383116978,-2.819267467118179
Au-Cu,0,-0.1,13.532366283751129,-8.096893975058222,1.3138769468383211
Au-Cu,0,-0.05,14.226185539680992,-7.010667279225964,1.7395660851089314
Au-Cu,0,0.0,14.955577669549177,-6.213078357026026,1.1104913220639159
Au-Cu,0,0.05,15.722366533603747,-5.141543582176158,0.8754002141839397
Au-Cu,0,0.1,16.52846950340732,-4.207132173278185,0.7714593649356204
Au-Cu,0,0.15,17.375902256264688,-3.321739263491188,0.7524909000791885
Au-Cu,0,0.2,18.26678381546601,-1.993367360377147,1.1118672187683973
Au-Cu,0,0.3,20.18791823962795,-1.1363942178474298,0.8484670891174569
Au-Cu,0,0.4,22.311100134925734,-0.7043430598869992,0.32519509165557453
Au-Cu,1,-0.4,10.025023511941784,-42.62565018907163,-15.599731672017032
Au-Cu,1,-0.3,11.079364438422655,-16.854652539673353,-8.737203965736771
Au-Cu,1,-0.2,12.244591368106246,-7.218903597757638,-3.964998280599793
Au-Cu,1,-0.15,12.872384992225454,-5.922768245000543,-4.419370341816148
Au-Cu,1,-0.1,13.532366283751129,-4.294189276637614,-0.026115069230334093
Au-Cu,1,-0.05,14.226185539680992,-3.8521925196024807,0.6206905796200597
Au-Cu,1,0.0,14.955577669549177,-3.61436350142128,0.2106513270065992
Au-Cu,1,0.05,15.722366533603747,-2.9949885850554936,0.17882408197811372
Au-Cu,1,0.1,16.52846950340732,-2.5074610428649136,0.2426189351447772
Au-Cu,1,0.15,17.375902256264688,-1.978165026392608,0.3742992154912997
Au-Cu,1,0.2,18.26678381546601,-0.9305609969686542,0.859971321592617
Au-Cu,1,0.3,20.18791823962795,-0.6387407125242364,0.7213511316723519
Au-Cu,1,0.4,22.311100134925734,-0.5040989691684958,0.25834790787959405
Au-Cu,2,-0.4,10.025023511941784,-48.94406428995555,-11.476952591850427
Au-Cu,2,-0.3,11.079364438422655,-21.67244808216725,-6.126773789005163
Au-Cu,2,-0.2,12.244591368106246,-10.801279668292151,-2.5618252890348825
Au-Cu,2,-0.15,12.872384992225454,-8.797227583409867,-2.7391259773988383
Au-Cu,2,-0.1,13.532366283751129,-6.687369555198501,1.2850208986352774
Au-Cu,2,-0.05,14.226185539680992,-5.859218337366988,1.6385720521221565
Au-Cu,2,0.0,14.955577669549177,-5.262763861032613,1.0163219296178432
Au-Cu,2,0.05,15.722366533603747,-4.2850872476730455,0.8071199776784573
Au-Cu,2,0.1,16.52846950340732,-3.5796393919685507,0.6962259862090754
Au-Cu,2,0.15,17.375902256264688,-2.7940471282704773,0.6882961986077922
Au-Cu,2,0.2,18.26678381546601,-1.4810376176508442,1.0808082490107505
Au-Cu,2,0.3,20.18791823962795,-0.9138647803369087,0.8193187938771208
Au-Cu,2,0.4,22.311100134925734,-0.6252759240022739,0.2733670146664954
Au-Ir,0,-0.4,10.802368844777366,-50.086284099977156,-45.324265113138615
Au-Ir,0,-0.3,11.938463893574374,-64.05869260798107,-61.514948769874984
Au-Ir,0,-0.2,13.194043101674561,-51.09555095062328,-55.42524080719944
Au-Ir,0,-0.15,13.870516157129934,-40.02649245393907,-36.508051145708095
Au-Ir,0,-0.1,14.58167272780734,-34.06042759612537,-31.978680538810362
Au-Ir,0,-0.05,15.329291075558393,-29.58682157596437,-27.69250435602604
Au-Ir,0,0.0,16.115240635669473,-23.54929619750788,-22.321266820454344
Au-Ir,0,0.05,16.9414866914237,-15.481358200864175,-16.06499992312018
Au-Ir,0,0.1,17.810095288332814,-13.731759045277448,-13.146169994551054
Au-Ir,0,0.15,18.723238400327098,-11.993880507429749,-9.905262310794166
Au-Ir,0,0.2,19.683199360821543,-7.7634284069976705,-6.766877266064425
Au-Ir,0,0.3,21.753299508265147,0.6535806985876,-3.429570119086198
Au-Ir,0,0.4,24.041113988723925,7.72844156514968,-1.1278859091649671
Au-Ir,1,-0.4,10.802368844777366,-53.6896385100057,-48.170449305023645
Au-Ir,1,-0.3,11.938463893574374,-66.07384436906324,-63.068407179030004
Au-Ir,1,-0.2,13.194043101674561,-52.70714463608654,-56.25494085626303
Au-Ir,1,-0.15,13.870516157129934,-41.71603687638167,-36.663243814546554
Au-Ir,1,-0.1,14.58167272780734,-35.21904160764652,-31.875200119191582
Au-Ir,1,-0.05,15.329291075558393,-30.90524740380301,-27.449656561707705
Au-Ir,1,0.0,16.115240635669473,-24.723368282241967,-22.041569839440875
Au-Ir,1,0.05,16.9414866914237,-15.919680802248294,-15.68912164629337
Au-Ir,1,0.1,17.810095288332814,-15.067121394573194,-12.775289142647306
Au-Ir,1,0.15,18.723238400327098,-12.837401498966218,-9.48226102010666
Au-Ir,1,0.2,19.683199360821543,-8.157961540876368,-6.296517692755996
Au-Ir,1,0.3,21.753299508265147,0.14829714824018467,-2.9929424997102934
Au-Ir,1,0.4,24.041113988723925,7.356263298334226,-0.7713337060832434
Au-Ir,2,-0.4,10.802368844777366,-45.56558001626432,-43.713695002434505
Au-Ir,2,-0.3,11.938463893574374,-60.34517171298967,-59.12333763278241
Au-Ir,2,-0.2,13.194043101674561,-48.38199002919569,-54.00968259784161
Au-Ir,2,-0.15,13.870516157129934,-37.78805066611069,-34.381529627093144
Au-Ir,2,-0.1,14.58167272780734,-31.890717824904094,-30.02946238827485
Au-Ir,2,-0.05,15.329291075558393,-27.94216746835388,-26.02758891550491
Au-Ir,2,0.0,16.115240635669473,-22.32723948008406,-20.99874133716815
Au-Ir,2,0.05,16.9414866914237,-14.284030687945299,-14.936828496730339
Au-Ir,2,0.1,17.810095288332814,-13.309777148032175,-12.314012534651807
Au-Ir,2,0.15,18.723238400327098,-11.51844411312832,-9.179644362209642
Au-Ir,2,0.2,19.683199360821543,-7.328734080086752,-6.140421247996524
Au-Ir,2,0.3,21.753299508265147,0.49054583118001277,-3.117805479495416
Au-Ir,2,0.4,24.041113988723925,7.138088731136326,-0.9937454593757844
Au-Ni,0,-0.4,9.666282538457162,-63.37526978258417,-23.393668802153492
Au-Ni,0,-0.3,10.682894347405304,-31.022241713898207,-18.287086361578243
Au-Ni,0,-0.2,11.806424153627066,-9.853476745761794,-8.370503008835167
Au-Ni,0,-0.15,12.411752464263898,-3.650482327700481,-0.6677773785634216
Au-Ni,0,-0.1,13.048116621054525,1.2886974876024822,11.558130338008139
Au-Ni,0,-0.05,13.717107865858214,-1.2996047035757474,2.13211002005592
Au-Ni,0,0.0,14.420399025248948,-2.720071266934013,0.010326079711762774
Au-Ni,0,0.05,15.15974869345321,-2.0021128786959568,-0.13005124673815105
Au-Ni,0,0.1,15.937005629751555,-0.3365719123145181,0.5596941196570019
Au-Ni,0,0.15,16.75411338133978,-0.5784441715051948,0.392723226307557
Au-Ni,0,0.2,17.61311514320929,1.2536394790237342,1.2063186410762432
Au-Ni,0,0.3,19.465502632992703,0.7413620185456533,0.6846883965208767
Au-Ni,0,0.4,21.51270741570848,2.7136173567609516,0.7698093930166071
Au-Ni,1,-0.4,9.666282538457162,-51.4258338759238,-29.092062733509657
Au-Ni,1,-0.3,10.682894347405304,-22.48760712122228,-22.042186168196633
Au-Ni,1,-0.2,11.806424153627066,-4.0228734946911295,-10.712946780334564
Au-Ni,1,-0.15,12.411752464263898,1.0634846659203483,-2.500825023846633
Au-Ni,1,-0.1,13.048116621054525,5.018551600819237,10.371167212721886
Au-Ni,1,-0.05,13.717107865858214,1.6471078228620475,0.9786967432313736
Au-Ni,1,0.0,14.420399025248948,-0.44285213444420624,-0.9266782670530809
Au-Ni,1,0.05,15.15974869345321,-0.3626733040335417,-0.8128355222908968
Au-Ni,1,0.1,15.937005629751555,0.7695836009625072,0.09894845479758421
Au-Ni,1,0.15,16.75411338133978,0.1543860383671636,0.0607462457482826
Au-Ni,1,0.2,17.61311514320929,1.5857409472465418,1.010273201717056
Au-Ni,1,0.3,19.465502632992703,0.8117809143625909,0.5556714334197913
Au-Ni,1,0.4,21.51270741570848,2.6865357679039716,0.7156052863144156
Au-Ni,2,-0.4,9.666282538457162,-58.402211029247574,-24.153782912756583
Au-Ni,2,-0.3,10.682894347405304,-27.891999035982376,-19.139262464800453
Au-Ni,2,-0.2,11.806424153627066,-7.881681462690532,-9.098545061354164
Au-Ni,2,-0.15,12.411752464263898,-2.0571783267013903,-1.2289865664725175
Au-Ni,2,-0.1,13.048116621054525,2.582081343543931,11.48847683931598
Au-Ni,2,-0.05,13.717107865858214,-0.23364566178793356,1.8556862141800325
Au-Ni,2,0.0,14.420399025248948,-1.8534466218101606,-0.2570958894274756
Au-Ni,2,0.05,15.15974869345321,-1.350247670892127,-0.3591464728350277
Au-Ni,2,0.1,15.937005629751555,0.110640312496569,0.37273510102386975
Au-Ni,2,0.15,16.75411338133978,-0.2837560568904326,0.24748079434967962
Au-Ni,2,0.2,17.61311514320929,1.369257446297737,1.0976949632498991
Au-Ni,2,0.3,19.465502632992703,0.8029115943351264,0.6113521159134522
Au-Ni,2,0.4,21.51270741570848,2.627959711376712,0.6866230208169859
Au-Pd,0,-0.4,11.151139118737758,17.54106961412945,-8.222782309221321
Au-Pd,0,-0.3,12.323914657444677,21.313595606124153,0.1714611846124756
Au-Pd,0,-0.2,13.620032076254063,16.273414462147706,-0.2178973382932842
Au-Pd,0,-0.15,14.318346053480225,14.800220062297473,3.0611847732358757
Au-Pd,0,-0.1,15.05246335393347,13.494341480720093,4.2783887169645105
Au-Pd,0,-0.05,15.824219653249566,10.687534663540333,4.62346378993705
Au-Pd,0,0.0,16.635544744166697,12.318862960448822,6.838855313504039
Au-Pd,0,0.05,17.48846736201253,7.697149227702088,5.526934982679326
Au-Pd,0,0.1,18.385120257599226,3.3446245775909746,4.076416270693741
Au-Pd,0,0.15,19.327745530211384,4.080749954813648,4.303694446836186
Au-Pd,0,0.2,20.31870023402212,2.76436776602201,2.8329909206012873
Au-Pd,0,0.3,22.455636591738106,4.322370607981407,1.131043658953108
Au-Pd,0,0.4,24.81731650806431,8.44831367827297,1.4881559997976805
Au-Pd,1,-0.4,11.151139118737758,18.487531792625308,-8.356485578024635
Au-Pd,1,-0.3,12.323914657444677,21.803108124593667,0.5219428199439715
Au-Pd,1,-0.2,13.620032076254063,16.673915059382267,-0.013087528808066401
Au-Pd,1,-0.15,14.318346053480225,15.179413721939316,3.2509710516456574
Au-Pd,1,-0.1,15.05246335393347,13.782975978374267,4.447330078159461
Au-Pd,1,-0.05,15.824219653249566,10.878754900233007,4.760035445375603
Au-Pd,1,0.0,16.635544744166697,12.499083198103717,6.979620550511252
Au-Pd,1,0.05,17.48846736201253,7.785489662250817,5.620259136696921
Au-Pd,1,0.1,18.385120257599226,3.4087349098209403,4.10470235957806
Au-Pd,1,0.15,19.327745530211384,4.126685407944945,4.316426842812029
Au-Pd,1,0.2,20.31870023402212,2.7283379563056536,2.812678766335934
Au-Pd,1,0.3,22.455636591738106,4.120132441990715,1.0292019669259147
Au-Pd,1,0.4,24.81731650806431,8.20694054636311,1.3805758282258012
Au-Pd,2,-0.4,11.151139118737758,17.732553087772402,-7.9903106801021755
Au-Pd,2,-0.3,12.323914657444677,21.408127960404762,0.17832996903275442
Au-Pd,2,-0.2,13.620032076254063,16.56946340218966,0.004642306923407328
Au-Pd,2,-0.15,14.318346053480225,15.061461846138073,3.0829264592275054
Au-Pd,2,-0.1,15.05246335393347,13.726680843540317,4.2178104909712175
Au-Pd,2,-0.05,15.824219653249566,10.903349594303023,4.528432372673083
Au-Pd,2,0.0,16.635544744166697,12.474340165519257,6.684058366346062
Au-Pd,2,0.05,17.48846736201253,7.871373736457365,5.398912525998326
Au-Pd,2,0.1,18.385120257599226,3.5213795515230535,3.9613052093934473
Au-Pd,2,0.15,19.327745530211384,4.261520318026978,4.209581389398381
Au-Pd,2,0.2,20.31870023402212,2.8895529241538855,2.749555684380334
Au-Pd,2,0.3,22.455636591738106,4.299220733868212,1.0501870505752073
Au-Pd,2,0.4,24.81731650806431,8.124196603564574,1.3070327405224256
Au-Pt,0,-0.4,11.210267467838255,1.624849331322268,-16.721556560624546
Au-Pt,0,-0.3,12.38926158930437,8.53385015989878,-9.26049744176824
Au-Pt,0,-0.2,13.692251604930867,12.267617906633214,-0.5993277712063136
Au-Pt,0,-0.15,14.394268356572049,11.34509026389659,1.008599373343365
Au-Pt,0,-0.1,15.132278276744206,10.786620274467316,2.581862670621954
Au-Pt,0,-0.05,15.908126774659975,9.710406325271125,3.5134133017519886
Au-Pt,0,0.0,16.723753875685574,10.41611866427672,4.724449526061585
Au-Pt,0,0.05,17.581199072414755,9.232091108591963,4.314100301477891
Au-Pt,0,0.1,18.4826064244626,8.100947522226278,3.8230220885585458
Au-Pt,0,0.15,19.43022991973134,7.527314300039621,2.9356013261406724
Au-Pt,0,0.2,20.426439110554192,8.091683485688668,2.2540202206730595
Au-Pt,0,0.3,22.57470646482749,7.919396230364784,0.9739990629114011
Au-Pt,0,0.4,24.948909069021656,7.483389530645502,1.4956185679597578
Au-Pt,1,-0.4,11.210267467838255,2.574501352309452,-16.396673145265893
Au-Pt,1,-0.3,12.38926158930437,9.840698480075712,-8.252601661284483
Au-Pt,1,-0.2,13.692251604930867,13.115989923055452,0.002906427912766326
Au-Pt,1,-0.15,14.394268356572049,11.99199046538676,1.5604530072358227
Au-Pt,1,-0.1,15.132278276744206,11.188664362230218,3.0652291660064246
Au-Pt,1,-0.05,15.908126774659975,9.969284751641055,3.9091644547922324
Au-Pt,1,0.0,16.723753875685574,10.616480349244648,5.049715554745848
Au-Pt,1,0.05,17.581199072414755,9.40138183883353,4.580823048702611
Au-Pt,1,0.1,18.4826064244626,8.298351271445863,4.032759548615097
Au-Pt,1,0.15,19.43022991973134,7.69253825458824,3.104653062985903
Au-Pt,1,0.2,20.426439110554192,8.19315076248138,2.3758099112797826
Au-Pt,1,0.3,22.57470646482749,7.93093223677937,1.0213487825597591
Au-Pt,1,0.4,24.948909069021656,7.566456548161223,1.5149455118471369
Au-Pt,2,-0.4,11.210267467838255,3.46121323414036,-15.701369022188144
Au-Pt,2,-0.3,12.38926158930437,9.46160721387937,-8.314147216803448
Au-Pt,2,-0.2,13.692251604930867,12.886576052097494,0.4055085788680644
Au-Pt,2,-0.15,14.394268356572049,11.715143347202273,1.710390955479097
Au-Pt,2,-0.1,15.132278276744206,11.019160440203391,3.11415292320936
Au-Pt,2,-0.05,15.908126774659975,9.870943164217437,3.9126099020824308
Au-Pt,2,0.0,16.723753875685574,10.334889934512617,4.945990388981478
Au-Pt,2,0.05,17.581199072414755,9.214410838239138,4.51392933536713
Au-Pt,2,0.1,18.4826064244626,8.041106994773443,3.9485866785224957
Au-Pt,2,0.15,19.43022991973134,7.3797157160885964,3.017330329222689
Au-Pt,2,0.2,20.426439110554192,7.8433723815352305,2.29147443881997
Au-Pt,2,0.3,22.57470646482749,7.578790504689716,0.9795294191405993
Au-Pt,2,0.4,24.948909069021656,7.0772652387034185,1.4514402321479718
Au-Rh,0,-0.4,10.661757391064278,-45.251034545613074,-34.07454594383723
Au-Rh,0,-0.3,11.78306420418233,-35.89128231848134,-44.47369792571055
Au-Rh,0,-0.2,13.022299884280484,-16.516530538898152,-17.21144700908858
Au-Rh,0,-0.15,13.689967476684915,-14.105342368844914,-18.218535764675327
Au-Rh,0,-0.1,14.391867118566662,-12.101147417088539,-15.397978392185312
Au-Rh,0,-0.05,15.129753924633626,-9.234857458956618,-12.107016086375856
Au-Rh,0,0.0,15.905472996249044,-6.608453115002326,-8.882907621600033
Au-Rh,0,0.05,16.72096403514598,-1.3614812862506331,-4.631311839913992
Au-Rh,0,0.1,17.578266193691977,-0.8185771471001143,-2.7830149999340312
Au-Rh,0,0.15,18.479523173832163,-1.5494406477794171,-1.257799463616109
Au-Rh,0,0.2,19.426988587460684,0.8226677141916805,0.9052831397101959
Au-Rh,0,0.3,21.47014281264905,1.0640983934298673,0.7444253660336367
Au-Rh,0,0.4,23.72817744347062,6.186413037924632,1.2508125370005874
Au-Rh,1,-0.4,10.661757391064278,-47.89538978626398,-34.77673196671893
Au-Rh,1,-0.3,11.78306420418233,-37.498040211011926,-44.23712116821884
Au-Rh,1,-0.2,13.022299884280484,-17.693005210335322,-16.88677560434092
Au-Rh,1,-0.15,13.689967476684915,-15.283610272517102,-17.612492362391613
Au-Rh,1,-0.1,14.391867118566662,-13.071560709509702,-14.725059367363903
Au-Rh,1,-0.05,15.129753924633626,-10.27812870986211,-11.464320778695383
Au-Rh,1,0.0,15.905472996249044,-7.742305826446656,-8.327111613313212
Au-Rh,1,0.05,16.72096403514598,-2.174546137058048,-4.092479832545515
Au-Rh,1,0.1,17.578266193691977,-1.8041535238602886,-2.353119152195792
Au-Rh,1,0.15,18.479523173832163,-2.5262151623312272,-0.9048966769135225
Au-Rh,1,0.2,19.426988587460684,0.04841708563338437,1.2669033823858913
Au-Rh,1,0.3,21.47014281264905,0.26840184638364695,0.9820790985860998
Au-Rh,1,0.4,23.72817744347062,5.542505613447613,1.3754004518706358
Au-Rh,2,-0.4,10.661757391064278,-42.09059228642039,-33.09437754245651
Au-Rh,2,-0.3,11.78306420418233,-33.616278858542536,-43.4141818243128
Au-Rh,2,-0.2,13.022299884280484,-14.87937273962141,-16.626557081376554
Au-Rh,2,-0.15,13.689967476684915,-12.965812962094704,-17.244665470899612
Au-Rh,2,-0.1,14.391867118566662,-11.122515967712928,-14.509277803229303
Au-Rh,2,-0.05,15.129753924633626,-8.508351678398627,-11.423171648357362
Au-Rh,2,0.0,15.905472996249044,-6.158703224974867,-8.41476104809165
Au-Rh,2,0.05,16.72096403514598,-0.8985747795656341,-4.287144146591842
Au-Rh,2,0.1,17.578266193691977,-0.5326153283239903,-2.5449364186291206
Au-Rh,2,0.15,18.479523173832163,-1.3425446634196874,-1.0906263699851073
Au-Rh,2,0.2,19.426988587460684,1.0367518515925853,1.0649268815419948
Au-Rh,2,0.3,21.47014281264905,1.115999930157424,0.8088106447728167
Au-Rh,2,0.4,23.72817744347062,5.97729904609722,1.214985984400681
Co-Cu,0,-0.4,7.663472637574219,20.662802221217245,-7.955213776606281
Co-Cu,0,-0.3,8.469447090515505,12.51644582649219,-4.977666718079002
Co-Cu,0,-0.2,9.360186616618142,5.068711478959834,-2.030697743896875
Co-Cu,0,-0.15,9.840093646736342,4.031030821301559,-3.411932295270192
Co-Cu,0,-0.1,10.344606036447262,-0.6871725177234104,-6.197485527112476
Co-Cu,0,-0.05,10.874985329513951,-1.115896314982785,-5.572658123169522
Co-Cu,0,0.0,11.432557750431307,0.0005530036149365899,-2.3347027286819153
Co-Cu,0,0.05,12.018717520678132,1.8677420774042972,1.5992767877050462
Co-Cu,0,0.1,12.634930344997029,1.1966720259844759,-0.5663834128272781
Co-Cu,0,0.15,13.282737076419721,-0.7857278385262392,-1.3477983617688063
Co-Cu,0,0.2,13.963757569202226,-1.4056316372239226,0.40219768043024645
Co-Cu,0,0.3,15.432338772540998,-2.577678264416032,-0.5530905462489756
Co-Cu,0,0.4,17.055372009303547,-0.7064390541027067,-0.053493540436201824
Co-Cu,1,-0.4,7.663472637574219,16.99152917768046,-7.659403957575167
Co-Cu,1,-0.3,8.469447090515505,7.714652146870218,-4.54622323433208
Co-Cu,1,-0.2,9.360186616618142,0.6670304764768125,-1.2586057026686632
Co-Cu,1,-0.15,9.840093646736342,-0.22128069095156852,-2.4790727041391722
Co-Cu,1,-0.1,10.344606036447262,-4.551825746425128,-5.087222401061771
Co-Cu,1,-0.05,10.874985329513951,-4.647563792134323,-4.648286927481893
Co-Cu,1,0.0,11.432557750431307,-3.21064824653783,-1.5270643855662829
Co-Cu,1,0.05,12.018717520678132,-1.0420717591014121,2.6725765375155532
Co-Cu,1,0.1,12.634930344997029,-1.3751968507406245,0.20272994012706602
Co-Cu,1,0.15,13.282737076419721,-3.0286503475785347,-0.7014491117602208
Co-Cu,1,0.2,13.963757569202226,-3.3119321852164165,1.1294145886203464
Co-Cu,1,0.3,15.432338772540998,-4.0661561505537955,0.021975652189896257
Co-Cu,1,0.4,17.055372009303547,-1.6744003741284983,0.31786950252575585
Co-Cu,2,-0.4,7.663472637574219,22.080411068312838,-7.7362190096255325
Co-Cu,2,-0.3,8.469447090515505,13.098281770308027,-3.9710874911909317
Co-Cu,2,-0.2,9.360186616618142,5.115892429832594,-0.8648181471755642
Co-Cu,2,-0.15,9.840093646736342,3.508410358836413,-2.3275797194057755
Co-Cu,2,-0.1,10.344606036447262,-1.1819740101745255,-5.207119403747388
Co-Cu,2,-0.05,10.874985329513951,-1.7240654120525851,-5.05148195320708
Co-Cu,2,0.0,11.432557750431307,-0.6761067123967464,-2.130359297656944
Co-Cu,2,0.05,12.018717520678132,1.1619634182151908,1.8019052495067585
Co-Cu,2,0.1,12.634930344997029,0.6298144583070223,-0.610933909019846
Co-Cu,2,0.15,13.282737076419721,-1.2008043921629863,-1.3464465632624592
Co-Cu,2,0.2,13.963757569202226,-1.7437187243334518,0.43903133153365614
Co-Cu,2,0.3,15.432338772540998,-2.916060413644526,-0.5747495933611954
Co-Cu,2,0.4,17.055372009303547,-1.008575708790727,-0.08745186398802661
Co-Ir,0,-0.4,8.440817970409801,-182.83479174162073,-29.97296732335801
Co-Ir,0,-0.3,9.328546545667225,-69.08126530357403,-78.08765343117311
Co-Ir,0,-0.2,10.309638350186457,-13.855223127451003,-52.45948427367589
Co-Ir,0,-0.15,10.83822481164082,-9.217341220584757,-38.772798685066306
Co-Ir,0,-0.1,11.39391248050347,-20.137914289406066,-37.38081453909426
Co-Ir,0,-0.05,11.978090865391348,-30.133014270122686,-27.872891597320834
Co-Ir,0,0.0,12.592220716551601,-43.27027974404771,-47.152198112215025
Co-Ir,0,0.05,13.237837678498085,-41.468147495431445,-40.67550066490232
Co-Ir,0,0.1,13.916556129922524,-32.378984446026124,-20.468871006071648
Co-Ir,0,0.15,14.630073220482128,-26.022158545019195,-17.421656302555466
Co-Ir,0,0.2,15.380173114557756,-21.11592245986057,-14.45707570245645
Co-Ir,0,0.3,16.997720041178187,-8.334177829551566,-6.878543802124714
Co-Ir,0,0.4,18.785385863101734,-4.522340822767305,-2.672559669352239
Co-Ir,1,-0.4,8.440817970409801,-172.49096869005166,-39.89836755447518
Co-Ir,1,-0.3,9.328546545667225,-59.87186991947771,-85.05977759824606
Co-Ir,1,-0.2,10.309638350186457,-6.621244872450122,-56.81500305288882
Co-Ir,1,-0.15,10.83822481164082,-2.704421425862218,-41.796591304687745
Co-Ir,1,-0.1,11.39391248050347,-14.432023495051132,-39.292972029700294
Co-Ir,1,-0.05,11.978090865391348,-25.3858001698988,-29.60683997065689
Co-Ir,1,0.0,12.592220716551601,-39.429180065921855,-48.72683217872358
Co-Ir,1,0.05,13.237837678498085,-38.46559364630426,-41.912843746728605
Co-Ir,1,0.1,13.916556129922524,-29.877494114195972,-21.752720983625554
Co-Ir,1,0.15,14.630073220482128,-23.806238428104546,-18.52165812448334
Co-Ir,1,0.2,15.380173114557756,-19.23207044306049,-15.32593490816341
Co-Ir,1,0.3,16.997720041178187,-6.903438190826158,-7.367394536813352
Co-Ir,1,0.4,18.785385863101734,-3.3799497153534275,-2.7455220377304443
Co-Ir,2,-0.4,8.440817970409801,-173.63391478086257,-31.112392554598085
Co-Ir,2,-0.3,9.328546545667225,-60.66160888121648,-78.26597097284635
Co-Ir,2,-0.2,10.309638350186457,-7.2180524215488955,-51.91920463496502
Co-Ir,2,-0.15,10.83822481164082,-3.4690633247712,-37.884072825307044
Co-Ir,2,-0.1,11.39391248050347,-15.191293381192688,-36.3098098820908
Co-Ir,2,-0.05,11.978090865391348,-26.070654163841922,-27.353358761836596
Co-Ir,2,0.0,12.592220716551601,-39.81625858273116,-46.017772421900915
Co-Ir,2,0.05,13.237837678498085,-38.557896607769415,-38.96655141199022
Co-Ir,2,0.1,13.916556129922524,-30.150762324662495,-19.384415525668082
Co-Ir,2,0.15,14.630073220482128,-24.443204678857143,-16.507042757616315
Co-Ir,2,0.2,15.380173114557756,-19.88885007453153,-13.577622410676017
Co-Ir,2,0.3,16.997720041178187,-8.105126025650613,-6.510430960267014
Co-Ir,2,0.4,18.785385863101734,-4.359397642174213,-2.3173797989471794
Co-Ni,0,-0.4,7.3047316640896,21.413981248930728,11.970304992700042
Co-Ni,0,-0.3,8.072976999498156,16.56565044308958,11.984947953495583
Co-Ni,0,-0.2,8.922019402138963,14.232237630743311,10.16085794694266
Co-Ni,0,-0.15,9.379461118774786,13.502415430309277,8.62000701299186
Co-Ni,0,-0.1,9.860356373750658,10.894443275229591,7.461989118002209
Co-Ni,0,-0.05,10.365907655691172,9.617257951114222,7.53403503144171
Co-Ni,0,0.0,10.89737910613108,8.669118127630204,6.83259062928939
Co-Ni,0,0.05,11.456099680527599,7.701293508116924,7.093494888905692
Co-Ni,0,0.1,12.043466471341267,7.074025765078486,7.662087731217587
Co-Ni,0,0.15,12.660948201494817,5.590546979793423,5.234708863086703
Co-Ni,0,0.2,13.310088896945507,3.79080180958265,3.6896064086319873
Co-Ni,0,0.3,14.709923165905751,2.5709006998417165,2.6612085321139625
Co-Ni,0,0.4,16.256979290086296,2.2276130815719517,1.7762635731947352
Co-Ni,1,-0.4,7.3047316640896,21.640297790321764,12.487879320809377
Co-Ni,1,-0.3,8.072976999498156,16.112521729710217,12.454382459957996
Co-Ni,1,-0.2,8.922019402138963,12.93857466829607,10.515242631039682
Co-Ni,1,-0.15,9.379461118774786,12.165083080756105,8.93671926474313
Co-Ni,1,-0.1,9.860356373750658,9.579967243389031,7.752760430670337
Co-Ni,1,-0.05,10.365907655691172,8.458514252424274,7.873494711896246
Co-Ni,1,0.0,10.89737910613108,7.706680905288404,7.136082106539789
Co-Ni,1,0.05,11.456099680527599,6.900788644978564,7.433011222929272
Co-Ni,1,0.1,12.043466471341267,6.323425327087707,8.073744314882621
Co-Ni,1,0.15,12.660948201494817,4.950236854319305,5.456248459432615
Co-Ni,1,0.2,13.310088896945507,3.234266938867575,3.8976836624179065
Co-Ni,1,0.3,14.709923165905751,2.1780548016394548,2.8018033556192226
Co-Ni,1,0.4,16.256979290086296,2.012163373365483,1.858180673110641
Co-Ni,2,-0.4,7.3047316640896,22.252030595735505,12.199287386069187
Co-Ni,2,-0.3,8.072976999498156,16.592873893596035,11.906888406216195
Co-Ni,2,-0.2,8.922019402138963,14.15442962433254,10.127399146783999
Co-Ni,2,-0.15,9.379461118774786,13.288031241749454,8.480675581898696
Co-Ni,2,-0.1,9.860356373750658,10.412814390937466,7.223520451025385
Co-Ni,2,-0.05,10.365907655691172,9.200955934667672,7.391728919653546
Co-Ni,2,0.0,10.89737910613108,8.237610341232658,6.486730055423283
Co-Ni,2,0.05,11.456099680527599,7.257992759288347,6.648553444899856
Co-Ni,2,0.1,12.043466471341267,6.669347300852644,7.495714707148786
Co-Ni,2,0.15,12.660948201494817,5.209037641317568,4.682532345570093
Co-Ni,2,0.2,13.310088896945507,3.507279450863746,3.2772484515464937
Co-Ni,2,0.3,14.709923165905751,2.4605253146509742,2.557287893692682
Co-Ni,2,0.4,16.256979290086296,2.1670567562661502,1.6972282498129148
Co-Pd,0,-0.4,8.789588244370195,29.6345865460584,9.484018415893276
Co-Pd,0,-0.3,9.713997309537529,29.53165167788028,11.39754102792128
Co-Pd,0,-0.2,10.73562732476596,33.01493665609129,17.59148320384459
Co-Pd,0,-0.15,11.286054707991113,29.561203383784758,21.144348389018337
Co-Pd,0,-0.1,11.864703106629605,22.92644357234338,21.316368305380458
Co-Pd,0,-0.05,12.473019443082524,16.198022087516005,17.336462840287112
Co-Pd,0,0.0,13.11252482504883,10.233636417288707,12.210320406533853
Co-Pd,0,0.05,13.784818349086917,8.246053672321048,12.842273798950727
Co-Pd,0,0.1,14.491581099188936,7.528213277048347,11.60463394946179
Co-Pd,0,0.15,15.23458035036642,6.267823318544885,9.992990069280062
Co-Pd,0,0.2,16.01567398775834,4.701654841733084,8.192467989436173
Co-Pd,0,0.3,17.700057124651153,0.9087115620343954,4.499492357941698
Co-Pd,0,0.4,19.56158838244212,0.41946579896934394,2.4435468842156194
Co-Pd,1,-0.4,8.789588244370195,35.47880519930117,6.902750208952693
Co-Pd,1,-0.3,9.713997309537529,34.62357631882624,9.873813340631084
Co-Pd,1,-0.2,10.73562732476596,36.823481648730265,16.67397111645339
Co-Pd,1,-0.15,11.286054707991113,32.82014643204534,20.750710344676612
Co-Pd,1,-0.1,11.864703106629605,25.58175367138675,20.61722784667211
Co-Pd,1,-0.05,12.473019443082524,18.398714803884037,16.8879521393138
Co-Pd,1,0.0,13.11252482504883,12.161263562693673,12.305877581183612
Co-Pd,1,0.05,13.784818349086917,9.777534357640395,12.224013195725401
Co-Pd,1,0.1,14.491581099188936,8.854231396168686,10.996116223331237
Co-Pd,1,0.15,15.23458035036642,7.403015896059039,9.427663264571798
Co-Pd,1,0.2,16.01567398775834,5.710100185791469,7.69115014649497
Co-Pd,1,0.3,17.700057124651153,1.782477116892185,4.101267916182326
Co-Pd,1,0.4,19.56158838244212,0.8681975493280909,2.2297262252977545
Co-Pd,2,-0.4,8.789588244370195,33.78034255105391,9.287265130312075
Co-Pd,2,-0.3,9.713997309537529,31.921715541955862,11.194972182956095
Co-Pd,2,-0.2,10.73562732476596,34.505141894124215,17.221857462018185
Co-Pd,2,-0.15,11.286054707991113,30.53778178842218,20.686076804037068
Co-Pd,2,-0.1,11.864703106629605,23.618126035776978,20.77919095259793
Co-Pd,2,-0.05,12.473019443082524,16.562907450918704,16.7325064966026
Co-Pd,2,0.0,13.11252482504883,10.403551825595185,11.981117973268432
Co-Pd,2,0.05,13.784818349086917,8.415552401821742,12.582747240367908
Co-Pd,2,0.1,14.491581099188936,7.703790028808815,11.323164954797628
Co-Pd,2,0.15,15.23458035036642,6.401352600004624,9.724970038648802
Co-Pd,2,0.2,16.01567398775834,4.8643271272057795,7.964018515353549
Co-Pd,2,0.3,17.700057124651153,1.1541867702777933,4.386788345131325
Co-Pd,2,0.4,19.56158838244212,0.6330584228271456,2.444620419831328
Co-Pt,0,-0.4,8.848716593470693,162.27506293945427,-12.799100169057562
Co-Pt,0,-0.3,9.779344241397222,101.56997196766032,-3.389572910746041
Co-Pt,0,-0.2,10.807846853442765,72.93296945119218,34.05852915936448
Co-Pt,0,-0.15,11.361977011082937,58.34634424109216,42.10788277658241
Co-Pt,0,-0.1,11.94451802944034,44.46496618264527,39.26707413231709
Co-Pt,0,-0.05,12.556926564492933,32.23642975931229,34.43499643928375
Co-Pt,0,0.0,13.200733956567706,25.986339346342906,33.24971454631742
Co-Pt,0,0.05,13.877550059489144,20.846991185785672,24.76621280445244
Co-Pt,0,0.1,14.589067266052309,17.977665552612017,20.978144745883437
Co-Pt,0,0.15,15.337064739886372,17.019465805606963,18.62402567904017
Co-Pt,0,0.2,16.123412864290408,14.797815979957583,15.771033444699343
Co-Pt,0,0.3,17.81912699774054,11.765861652188997,10.713389660427369
Co-Pt,0,0.4,19.69318094339947,6.686882391156082,5.605325835661524
Co-Pt,1,-0.4,8.848716593470693,176.44469228008614,-20.17794236021182
Co-Pt,1,-0.3,9.779344241397222,112.60646411965064,-7.399677896408269
Co-Pt,1,-0.2,10.807846853442765,80.93880328195266,31.890175402783694
Co-Pt,1,-0.15,11.361977011082937,65.29411201631596,40.817739178861636
Co-Pt,1,-0.1,11.94451802944034,50.4816996949993,37.6897611238387
Co-Pt,1,-0.05,12.556926564492933,37.411841831177405,33.40241674127073
Co-Pt,1,0.0,13.200733956567706,30.377241206856027,32.75314394836096
Co-Pt,1,0.05,13.877550059489144,24.578015804346155,23.835190710795803
Co-Pt,1,0.1,14.589067266052309,21.109290812319827,20.248419093960724
Co-Pt,1,0.15,15.337064739886372,19.649634442486217,18.045448295446057
Co-Pt,1,0.2,16.123412864290408,16.8990700059038,15.33577729547351
Co-Pt,1,0.3,17.81912699774054,13.190109710658676,10.463965757703942
Co-Pt,1,0.4,19.69318094339947,7.471960830795967,5.566845377357981
Co-Pt,2,-0.4,8.848716593470693,167.7734149595396,-12.747149600315536
Co-Pt,2,-0.3,9.779344241397222,104.0574624330496,-3.987655016993581
Co-Pt,2,-0.2,10.807846853442765,73.90121201411988,32.10006844525481
Co-Pt,2,-0.15,11.361977011082937,59.04094130181095,40.560659925928135
Co-Pt,2,-0.1,11.94451802944034,44.93127103431865,36.95191074184284
Co-Pt,2,-0.05,12.556926564492933,32.768378790980584,33.53894133454024
Co-Pt,2,0.0,13.200733956567706,26.522805956930764,33.556035898423254
Co-Pt,2,0.05,13.877550059489144,21.18042535026283,24.28445365361013
Co-Pt,2,0.1,14.589067266052309,18.09376542139034,20.563741482530418
Co-Pt,2,0.15,15.337064739886372,17.137188064779355,18.2845505729048
Co-Pt,2,0.2,16.123412864290408,14.89606025186037,15.508283238370819
Co-Pt,2,0.3,17.81912699774054,11.866130580292705,10.507621735965197
Co-Pt,2,0.4,19.69318094339947,6.487197958663369,5.437491930549915
Co-Rh,0,-0.4,8.300206516696713,-90.74132337109575,-7.563367155996036
Co-Rh,0,-0.3,9.17314685627518,-38.13368164563631,-31.334911473609562
Co-Rh,0,-0.2,10.13789513279238,-14.393284117037847,-20.200011125021355
Co-Rh,0,-0.15,10.657676131195803,-10.173059813074921,-10.623353957958425
Co-Rh,0,-0.1,11.204106871262793,-8.851826094464785,-3.8956568684629236
Co-Rh,0,-0.05,11.778553714466582,-13.85198546770765,-11.214527317982913
Co-Rh,0,0.0,12.382453077131174,-18.51765947702439,-17.099257446165737
Co-Rh,0,0.05,13.017315022220362,-18.538551161420408,-12.32515104273233
Co-Rh,0,0.1,13.68472703528169,-16.541718979786975,-9.719509023304743
Co-Rh,0,0.15,14.386357993987197,-13.216242135469262,-7.276907276721113
Co-Rh,0,0.2,15.123962341196899,-8.765300732531683,-4.639637272004274
Co-Rh,0,0.3,16.714563345562098,-0.9847568349127847,-0.5634655090715142
Co-Rh,0,0.4,18.472449317848433,1.7032213309775759,1.9381521165635438
Co-Rh,1,-0.4,8.300206516696713,-84.33176607441737,-13.43246964143941
Co-Rh,1,-0.3,9.17314685627518,-32.01749296648255,-35.2899535818047
Co-Rh,1,-0.2,10.13789513279238,-9.621638051922476,-22.397261563867893
Co-Rh,1,-0.15,10.657676131195803,-6.040859814703555,-12.14708568886572
Co-Rh,1,-0.1,11.204106871262793,-5.220921237140313,-4.607791669860618
Co-Rh,1,-0.05,11.778553714466582,-10.786091223880595,-12.003032542991075
Co-Rh,1,0.0,12.382453077131174,-15.88662079329801,-17.92568620998429
Co-Rh,1,0.05,13.017315022220362,-16.097540484960508,-12.566974033621419
Co-Rh,1,0.1,13.68472703528169,-14.387027856887842,-10.199488316196499
Co-Rh,1,0.15,14.386357993987197,-11.292135897023757,-7.757856231855545
Co-Rh,1,0.2,15.123962341196899,-7.124549000882417,-5.0697630686366
Co-Rh,1,0.3,16.714563345562098,0.1831474263780856,-0.9613895301842491
Co-Rh,1,0.4,18.472449317848433,2.59862650371356,1.7381460002117142
Co-Rh,2,-0.4,8.300206516696713,-81.96212191851083,-9.71326521635944
Co-Rh,2,-0.3,9.17314685627518,-31.09845673434794,-31.901898832252012
Co-Rh,2,-0.2,10.13789513279238,-10.03288576758302,-20.124594915255397
Co-Rh,2,-0.15,10.657676131195803,-6.497240271923809,-10.1497030824839
Co-Rh,2,-0.1,11.204106871262793,-5.958684875069999,-3.3293435114600314
Co-Rh,2,-0.05,11.778553714466582,-11.458347555304627,-10.586793804048986
Co-Rh,2,0.0,12.382453077131174,-16.53169353150797,-16.551859665695634
Co-Rh,2,0.05,13.017315022220362,-16.787954634392936,-11.31602321981971
Co-Rh,2,0.1,13.68472703528169,-15.120796701083975,-8.956026884533468
Co-Rh,2,0.15,14.386357993987197,-12.16715185939962,-6.663544593354488
Co-Rh,2,0.2,15.123962341196899,-8.020367824317457,-4.123661874189543
Co-Rh,2,0.3,16.714563345562098,-0.7940577443550589,-0.3635039518643919
Co-Rh,2,0.4,18.472449317848433,2.0490783580087006,2.136483085395237
Cu-Ir,0,-0.4,8.815219543017006,-129.5674771871215,-72.83165010244068
Cu-Ir,0,-0.3,9.742324275394495,-81.13627980929708,-99.19301541152856
Cu-Ir,0,-0.2,10.766933463628403,-57.68034040717663,-94.4111982927611
Cu-Ir,0,-0.15,11.318965946916332,-76.84580764271014,-107.67713734105334
Cu-Ir,0,-0.1,11.899301740857615,-83.61556593213537,-94.03614053748488
Cu-Ir,0,-0.05,12.509391987220516,-87.60718694091193,-97.79408977652099
Cu-Ir,0,0.0,13.150762229402762,-80.19374383182327,-82.72188737360392
Cu-Ir,0,0.05,13.82501622708465,-64.52255438165955,-48.19899722749975
Cu-Ir,0,0.1,14.533839966463603,-54.05638344361921,-40.15136112128353
Cu-Ir,0,0.15,15.279005876097866,-45.40184155444764,-33.526269201875174
Cu-Ir,0,0.2,16.06237725890112,-35.543529447751816,-26.868212100650066
Cu-Ir,0,0.3,17.751672221697152,-20.469674431255775,-15.895666389934306
Cu-Ir,0,0.4,19.618631886631015,-10.115870717540835,-7.624731669880611
Cu-Ir,1,-0.4,8.815219543017006,-122.43929084817047,-81.1814690741639
Cu-Ir,1,-0.3,9.742324275394495,-75.25675684607553,-105.23378085000421
Cu-Ir,1,-0.2,10.766933463628403,-53.530577180101076,-98.66495021621023
Cu-Ir,1,-0.15,11.318965946916332,-73.60936578843575,-110.55389091346242
Cu-Ir,1,-0.1,11.899301740857615,-81.64049159830508,-96.32602039972099
Cu-Ir,1,-0.05,12.509391987220516,-86.51930595549763,-99.46714561215204
Cu-Ir,1,0.0,13.150762229402762,-79.84221566854285,-83.62431759900082
Cu-Ir,1,0.05,13.82501622708465,-64.66336621407669,-48.673563216285636
Cu-Ir,1,0.1,14.533839966463603,-54.31565483447566,-40.43143929724504
Cu-Ir,1,0.15,15.279005876097866,-45.868480474656174,-33.7101658599106
Cu-Ir,1,0.2,16.06237725890112,-36.18277827945425,-26.979856204930904
Cu-Ir,1,0.3,17.751672221697152,-21.04700192967076,-15.712060471176411
Cu-Ir,1,0.4,19.618631886631015,-10.252457250691846,-7.109164555297976
Cu-Ir,2,-0.4,8.815219543017006,-115.51500521195723,-68.54800326192588
Cu-Ir,2,-0.3,9.742324275394495,-68.51785351293937,-95.53497985626407
Cu-Ir,2,-0.2,10.766933463628403,-48.04168996211609,-91.33836591663255
Cu-Ir,2,-0.15,11.318965946916332,-68.28321184264446,-104.1296189318415
Cu-Ir,2,-0.1,11.899301740857615,-76.36496165073986,-90.72242179416935
Cu-Ir,2,-0.05,12.509391987220516,-81.37517400664237,-94.52316214774015
Cu-Ir,2,0.0,13.150762229402762,-75.00991550996089,-79.51566247460093
Cu-Ir,2,0.05,13.82501622708465,-60.24284278154502,-45.11621089774171
Cu-Ir,2,0.1,14.533839966463603,-50.334135971186676,-37.467473665780226
Cu-Ir,2,0.15,15.279005876097866,-42.33208475572238,-31.24963921083924
Cu-Ir,2,0.2,16.06237725890112,-33.150992590862614,-25.006781490290766
Cu-Ir,2,0.3,17.751672221697152,-19.252768544008703,-14.682495367955033
Cu-Ir,2,0.4,19.618631886631015,-9.469684263513791,-6.858717361400684
Cu-Ni,0,-0.4,7.679133236696804,35.96324975781991,-10.520240288718837
Cu-Ni,0,-0.3,8.486754729225426,18.517434787278187,-8.181943205016694
Cu-Ni,0,-0.2,9.379314515580909,9.92066559453874,-5.166049935524128
Cu-Ni,0,-0.15,9.860202254050298,9.274843525006256,-4.674340039033512
Cu-Ni,0,-0.1,10.3657456341048,3.4800184072468663,-6.654794315735708
Cu-Ni,0,-0.05,10.897208777520339,2.2823860498071444,-3.9272547423753275
Cu-Ni,0,0.0,11.455920618982239,2.1662350796381094,0.07417020758608579
Cu-Ni,0,0.05,12.04327822911416,0.18619290169769198,-3.2543410437501654
Cu-Ni,0,0.1,12.660750307882344,2.165534431150935,7.0911252414433
Cu-Ni,0,0.15,13.309880857110553,1.355119158345099,6.398886226476426
Cu-Ni,0,0.2,13.992293041288866,-0.9517036295003528,-0.5582212886988144
Cu-Ni,0,0.3,15.463875346424713,0.10474929240860753,-0.41703025972641944
Cu-Ni,0,0.4,17.090225313615573,1.386264093669095,-0.23410058829286834
Cu-Ni,1,-0.4,7.679133236696804,35.23864657416922,-10.827708852889518
Cu-Ni,1,-0.3,8.486754729225426,17.938111944904268,-8.35340662105909
Cu-Ni,1,-0.2,9.379314515580909,9.309242696731623,-5.267662237740186
Cu-Ni,1,-0.15,9.860202254050298,8.751042025952508,-4.7233553662173495
Cu-Ni,1,-0.1,10.3657456341048,2.8708431591178023,-6.735189703410525
Cu-Ni,1,-0.05,10.897208777520339,1.78087452557087,-3.8443041714254655
Cu-Ni,1,0.0,11.455920618982239,1.772688826696256,0.2890069467726501
Cu-Ni,1,0.05,12.04327822911416,-0.1488546458818044,-3.2075081145311968
Cu-Ni,1,0.1,12.660750307882344,1.9017819867479517,7.235572740915568
Cu-Ni,1,0.15,13.309880857110553,1.0933460181620818,6.578849043092864
Cu-Ni,1,0.2,13.992293041288866,-1.2382732641462266,-0.41754551932428197
Cu-Ni,1,0.3,15.463875346424713,-0.20018840961966888,-0.30134143253345785
Cu-Ni,1,0.4,17.090225313615573,1.0719260827981523,-0.1619137438971086
Cu-Ni,2,-0.4,7.679133236696804,35.52550596295944,-10.548555295824746
Cu-Ni,2,-0.3,8.486754729225426,18.775106946211512,-7.710414961600995
Cu-Ni,2,-0.2,9.379314515580909,10.158592442213289,-4.5369760627124105
Cu-Ni,2,-0.15,9.860202254050298,9.437504675079966,-4.106045038397277
Cu-Ni,2,-0.1,10.3657456341048,3.6959990423436087,-6.224648646880844
Cu-Ni,2,-0.05,10.897208777520339,2.4781195989088802,-3.6378759947986774
Cu-Ni,2,0.0,11.455920618982239,2.3375851136897006,0.21685937933410038
Cu-Ni,2,0.05,12.04327822911416,0.3695128403062576,-3.209404609948338
Cu-Ni,2,0.1,12.660750307882344,2.31948621650781,6.963498122972273
Cu-Ni,2,0.15,13.309880857110553,1.4906985050735513,6.368004061852575
Cu-Ni,2,0.2,13.992293041288866,-0.845185047001128,-0.45256322975078833
Cu-Ni,2,0.3,15.463875346424713,0.05488648025952299,-0.3507548377067865
Cu-Ni,2,0.4,17.090225313615573,1.2215586491293338,-0.2190901754601608
Cu-Pd,0,-0.4,9.1639898169774,16.52567649523246,-5.485499453454357
Cu-Pd,0,-0.3,10.1277750392648,15.529625054910511,-6.75200343543685
Cu-Pd,0,-0.2,11.192922438207907,11.318440674215312,-4.522286776031484
Cu-Pd,0,-0.15,11.766795843266626,6.905680108570985,0.33477419959950416
Cu-Pd,0,-0.1,12.370092366983748,2.6589207253213543,2.199826162353193
Cu-Pd,0,-0.05,13.004320564911692,-2.8365235425589104,-3.6212953484213504
Cu-Pd,0,0.0,13.67106633789999,-2.9716045012779384,3.2810775624219244
Cu-Pd,0,0.05,14.37199689767348,-2.4576124585497117,4.848756702574902
Cu-Pd,0,0.1,15.108864935730015,-1.548783089044224,5.173109125038239
Cu-Pd,0,0.15,15.883513005982158,-1.400765282484178,4.781063201959534
Cu-Pd,0,0.2,16.6978781321017,1.4178376560580956,5.610170838346461
Cu-Pd,0,0.3,18.454009305170118,-3.0709099826325907,1.9824995271633095
Cu-Pd,0,0.4,20.3948344059714,-2.8039826496504188,0.183617371493584
Cu-Pd,1,-0.4,9.1639898169774,22.321841917189225,-8.3817375417961
Cu-Pd,1,-0.3,10.1277750392648,20.623631029146143,-8.846545090818623
Cu-Pd,1,-0.2,11.192922438207907,15.323607986719514,-5.7973119404813405
Cu-Pd,1,-0.15,11.766795843266626,10.383550037618882,-0.9300778373687564
Cu-Pd,1,-0.1,12.370092366983748,5.696992039106505,1.135367435645846
Cu-Pd,1,-0.05,13.004320564911692,-0.009759473473861255,-3.9193832739506305
Cu-Pd,1,0.0,13.67106633789999,-0.5356171465078672,2.6997189439669866
Cu-Pd,1,0.05,14.37199689767348,-0.42838635714684903,4.247879571181148
Cu-Pd,1,0.1,15.108864935730015,0.1619955670251953,4.587000966310749
Cu-Pd,1,0.15,15.883513005982158,0.08621640151519676,4.217424774027196
Cu-Pd,1,0.2,16.6978781321017,2.5739709130051303,5.086656897442922
Cu-Pd,1,0.3,18.454009305170118,-2.0781197195150596,1.5460382902036593
Cu-Pd,1,0.4,20.3948344059714,-2.10898501469176,-0.18042821255529432
Cu-Pd,2,-0.4,9.1639898169774,19.212336026098523,-5.030218353101323
Cu-Pd,2,-0.3,10.1277750392648,18.014965753873764,-5.945777887984735
Cu-Pd,2,-0.2,11.192922438207907,13.31325924377935,-3.634971929221147
Cu-Pd,2,-0.15,11.766795843266626,8.633205873507382,0.5644374057925424
Cu-Pd,2,-0.1,12.370092366983748,4.230703155468744,2.3437466885053206
Cu-Pd,2,-0.05,13.004320564911692,-1.1288085421338219,-2.445707563604459
Cu-Pd,2,0.0,13.67106633789999,-1.5333487500193297,3.804986615459029
Cu-Pd,2,0.05,14.37199689767348,-1.3086833587369473,5.182066989979675
Cu-Pd,2,0.1,15.108864935730015,-0.601902690042593,5.412642972532003
Cu-Pd,2,0.15,15.883513005982158,-0.5453319159691375,4.959250015091362
Cu-Pd,2,0.2,16.6978781321017,1.9762291742010385,5.705350410160156
Cu-Pd,2,0.3,18.454009305170118,-2.4907725177377062,2.0601445094312556
Cu-Pd,2,0.4,20.3948344059714,-2.506676827836953,0.21814843519012508
Cu-Pt,0,-0.4,9.223118166077898,148.28315734919767,-22.41547411030023
Cu-Pt,0,-0.3,10.193121971124494,58.64027917265853,-26.690983432626282
Cu-Pt,0,-0.2,11.26514196688471,18.799481826949126,-7.6647006416812715
Cu-Pt,0,-0.15,11.84271814635845,8.513670668092564,-3.131743544829156
Cu-Pt,0,-0.1,12.449907289794483,0.2833483249286476,-1.0204244816321824
Cu-Pt,0,-0.05,13.088227686322101,-2.2385517969845825,2.9178394645193837
Cu-Pt,0,0.0,13.759275469418867,-1.9538183585019775,7.05440877096798
Cu-Pt,0,0.05,14.464728608075706,-0.5731467922789433,7.587150800192992
Cu-Pt,0,0.1,15.206351102593388,1.5649118517095433,7.9930693583819235
Cu-Pt,0,0.15,15.98599739550211,3.2153215403214,7.734014588970775
Cu-Pt,0,0.2,16.80561700863377,4.605912858013604,7.191848078212868
Cu-Pt,0,0.3,18.573079178259505,4.679794099923455,4.4291163912608456
Cu-Pt,0,0.4,20.52642696692875,4.137647308164952,1.8757390454616898
Cu-Pt,1,-0.4,9.223118166077898,165.77055887159403,-28.473704879323876
Cu-Pt,1,-0.3,10.193121971124494,72.74248682770678,-30.922147158182643
Cu-Pt,1,-0.2,11.26514196688471,29.53071446726542,-10.30969719657001
Cu-Pt,1,-0.15,11.84271814635845,17.612973575035642,-5.191640090920636
Cu-Pt,1,-0.1,12.449907289794483,7.770438879253902,-2.863884560072588
Cu-Pt,1,-0.05,13.088227686322101,3.7329929426036577,1.7197553382603488
Cu-Pt,1,0.0,13.759275469418867,2.812498040713265,6.131871224486475
Cu-Pt,1,0.05,14.464728608075706,3.2110638928085278,6.865908795201261
Cu-Pt,1,0.1,15.206351102593388,4.619561863824097,7.422217622048235
Cu-Pt,1,0.15,15.98599739550211,5.695402210823334,7.289023621716338
Cu-Pt,1,0.2,16.80561700863377,6.689846842748727,6.866798704132685
Cu-Pt,1,0.3,18.573079178259505,6.1603363623613285,4.301600267967938
Cu-Pt,1,0.4,20.52642696692875,5.166360783309977,1.8443702065313947
Cu-Pt,2,-0.4,9.223118166077898,155.81370124787057,-19.944115532745762
Cu-Pt,2,-0.3,10.193121971124494,63.3765321313035,-25.693622653120872
Cu-Pt,2,-0.2,11.26514196688471,22.729728984171093,-6.7471945352056135
Cu-Pt,2,-0.15,11.84271814635845,11.810096279449125,-3.446028361129611
Cu-Pt,2,-0.1,12.449907289794483,3.3691787820409393,-0.7093407896530276
Cu-Pt,2,-0.05,13.088227686322101,0.8645958702073745,5.042575330797804
Cu-Pt,2,0.0,13.759275469418867,0.4678531039437008,8.187794215617552
Cu-Pt,2,0.05,14.464728608075706,1.2579221068960225,8.506782608289042
Cu-Pt,2,0.1,15.206351102593388,3.0369832777949317,8.733242803042433
Cu-Pt,2,0.15,15.98599739550211,4.3817006249154025,8.310272206372622
Cu-Pt,2,0.2,16.80561700863377,5.273101697648407,7.644325491408062
Cu-Pt,2,0.3,18.573079178259505,5.084540602496671,4.678173922945561
Cu-Pt,2,0.4,20.52642696692875,4.144217271708361,2.0266900879624523
Cu-Rh,0,-0.4,8.674608089303918,-67.3688550542129,-40.11555234356552
Cu-Rh,0,-0.3,9.58692458600245,-40.479410817558694,-50.72468702044379
Cu-Rh,0,-0.2,10.595190246234326,-40.255173729309874,-52.02545826472819
Cu-Rh,0,-0.15,11.138417266471317,-42.78525314584717,-48.30732186748997
Cu-Rh,0,-0.1,11.709496131616936,-46.20078603143524,-53.43264721402689
Cu-Rh,0,-0.05,12.30985483629575,-46.37963935248264,-51.94185167462829
Cu-Rh,0,0.0,12.940994589982335,-41.46736660935086,-37.85776987953348
Cu-Rh,0,0.05,13.604493570806925,-36.157411453098476,-26.996145936191883
Cu-Rh,0,0.1,14.302010871822768,-31.018827338677497,-20.927418251870886
Cu-Rh,0,0.15,15.035290649602935,-24.53316519355947,-16.06884017872528
Cu-Rh,0,0.2,15.80616648554026,-18.581083524719983,-12.176061330519161
Cu-Rh,0,0.3,17.468515526081063,-7.539063823040232,-5.304878155411007
Cu-Rh,0,0.4,19.305695341377714,-3.0440021937118606,-1.1661671617609886
Cu-Rh,1,-0.4,8.674608089303918,-66.56992198883508,-45.466451565908365
Cu-Rh,1,-0.3,9.58692458600245,-39.98350080235237,-53.91691121436861
Cu-Rh,1,-0.2,10.595190246234326,-40.448760878101375,-54.09108911990049
Cu-Rh,1,-0.15,11.138417266471317,-43.053579367778305,-49.77772234711169
Cu-Rh,1,-0.1,11.709496131616936,-46.535286252077015,-54.506323962790724
Cu-Rh,1,-0.05,12.30985483629575,-46.75488610532396,-52.68693009046761
Cu-Rh,1,0.0,12.940994589982335,-41.86860240128977,-38.104518280282925
Cu-Rh,1,0.05,13.604493570806925,-36.551897875000805,-27.10108507658386
Cu-Rh,1,0.1,14.302010871822768,-31.360436858309797,-20.941698309350063
Cu-Rh,1,0.15,15.035290649602935,-24.931124803440476,-16.057146544568628
Cu-Rh,1,0.2,15.80616648554026,-19.1693507564115,-12.191048236459048
Cu-Rh,1,0.3,17.468515526081063,-7.9733119295364485,-5.291154443642999
Cu-Rh,1,0.4,19.305695341377714,-3.3228742301244383,-1.0645162220315167
Cu-Rh,2,-0.4,8.674608089303918,-58.79482395399013,-38.58099604025175
Cu-Rh,2,-0.3,9.58692458600245,-33.086268529980465,-48.49394060426106
Cu-Rh,2,-0.2,10.595190246234326,-34.71136103462069,-49.97732052161318
Cu-Rh,2,-0.15,11.138417266471317,-37.889524393807406,-45.99401844489237
Cu-Rh,2,-0.1,11.709496131616936,-42.0543802341354,-51.440579551363804
Cu-Rh,2,-0.05,12.30985483629575,-42.78076388597704,-50.151093004184034
Cu-Rh,2,0.0,12.940994589982335,-38.287282151506425,-35.85759581184193
Cu-Rh,2,0.05,13.604493570806925,-33.57680671419772,-25.383842552284683
Cu-Rh,2,0.1,14.302010871822768,-28.822789357885735,-19.586592411885572
Cu-Rh,2,0.15,15.035290649602935,-22.71735220023182,-14.991752797540936
Cu-Rh,2,0.2,15.80616648554026,-17.225865615429313,-11.331473295682702
Cu-Rh,2,0.3,17.468515526081063,-6.710881366127128,-4.806780520087393
Cu-Rh,2,0.4,19.305695341377714,-2.5646223570737066,-0.8476987560149947
Ir-Ni,0,-0.4,8.456478569532386,-213.16319705306572,-24.878009828557605
Ir-Ni,0,-0.3,9.345854184377146,-107.17334011426094,-79.76461572549424
Ir-Ni,0,-0.2,10.328766249149222,-55.0872258704911,-74.81227298268564
Ir-Ni,0,-0.15,10.858333418954777,-56.66218025131698,-78.45796453700129
Ir-Ni,0,-0.1,11.41505207816101,-66.25638313826532,-81.18992555573652
Ir-Ni,0,-0.05,12.000314313397737,-69.54092711618179,-69.51702877039573
Ir-Ni,0,0.0,12.615583585102533,-71.69646826368884,-74.05201104361208
Ir-Ni,0,0.05,13.262398386934112,-63.26917995676961,-58.836320557578375
Ir-Ni,0,0.1,13.942376092807837,-51.1474664265411,-37.74383065294266
Ir-Ni,0,0.15,14.65721700117296,-41.3466366395318,-32.196210020488884
Ir-Ni,0,0.2,15.408708586644398,-33.1211641819623,-26.788022293205955
Ir-Ni,0,0.3,17.029256615061904,-15.031465891252621,-14.043802128355344
Ir-Ni,0,0.4,18.82023916741376,-12.7589472417102,-8.406969019146421
Ir-Ni,1,-0.4,8.456478569532386,-204.1653642114986,-36.034331149529265
Ir-Ni,1,-0.3,9.345854184377146,-98.48136014914846,-88.16371463511928
Ir-Ni,1,-0.2,10.328766249149222,-48.108656250252416,-80.94988282601706
Ir-Ni,1,-0.15,10.858333418954777,-50.13457040544257,-83.18078217287649
Ir-Ni,1,-0.1,11.41505207816101,-60.271335759614125,-84.44360639111888
Ir-Ni,1,-0.05,12.000314313397737,-64.35658460695052,-72.39317558516682
Ir-Ni,1,0.0,12.615583585102533,-67.5491237862991,-76.27232983955857
Ir-Ni,1,0.05,13.262398386934112,-60.2204096109592,-60.17302854679505
Ir-Ni,1,0.1,13.942376092807837,-48.826280004494045,-38.96372232259728
Ir-Ni,1,0.15,14.65721700117296,-39.398624486515175,-33.204853569353105
Ir-Ni,1,0.2,15.408708586644398,-31.75560137459505,-27.472766459690387
Ir-Ni,1,0.3,17.029256615061904,-14.0097322359363,-14.425673386121165
Ir-Ni,1,0.4,18.82023916741376,-12.155838940320482,-8.647918964215231
Ir-Ni,2,-0.4,8.456478569532386,-201.97983448223061,-23.669596471384427
Ir-Ni,2,-0.3,9.345854184377146,-98.17059099977924,-78.10206761166471
Ir-Ni,2,-0.2,10.328766249149222,-48.451148011887405,-72.66125272944835
Ir-Ni,2,-0.15,10.858333418954777,-50.625026169696476,-76.15216940532804
Ir-Ni,2,-0.1,11.41505207816101,-60.90845072280981,-78.94772386013311
Ir-Ni,2,-0.05,12.000314313397737,-64.7947771493504,-67.26134356969764
Ir-Ni,2,0.0,12.615583585102533,-68.00232143891525,-72.60026912568448
Ir-Ni,2,0.05,13.262398386934112,-60.54407534964592,-57.447896609884125
Ir-Ni,2,0.1,13.942376092807837,-49.11543977528417,-36.476481933923715
Ir-Ni,2,0.15,14.65721700117296,-39.73768473977516,-31.21042810908768
Ir-Ni,2,0.2,15.408708586644398,-32.084020248220234,-25.907806931607684
Ir-Ni,2,0.3,17.029256615061904,-14.384950490812226,-13.467009984321482
Ir-Ni,2,0.4,18.82023916741376,-12.692499590679047,-8.003171496010273
Ir-Pd,0,-0.4,9.941335149812982,-31.943340494327714,-44.16462842403102
Ir-Pd,0,-0.3,10.986874494416519,-9.880673899553202,-37.194113627375756
Ir-Pd,0,-0.2,12.14237417177622,-23.406674634540618,-28.324068753137485
Ir-Pd,0,-0.15,12.764927008171105,-30.29163894426746,-50.105619485687455
Ir-Pd,0,-0.1,13.419398811039956,-22.95990421081703,-30.076302294622987
Ir-Pd,0,-0.05,14.10742610078909,-16.77573380730189,-16.82511029171996
Ir-Pd,0,0.0,14.830729304020284,-13.779463014324596,-15.685465457126226
Ir-Pd,0,0.05,15.591117055493433,-13.5609301304149,-15.157023900913108
Ir-Pd,0,0.1,16.39049072065551,-10.43415289093832,-12.396515424012708
Ir-Pd,0,0.15,17.230849150044563,-8.967528060153601,-10.119994091645328
Ir-Pd,0,0.2,18.11429367745723,-12.822372146477067,-10.126423553810286
Ir-Pd,0,0.3,20.019390573807307,-9.278210397497812,-5.747997165635324
Ir-Pd,0,0.4,22.12484825976959,-4.006024148769867,-3.650811531833361
Ir-Pd,1,-0.4,9.941335149812982,-32.81282160294888,-44.41581850132767
Ir-Pd,1,-0.3,10.986874494416519,-9.750598797591907,-37.13341969915339
Ir-Pd,1,-0.2,12.14237417177622,-22.921518111285422,-28.023202909185382
Ir-Pd,1,-0.15,12.764927008171105,-30.244493803527615,-51.436747867383914
Ir-Pd,1,-0.1,13.419398811039956,-23.428700778301035,-30.90502145687114
Ir-Pd,1,-0.05,14.10742610078909,-17.069241217987926,-17.190087274033388
Ir-Pd,1,0.0,14.830729304020284,-13.719926072577211,-16.026424119239127
Ir-Pd,1,0.05,15.591117055493433,-13.893099792571778,-15.347783203725271
Ir-Pd,1,0.1,16.39049072065551,-10.483502764917931,-12.560602566235897
Ir-Pd,1,0.15,17.230849150044563,-9.08027400701266,-10.228125963123261
Ir-Pd,1,0.2,18.11429367745723,-13.430875849706215,-10.179025669924883
Ir-Pd,1,0.3,20.019390573807307,-9.514071708271523,-5.79839655007648
Ir-Pd,1,0.4,22.12484825976959,-4.277458268296533,-3.639275697603093
Ir-Pd,2,-0.4,9.941335149812982,-30.109830969984948,-42.15204675578133
Ir-Pd,2,-0.3,10.986874494416519,-7.5015364446504895,-35.897339827040554
Ir-Pd,2,-0.2,12.14237417177622,-20.762057249420703,-26.695280765097454
Ir-Pd,2,-0.15,12.764927008171105,-28.363292623894036,-50.25330657628356
Ir-Pd,2,-0.1,13.419398811039956,-21.645501541008855,-29.823309333541864
Ir-Pd,2,-0.05,14.10742610078909,-15.662674597100903,-16.141387346027482
Ir-Pd,2,0.0,14.830729304020284,-12.757956098672562,-15.135494648422764
Ir-Pd,2,0.05,15.591117055493433,-13.07532009173592,-14.771924617087572
Ir-Pd,2,0.1,16.39049072065551,-9.939906281013647,-12.102721905173961
Ir-Pd,2,0.15,17.230849150044563,-8.671668195635792,-9.874354122038891
Ir-Pd,2,0.2,18.11429367745723,-12.95133751186063,-9.957586516623053
Ir-Pd,2,0.3,20.019390573807307,-9.165830371722816,-5.513921635777139
Ir-Pd,2,0.4,22.12484825976959,-4.132825109938889,-3.4996806968361507
Ir-Pt,0,-0.4,10.00046349891348,18.857725787021902,4.011764692007472
Ir-Pt,0,-0.3,11.052221426276214,14.56851378579683,5.08193090247967
Ir-Pt,0,-0.2,12.214593700453026,3.3073271166281577,7.145653051387462
Ir-Pt,0,-0.15,12.840849311262929,-4.688554017192999,-9.255573566327831
Ir-Pt,0,-0.1,13.499213733850691,-4.1826792079842825,-2.3373448328788013
Ir-Pt,0,-0.05,14.191333222199498,-4.425582357546697,-1.2282899118900157
Ir-Pt,0,0.0,14.918938435539161,-5.590773183123461,-3.321855383690063
Ir-Pt,0,0.05,15.68384876589566,-6.541368628311955,-4.906975819364116
Ir-Pt,0,0.1,16.487976887518883,-6.318553402525448,-5.405670709923194
Ir-Pt,0,0.15,17.333333539564517,-6.348925068482188,-5.574598641912791
Ir-Pt,0,0.2,18.2220325539893,-7.183428497395251,-5.481002306359524
Ir-Pt,0,0.3,20.138460446896694,-7.414584211575215,-4.157021903010061
Ir-Pt,0,0.4,22.256440820726937,-5.0581401598616855,-2.534718900051752
Ir-Pt,1,-0.4,10.00046349891348,17.089011263034692,4.4367695888540775
Ir-Pt,1,-0.3,11.052221426276214,12.732253969116591,5.524330452159186
Ir-Pt,1,-0.2,12.214593700453026,1.837014112658714,7.489453722163997
Ir-Pt,1,-0.15,12.840849311262929,-5.62817721977568,-8.807223441425728
Ir-Pt,1,-0.1,13.499213733850691,-5.39087901026588,-2.1854061232290336
Ir-Pt,1,-0.05,14.191333222199498,-5.47318617223594,-1.18517144455071
Ir-Pt,1,0.0,14.918938435539161,-6.367370687433188,-3.3815493040578435
Ir-Pt,1,0.05,15.68384876589566,-7.335757748296498,-5.0065039699377625
Ir-Pt,1,0.1,16.487976887518883,-6.752882532814729,-5.565256400639364
Ir-Pt,1,0.15,17.333333539564517,-6.748136267547563,-5.711684383503662
Ir-Pt,1,0.2,18.2220325539893,-7.72709949782526,-5.606502430014647
Ir-Pt,1,0.3,20.138460446896694,-7.391035861732885,-4.322370444458979
Ir-Pt,1,0.4,22.256440820726937,-5.036800750273138,-2.6339273129454304
Ir-Pt,2,-0.4,10.00046349891348,16.893838412144547,5.227799861928096
Ir-Pt,2,-0.3,11.052221426276214,13.997578934544773,4.94533679265325
Ir-Pt,2,-0.2,12.214593700453026,3.7614348495996928,7.2182204345571215
Ir-Pt,2,-0.15,12.840849311262929,-4.040856476737265,-9.816876325275542
Ir-Pt,2,-0.1,13.499213733850691,-3.6842642459479977,-2.640474587316186
Ir-Pt,2,-0.05,14.191333222199498,-3.88941156801151,-1.2101464712072019
Ir-Pt,2,0.0,14.918938435539161,-4.9822901844126335,-3.2607377587624278
Ir-Pt,2,0.05,15.68384876589566,-6.153246134711865,-4.89084181835709
Ir-Pt,2,0.1,16.487976887518883,-5.8032209548018505,-5.27309724977013
Ir-Pt,2,0.15,17.333333539564517,-6.046154662616509,-5.437606834227175
Ir-Pt,2,0.2,18.2220325539893,-7.188717827592874,-5.433035325814702
Ir-Pt,2,0.3,20.138460446896694,-7.1734164486850105,-3.9768795317081094
Ir-Pt,2,0.4,22.256440820726937,-4.915856199344136,-2.4151228181005036
Ir-Rh,0,-0.4,9.4519534221395,46.904454637751996,5.266769255629187
Ir-Rh,0,-0.3,10.44602404115417,27.131144389445115,3.7535587491937776
Ir-Rh,0,-0.2,11.54464197980264,7.949370472842737,1.5765939732972003
Ir-Rh,0,-0.15,12.136548431375795,4.5850713520770245,7.848167303357005
Ir-Rh,0,-0.1,12.758802575673146,-2.3135496830697035,-8.754827856577345
Ir-Rh,0,-0.05,13.412960372173147,-1.5590325528713647,-4.718416814052785
Ir-Rh,0,0.0,14.100657556102629,0.7509534446250127,-0.5676501052467016
Ir-Rh,0,0.05,14.82361372862688,2.048875501937324,-0.540258936457541
Ir-Rh,0,0.1,15.583636656748261,1.9873347895069369,-0.7433215558422636
Ir-Rh,0,0.15,16.38262679366534,3.016098959242389,0.025449259640155146
Ir-Rh,0,0.2,17.22258203089579,2.7325036128831055,0.5516394815531044
Ir-Rh,0,0.3,19.033896794718252,-0.4328047819595147,0.32612999700706563
Ir-Rh,0,0.4,21.035709195175897,-2.721296282112098,-0.09235711222765458
Ir-Rh,1,-0.4,9.4519534221395,47.2320065295049,5.8086845217901475
Ir-Rh,1,-0.3,10.44602404115417,28.285699805163937,4.686922705538234
Ir-Rh,1,-0.2,11.54464197980264,8.729201404781874,2.0874767446214286
Ir-Rh,1,-0.15,12.136548431375795,5.2218605175017565,8.459687031090164
Ir-Rh,1,-0.1,12.758802575673146,-2.228278378602503,-9.0740929475464
Ir-Rh,1,-0.05,13.412960372173147,-1.616302195047018,-4.906509537375983
Ir-Rh,1,0.0,14.100657556102629,0.7304988208208787,-0.6350789292136065
Ir-Rh,1,0.05,14.82361372862688,2.1000920704705037,-0.632872079772702
Ir-Rh,1,0.1,15.583636656748261,1.9928769356450435,-0.8347379312868082
Ir-Rh,1,0.15,16.38262679366534,3.103869334525571,-0.06312114817758442
Ir-Rh,1,0.2,17.22258203089579,2.8824181159972038,0.4749575629537919
Ir-Rh,1,0.3,19.033896794718252,-0.27423053550617565,0.27842825705543006
Ir-Rh,1,0.4,21.035709195175897,-2.5023920672558604,-0.10792711841566936
Ir-Rh,2,-0.4,9.4519534221395,44.88602565216737,4.613087841807541
Ir-Rh,2,-0.3,10.44602404115417,26.081768300898332,3.2957842172475504
Ir-Rh,2,-0.2,11.54464197980264,7.408848114808767,1.4003844193217627
Ir-Rh,2,-0.15,12.136548431375795,4.076587961460504,7.205423236804491
Ir-Rh,2,-0.1,12.758802575673146,-2.520016335067924,-8.446549599975523
Ir-Rh,2,-0.05,13.412960372173147,-1.7353620569597774,-4.450217872252756
Ir-Rh,2,0.0,14.100657556102629,0.5554373273054104,-0.6086427276814882
Ir-Rh,2,0.05,14.82361372862688,1.8831080824010593,-0.6170632232160151
Ir-Rh,2,0.1,15.583636656748261,1.8466057963599025,-0.8381687564904736
Ir-Rh,2,0.15,16.38262679366534,2.9062321025506024,-0.11023243167621194
Ir-Rh,2,0.2,17.22258203089579,2.6440592261364886,0.40286256584358
Ir-Rh,2,0.3,19.033896794718252,-0.4450291482540528,0.234295883671833
Ir-Rh,2,0.4,21.035709195175897,-2.692650445476316,-0.12524816434200298
Ni-Pd,0,-0.4,8.805248843492778,-9.048209872103142,-6.968440349296511
Ni-Pd,0,-0.3,9.731304948247448,-6.197923268391925,-3.863272280781007
Ni-Pd,0,-0.2,10.754755223728724,3.6433671186668986,-5.916642051589142
Ni-Pd,0,-0.15,11.306163315305069,4.6713526209558465,-1.4493207557173142
Ni-Pd,0,-0.1,11.88584270428714,1.5744076461227687,-3.162649805962711
Ni-Pd,0,-0.05,12.49524289108891,0.06911360104237495,1.100875974696786
Ni-Pd,0,0.0,13.13588769359976,-0.6934149037155342,4.908375251514339
Ni-Pd,0,0.05,13.809379057522941,-1.4499679393359814,3.088099302361483
Ni-Pd,0,0.1,14.51740106207425,-1.0702999561328614,3.098680806137177
Ni-Pd,0,0.15,15.26172413105725,-0.036129674089619396,3.475161071460554
Ni-Pd,0,0.2,16.04420945984498,0.35249496255992835,3.48426163149195
Ni-Pd,0,0.3,17.731593698534866,-1.4832524910315676,2.13448599938965
Ni-Pd,0,0.4,19.596441686754144,-1.8791528336680208,1.1140558295591576
Ni-Pd,1,-0.4,8.805248843492778,-4.253641068449463,-9.883789402555356
Ni-Pd,1,-0.3,9.731304948247448,-1.6290121536135713,-5.764275516225519
Ni-Pd,1,-0.2,10.754755223728724,7.143499463467852,-7.660059016740398
Ni-Pd,1,-0.15,11.306163315305069,7.809706769785492,-2.599140434175154
Ni-Pd,1,-0.1,11.88584270428714,4.21580006213602,-4.660094082794948
Ni-Pd,1,-0.05,12.49524289108891,2.39580608477383,0.09241133028629749
Ni-Pd,1,0.0,13.13588769359976,1.370836037994323,4.562753774539531
Ni-Pd,1,0.05,13.809379057522941,0.23421482398262594,2.4083383144345927
Ni-Pd,1,0.1,14.51740106207425,0.368266322714706,2.478368103831177
Ni-Pd,1,0.15,15.26172413105725,1.1822895250953174,2.930753846256082
Ni-Pd,1,0.2,16.04420945984498,1.4213892206447136,3.0071516035429924
Ni-Pd,1,0.3,17.731593698534866,-0.6766669681373332,1.7687540730454956
Ni-Pd,1,0.4,19.596441686754144,-1.3111303437581263,0.8441635562246051
Ni-Pd,2,-0.4,8.805248843492778,-6.68675011958823,-6.598717333380955
Ni-Pd,2,-0.3,9.731304948247448,-4.212827438020788,-3.421182557435256
Ni-Pd,2,-0.2,10.754755223728724,5.021622432358222,-5.849338540564297
Ni-Pd,2,-0.15,11.306163315305069,5.899674454020358,-1.298025511944314
Ni-Pd,2,-0.1,11.88584270428714,2.6996149803179343,-3.3147345862896467
Ni-Pd,2,-0.05,12.49524289108891,1.05646764320361,1.0142702400416803
Ni-Pd,2,0.0,13.13588769359976,0.09837902560879892,5.000508736101006
Ni-Pd,2,0.05,13.809379057522941,-0.7937175305902052,3.064446091500076
Ni-Pd,2,0.1,14.51740106207425,-0.5187135780613713,3.0231766211774986
Ni-Pd,2,0.15,15.26172413105725,0.4269552469101995,3.3925795562815586
Ni-Pd,2,0.2,16.04420945984498,0.7763761402259466,3.408619522236033
Ni-Pd,2,0.3,17.731593698534866,-1.1598414387189702,2.1044200166012295
Ni-Pd,2,0.4,19.596441686754144,-1.6352944464039254,1.0950487332527101
Ni-Pt,0,-0.4,8.864377192593277,84.6385005486791,-31.879644204545798
Ni-Pt,0,-0.3,9.796651880107143,30.01414860614134,-29.996630427940616
Ni-Pt,0,-0.2,10.826974752405532,11.455700546865703,-9.702355409506206
Ni-Pt,0,-0.15,11.382085618396895,4.921116447116195,-1.1059011511407741
Ni-Pt,0,-0.1,11.965657627097878,0.4767937852060486,-0.25522106958144486
Ni-Pt,0,-0.05,12.579150012499321,-1.3533543779567205,5.505081863646287
Ni-Pt,0,0.0,13.224096825118638,-0.7519542851895172,10.222893573014737
Ni-Pt,0,0.05,13.90211076792517,-0.7683272102119344,6.886659143140209
Ni-Pt,0,0.1,14.614887228937622,1.0165470031828303,6.5559407883873835
Ni-Pt,0,0.15,15.364208520577204,3.756488428499105,7.223590378201224
Ni-Pt,0,0.2,16.15194833637705,4.574536860965248,6.994497506969158
Ni-Pt,0,0.3,17.850663571624253,2.9391409531305817,4.755232453804971
Ni-Pt,0,0.4,19.728034247711495,1.2732179441499851,2.1578600813222404
Ni-Pt,1,-0.4,8.864377192593277,98.88068672794128,-40.3300160388979
Ni-Pt,1,-0.3,9.796651880107143,42.40483011328887,-34.75039474111878
Ni-Pt,1,-0.2,10.826974752405532,20.91930399629514,-13.641960462979812
Ni-Pt,1,-0.15,11.382085618396895,13.267231742931415,-3.7576245044995606
Ni-Pt,1,-0.1,11.965657627097878,7.44613752340476,-3.644779368657482
Ni-Pt,1,-0.05,12.579150012499321,4.636200238042952,3.913296247314613
Ni-Pt,1,0.0,13.224096825118638,4.2138816055027855,9.943428394417449
Ni-Pt,1,0.05,13.90211076792517,3.0413491256888094,5.858968613665202
Ni-Pt,1,0.1,14.614887228937622,3.8722441031297596,5.815014481054659
Ni-Pt,1,0.15,15.364208520577204,6.175801642843125,6.655887745516214
Ni-Pt,1,0.2,16.15194833637705,6.4966383930078795,6.5908958357566085
Ni-Pt,1,0.3,17.850663571624253,4.4856053859160285,4.545975860833835
Ni-Pt,1,0.4,19.728034247711495,2.0571450222064995,2.121051011180881
Ni-Pt,2,-0.4,8.864377192593277,91.1100177665069,-29.949560065892097
Ni-Pt,2,-0.3,9.796651880107143,34.24091145650465,-29.375529308847934
Ni-Pt,2,-0.2,10.826974752405532,14.579954701966322,-10.39223251383926
Ni-Pt,2,-0.15,11.382085618396895,7.779531728632193,-1.4451057533525844
Ni-Pt,2,-0.1,11.965657627097878,2.946218786983739,-1.5601674624710595
Ni-Pt,2,-0.05,12.579150012499321,0.8449244615026317,5.511969604570851
Ni-Pt,2,0.0,13.224096825118638,1.1413728275726194,11.235353026628959
Ni-Pt,2,0.05,13.90211076792517,0.5424888214599736,6.936947007355636
Ni-Pt,2,0.1,14.614887228937622,1.7927427944852434,6.581907839260563
Ni-Pt,2,0.15,15.364208520577204,4.386750606584603,7.203565616899587
Ni-Pt,2,0.2,16.15194833637705,5.025184806099568,6.981510214448113
Ni-Pt,2,0.3,17.850663571624253,3.4149287134353687,4.728573696570143
Ni-Pt,2,0.4,19.728034247711495,1.3571492090912294,2.171244486730349
Ni-Rh,0,-0.4,8.315867115819298,-137.7298759314249,-8.109429940718519
Ni-Rh,0,-0.3,9.1904544949851,-86.18650699030579,-42.376170777499766
Ni-Rh,0,-0.2,10.157023031755145,-52.32731287776198,-40.43186734791174
Ni-Rh,0,-0.15,10.677784738509759,-48.9209644966507,-40.761477764006024
Ni-Rh,0,-0.1,11.225246468920332,-42.847247657012005,-33.41101761164301
Ni-Rh,0,-0.05,11.80077716247297,-42.07408634341992,-41.35625969488578
Ni-Rh,0,0.0,12.405815945682106,-38.373165785502465,-35.94363352817949
Ni-Rh,0,0.05,13.04187573065639,-31.318340977865226,-21.334268840578453
Ni-Rh,0,0.1,13.710546998167002,-27.405568294450745,-19.928456334471655
Ni-Rh,0,0.15,14.413501774678029,-22.713963677742772,-16.204513163822327
Ni-Rh,0,0.2,15.15249781328354,-16.38640067280861,-11.832658524835818
Ni-Rh,0,0.3,16.746099919445815,-5.94206316311337,-4.810717513733241
Ni-Rh,0,0.4,18.507302622160456,-3.205714092205125,-1.3297811754860778
Ni-Rh,1,-0.4,8.315867115819298,-134.75352895245564,-14.262979324179902
Ni-Rh,1,-0.3,9.1904544949851,-83.11173888086923,-46.22180022888343
Ni-Rh,1,-0.2,10.157023031755145,-49.92241970030444,-42.860687499139495
Ni-Rh,1,-0.15,10.677784738509759,-46.83317135018912,-42.86269367487779
Ni-Rh,1,-0.1,11.225246468920332,-40.93544406175055,-34.83018470269476
Ni-Rh,1,-0.05,11.80077716247297,-40.41700680549215,-42.713666947541036
Ni-Rh,1,0.0,12.405815945682106,-36.99963160826775,-37.02009621367784
Ni-Rh,1,0.05,13.04187573065639,-30.22449562187925,-21.792775802542344
Ni-Rh,1,0.1,13.710546998167002,-26.62267919632638,-20.450922869796624
Ni-Rh,1,0.15,14.413501774678029,-21.996069443891113,-16.67367163680125
Ni-Rh,1,0.2,15.15249781328354,-15.801311331023358,-12.242440553069747
Ni-Rh,1,0.3,16.746099919445815,-5.287943770596791,-5.182191368303732
Ni-Rh,1,0.4,18.507302622160456,-2.7461882279907024,-1.538183639781703
Ni-Rh,2,-0.4,8.315867115819298,-127.64252156469622,-7.620262714553684
Ni-Rh,2,-0.3,9.1904544949851,-78.02042989682344,-40.607738014356656
Ni-Rh,2,-0.2,10.157023031755145,-46.80285653608156,-38.700810486884755
Ni-Rh,2,-0.15,10.677784738509759,-43.929287029164875,-38.82246883834688
Ni-Rh,2,-0.1,11.225246468920332,-38.700025570118335,-31.858859430946534
Ni-Rh,2,-0.05,11.80077716247297,-38.462313202578216,-39.68390740507361
Ni-Rh,2,0.0,12.405815945682106,-35.43086730971316,-34.72615990844918
Ni-Rh,2,0.05,13.04187573065639,-29.217578899816317,-20.91758820244723
Ni-Rh,2,0.1,13.710546998167002,-25.684991314912377,-19.150362493191086
Ni-Rh,2,0.15,14.413501774678029,-21.296986556220332,-15.509361439530586
Ni-Rh,2,0.2,15.15249781328354,-15.332092831805673,-11.269415014134253
Ni-Rh,2,0.3,16.746099919445815,-5.331411466855399,-4.531516317211947
Ni-Rh,2,0.4,18.507302622160456,-2.9114019319510454,-1.1338593549791052
Pd-Pt,0,-0.4,10.349233772873873,39.00341231895713,0.05998826806732331
Pd-Pt,0,-0.3,11.437672190146516,13.702405748662748,-1.2241720532385707
Pd-Pt,0,-0.2,12.64058267503253,7.059167490448088,-3.7602532350397353
Pd-Pt,0,-0.15,13.288679207613223,7.083315162283816,-0.5847989539989429
Pd-Pt,0,-0.1,13.970004359976826,7.455024832110663,3.736681692635135
Pd-Pt,0,-0.05,14.686261799890675,7.201099011339582,3.4943080637507915
Pd-Pt,0,0.0,15.43924254403639,6.292247574663176,3.1299689316272845
Pd-Pt,0,0.05,16.23082943648449,5.701157892518661,3.0098759265779917
Pd-Pt,0,0.1,17.063001856785295,5.307406109818292,2.770066359158721
Pd-Pt,0,0.15,17.93784066944881,3.1904917329557527,1.6385865047235189
Pd-Pt,0,0.2,18.857533427189885,2.3142447465271845,1.3292751090229715
Pd-Pt,0,0.3,20.84079753036966,1.304946403944176,0.5283156248122033
Pd-Pt,0,0.4,23.032643340067324,1.1807591179248396,0.33252341403435315
Pd-Pt,1,-0.4,10.349233772873873,40.76343691060156,-0.4813173935534769
Pd-Pt,1,-0.3,11.437672190146516,14.798427655615438,-1.7272436708000083
Pd-Pt,1,-0.2,12.64058267503253,7.559892103577589,-4.2268374954199315
Pd-Pt,1,-0.15,13.288679207613223,7.207102738688377,-0.9674179586692904
Pd-Pt,1,-0.1,13.970004359976826,7.382221724760495,3.8034010075653972
Pd-Pt,1,-0.05,14.686261799890675,7.024674092748389,3.648719488532899
Pd-Pt,1,0.0,15.43924254403639,5.978720037158416,3.338542815887255
Pd-Pt,1,0.05,16.23082943648449,5.332005281000668,3.2592978951686042
Pd-Pt,1,0.1,17.063001856785295,4.966725646232222,3.0304073635097755
Pd-Pt,1,0.15,17.93784066944881,2.7770355628466143,1.8980819598806178
Pd-Pt,1,0.2,18.857533427189885,1.9831697680214688,1.5743271535143037
Pd-Pt,1,0.3,20.84079753036966,1.041545138043954,0.719747344516407
Pd-Pt,1,0.4,23.032643340067324,0.9907749739201334,0.5050670113427894
Pd-Pt,2,-0.4,10.349233772873873,38.76236981413359,-0.3826949554546281
Pd-Pt,2,-0.3,11.437672190146516,13.80591653133879,-1.680873208192
Pd-Pt,2,-0.2,12.64058267503253,7.1964579850003,-4.04024701533224
Pd-Pt,2,-0.15,13.288679207613223,7.061966571109775,-0.7868926223188549
Pd-Pt,2,-0.1,13.970004359976826,7.2644125446513295,3.607403104502879
Pd-Pt,2,-0.05,14.686261799890675,6.928410770467851,3.385898652570924
Pd-Pt,2,0.0,15.43924254403639,6.01923221521067,3.0187380672365483
Pd-Pt,2,0.05,16.23082943648449,5.414480857187577,2.9152138191893915
Pd-Pt,2,0.1,17.063001856785295,5.015645199299456,2.698795063073044
Pd-Pt,2,0.15,17.93784066944881,2.9608601009337576,1.5658881321546287
Pd-Pt,2,0.2,18.857533427189885,2.086513706381217,1.2811384274496622
Pd-Pt,2,0.3,20.84079753036966,1.1086278882688618,0.5043107342062134
Pd-Pt,2,0.4,23.032643340067324,1.0429727402593632,0.32374404820723574
Pd-Rh,0,-0.4,9.800723696099894,-22.47158501703129,-23.08154756979195
Pd-Rh,0,-0.3,10.831474805024474,-13.511110984750857,-15.155377450837916
Pd-Rh,0,-0.2,11.970630954382143,-16.890205545519766,-21.435915870524315
Pd-Rh,0,-0.15,12.584378327726087,-13.634476630474078,-15.468228009363449
Pd-Rh,0,-0.1,13.229593201799279,-10.166547377287612,-9.859576922068605
Pd-Rh,0,-0.05,13.907888949864324,-8.075495190914419,-7.504277270775159
Pd-Rh,0,0.0,14.620961664599857,-6.8068041382920645,-6.797496650823985
Pd-Rh,0,0.05,15.37059439921571,-5.312274080280043,-5.712744941517464
Pd-Rh,0,0.1,16.158661626014673,-4.574893732079674,-4.767636506094518
Pd-Rh,0,0.15,16.98713392354963,-3.646455126364411,-3.8779983146279537
Pd-Rh,0,0.2,17.858082904096374,-3.120227891024921,-2.9931944352760564
Pd-Rh,0,0.3,19.736233878191218,-2.270329053319697,-1.7041061216918898
Pd-Rh,0,0.4,21.811911714516288,-0.7803591962622632,-0.9727194677335769
Pd-Rh,1,-0.4,9.800723696099894,-24.93588247186966,-23.135014676779385
Pd-Rh,1,-0.3,10.831474805024474,-15.209591687068466,-15.12191469506648
Pd-Rh,1,-0.2,11.970630954382143,-18.149659740361358,-21.480557411674177
Pd-Rh,1,-0.15,12.584378327726087,-14.67411724846338,-15.279813661824194
Pd-Rh,1,-0.1,13.229593201799279,-11.090862626984286,-9.671533651236846
Pd-Rh,1,-0.05,13.907888949864324,-8.910736970005214,-7.558850469162353
Pd-Rh,1,0.0,14.620961664599857,-7.443099875776818,-6.865308300901736
Pd-Rh,1,0.05,15.37059439921571,-5.887935260376388,-5.737975208445635
Pd-Rh,1,0.1,16.158661626014673,-5.049303431741491,-4.75776668813945
Pd-Rh,1,0.15,16.98713392354963,-4.004426907212035,-3.84782394602338
Pd-Rh,1,0.2,17.858082904096374,-3.4719744676191353,-2.900437255029457
Pd-Rh,1,0.3,19.736233878191218,-2.560743201458412,-1.5723702544372264
Pd-Rh,1,0.4,21.811911714516288,-1.0427494880460153,-0.8280484651898168
Pd-Rh,2,-0.4,9.800723696099894,-21.348626320385392,-22.10925698554054
Pd-Rh,2,-0.3,10.831474805024474,-12.431267189890805,-14.950905555575167
Pd-Rh,2,-0.2,11.970630954382143,-15.799377386964053,-20.977673887361796
Pd-Rh,2,-0.15,12.584378327726087,-12.819453813821331,-15.579041546270924
Pd-Rh,2,-0.1,13.229593201799279,-9.645609745272889,-10.157413548055034
Pd-Rh,2,-0.05,13.907888949864324,-7.637053807520953,-7.371195916688116
Pd-Rh,2,0.0,14.620961664599857,-6.422479491504456,-6.6724189498477635
Pd-Rh,2,0.05,15.37059439921571,-5.139589892742805,-5.664354036646686
Pd-Rh,2,0.1,16.158661626014673,-4.493447771380184,-4.746700470111837
Pd-Rh,2,0.15,16.98713392354963,-3.509570956109277,-3.8144703139697693
Pd-Rh,2,0.2,17.858082904096374,-3.1499581007923463,-2.991901099909537
Pd-Rh,2,0.3,19.736233878191218,-2.193354991988971,-1.5989122151778514
Pd-Rh,2,0.4,21.811911714516288,-0.7801151297270789,-0.8847787150057446
Pt-Rh,0,-0.4,9.859852045200391,36.37028836567184,-2.297123145969615
Pt-Rh,0,-0.3,10.896821736884169,22.805827713043158,13.602218625812638
Pt-Rh,0,-0.2,12.042850483058949,8.68455190851263,5.122576327828488
Pt-Rh,0,-0.15,12.660300630817911,7.997317082465205,10.716460562886335
Pt-Rh,0,-0.1,13.309408124610014,8.336950857402284,12.315060438741497
Pt-Rh,0,-0.05,13.991796071274733,6.385123711620121,7.284304020707654
Pt-Rh,0,0.0,14.709170796118734,4.2877567876866856,5.350644335191342
Pt-Rh,0,0.05,15.463326109617936,3.953127982081642,4.3356905573101745
Pt-Rh,0,0.1,16.256147792878046,2.631358709145878,2.9630256819875984
Pt-Rh,0,0.15,17.089618313069586,1.5791219121774456,1.5968157460351364
Pt-Rh,0,0.2,17.965821780628442,2.896826378763477,1.7693444657237276
Pt-Rh,0,0.3,19.855303751280605,0.39836430325467137,0.45472326732433543
Pt-Rh,0,0.4,21.943504275473636,-0.17644894107331405,0.6284406576649421
Pt-Rh,1,-0.4,9.859852045200391,36.0803338453937,-2.309548599812124
Pt-Rh,1,-0.3,10.896821736884169,22.207482457822127,13.907521310047816
Pt-Rh,1,-0.2,12.042850483058949,7.770116683725987,5.25682987125323
Pt-Rh,1,-0.15,12.660300630817911,7.187932573329595,11.312076074141475
Pt-Rh,1,-0.1,13.309408124610014,7.399793148612307,12.949883066715511
Pt-Rh,1,-0.05,13.991796071274733,5.437327584372123,7.782299805374014
Pt-Rh,1,0.0,14.709170796118734,3.4801291899235505,5.80689547068625
Pt-Rh,1,0.05,15.463326109617936,3.2075688194699614,4.749995290258106
Pt-Rh,1,0.1,16.256147792878046,2.0381666226395687,3.329253023869651
Pt-Rh,1,0.15,17.089618313069586,1.1144072200832416,1.9168046734703392
Pt-Rh,1,0.2,17.965821780628442,2.432538062437743,2.0319267109883494
Pt-Rh,1,0.3,19.855303751280605,0.07335914315107046,0.6686878796909914
Pt-Rh,1,0.4,21.943504275473636,-0.45885442614661015,0.7986038453907146
Pt-Rh,2,-0.4,9.859852045200391,35.94249710019363,-2.167902655622681
Pt-Rh,2,-0.3,10.896821736884169,22.35878842277425,13.16383161365344
Pt-Rh,2,-0.2,12.042850483058949,8.346062836117417,4.614079558984605
Pt-Rh,2,-0.15,12.660300630817911,7.6521307288634866,10.087888591896709
Pt-Rh,2,-0.1,13.309408124610014,7.984858073703107,11.841663546273866
Pt-Rh,2,-0.05,13.991796071274733,6.116738725734401,6.9424418871502045
Pt-Rh,2,0.0,14.709170796118734,4.155382264182509,5.089584412526836
Pt-Rh,2,0.05,15.463326109617936,3.801927643108989,4.110912510408177
Pt-Rh,2,0.1,16.256147792878046,2.565079305351355,2.803166929792184
Pt-Rh,2,0.15,17.089618313069586,1.5971260631356032,1.517925223096464
Pt-Rh,2,0.2,17.965821780628442,2.8230559631640753,1.6896516619649533
Pt-Rh,2,0.3,19.855303751280605,0.4195760968335401,0.479130272429511
Pt-Rh,2,0.4,21.943504275473636,-0.1743888187232919,0.6630296797524189


exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content data/hm_shear_clamped.csv -Raw' in C:\Users\can02\Projects\AI driven Science
 succeeded in 389ms:
comp,n_el,V0,K44,Kp,time
Cu:0.1111;Ir:0.2685;Ni:0.6204,3,11.94978861424134,-54.20079542116013,-55.224767834782185,2026-10-31T19:39:16
Au:0.2037;Ir:0.3611;Pd:0.2407;Rh:0.1944,4,15.213192702943054,-16.375493218240656,-16.950609473613955,2026-10-31T19:39:29
Au:0.4074;Cu:0.2130;Pt:0.3796,3,15.748955644407335,6.078173723678074,6.306101604588543,2026-10-31T19:39:39
Cu:0.3611;Ni:0.3426;Pd:0.2963,3,12.619943344626295,-0.2916627145876994,3.076496516451004,2026-10-31T19:39:50
Ag:0.1296;Au:0.1667;Co:0.2685;Ir:0.1019;Ni:0.3333,5,13.317246229446562,-13.421838121832529,-8.941871658244551,2026-10-31T19:40:03
Ag:0.1019;Co:0.1204;Cu:0.5278;Pt:0.1204;Rh:0.1296,5,13.125888529794505,-12.707971584557908,-7.624265708124541,2026-10-31T19:40:15
Au:0.1204;Co:0.4074;Cu:0.3426;Pt:0.1296,4,12.70815731147092,3.953727444987571,6.345689905685805,2026-10-31T19:40:27
Cu:0.4259;Ir:0.4074;Rh:0.1667,3,13.25268774999902,-68.43122407648413,-66.71825518439655,2026-10-31T19:40:38
Au:0.5926;Ni:0.2870;Rh:0.1204,3,15.426141323230768,-2.5602501387941365,-2.849229106073083,2026-10-31T19:40:48
Ag:0.3056;Au:0.1111;Co:0.1759;Ir:0.4074,4,15.185911624430105,-22.160513574079268,-23.099352703324385,2026-10-31T19:40:59
Ag:0.3148;Au:0.1204;Co:0.3148;Ir:0.1296;Ni:0.1204,5,14.366526726780815,-9.472907071320266,-9.930051947608533,2026-10-31T19:41:11
Ag:0.2963;Au:0.1852;Pt:0.5185,3,16.656044189055716,14.790197291302894,8.094723680365957,2026-10-31T19:41:21
Au:0.2037;Ni:0.6019;Pd:0.1944,3,13.2077509125982,3.1719140105145316,5.393755400202467,2026-10-31T19:41:32
Ag:0.1759;Au:0.2778;Rh:0.5463,3,15.705003466162205,-7.070614172764743,-9.883967873827405,2026-10-31T19:41:42
Ag:0.1111;Ni:0.4537;Pt:0.4352,3,13.69441438281571,1.348078287046025,5.81004789185321,2026-10-31T19:41:52
Au:0.5833;Ir:0.2407;Rh:0.1759,3,16.340695589930206,-11.345556837545834,-12.691758508248007,2026-10-31T19:42:02
Au:0.2407;Co:0.1944;Cu:0.1296;Pt:0.1852;Rh:0.2500,5,14.329719248039257,-2.8111835444168625,-1.1084622699428885,2026-10-31T19:42:14
Au:0.3889;Ir:0.4722;Pt:0.1389,3,15.883255622945413,-19.917847879910624,-18.552319376616634,2026-10-31T19:42:24
Ag:0.2778;Au:0.2685;Co:0.1111;Ni:0.1389;Pt:0.2037,5,15.655680222453226,8.643948444252505,4.719440855002749,2026-10-31T19:42:35
Au:0.2037;Cu:0.3704;Pd:0.3148;Rh:0.1111,4,14.467601777767428,-4.5457841585628165,-0.6747471580819249,2026-10-31T19:42:46
Ag:0.2315;Au:0.1111;Co:0.3611;Rh:0.2963,4,14.163570338649246,-8.725081588172603,-8.133301288611072,2026-10-31T19:42:57
Ag:0.1944;Au:0.2500;Pd:0.1759;Pt:0.3796,4,16.542757293605288,13.140629604690567,7.588615980526209,2026-10-31T19:43:07
Co:0.2315;Ir:0.6111;Rh:0.1574,3,13.448861668869723,-20.614893585201543,-18.362858592009825,2026-10-31T19:43:18
Co:0.3241;Cu:0.3519;Pt:0.2037;Rh:0.1204,4,12.57934154562797,-8.137312013433117,-6.94213050458972,2026-10-31T19:43:30
Ag:0.2870;Co:0.3704;Pd:0.3426,3,14.407345168046083,5.296620105455871,6.383593812427618,2026-10-31T19:43:40
Au:0.4537;Ni:0.2593;Pt:0.2870,3,15.418456466517071,5.553980909007053,3.7369106903739904,2026-10-31T19:43:50
Cu:0.1759;Ir:0.2130;Pt:0.6111,3,14.64618064598962,-6.073336730829489,-1.826143784890575,2026-10-31T19:44:00
Ag:0.1111;Co:0.1111;Ir:0.6667;Rh:0.1111,4,14.274268331294598,-22.638791597196256,-18.06691590975176,2026-10-31T19:44:11
Cu:0.1204;Pd:0.2685;Pt:0.1389;Rh:0.4722,4,14.281522078952122,-9.515602319635772,-6.455602510789042,2026-10-31T19:44:22
Au:0.1759;Co:0.5833;Cu:0.1204;Pd:0.1204,4,12.786944309282832,6.52830960035742,9.52296580567938,2026-10-31T19:44:34
Ag:0.2870;Co:0.1944;Ni:0.3426;Pt:0.1759,4,13.706979213359705,3.6199690834221534,4.425343635414349,2026-10-31T19:44:45
Ag:0.2407;Cu:0.3056;Ni:0.1204;Rh:0.3333,4,13.903481551774316,-21.110588589536142,-18.31605031725299,2026-10-31T19:44:57
Ag:0.6574;Ni:0.1019;Pd:0.2407,3,16.536441516807713,3.861816040937756,3.526043198716264,2026-10-31T19:45:07
Au:0.3981;Ir:0.2778;Pt:0.3241,3,16.141857531146073,-8.840897783964541,-9.591039976554729,2026-10-31T19:45:17
Cu:0.7593;Ni:0.1389;Pd:0.1019,3,12.186003035629243,-0.23935711679323365,0.47470426321767284,2026-10-31T19:45:28
Au:0.1574;Co:0.4352;Ir:0.2685;Pd:0.1389,4,13.527596398924924,-21.12974472298478,-14.370143888282472,2026-10-31T19:45:40
Au:0.4537;Ni:0.1667;Pd:0.3796,3,15.778069412168804,6.49988806683221,4.47295282520855,2026-10-31T19:45:50
Ag:0.1204;Cu:0.1019;Ir:0.7778,3,14.50058911522846,-33.1989323331291,-26.080064028817976,2026-10-31T19:46:00
Au:0.2963;Cu:0.1204;Rh:0.5833,3,14.855997054964185,-14.056645308457247,-13.247171883325294,2026-10-31T19:46:10
Co:0.4815;Ir:0.2500;Pt:0.2685,3,12.982565892162194,-9.93835402648605,-6.878134752155616,2026-10-31T19:46:21
Au:0.2037;Co:0.2407;Pt:0.1019;Rh:0.4537,4,14.152235211967035,-5.961139822617412,-3.587714457953573,2026-10-31T19:46:32
Ag:0.2222;Ir:0.3611;Ni:0.1759;Pd:0.2407,4,14.747700353244566,-23.802451321276774,-21.39973790267062,2026-10-31T19:46:43
Ag:0.2500;Cu:0.3056;Ni:0.1296;Rh:0.3148,4,13.912891518004082,-20.2957756319433,-17.289050168034684,2026-10-31T19:46:53
Au:0.2037;Co:0.2315;Ni:0.2315;Rh:0.3333,4,13.325635558012562,-12.6352511041677,-8.881783265385744,2026-10-31T19:47:05
Ag:0.3148;Co:0.2685;Ni:0.2130;Rh:0.2037,4,13.691688900996553,-10.308019779747596,-9.786082086410156,2026-10-31T19:47:16
Ag:0.2315;Co:0.1389;Pd:0.1296;Pt:0.5000,4,15.393794786362758,14.205848409475648,10.972941440433937,2026-10-31T19:47:27
Cu:0.3889;Ni:0.3148;Pd:0.1111;Pt:0.1852,4,12.68237193956398,-1.5173014064559818,3.012538399470321,2026-10-31T19:47:38
Au:0.1574;Co:0.2130;Cu:0.3333;Ni:0.2963,4,12.369231516488318,0.18928549173634024,1.7745711110523228,2026-10-31T19:47:50
Au:0.3611;Cu:0.2778;Pd:0.3611,3,15.345317789577058,3.282960939753673,5.4471274742874565,2026-10-31T19:48:00
Cu:0.4074;Ni:0.4907;Pd:0.1019,3,11.808252231573274,0.30411226827804344,-2.688693648185914,2026-10-31T19:48:11
Au:0.4167;Ir:0.3056;Pd:0.2778,3,16.10507038854169,-10.570573650789257,-11.903833066597429,2026-10-31T19:48:21
Co:0.4815;Cu:0.3611;Pd:0.1574,3,11.982077421496395,3.9412232994061993,3.3269316385972547,2026-10-31T19:48:31
Ni:0.2870;Pt:0.4537;Rh:0.2593,3,13.780965527328856,-4.014526218363165,1.6804231297388492,2026-10-31T19:48:42
Ag:0.1389;Co:0.2407;Ni:0.1481;Rh:0.4722,4,13.272120311247066,-21.481840312641072,-16.186336984051966,2026-10-31T19:48:53
Ir:0.1111;Pt:0.1111;Rh:0.7778,3,14.119322297572218,1.1850613791694582,1.826505596258236,2026-10-31T19:49:03
Au:0.2222;Ir:0.3519;Pd:0.3148;Rh:0.1111,4,15.393458274354758,-15.388165479447313,-16.19328065026759,2026-10-31T19:49:14
Co:0.1852;Cu:0.2315;Pd:0.5833,3,13.7440650761712,0.776863419976561,6.544704482639729,2026-10-31T19:49:24
Cu:0.5370;Ni:0.2870;Pd:0.1759,3,12.273720028378253,0.06738502241768467,-0.2592138192415616,2026-10-31T19:49:35
Ag:0.4537;Au:0.3981;Pt:0.1481,3,17.528017639256674,8.158438244676748,4.080003988957273,2026-10-31T19:49:45
Co:0.2407;Pd:0.3796;Pt:0.3796,3,14.338848647817967,15.637747967896047,14.667435456472155,2026-10-31T19:49:55
Ag:0.1944;Co:0.4815;Ni:0.3241,3,12.243527133737988,1.3960032296640368,3.0462083192676803,2026-10-31T19:50:06
Ni:0.5370;Pd:0.2963;Rh:0.1667,3,12.728560989644102,-13.48635584036199,-8.680275996547959,2026-10-31T19:50:17
Ag:0.4815;Ir:0.3704;Ni:0.1481,3,15.508348819249733,-21.611854223000993,-23.490377338103514,2026-10-31T19:50:27
Cu:0.1019;Ni:0.6296;Pt:0.2685,3,12.266712937074866,-1.8848819581061944,-2.9965278081402538,2026-10-31T19:50:38
Au:0.3333;Cu:0.3704;Ni:0.2963,3,13.650073704287541,-4.47288475425671,2.4674148472660162,2026-10-31T19:50:49
Au:0.2222;Pd:0.4537;Rh:0.3241,3,15.448637741302186,-2.4364805214520633,-5.195379951353661,2026-10-31T19:50:59
Ag:0.1111;Au:0.1296;Ni:0.3796;Pt:0.3796,4,14.344300356756639,3.210917147311569,4.678820445495399,2026-10-31T19:51:09
Au:0.2870;Pt:0.3148;Rh:0.3981,3,15.561061157055143,-1.0314943467791584,-3.2359944221008163,2026-10-31T19:51:19
Au:0.2500;Co:0.1111;Cu:0.6389,3,13.349230542260294,-3.57086630654398,0.7120158478585924,2026-10-31T19:51:30
Ag:0.2593;Ni:0.1204;Pd:0.1759;Pt:0.4444,4,15.54165551660623,10.334581518872785,7.514155738784122,2026-10-31T19:51:41
Co:0.1111;Pt:0.7778;Rh:0.1111,3,14.828632986985433,10.29854809023672,10.193960382253579,2026-10-31T19:51:51
Au:0.2685;Co:0.2870;Ni:0.3333;Pt:0.1111,4,13.297360897857772,6.262333327484401,12.620431225866739,2026-10-31T19:52:03
Ag:0.2500;Co:0.1667;Ir:0.2870;Rh:0.2963,4,14.495892497687278,-23.699806241320395,-21.15172769264694,2026-10-31T19:52:14
Ag:0.1667;Au:0.2407;Rh:0.5926,3,15.519181077881493,-7.81785825244133,-10.280602429803825,2026-10-31T19:52:24
Ag:0.1944;Cu:0.5833;Pt:0.2222,3,13.912883803929752,0.9907214702282927,1.6891714790996668,2026-10-31T19:52:35
Cu:0.3241;Pt:0.3519;Rh:0.3241,3,13.852462937854447,-11.506338487785605,-4.28007748897066,2026-10-31T19:52:45
Ag:0.4444;Au:0.3056;Cu:0.1019;Pd:0.1481,4,16.900257318894983,3.888952733159218,3.9349100936126393,2026-10-31T19:52:56
Co:0.5556;Cu:0.1574;Ni:0.1574;Rh:0.1296,4,11.448186565657153,-8.701809704924855,-7.978993807893352,2026-10-31T19:53:08
Au:0.4352;Co:0.1667;Pt:0.3981,3,15.792985423038235,10.501279255190378,7.38666770432032,2026-10-31T19:53:18
Ag:0.1759;Co:0.2500;Ir:0.3148;Ni:0.1111;Pd:0.1481,5,13.848427119543777,-27.554314946941105,-20.172766489138848,2026-10-31T19:53:30
Co:0.1389;Ni:0.2870;Pd:0.5741,3,13.457682084259922,2.9867237844872214,6.438861887201654,2026-10-31T19:53:41
Co:0.3519;Cu:0.2407;Ir:0.4074,3,12.542891131332636,-62.96898623955197,-68.4705416585423,2026-10-31T19:53:52
Ag:0.3333;Au:0.1667;Co:0.1944;Cu:0.3056,4,14.712042378385702,-2.7995090826129956,0.6945048060258269,2026-10-31T19:54:03
Cu:0.3889;Pt:0.2778;Rh:0.3333,3,13.606698188189982,-17.30978749949582,-9.392649074663327,2026-10-31T19:54:14
Ag:0.1019;Cu:0.4630;Rh:0.4352,3,13.415184519330378,-32.22105557032864,-26.908136511732273,2026-10-31T19:54:25
Ag:0.3704;Cu:0.4074;Pd:0.2222,3,14.904452124799425,-0.8589028817716213,2.7830293745589336,2026-10-31T19:54:35
Co:0.1019;Pd:0.5278;Pt:0.1481;Rh:0.2222,4,14.596509022372679,2.790950167741209,2.340867716058475,2026-10-31T19:54:46
Ag:0.4259;Cu:0.3519;Pt:0.2222,3,15.268317597329162,3.968384400595336,3.566908035328897,2026-10-31T19:54:56
Ag:0.3796;Ni:0.4259;Rh:0.1944,3,14.123948178507174,-11.196712051560567,-10.823611985144817,2026-10-31T19:55:06
Co:0.7500;Pt:0.1389;Rh:0.1111,3,11.85555308566313,8.983179141891947,5.7751530270011875,2026-10-31T19:55:17
Co:0.2500;Cu:0.1296;Ni:0.3056;Pd:0.3148,4,12.44243458963978,4.045744684451151,5.730620155640041,2026-10-31T19:55:29
Ag:0.2778;Au:0.6111;Ni:0.1111,3,17.120449696825826,3.045833251770154,1.7659057920313026,2026-10-31T19:55:39
Ag:0.1019;Au:0.1019;Ni:0.4352;Pd:0.1574;Rh:0.2037,5,13.64257782535617,-11.288983915586547,-8.704307888424399,2026-10-31T19:55:52
Ag:0.1759;Ni:0.1667;Pt:0.5556;Rh:0.1019,4,15.00124024744498,5.705833534154132,5.555867884582994,2026-10-31T19:56:03


web search: 
web search: https://www.osti.gov/servlets/purl/1462702/
codex
Mevcut CSV�?tlerden K�?� gǬrǬltǬ ��l��e�Yini yeniden hesaplad��m: toplam RMSE 1,892 GPa; Co�?tlu sat��rlarda 2,419, Co�?tsuzlarda 1,405 GPa. Tek bir s��f��r ortalamal�� Gaussian bu fark�� temsil etmiyor. Grid i��in de somut bir s��n��r a����Y�� var: ��ekim kurallar��n��n izin verdi�Yi Au�'%�'?Co�'%Ni�'% bile�Yiminde Co�?"Ni girdisi ln(V/Vij)=0,430 gerektiriyor; mevcut grid +0,40�?tta bitiyor. Bu bir kar�Y�� ��rnek; sabit 80�?tli ��ekimde bulundu�Yunu do�Yrulamad��m.

web search: 
web search: https://www.osti.gov/pages/servlets/purl/1462702
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$p='"'C:\\Users\\can02\\.codex\\memories\\MEMORY.md'; "'$t=Get-Content -Encoding UTF8 $p; 110..116 | ForEach-Object { '"'{0}: {1}' -f ("'$_+1),$t[$_] }; Get-Item scripts/k_asym_w1.py,scripts/k_shear_transfer.py,harness/context.py,harness/ledger.py,harness/power.py -ErrorAction SilentlyContinue | Select-Object Name,LastWriteTime,Length' in C:\Users\can02\Projects\AI driven Science
 succeeded in 434ms:
111: ## Task 3: Audit cobalt K44 controls, spin state, and matched MACE/PBE design, success/partial
112: 
113: ### rollout_summary_files
114: 
115: - rollout_summaries/2026-11-01T21-57-13-hXmh-audit_cobalt_anomaly_spin_mace_pbe_tests.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\02\rollout-2026-11-02T00-57-13-01a1991d-dbfb-72e3-85ce-9cf49c2550d9.jsonl, updated_at=2026-10-31T22:53:56+00:00, thread_id=01a1991d-dbfb-72e3-85ce-9cf49c2550d9, spin-control bug verified; experiments redesigned)
116: - rollout_summaries/2026-10-31T21-44-07-VJVR-validate_k44_shear_transfer_hypotheses.md (cwd=\\?\C:\Users\can02\Projects\AI driven Science, rollout_path=C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-8431-7393-ae70-82453cb5df2f.jsonl, updated_at=2026-10-31T20:57:09+00:00, thread_id=01a193eb-8431-7393-ae70-82453cb5df2f, direction/seed averaging retained; composition asymmetry dropped)
117: 

Name                LastWriteTime       Length
----                -------------       ------
k_asym_w1.py        3.11.2026 12:53:53   10433
k_shear_transfer.py 31.10.2026 19:38:10   9651
context.py          31.10.2026 09:40:58   2193
ledger.py           31.10.2026 09:34:56   3243
power.py            31.10.2026 09:34:56   1507



codex
**Mevcut sǬrǬm hesap ba�Ylatmaya uygun de�Yil.** En kritik hata [k_asym_w1.py:124](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:124>): `arm.endswith("sym")`, `"asym"` i��in de `True`. Dolay��s��yla:

- `OV-asym = OV-sym`: H1, belirtilen asimetrik rakibi kar�Y��la�Yt��rm��yor.
- `VV-asym = VV-sym`: H2�?tde kazan�� **0**, p **1**; gǬ�� **0** olur.
- Yeni 25:75 ve 75:25 hesaplar�� yap��l��yor fakat tahminlerde kullan��lm��yor.

Dosya de�Yi�Ytirmedim; MACE hesab�� veya yan etkili import ��al��Yt��rmad��m.

1. **OV-asym, Wu/Marker�?t��n adil temsilcisi mi?**

   **Bu haliyle yaln��z bir analog; y��ntemlerin yeniden uygulanmas�� de�Yil.** �o�� ayr�� fark var:

   - **Fit:** �o�� noktadan Ǭ�� RK katsay��s�� belirlemek cebirsel olarak ge��erli ama doygun interpolasyon: uyum hatas�� ve model derecesini do�Yrulayacak ba�Y��ms��z nokta kalm��yor. Wu, ikilileri `x=0,0.1,�?�,1` Ǭzerinde hesapl��yor; Eq. 5.1 ayr��ca on-site/inter-site yap��s�� i��eriyor. �o�� noktal�� Muggianu bunun birebir kar�Y��l��Y�� de�Yil. Bunu [��zgǬn tezde, ss. 43�?"44](C:/Users/can02/Downloads/etd.pdf) do�Yrulad��m.
   - **Hacim:** [Sat��r 123](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:123>) ikilinin **Vegard hacmini** kullan��yor; denge hacmini bulmuyor. Bu fark��n rakibi hangi y��nde etkiledi�Yi hesaplanmadan bilinemez.
   - **G��zlenebilir ve referans:** [curvatures():64](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_transfer.py:64>) ideal konumlarda, ayn�� hacimdeki saf referanslar�� ����kararak **clamped kar��Y��m e�Yrili�Yi** hesapl��yor. Bu, denge hacimlerindeki elastik sabitlerden ve onlar��n saf-element referanslar��ndan farkl��d��r. Taslak da ��n-gerilme katk��s��n�� a����k��a ay��r��yor: [draft_v5.md:61](<C:/Users/can02/Projects/AI driven Science/paper/draft_v5.md:61>).

   **DǬzeltme:** W1�?ti �?oikili Vegard hacmi / hedef Vegard hacmi �- simetrik / asimetrik temsil�?? kar�Y��la�Yt��rmas�� olarak s��n��rland��r; OV ad��n�� ��rne�Yin `BV` yap. Wu/Marker�?t�� ge��ti�Yi iddias�� i��in denge hacmi, relaksasyon ve referans tan��mlar�� e�Yle�Yen ayr�� benchmark gerekir. Marker�?t��n CALPHAD yakla�Y��m��n�� kaynak almak makul; mevcut kolu onun tam modeli diye adland��rmak de�Yil. [Marker 2017](https://www.sciencedirect.com/science/article/abs/pii/S0927025617304597)

   RK derecesini hedeflere bakmadan, ek ikili bile�Yimler ve ba�Y��ms��z seed kontrolleriyle se��. Ayr��ca H1 hem hacmi hem model esnekli�Yini de�Yi�Ytiriyor; **hacmin etkisini tek ba�Y��na** g��stermek i��in ayn�� derecedeki `VV-asym�?"BV-asym` kar�Y��la�Yt��rmas��n�� ��nceden belirlemek gerekir.

2. **H1/H2 gǬ�� hesab�� ger��ek��i mi; s��z��nt�� var m��?**

   [Sat��r 137�?"158](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:137>) gelecekteki W1 hedeflerini okumuyor: bu a����dan do�Yrudan hedef s��z��nt��s�� yok. Fakat gǬrǬltǬ modeli yeterince gerek��elendirilmi�Y de�Yil.

   Mevcut CSV�?tlerden ba�Y��ms��z spline hesab��yla yeniden buldu�Yum K�?� art��klar��:

   | hm grubu | n | RMSE |
   |---|---:|---:|
   | TǬmǬ | 94 | 1,892 GPa |
   | Co i��eren | 39 | 2,419 GPa |
   | Co i��ermeyen | 55 | 1,405 GPa |

   **Tek, s��f��r ortalamal�� iid Gaussian bu bile�Yim ba�Y��ml��l��Y��n�� siler.** `.orchestra/LESSONS.md:92�?"96` da art��Y��n bǬyǬk b��lǬmǬnǬn kompozisyon kaynakl�� oldu�Yunu s��ylǬyor.

   Ayr��ca hm hedefleri [seed 0](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_kp_hm.py:77>), girdiler seed 0�?"2: gǬrǬltǬ kalibrasyonu tarihsel ortak-seed protokolǬnden geliyor. Bunun K�?� gǬrǬltǬsǬnǬ mutlaka kǬ��ǬlttǬ�YǬnǬ s��yleyemem: yaln��z seed 1�?"2 girdileriyle RMSE **1,880 GPa** ����kt��. Ancak bu kontrol, yeni tasar��m��n gǬrǬltǬ modelini do�Yrulam��yor.

   H2�?tde kullan��lan `VV-sym` art��Y��, asimetri dǬzeltmesinin a����klayabilece�Yi sinyali de i��erir; tamam��n�� gǬrǬltǬ saymak **muhafazakǽr olabilir**. Buna kar�Y��l��k ger��ek bile�Yimsel sapmay�� s��f��r ortalamal�� ba�Y��ms��z gǬrǬltǬye ��evirmek iyimser olabilir. Y��nǬ ��nceden belli de�Yil.

   **DǬzeltme:** Ayr��k seed�?tli g��rǬlmǬ�Y verilerden Co/bile�Yen say��s��/hacim fark��na ba�Yl�� art��k senaryolar�� kur; sistematik sapmay�� koruyan gǬ�� kontrolleri ekle. `truth=old` yaln��z tek bir null senaryosudur; e�Yit beklenen hata gibi s��n��r durumlar��n�� da denetle.

   GǬ��te **1.000**, sonu��ta **4.000** permǬtasyon kullan��l��yor. Ayn�� test ayar��n�� kullan; 200 simǬlasyonda ��l��Ǭlen gǬ�� 0,80�?tin standart hatas�� yakla�Y��k **0,028**, dolay��s��yla e�Yik yak��n��ndaki kay��t karar��n�� daha fazla simǬlasyon ve belirsizlik aral��Y��yla ver. `harness/power.py` kullanmak tek ba�Y��na bu varsay��m sorunlar��n�� ����zmez.

3. **Bile�Yim ��ekimi, Co oran�� ve ��=0,0025**

   [��ekim:52�?"74](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:52>) hedef de�Yerlerini kullanm��yor; 27/27/26 bile�Yen kotas�� ve asimetri �Yart�� ��nceden sabitlenirse uygundur. Ancak sonu�� yaln��z bu kesilmi�Y da�Y��l��ma genellenebilir; bǬtǬn ��ok bile�Yenli ala�Y��mlara de�Yil.

   **Co�?tnun 40/80 olmas�� tek ba�Y��na sorun de�Yil.** Kotalardan beklenen say�� yakla�Y��k **35,44**; 40 ola�Yand��Y�� g��rǬnmǬyor. Bilinen hata fark�� nedeniyle Co�?tlu/Co�?tsuz sonu��lar�� ��nceden tan��mlay��p **ikisini de** raporla. Kod �Yu anda yaln��z Co�?tsuz altgrubu ayr��ca yazd��r��yor.

   **Seed 100, girdilerle ayr��d��r; bǬtǬn hedeflerde ayn�� olmas�� ise ayr�� sorun.** [compute.py:49�?"56](<C:/Users/can02/Projects/AI driven Science/harness/compute.py:49>) yaln��z seed ve hǬcre boyutuna ba�Yl�� ortak permǬtasyon kullan��yor. Sat��rlar��n konfigǬrasyon hatalar�� ba�Y��ml�� olabilir; ba�Y��ms��z sat��r i�Yaret ��evirmesi bunu hesaba katm��yor. Her hedefe farkl��, girdilerden ayr��k seed ata. Bunlar ayr��ca optimize edilmi�Y SQS de�Yil, rastgele yerle�Yimler.

   **��=0,0025 uygundur ve muhafazakǽrd��r:** iki K�?� testi i��in Bonferroni toplam s��n��r�� 0,005 olur. K44 ve altgruplar do�Yrulay��c�� iddiaya d��nǬ�YtǬrǬlecekse test ailesini yeniden tan��mlamak gerekir.

4. **`k_shear_transfer` import�?tu yan etkili mi?**

   **Evet, kesinlikle.** [Sat��r 40�?"41](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_transfer.py:40>) modeli yǬkler; Ǭst dǬzey b��lǬmler eksik ikilileri ve h3 hedeflerini hesaplay��p CSV�?tye yazabilir, ��n kay��t olu�Yturabilir ve eski hedef sonu��lar��n�� okuyup test eder. `__main__` korumas�� yaln��z en sondaki sonu�� kayd��n�� kaps��yor.

   W1�?tdeki `sys.argv = sys.argv[:1]` bunlar�� ��nlemez. Fonksiyonlar�� yan etkisiz yard��mc�� modǬle ay��r; hesap, model yǬkleme ve yaz��m ak��Y��n�� `main()` i��ine al.

5. **RK, i�Yaret, spline ve grid**

   | Kontrol | Sonu�� |
   |---|---|
   | RK ����zǬmǬ | **Do�Yru**, fakat mevcut dallanma hatas�� nedeniyle kullan��lm��yor. |
   | `t = x_a �^' x_b` | **Muggianu i��in do�Yru.** `ctx.pairs()` ve ikili anahtarlar alfabetik s��ralamada tutarl��. |
   | Mutlak `ln V` spline ekseni | **Do�Yru.** `ln(V/Vref)` ekseninden sabit ��telemedir; sorgular da mutlak `ln V`. |
   | Grid kapsam�� | **Garanti edilmiyor; sessiz ekstrapolasyon mǬmkǬn.** |

   [Grid:87�?"88](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:87>) yaln��z mevcut `[-0,40,+0,40]` listesini kesiyor. ��ekim kurallar��na uygun **Au�'%�'?Co�'%Ni�'%** hǬcresinde Co�?"Ni 50:50 girdisi i��in gereken de�Yer **+0,42985**. `CubicSpline` varsay��lan ekstrapolasyonu bunu sessizce hesaplar. Bu, sabit 80�?tli ��ekimde do�Yrulanm��Y bir ihlal de�Yil; kapsam garantisinin bulunmad��Y��n�� g��steren somut kar�Y�� ��rnek.

   Bile�Yim ekseninde de `t=��0,5` ile fit edilen polinom, izin verilen hedeflerde `|t|=0,75` g��rebilir. Bunu ayr��ca kapsama kontrolǬne kat. �o�� noktal�� ����zǬmde
   `L2 = (32/3)(K25+K75) �^' 16K50`; e�Yit ba�Y��ms��z giri�Y gǬrǬltǬsǬnde L2 belirsizli�Yi yakla�Y��k **22�f** olur. Bu tek ba�Y��na tahmin hatas�� de�Yildir, fakat derece do�Yrulamas��n��n ��nemini g��sterir.

   ��ki ek yǬrǬtme a����Y�� var: [sat��r 191�?"192](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:191>) hedefleri bile�Yim anahtar��yla e�Yle�Ytirmeden dosya s��ras��yla kar�Y��la�Yt��r��yor; [sat��r 151�?"154](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:151>) eski ��n kayd�� kod/girdi hash�?tlerini do�Yrulamadan yeniden kullan��yor. Devam ko�Yular��nda ikisi de yanl��Y de�Yerlendirmeye yol a��abilir. Sonu�� kayd�� ayr��ca ba�Y��ms��z denetimden sonra `ledger.verdict` ile kapat��lmal��.

**VERDICT: NO-GO �?" mevcut betik i��in.** Hesaptan ��nce gerekli dǬzeltmeler:

- Asimetrik kol se��imini dǬzelt ve d��rt kolun ger��ekten ayr��Yt��Y��n�� kontrol et.
- Import�?tu yan etkisiz yap.
- Kar�Y��la�Yt��rman��n kapsam��n�� ve ortak g��zlenebilir tan��m��n�� sabitle.
- Hedef ba�Y��na ba�Y��ms��z seed; bile�Yimsel art��klar�� koruyan gǬ�� hesab�� kullan.
- Hacim/bile�Yim kapsam��n�� do�Yrula; sessiz ekstrapolasyonu kapat.
- Bile�Yimle e�Yle�Ytirme, tam hassasiyetli kay��t ve ��n kay��t/girdi hash kontrolǬ ekle.

Wu�?tnun y��ntemini ��zgǬn PDF�?tden okudum; Marker�?t��n ayr��nt��lar�� i��in mevcut tam-metin denetim kayd��n�� kulland��m, PDF�?tsini bu tur yeniden a��amad��m. Python ortam�� ��al��Ymad��Y��ndan 80�?tli ��ekimi yeniden Ǭretmedim; **40/80 say��s��n�� verdi�Yin bilgi olarak ald��m**.


tokens used
111.692
**Mevcut sǬrǬm hesap ba�Ylatmaya uygun de�Yil.** En kritik hata [k_asym_w1.py:124](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:124>): `arm.endswith("sym")`, `"asym"` i��in de `True`. Dolay��s��yla:

- `OV-asym = OV-sym`: H1, belirtilen asimetrik rakibi kar�Y��la�Yt��rm��yor.
- `VV-asym = VV-sym`: H2�?tde kazan�� **0**, p **1**; gǬ�� **0** olur.
- Yeni 25:75 ve 75:25 hesaplar�� yap��l��yor fakat tahminlerde kullan��lm��yor.

Dosya de�Yi�Ytirmedim; MACE hesab�� veya yan etkili import ��al��Yt��rmad��m.

1. **OV-asym, Wu/Marker�?t��n adil temsilcisi mi?**

   **Bu haliyle yaln��z bir analog; y��ntemlerin yeniden uygulanmas�� de�Yil.** �o�� ayr�� fark var:

   - **Fit:** �o�� noktadan Ǭ�� RK katsay��s�� belirlemek cebirsel olarak ge��erli ama doygun interpolasyon: uyum hatas�� ve model derecesini do�Yrulayacak ba�Y��ms��z nokta kalm��yor. Wu, ikilileri `x=0,0.1,�?�,1` Ǭzerinde hesapl��yor; Eq. 5.1 ayr��ca on-site/inter-site yap��s�� i��eriyor. �o�� noktal�� Muggianu bunun birebir kar�Y��l��Y�� de�Yil. Bunu [��zgǬn tezde, ss. 43�?"44](C:/Users/can02/Downloads/etd.pdf) do�Yrulad��m.
   - **Hacim:** [Sat��r 123](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:123>) ikilinin **Vegard hacmini** kullan��yor; denge hacmini bulmuyor. Bu fark��n rakibi hangi y��nde etkiledi�Yi hesaplanmadan bilinemez.
   - **G��zlenebilir ve referans:** [curvatures():64](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_transfer.py:64>) ideal konumlarda, ayn�� hacimdeki saf referanslar�� ����kararak **clamped kar��Y��m e�Yrili�Yi** hesapl��yor. Bu, denge hacimlerindeki elastik sabitlerden ve onlar��n saf-element referanslar��ndan farkl��d��r. Taslak da ��n-gerilme katk��s��n�� a����k��a ay��r��yor: [draft_v5.md:61](<C:/Users/can02/Projects/AI driven Science/paper/draft_v5.md:61>).

   **DǬzeltme:** W1�?ti �?oikili Vegard hacmi / hedef Vegard hacmi �- simetrik / asimetrik temsil�?? kar�Y��la�Yt��rmas�� olarak s��n��rland��r; OV ad��n�� ��rne�Yin `BV` yap. Wu/Marker�?t�� ge��ti�Yi iddias�� i��in denge hacmi, relaksasyon ve referans tan��mlar�� e�Yle�Yen ayr�� benchmark gerekir. Marker�?t��n CALPHAD yakla�Y��m��n�� kaynak almak makul; mevcut kolu onun tam modeli diye adland��rmak de�Yil. [Marker 2017](https://www.sciencedirect.com/science/article/abs/pii/S0927025617304597)

   RK derecesini hedeflere bakmadan, ek ikili bile�Yimler ve ba�Y��ms��z seed kontrolleriyle se��. Ayr��ca H1 hem hacmi hem model esnekli�Yini de�Yi�Ytiriyor; **hacmin etkisini tek ba�Y��na** g��stermek i��in ayn�� derecedeki `VV-asym�?"BV-asym` kar�Y��la�Yt��rmas��n�� ��nceden belirlemek gerekir.

2. **H1/H2 gǬ�� hesab�� ger��ek��i mi; s��z��nt�� var m��?**

   [Sat��r 137�?"158](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:137>) gelecekteki W1 hedeflerini okumuyor: bu a����dan do�Yrudan hedef s��z��nt��s�� yok. Fakat gǬrǬltǬ modeli yeterince gerek��elendirilmi�Y de�Yil.

   Mevcut CSV�?tlerden ba�Y��ms��z spline hesab��yla yeniden buldu�Yum K�?� art��klar��:

   | hm grubu | n | RMSE |
   |---|---:|---:|
   | TǬmǬ | 94 | 1,892 GPa |
   | Co i��eren | 39 | 2,419 GPa |
   | Co i��ermeyen | 55 | 1,405 GPa |

   **Tek, s��f��r ortalamal�� iid Gaussian bu bile�Yim ba�Y��ml��l��Y��n�� siler.** `.orchestra/LESSONS.md:92�?"96` da art��Y��n bǬyǬk b��lǬmǬnǬn kompozisyon kaynakl�� oldu�Yunu s��ylǬyor.

   Ayr��ca hm hedefleri [seed 0](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_kp_hm.py:77>), girdiler seed 0�?"2: gǬrǬltǬ kalibrasyonu tarihsel ortak-seed protokolǬnden geliyor. Bunun K�?� gǬrǬltǬsǬnǬ mutlaka kǬ��ǬlttǬ�YǬnǬ s��yleyemem: yaln��z seed 1�?"2 girdileriyle RMSE **1,880 GPa** ����kt��. Ancak bu kontrol, yeni tasar��m��n gǬrǬltǬ modelini do�Yrulam��yor.

   H2�?tde kullan��lan `VV-sym` art��Y��, asimetri dǬzeltmesinin a����klayabilece�Yi sinyali de i��erir; tamam��n�� gǬrǬltǬ saymak **muhafazakǽr olabilir**. Buna kar�Y��l��k ger��ek bile�Yimsel sapmay�� s��f��r ortalamal�� ba�Y��ms��z gǬrǬltǬye ��evirmek iyimser olabilir. Y��nǬ ��nceden belli de�Yil.

   **DǬzeltme:** Ayr��k seed�?tli g��rǬlmǬ�Y verilerden Co/bile�Yen say��s��/hacim fark��na ba�Yl�� art��k senaryolar�� kur; sistematik sapmay�� koruyan gǬ�� kontrolleri ekle. `truth=old` yaln��z tek bir null senaryosudur; e�Yit beklenen hata gibi s��n��r durumlar��n�� da denetle.

   GǬ��te **1.000**, sonu��ta **4.000** permǬtasyon kullan��l��yor. Ayn�� test ayar��n�� kullan; 200 simǬlasyonda ��l��Ǭlen gǬ�� 0,80�?tin standart hatas�� yakla�Y��k **0,028**, dolay��s��yla e�Yik yak��n��ndaki kay��t karar��n�� daha fazla simǬlasyon ve belirsizlik aral��Y��yla ver. `harness/power.py` kullanmak tek ba�Y��na bu varsay��m sorunlar��n�� ����zmez.

3. **Bile�Yim ��ekimi, Co oran�� ve ��=0,0025**

   [��ekim:52�?"74](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:52>) hedef de�Yerlerini kullanm��yor; 27/27/26 bile�Yen kotas�� ve asimetri �Yart�� ��nceden sabitlenirse uygundur. Ancak sonu�� yaln��z bu kesilmi�Y da�Y��l��ma genellenebilir; bǬtǬn ��ok bile�Yenli ala�Y��mlara de�Yil.

   **Co�?tnun 40/80 olmas�� tek ba�Y��na sorun de�Yil.** Kotalardan beklenen say�� yakla�Y��k **35,44**; 40 ola�Yand��Y�� g��rǬnmǬyor. Bilinen hata fark�� nedeniyle Co�?tlu/Co�?tsuz sonu��lar�� ��nceden tan��mlay��p **ikisini de** raporla. Kod �Yu anda yaln��z Co�?tsuz altgrubu ayr��ca yazd��r��yor.

   **Seed 100, girdilerle ayr��d��r; bǬtǬn hedeflerde ayn�� olmas�� ise ayr�� sorun.** [compute.py:49�?"56](<C:/Users/can02/Projects/AI driven Science/harness/compute.py:49>) yaln��z seed ve hǬcre boyutuna ba�Yl�� ortak permǬtasyon kullan��yor. Sat��rlar��n konfigǬrasyon hatalar�� ba�Y��ml�� olabilir; ba�Y��ms��z sat��r i�Yaret ��evirmesi bunu hesaba katm��yor. Her hedefe farkl��, girdilerden ayr��k seed ata. Bunlar ayr��ca optimize edilmi�Y SQS de�Yil, rastgele yerle�Yimler.

   **��=0,0025 uygundur ve muhafazakǽrd��r:** iki K�?� testi i��in Bonferroni toplam s��n��r�� 0,005 olur. K44 ve altgruplar do�Yrulay��c�� iddiaya d��nǬ�YtǬrǬlecekse test ailesini yeniden tan��mlamak gerekir.

4. **`k_shear_transfer` import�?tu yan etkili mi?**

   **Evet, kesinlikle.** [Sat��r 40�?"41](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_transfer.py:40>) modeli yǬkler; Ǭst dǬzey b��lǬmler eksik ikilileri ve h3 hedeflerini hesaplay��p CSV�?tye yazabilir, ��n kay��t olu�Yturabilir ve eski hedef sonu��lar��n�� okuyup test eder. `__main__` korumas�� yaln��z en sondaki sonu�� kayd��n�� kaps��yor.

   W1�?tdeki `sys.argv = sys.argv[:1]` bunlar�� ��nlemez. Fonksiyonlar�� yan etkisiz yard��mc�� modǬle ay��r; hesap, model yǬkleme ve yaz��m ak��Y��n�� `main()` i��ine al.

5. **RK, i�Yaret, spline ve grid**

   | Kontrol | Sonu�� |
   |---|---|
   | RK ����zǬmǬ | **Do�Yru**, fakat mevcut dallanma hatas�� nedeniyle kullan��lm��yor. |
   | `t = x_a �^' x_b` | **Muggianu i��in do�Yru.** `ctx.pairs()` ve ikili anahtarlar alfabetik s��ralamada tutarl��. |
   | Mutlak `ln V` spline ekseni | **Do�Yru.** `ln(V/Vref)` ekseninden sabit ��telemedir; sorgular da mutlak `ln V`. |
   | Grid kapsam�� | **Garanti edilmiyor; sessiz ekstrapolasyon mǬmkǬn.** |

   [Grid:87�?"88](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:87>) yaln��z mevcut `[-0,40,+0,40]` listesini kesiyor. ��ekim kurallar��na uygun **Au�'%�'?Co�'%Ni�'%** hǬcresinde Co�?"Ni 50:50 girdisi i��in gereken de�Yer **+0,42985**. `CubicSpline` varsay��lan ekstrapolasyonu bunu sessizce hesaplar. Bu, sabit 80�?tli ��ekimde do�Yrulanm��Y bir ihlal de�Yil; kapsam garantisinin bulunmad��Y��n�� g��steren somut kar�Y�� ��rnek.

   Bile�Yim ekseninde de `t=��0,5` ile fit edilen polinom, izin verilen hedeflerde `|t|=0,75` g��rebilir. Bunu ayr��ca kapsama kontrolǬne kat. �o�� noktal�� ����zǬmde
   `L2 = (32/3)(K25+K75) �^' 16K50`; e�Yit ba�Y��ms��z giri�Y gǬrǬltǬsǬnde L2 belirsizli�Yi yakla�Y��k **22�f** olur. Bu tek ba�Y��na tahmin hatas�� de�Yildir, fakat derece do�Yrulamas��n��n ��nemini g��sterir.

   ��ki ek yǬrǬtme a����Y�� var: [sat��r 191�?"192](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:191>) hedefleri bile�Yim anahtar��yla e�Yle�Ytirmeden dosya s��ras��yla kar�Y��la�Yt��r��yor; [sat��r 151�?"154](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:151>) eski ��n kayd�� kod/girdi hash�?tlerini do�Yrulamadan yeniden kullan��yor. Devam ko�Yular��nda ikisi de yanl��Y de�Yerlendirmeye yol a��abilir. Sonu�� kayd�� ayr��ca ba�Y��ms��z denetimden sonra `ledger.verdict` ile kapat��lmal��.

**VERDICT: NO-GO �?" mevcut betik i��in.** Hesaptan ��nce gerekli dǬzeltmeler:

- Asimetrik kol se��imini dǬzelt ve d��rt kolun ger��ekten ayr��Yt��Y��n�� kontrol et.
- Import�?tu yan etkisiz yap.
- Kar�Y��la�Yt��rman��n kapsam��n�� ve ortak g��zlenebilir tan��m��n�� sabitle.
- Hedef ba�Y��na ba�Y��ms��z seed; bile�Yimsel art��klar�� koruyan gǬ�� hesab�� kullan.
- Hacim/bile�Yim kapsam��n�� do�Yrula; sessiz ekstrapolasyonu kapat.
- Bile�Yimle e�Yle�Ytirme, tam hassasiyetli kay��t ve ��n kay��t/girdi hash kontrolǬ ekle.

Wu�?tnun y��ntemini ��zgǬn PDF�?tden okudum; Marker�?t��n ayr��nt��lar�� i��in mevcut tam-metin denetim kayd��n�� kulland��m, PDF�?tsini bu tur yeniden a��amad��m. Python ortam�� ��al��Ymad��Y��ndan 80�?tli ��ekimi yeniden Ǭretmedim; **40/80 say��s��n�� verdi�Yin bilgi olarak ald��m**.


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
# Durum (2 Kas��m 2026)

Tek giri�Y noktas��. Ayr��nt�� ve kan��t defterde (`claims/claims.jsonl`, kimlikler a�Ya�Y��da), dersler `.orchestra/LESSONS.md` i��inde. `.orchestra/NIGHT_REPORT.md` 31 Ekim sabah��na ait ve eskidir ("iki ba�Y��ms��z holdout" ifadesi d26bd71285 ile dǬzeltildi).

## Bulgular

| # | Bulgu | Seviye | Kan��t | A����k olan |
|---|---|---|---|---|
| 1 | **K' hacim transferi.** Rastgele fcc ala�Y��m��n kar��Y��m K' de�Yeri = ל 4 x_i x_j K'_ij(V0), ikililer ala�Y��m hacminde. ��ki k��r sette hata yar��ya iniyor, k 1.08 ve 1.08. | L2 (697c2d6d75) | h3: 4c29d9754c ��' 6e0923b413 (ortak iddia K44 yǬzǬnden FAIL); hm_fresh: 67a358fc59 ��' d92844787f (PASS) | mpa modelinde k 1.33 [1.11, 1.51] (851aec6883 ��' 86767e478d), ama s��z��nt��s��z 150 ala�Y��mda 1.10 [0.94, 1.26] (kay��ts��z; 6bc0e190a8 FAIL, sebep design). Denklik testi 88b9465108 FAIL: 1200 ala�Y��m, k 1.14 [1.10, 1.18], kural yine hatay�� 4.81'den 2.21 GPa'ya indiriyor (43370bbb27, verdict 736bcac471, Astra: kod hatas�� yok). k kompozisyona ba�Yl�� (ke�Yifsel): 3 element 1.00, Cu'suz 1.00, Cu'lu 1.24, max|dlnV| > 0.25 iken 1.41. omat da benzer (1.11). k = 1 iddias�� dǬ�YtǬ; bǬyǬk hacim fark��nda transfer eksik kal��yor. PBE yok. LiteratǬr (tam metin): k��smen biliniyor; hacim ad��m��, k��r test ve K'/K44 kar�Y��tl��Y�� bulunamad��. "Hacim transferli regular-solution / kesik tens��rel CE kural��" diye yaz��lmal��, Marker 2017 okunmadan yaz��lmamal��. |
| 2 | **Enerji hacim transferi: D�o�?T�o.** Standart Muggianu (saf elementler kendi hacminde) ayn�� i�Yi yap��yor, 11.4 ile 11.5 meV, kural 13.3 (S2 denetimi, defterde dǬzeltme). Eski metin: E_mix hatas�� 36.4 ��' 13.1 meV, yaln��z hm_fresh (n 94) ger��ekten k��rdǬ. Tam hesapta k 0.94 ile 0.98; 0.81 do�Yrusalla�Yt��rma etkisi. | L2 (05f01df6ec, dǬzeltme d26bd71285) | 1708d0db77, k_direct | Fikrin ��zǬ Zunger 1987-89'da biliniyor (`claims/literature.jsonl`). PBE dǬzenli hǬcre L3'Ǭ FAIL (8541e914ea). |
| 3 | **K44 Co'suz ala�Y��mlarda transfer oluyor** (��n kay��t e410c96a32 ��' d9460850ce, 120 taze ala�Y��m, kazan�� 0.51, p 2.5e-4, k 1.23); Co'lularda olmuyor (kazan�� 0.11). Eski g��zlem: Ayn�� kural K44'te zay��f: kazan�� 0.12 ile 0.20, k 0.69 ile 0.86. En k��tǬ hatalar Co'ca zengin ala�Y��mlarda. | g��zlem | LESSONS 14 ile 16 | Neden a����k; ba�Y��ms��z denetim yap��lmad��. Ke�Yif bak��Y�� (g��rǬlmǬ�Y 269 sat��r, kay��t de�Yil): "E_F'de yǬksek DOS" a����klamas�� desteklenmiyor, art��k Pd/Pt/Ni/Rh/Ir/Co oran��yla iki kanalda da benzer bǬyǬyor (K44/K' rms oran�� 1.15 ile 1.4). En bǬyǬk hatalar iki kanalda da Co'lu ala�Y��mlarda (|r44| ile Co r 0.33): s��radaki �YǬpheli Co manyetizmas��. K44'Ǭn hacim kaymas�� da kǬ��Ǭk, kazan�� i��in az yer var (a2: pair 3.56 ��' kural 2.66, K' 5.67 ��' 1.80). |
| 3b | **Ortak kayma taban��.** Hacim kural��n��n K44 ve K''te ka����rd��Y�� k��s��m ayn�� ve kompozisyona ait: K44 - K' kural�� ge��iyor (kazan�� 0.49), hǬcreler aras�� r 0.75, bilinen ��n gerilme ��zde�Yli�Yi ����kar��l��nca r 0.67, k 0.99. K44'Ǭn "tutmamas��" bu tabandan. | L0, Ǭ�� ��n kay��tl�� PASS (b86e0d8a40, fd786169e3, ede47f1d65), Ǭ��Ǭ de Astra denetimi PLAUSIBLE | `data/k_aniso_s100_clamped.csv`, `k_floor_cells.csv`, `k_floor_stress_*.csv`; LESSONS 20-22 | ��kili referanslardan gelen ortak hata d��Ylanmad�� (iki ba�Y��ms��z ikili paneli gerekli). Fiziksel anlam�� a����k; MACE only. |
| 4 | **MACE kar��Y��m kayma e�Yrili�Yinde L1'den ge��miyor.** 8 dǬzenli L1_2 hǬcrede K' i�Yareti 8/8 do�Yru, K44 i�Yareti 5/8 (Au3Ir PBE �^'32.4, MACE +3.2 GPa); medyan sapma K' i��in %47, K44 i��in %56. K' kural�� yaln��z MACE i��inde g��sterilmi�Y say��l��r. | L1 FAIL (b3214734c2, Astra denetimli) | `data/hiso_l12_dft_v2.csv`, `data/hiso_l12_mace.csv` | dense-k ve ecutrho kontrolleri ko�Yuyor. |
| 5 | **H-iso.** HǬcre i��i i�Yaret okumas��yla PASS (n 6, medyan K44/K' 0.94), tek i�Yaret okumas��yla FAIL (Pt3Cu pozitif). Ag3Ir 0.54, Ag3Rh 0.39, Pt3Cu 2.61: hǬcre baz��nda izotropi yok. | L0, PLAUSIBLE (b3214734c2, sebep numerics, a����k) | `scripts/hiso_l12_v2.py` | 34/78 ko�Yuda negative rho; ecutrho �-1.5 ve kspacing 0.08 kontrolleri bitince kapan��r. |

Yanl��Ylanan adaylar (A2, H-sm, R3, R3b, HM2-T4, Astra EOS kapan��Y��) ve gerek��eleri defterde `verdict on ...` kay��tlar��nda.

## ��al��Yan i�Yler

- **H-iso kontrolleri (PBE, 2 ��ekirdek, s��ral��):** dense bitti (`data/hiso_l12_dft_v2_dense.csv`, kspacing 0.08). Cu3Ir de�Yi�Ymedi (K44 �^'54.75 ��' �^'54.71, K' �^'57.39 ��' �^'57.42). Ag3Rh K' kararl�� (�^'17.97 ��' �^'17.44) ama K44 �^'7.04 ��' �^'3.64 GPa, oran 0.39 ��' 0.21: Ag3Rh K44 k-yak��nsak de�Yil. Medyan K44/K' 0.942 ��' 0.941, i�Yaretler ayn��, H-iso okumas�� de�Yi�Ymiyor. rho ko�Yusu 2 Kas��m 13:43'te reboot ile 8/18'de kesildi; 3 Kas��m 12:35'te devam ettirildi (log `data/hiso_l12_dft_v2_rho_resume1.log`, kalan Rh_t+ ve Pt3Cu, yakla�Y��k 3 saat).

## S��radaki ad��mlar

1. Dense ve rho bitince H-iso'yu kapat: oranlar ve MACE fark�� ��%10 i��inde kal��yorsa verdict b3214734c2'yi kesinle�Ytir, kalm��yorsa sebep numerics ve yeni ko�Yu.
2. K' kural�� i��in PBE (L3). **Tasar��m uyar��s��:** dǬzenli 4 atomlu hǬcreler enerji kural��nda PBE'de +10 meV'lik sabit hacim ��ok cisim terimi ta�Y��d��Y�� i��in yanl��Y test ����kt�� (d440b9eb7b, 8541e914ea). K' i��in de dǬzenli hǬcre kullan��lacaksa bu ��nce dǬ�YǬnǬlmeli; do�Yru alan PBE SQS hǬcreleri (32 atom ve ǬstǬ) ve bu laptopta gǬnler sǬrer, kiral��k sunucu se��ene�Yi var.
3. PBE h��zland��rma: Cu3Ir'de smearing ve k-a�Y�� gev�Yetmeyi referansa kar�Y�� test et.
4. ~~Veri dǬzeltmesi~~ yap��ld�� (2 Kas��m): `scripts/fix_counts2.py` ��' `data/h1_ev_rows_fixed2.csv`, `h3_fresh_rows_fixed2.csv` (44 Ǭ��lǬde �^'0.31 ile �^'0.71 meV, R ve B_chem yeniden). hm3 ve di�Yerlerinde 1/3 yok, yeni mǬhǬr gerekmedi. Enerji analizleri bundan sonra `_fixed2` okumal��.
5. L4 (2 Kas��m): son tarama ve Astra denetimi yap��ld�� (`claims/literature.jsonl` sat��r 63 ve 64, `.orchestra/audits/L4_kprime_astra.md`). Karar PARTIALLY KNOWN, KEEP: kural ortak hacimli ikili regular-solution enerjisinin kayma tǬrevi, ��zgǬl uygulama bulunmad��. Wu 2021 tezi okundu (sat��r 65): ikili EMTO'dan bcc Ǭ��lǬlere excess C' ve C44 aktar��m�� var, ama her bile�Yim kendi hacminde; Vegard hacmi ad��m�� yok. L4 taramas�� kapand�� (arama s��n��rl��), en yak��n ��ncǬl olarak draft_v5'e eklendi. Yeni risk: Soyemi 2026 ve Chong 2026, kural��n MACE i��inde tutmas��n��n model yanl��l��Y�� olabilece�Yini dǬ�YǬndǬrǬyor; PBE aktar��m testi bu yǬzden daha ��nemli.
5b. Deney verisi (ajan taramas�� 1 Kas��m): bu dokuz elementte ��l��ǬlmǬ�Y tek kristal ala�Y��m sabitleri yaln��z kapal�� eri�Yimde (Cu-Ni Epstein-Carlson 1965, Schmunk-Smith 1960; Cu-Au Chiarodo 1972, dC/dP ile; Pd-Ag Hoare-Yates 1954; Co-Ni Weston-Granato 1975). 3+ bile�Yenli ��l��Ǭm yok. KǬtǬphane PDF'i gerekli.
5c. ~~nspin hatas��~~ dǬzeltildi (2 Kas��m): `extra={'system.nspin': 1}` art��k ba�Ylang���� momenti koymuyor, Co girdisinde nspin 1 do�Yruland��.
6. Makale: `paper/draft_v5.md` (v4 art�� model yanl��l��Y�� s��n��r��, madde 6, ve Soyemi, Chong kaynaklar��; ar�Yiv henǬz v4 ile). v4: Astra v4 incelemesindeki (`.orchestra/audits/draft_v4_astra.md`) bǬtǬn kapsam ve say�� dǬzeltmeleri uyguland��. Ar�Yiv `paper/repro_20261102_2.zip` (v4, requirements.txt, manifest do�Yru; ar�Yivden `chain.py` ve `fix_counts2.py` birebir Ǭretiyor). G��nderim i��in kalan: yazar��n son okumas��, Zenodo'ya ar�Yiv yǬkleme ve DOI'yi metne yazma, ChemRxiv g��nderimi. Bunlar�� yazar yapar. Dense/rho sonucu gelince 5.1'deki "pending" cǬmlesi gǬncellenir.

## Harness haritas��

| Par��a | Yer |
|---|---|
| Hesap (MACE, SQS, curvature) | `harness/compute.py`, `harness/context.py` (ikili V_ij, Vegard) |
| PBE | `harness/dft.py` (`Settings(kpts=..., ecut_elements=...)` zorunlu) |
| Defter, ��n kay��t, gǬ�� | `harness/ledger.py`, `harness/power.py` |
| Arena (mǬhǬrlǬ holdout) | `harness/arena.py`, `data/sealed/`, `candidates/` |
| Ajanlar | `scripts/discovery_round.py` (arena turu), `scripts/swarm.py` (cepheler `.orchestra/fronts/`) |
| K' testleri | `scripts/k_shear_transfer.py` (h3), `k_shear_kp_hm.py` (hm_fresh), `k_shear_mpa.py` (model de�Yi�Yimi); veri `data/binary_kgrid*.csv`, `data/*_shear_clamped*.csv` |
| Enerji kural�� | `scripts/hm_l2_fixed.py`, `scripts/k_direct.py`, `candidates/champion_volume_transfer.py` |

Veri kǬmeleri: h1 (ke�Yif, g��rǬlmǬ�Y), h3 (model se��iminde kullan��ld��, K i��in k��rdǬ), hm_fresh (enerji ve K' i��in k��rdǬ, art��k g��rǬldǬ), hm3fix (mǬhǬrlǬ, ajanlar g��rmez).

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$i=0; Get-Content scripts/k_asym_w1.py | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ }; rg --files -g AGENTS.md -g '"'*w1*' -g '*k_shear*' -g '*k_asym*'" in C:\Users\can02\Projects\AI driven Science
 succeeded in 462ms:
   1: """W1: where the binaries are read versus how their composition dependence is represented.
   2: 
   3: python scripts/k_asym_w1.py            binaries, compositions, power, registration (stops before targets)
   4: python scripts/k_asym_w1.py targets    targets and test, only for hypotheses already registered
   5: Prior binary-to-multicomponent elastic models (Marker 2017 CALPHAD; Wu 2021 Eq. 5.1) model the composition dependence
   6: of each binary (Redlich-Kister, Muggianu) but keep each binary at its own volume. Our rule uses 50:50 binaries only,
   7: read at the alloy's Vegard volume. W1 compares the two representations on one observable and combines them. It is not
   8: a reimplementation of Wu or Marker: their binaries sit at relaxed equilibrium volumes and their targets are equilibrium
   9: Cij; here every arm and the target are clamped mixing curvatures (k_shear_transfer.curvatures convention), so the arm
  10: BV-asym is an analogue of their representation, not their model (Astra design review, w1_design_astra.md).
  11: Arms, per channel (K' primary, K44 secondary, Co and Co-free subgroups both reported):
  12:   BV-asym  binaries at x_A = 0.25, 0.5, 0.75, each at its own (binary) Vegard volume; exact L0, L1, L2 per pair;
  13:            Muggianu  K = sum x_a x_b [L0 + L1 (x_a - x_b) + L2 (x_a - x_b)^2]
  14:   VV-sym   sum 4 x_a x_b K_ab(0.5; V0), V0 the alloy Vegard volume                          (our rule, unchanged)
  15:   VV-asym  BV-asym with every binary curvature read at V0
  16:   BV-sym   sum 4 x_a x_b K_ab(0.5; V_ab)                                                       (reported only)
  17: Hypotheses on K', each registered only if power >= 0.8 and false pass <= 0.05; three tests, alpha 0.005 / 3:
  18:   H1  RMSE(VV-sym)  <= 0.9 RMSE(BV-asym)   parameter-free rule against the asymmetric binary-volume representation
  19:   H2  RMSE(VV-asym) <= 0.9 RMSE(VV-sym)    does adding the asymmetry help once the volume is right
  20:   H3  RMSE(VV-asym) <= 0.9 RMSE(BV-asym)   the volume step alone, at equal representation degree
  21: Design choices fixed before any target: degree 2 (three binary compositions, an exact fit; extra points at x = 1/8 and
  22: 7/8, dlnV = 0, are computed as a reported diagnostic only); targets keep every pairwise |x_a - x_b| <= 0.5 (the fitted
  23: t range) and need no volume outside the binary grids; each target has its own SQS seed 100 + i; noise for the power
  24: check is drawn from the rule's hm residuals, Co rows from Co rows (composition-dependent, not iid Gaussian).
  25: """
  26: 
  27: import datetime as dt
  28: import os
  29: import sys
  30: import time
  31: from pathlib import Path
  32: 
  33: ROOT = Path(__file__).resolve().parent.parent
  34: os.environ["HARNESS_MODEL"] = "medium-omat-0"
  35: sys.path.insert(0, str(ROOT))
  36: 
  37: import numpy as np  # noqa: E402
  38: import pandas as pd  # noqa: E402
  39: from ase.build import bulk  # noqa: E402
  40: from scipy.interpolate import CubicSpline  # noqa: E402
  41: 
  42: from harness import compute, ledger  # noqa: E402
  43: from harness.compute import GPA  # noqa: E402
  44: from harness.context import context  # noqa: E402
  45: from harness.features import parse_comp  # noqa: E402
  46: 
  47: ctx = context()
  48: SCRIPT = str(Path(__file__))
  49: BIN5 = ROOT / "data" / "binary_kgrid.csv"
  50: BIN = ROOT / "data" / "binary_kgrid_asym.csv"
  51: DIAG = ROOT / "data" / "binary_k_asym_diag.csv"
  52: TGT = ROOT / "data" / "w1_shear_clamped.csv"
  53: COMPS = ROOT / "data" / "w1_compositions.csv"
  54: XS = (0.25, 0.75)
  55: ELS = ["Ag", "Au", "Co", "Cu", "Ir", "Ni", "Pd", "Pt", "Rh"]
  56: GRID = [-0.40, -0.30, -0.20, -0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40]  # as binary_kgrid.csv
  57: LNV_MAX = 0.35  # targets may not need binaries beyond this, so splines never extrapolate
  58: N_TGT, N_PERM, N_SIM = 80, 4000, 500
  59: CH = ("Kp", "K44")
  60: HYP = {"H1": ("VV-sym", "BV-asym"), "H2": ("VV-asym", "VV-sym"), "H3": ("VV-asym", "BV-asym")}
  61: ALPHA = 0.005 / len(HYP)
  62: ARMS = ("BV-asym", "VV-sym", "VV-asym", "BV-sym")
  63: key = lambda c: ";".join(f"{e}:{v:.6f}" for e, v in sorted(c.items()))  # noqa: E731
  64: 
  65: # Same strain protocol as k_shear_transfer.py (copied, because importing that script runs its pipeline)
  66: AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
  67: _calc = None
  68: 
  69: 
  70: def e_strained(atoms, v_atom, F):
  71:     global _calc
  72:     _calc = _calc or compute.calculator()
  73:     a = atoms.copy()
  74:     a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
  75:     a.set_cell(a.cell @ F.T, scale_atoms=True)
  76:     a.calc = _calc
  77:     t = time.perf_counter()
  78:     e = a.get_potential_energy() / len(a)
  79:     time.sleep(time.perf_counter() - t)  # 50% duty cycle, keeps the laptop cool
  80:     return e
  81: 
  82: 
  83: def F_of(name, s):
  84:     if name == "K44":
  85:         F = np.eye(3)
  86:         F[0, 1] = s
  87:         return F
  88:     return np.diag([np.exp(s), np.exp(-s), 1.0])
  89: 
  90: 
  91: def curvatures(alloy, x, v):
  92:     pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in x}
  93:     out = {}
  94:     for name in CH[::-1]:
  95:         em = [e_strained(alloy, v, F_of(name, s)) - sum(xi * e_strained(pures[el], v, F_of(name, s))
  96:                                                          for el, xi in x.items()) for s in AMPS]
  97:         c2 = np.polyfit(AMPS, em, 2)[0]
  98:         out[name] = (2 * c2 if name == "K44" else c2 / 2) / v * GPA
  99:     return out
 100: 
 101: 
 102: def pair_need(c):
 103:     """ln(V0 / V_binary) for every binary composition a target reads, keyed (a, b, x_a)."""
 104:     v0 = ctx.vegard(c)
 105:     return {(a, b, xa): np.log(v0 / ctx.vegard({a: xa, b: 1 - xa})) for a, b, _, _ in ctx.pairs(c)
 106:             for xa in (0.25, 0.5, 0.75)}
 107: 
 108: 
 109: def draw_targets():
 110:     if COMPS.exists():
 111:         return [parse_comp(s) for s in pd.read_csv(COMPS).comp]
 112:     rng, out, seen = np.random.default_rng(2611), [], set()
 113:     quota = {3: 27, 4: 27, 5: 26}  # equal shares; a free draw gave 58/17/5 because the 1/12 floor rejects n = 5
 114:     while len(out) < N_TGT:
 115:         n = int(rng.integers(3, 6))
 116:         if sum(len(c) == n for c in out) >= quota[n]:
 117:             continue
 118:         els = sorted(rng.choice(ELS, n, replace=False))
 119:         x = rng.dirichlet([0.7] * n)
 120:         if x.min() < 1 / 12:
 121:             continue
 122:         cnt = np.round(x * 108).astype(int)
 123:         cnt[np.argmax(cnt)] += 108 - cnt.sum()
 124:         c = {e: k / 108 for e, k in zip(els, cnt)}
 125:         spread = max(c.values()) - min(c.values())
 126:         if not 0.15 < spread <= 0.5 or key(c) in seen:  # off-equiatomic, inside the fitted t range
 127:             continue
 128:         if max(abs(d) for d in pair_need(c).values()) > LNV_MAX:
 129:             continue
 130:         seen.add(key(c))
 131:         out.append(c)
 132:     pd.DataFrame({"comp": [key(c) for c in out], "seed": [100 + i for i in range(len(out))]}).to_csv(COMPS, index=False)
 133:     return out
 134: 
 135: 
 136: comps = draw_targets()
 137: seeds = pd.read_csv(COMPS).seed.tolist()
 138: need = {}
 139: for c in comps:
 140:     for k, d in pair_need(c).items():
 141:         need.setdefault(k, []).append(d)
 142: 
 143: # 1. off-equiatomic binaries on the ln V grid around each binary's own Vegard volume, as wide as the targets need
 144: done = set(map(tuple, pd.read_csv(BIN)[["pair", "xA", "seed", "dlnV"]].astype(str).values)) if BIN.exists() else set()
 145: for (a, b, xa), ds in sorted(need.items()):
 146:     if xa == 0.5:
 147:         continue
 148:     lo, hi = min(min(ds), 0.0) - 0.1, max(max(ds), 0.0) + 0.1
 149:     grid = [d for d in GRID if lo <= d <= hi]
 150:     for seed in (0, 1, 2):
 151:         alloy = compute.solid_solution({a: xa, b: 1 - xa}, "fcc", reps=3, seed=seed)
 152:         x = compute.actual_fractions(alloy)
 153:         for d in grid:
 154:             if (f"{a}-{b}", str(xa), str(seed), str(d)) in done:
 155:                 continue
 156:             v = ctx.vegard({a: xa, b: 1 - xa}) * np.exp(d)
 157:             r = {"pair": f"{a}-{b}", "xA": xa, "xA_actual": x[a], "seed": seed, "dlnV": d, "V": v,
 158:                  **curvatures(alloy, x, v)}
 159:             pd.DataFrame([r]).to_csv(BIN, mode="a", header=not BIN.exists(), index=False, float_format="%.10g")
 160:     print("binary", a, b, xa, flush=True)
 161: 
 162: # degree diagnostic (reported only): x = 1/8, 7/8 at the binary's own Vegard volume
 163: done = set(map(tuple, pd.read_csv(DIAG)[["pair", "xA", "seed"]].astype(str).values)) if DIAG.exists() else set()
 164: for a, b in sorted({(a, b) for a, b, _ in need}):
 165:     for xa in (0.125, 0.875):
 166:         for seed in (0, 1, 2):
 167:             if (f"{a}-{b}", str(xa), str(seed)) in done:
 168:                 continue
 169:             alloy = compute.solid_solution({a: xa, b: 1 - xa}, "fcc", reps=3, seed=seed)
 170:             x = compute.actual_fractions(alloy)
 171:             v = ctx.vegard({a: xa, b: 1 - xa})
 172:             r = {"pair": f"{a}-{b}", "xA": xa, "xA_actual": x[a], "seed": seed, "V": v, **curvatures(alloy, x, v)}
 173:             pd.DataFrame([r]).to_csv(DIAG, mode="a", header=not DIAG.exists(), index=False, float_format="%.10g")
 174: print("diagnostic binaries done", flush=True)
 175: 
 176: # splines in absolute ln V, x = 0.25, 0.75 (this script) and 0.5 (binary_kgrid.csv); no extrapolation allowed
 177: SPL, RANGE = {}, {}
 178: g = pd.read_csv(BIN).groupby(["pair", "xA", "dlnV"])[["V", *CH]].mean().reset_index()
 179: g5 = pd.read_csv(BIN5).groupby(["pair", "dlnV"])[["V", *CH]].mean().reset_index().assign(xA=0.5)
 180: for (pair, xa), s in pd.concat([g, g5]).groupby(["pair", "xA"]):
 181:     lv = np.log(s.V.values)
 182:     RANGE[(tuple(pair.split("-")), xa)] = (lv.min(), lv.max())
 183:     for ch in CH:
 184:         SPL[(tuple(pair.split("-")), xa, ch)] = CubicSpline(lv, s[ch].values, extrapolate=False)
 185: 
 186: 
 187: def k_at(a, b, x, ch, lnv):
 188:     lo, hi = RANGE[((a, b), x)]
 189:     assert lo - 1e-9 <= lnv <= hi + 1e-9, ("extrapolation", a, b, x, lnv, lo, hi)
 190:     return float(SPL[((a, b), x, ch)](lnv))
 191: 
 192: 
 193: def rk(k25, k50, k75):
 194:     """Exact L0, L1, L2 from K(x) = x(1-x)[L0 + L1 t + L2 t^2], t = 2x - 1, at x = 0.25, 0.5, 0.75."""
 195:     y = np.array([k25 / (3 / 16), k50 / 0.25, k75 / (3 / 16)])
 196:     return np.linalg.solve(np.array([[1, -0.5, 0.25], [1, 0, 0], [1, 0.5, 0.25]]), y)
 197: 
 198: 
 199: def predict(c, ch, arm):
 200:     vol, rep = arm.split("-")
 201:     v0, tot = ctx.vegard(c), 0.0
 202:     for a, b, xa, xb in ctx.pairs(c):
 203:         at = lambda x: np.log(v0) if vol == "VV" else np.log(ctx.vegard({a: x, b: 1 - x}))  # noqa: E731
 204:         if rep == "sym":
 205:             tot += 4 * xa * xb * k_at(a, b, 0.5, ch, at(0.5))
 206:         else:
 207:             L = rk(*(k_at(a, b, x, ch, at(x)) for x in (0.25, 0.5, 0.75)))
 208:             t = xa - xb
 209:             tot += xa * xb * (L[0] + L[1] * t + L[2] * t * t)
 210:     return tot
 211: 
 212: 
 213: P = {ch: {arm: np.array([predict(c, ch, arm) for c in comps]) for arm in ARMS} for ch in CH}
 214: for ch in CH:  # the four arms must really differ (the first draft's endswith("sym") made asym equal sym)
 215:     for i, a1 in enumerate(ARMS):
 216:         for a2 in ARMS[i + 1:]:
 217:             assert np.abs(P[ch][a1] - P[ch][a2]).max() > 1e-6, (ch, a1, a2)
 218: 
 219: # 2. power with composition-dependent noise, then registration
 220: hm = pd.read_csv(ROOT / "data" / "hm_shear_clamped.csv")
 221: hmc = [parse_comp(s) for s in hm.comp]
 222: res_hm = hm.Kp.values - np.array([predict(c, "Kp", "VV-sym") for c in hmc])
 223: pool = {True: res_hm[["Co" in c for c in hmc]], False: res_hm[["Co" not in c for c in hmc]]}
 224: co = np.array(["Co" in c for c in comps])
 225: 
 226: 
 227: def signflip(y, new, old, rng):
 228:     d = (y - old) ** 2 - (y - new) ** 2
 229:     gain = 1 - np.sqrt(np.mean((y - new) ** 2)) / np.sqrt(np.mean((y - old) ** 2))
 230:     flips = rng.choice([-1.0, 1.0], (N_PERM, len(d)))
 231:     p = (np.sum((flips * d).mean(1) >= d.mean()) + 1) / (N_PERM + 1)
 232:     return gain >= 0.10 and p < ALPHA, float(gain), float(p)
 233: 
 234: 
 235: def noise(rng):
 236:     e = np.empty(len(comps))
 237:     for flag in (True, False):
 238:         e[co == flag] = rng.choice(pool[flag], (co == flag).sum()) * rng.choice([-1, 1], (co == flag).sum())
 239:     return e
 240: 
 241: 
 242: def power(new, old):
 243:     rng = np.random.default_rng(7)
 244:     run = lambda truth: np.mean([signflip(truth + noise(rng), P["Kp"][new], P["Kp"][old], rng)[0]  # noqa: E731
 245:                                  for _ in range(N_SIM)])
 246:     pw, fp = run(P["Kp"][new]), run(P["Kp"][old])
 247:     fp_mid = run(0.5 * (P["Kp"][new] + P["Kp"][old]))  # equal expected error, the boundary case
 248:     return {"power": round(float(pw), 3), "false_pass": round(float(max(fp, fp_mid)), 3), "n_sims": N_SIM,
 249:             "power_se": round(float(np.sqrt(pw * (1 - pw) / N_SIM)), 3)}
 250: 
 251: 
 252: regs = {}
 253: for h, (new, old) in HYP.items():
 254:     tag = f"W1 {h}:"
 255:     found = [e for e in ledger.entries() if e["claim"].startswith(tag) and "prereg" in e["notes"]]
 256:     if found:
 257:         assert found[-1]["evidence"].get(SCRIPT) == ledger.file_hash(SCRIPT), f"{h}: script changed since registration"
 258:         regs[h] = found[-1]
 259:         continue
 260:     if any(e["claim"].startswith(f"Design note, {tag}") for e in ledger.entries()):
 261:         continue
 262:     pw = power(new, old)
 263:     d = P["Kp"][new] - P["Kp"][old]
 264:     print(f"{h}: rms(new - old) {np.sqrt(np.mean(d**2)):.2f} GPa, hm residual rms {np.sqrt(np.mean(res_hm**2)):.2f}, "
 265:           f"{pw}", flush=True)
 266:     claim = (f"{tag} on {len(comps)} fresh off-equiatomic fcc alloys (3-5 of {''.join(ELS)}), clamped mixing K' "
 267:              f"RMSE({new}) <= 0.9 RMSE({old}) and paired sign-flip p < {ALPHA:.4f}; MACE medium-omat-0, per-target "
 268:              f"SQS seeds 100-{99 + len(comps)}, targets computed after registration")
 269:     try:
 270:         regs[h] = ledger.register(claim, SCRIPT, pw, notes="literature gap Wu 2021 / Marker 2017 (literature.jsonl "
 271:                                   "line 65); design reviewed by Astra (.orchestra/audits/w1_design_astra.md)")
 272:         print("registered", h, regs[h]["id"], flush=True)
 273:     except ValueError as err:
 274:         ledger.record(f"Design note, {tag} not registered: {err}", "L0", [SCRIPT, str(BIN)],
 275:                       notes=f"design; effect below detectability at n {len(comps)}")
 276:         print(h, "not registered:", err, flush=True)
 277: 
 278: if "targets" not in sys.argv[1:]:
 279:     sys.exit(0)
 280: if not regs:
 281:     sys.exit("no hypothesis registered; no target computed")
 282: 
 283: # 3. targets, each with its own seed
 284: done = set(pd.read_csv(TGT)["comp"]) if TGT.exists() else set()
 285: for c, seed in zip(comps, seeds):
 286:     if key(c) in done:
 287:         continue
 288:     alloy = compute.solid_solution(c, "fcc", reps=3, seed=seed)
 289:     x = compute.actual_fractions(alloy)
 290:     assert max(abs(x[e] - c[e]) for e in c) < 1e-6, (key(c), x)
 291:     r = {"comp": key(c), "seed": seed, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
 292:          "time": dt.datetime.now().isoformat(timespec="seconds")}
 293:     pd.DataFrame([r]).to_csv(TGT, mode="a", header=not TGT.exists(), index=False, float_format="%.10g")
 294: print("targets done", flush=True)
 295: 
 296: # 4. test, matched by composition key
 297: t = pd.read_csv(TGT).set_index("comp").loc[[key(c) for c in comps]]
 298: y = {ch: t[ch].values for ch in CH}
 299: rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
 300: for ch in CH:
 301:     for name, m in (("all", np.ones(len(comps), bool)), ("Co", co), ("Co-free", ~co)):
 302:         print(ch, name, int(m.sum()), {arm: round(rm((y[ch] - P[ch][arm])[m]), 3) for arm in ARMS}, flush=True)
 303: rng = np.random.default_rng(11)
 304: for h, reg in regs.items():
 305:     new, old = HYP[h]
 306:     ok, gain, p = signflip(y["Kp"], P["Kp"][new], P["Kp"][old], rng)
 307:     k44 = signflip(y["K44"], P["K44"][new], P["K44"][old], rng)
 308:     print(f"{h}: gain {gain:.3f}, p {p:.1e} -> {'PASS' if ok else 'FAIL'}; K44 (secondary) gain {k44[1]:.3f}, "
 309:           f"p {k44[2]:.1e}", flush=True)
 310:     ledger.record(f"W1 {h} result: {'PASS' if ok else 'FAIL'}, K' RMSE {new} {rm(y['Kp'] - P['Kp'][new]):.3f} vs "
 311:                   f"{old} {rm(y['Kp'] - P['Kp'][old]):.3f} GPa, gain {gain:.3f}, p {p:.1e}; K44 gain {k44[1]:.3f}",
 312:                   "L0", [str(BIN), str(DIAG), str(TGT), str(COMPS), SCRIPT],
 313:                   notes=f"prereg {reg['id']}; independent audit and ledger.verdict pending")
AGENTS.md
scripts\__pycache__\k_shear_transfer.cpython-312.pyc
scripts\__pycache__\k_shear_mpa.cpython-312.pyc
scripts\__pycache__\k_shear_kp_hm.cpython-312.pyc
scripts\k_shear_transfer.py
scripts\k_shear_mpa.py
scripts\k_shear_kp_hm.py
scripts\k_asym_w1.py
graft\scripts\k_shear_transfer.md
graft\scripts\k_shear_mpa.md
graft\scripts\k_shear_kp_hm.md
graft\scripts\k_asym_w1.md
data\k_shear_mpa.log
data\k_shear_mpa.err
data\k_shear_kp_hm.log
data\k_shear_kp_hm.err
data\k_shear_transfer.log
data\k_shear_transfer.err
data\k_shear_transfer2.err
data\k_shear_transfer2.log

codex
Bilimsel sonuç denetimi skill’ini kullanıyorum. Kol seçimi ve bileşimle eşleştirme düzeltilmiş görünüyor. Mevcut dosyada kanal döngüsü `CH[::-1]`; yani kullanıcının notunun aksine şu an K44 önce hesaplanıyor. Ön kayıt kontrolünün hangi girdileri koruduğunu ve gürültü modelinin kalan sınırlarını kontrol ediyorum.

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content -Encoding UTF8 .orchestra/audits/w1_design_astra.md -Tail 180; Get-Content -Encoding UTF8 .orchestra/LESSONS.md -TotalCount 160; Get-Content -Encoding UTF8 STATUS.md -TotalCount 90' in C:\Users\can02\Projects\AI driven Science
exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$i=0; Get-Content scripts/k_shear_transfer.py | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ }; $i=0; Get-Content harness/ledger.py | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ }' in C:\Users\can02\Projects\AI driven Science
 succeeded in 429ms:
ledger.py           31.10.2026 09:34:56   3243
power.py            31.10.2026 09:34:56   1507



codex
**Mevcut s�r�m hesap ba�latmaya uygun de�il.** En kritik hata [k_asym_w1.py:124](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:124>): `arm.endswith("sym")`, `"asym"` i�in de `True`. Dolay�s�yla:

- `OV-asym = OV-sym`: H1, belirtilen asimetrik rakibi kar��la�t�rm�yor.
- `VV-asym = VV-sym`: H2'de kazan� **0**, p **1**; g�� **0** olur.
- Yeni 25:75 ve 75:25 hesaplar� yap�l�yor fakat tahminlerde kullan�lm�yor.

Dosya de�i�tirmedim; MACE hesab� veya yan etkili import �al��t�rmad�m.

1. **OV-asym, Wu/Marker'�n adil temsilcisi mi?**

   **Bu haliyle yaln�z bir analog; y�ntemlerin yeniden uygulanmas� de�il.** �� ayr� fark var:

   - **Fit:** �� noktadan �� RK katsay�s� belirlemek cebirsel olarak ge�erli ama doygun interpolasyon: uyum hatas� ve model derecesini do�rulayacak ba��ms�z nokta kalm�yor. Wu, ikilileri `x=0,0.1,,1` �zerinde hesapl�yor; Eq. 5.1 ayr�ca on-site/inter-site yap�s� i�eriyor. �� noktal� Muggianu bunun birebir kar��l��� de�il. Bunu [�zg�n tezde, ss. 43-44](C:/Users/can02/Downloads/etd.pdf) do�rulad�m.
   - **Hacim:** [Sat�r 123](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:123>) ikilinin **Vegard hacmini** kullan�yor; denge hacmini bulmuyor. Bu fark�n rakibi hangi y�nde etkiledi�i hesaplanmadan bilinemez.
   - **G�zlenebilir ve referans:** [curvatures():64](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_transfer.py:64>) ideal konumlarda, ayn� hacimdeki saf referanslar� ��kararak **clamped kar���m e�rili�i** hesapl�yor. Bu, denge hacimlerindeki elastik sabitlerden ve onlar�n saf-element referanslar�ndan farkl�d�r. Taslak da �n-gerilme katk�s�n� a��k�a ay�r�yor: [draft_v5.md:61](<C:/Users/can02/Projects/AI driven Science/paper/draft_v5.md:61>).

   **D�zeltme:** W1'i "ikili Vegard hacmi / hedef Vegard hacmi � simetrik / asimetrik temsil" kar��la�t�rmas� olarak s�n�rland�r; OV ad�n� �rne�in `BV` yap. Wu/Marker'� ge�ti�i iddias� i�in denge hacmi, relaksasyon ve referans tan�mlar� e�le�en ayr� benchmark gerekir. Marker'�n CALPHAD yakla��m�n� kaynak almak makul; mevcut kolu onun tam modeli diye adland�rmak de�il. [Marker 2017](https://www.sciencedirect.com/science/article/abs/pii/S0927025617304597)

   RK derecesini hedeflere bakmadan, ek ikili bile�imler ve ba��ms�z seed kontrolleriyle se�. Ayr�ca H1 hem hacmi hem model esnekli�ini de�i�tiriyor; **hacmin etkisini tek ba��na** g�stermek i�in ayn� derecedeki `VV-asym-BV-asym` kar��la�t�rmas�n� �nceden belirlemek gerekir.

2. **H1/H2 g�� hesab� ger�ek�i mi; s�z�nt� var m�?**

   [Sat�r 137-158](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:137>) gelecekteki W1 hedeflerini okumuyor: bu a��dan do�rudan hedef s�z�nt�s� yok. Fakat g�r�lt� modeli yeterince gerek�elendirilmi� de�il.

   Mevcut CSV'lerden ba��ms�z spline hesab�yla yeniden buldu�um K' art�klar�:

   | hm grubu | n | RMSE |
   |---|---:|---:|
   | T�m� | 94 | 1,892 GPa |
   | Co i�eren | 39 | 2,419 GPa |
   | Co i�ermeyen | 55 | 1,405 GPa |

   **Tek, s�f�r ortalamal� iid Gaussian bu bile�im ba��ml�l���n� siler.** `.orchestra/LESSONS.md:92-96` da art���n b�y�k b�l�m�n�n kompozisyon kaynakl� oldu�unu s�yl�yor.

   Ayr�ca hm hedefleri [seed 0](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_kp_hm.py:77>), girdiler seed 0-2: g�r�lt� kalibrasyonu tarihsel ortak-seed protokol�nden geliyor. Bunun K' g�r�lt�s�n� mutlaka k���ltt���n� s�yleyemem: yaln�z seed 1-2 girdileriyle RMSE **1,880 GPa** ��kt�. Ancak bu kontrol, yeni tasar�m�n g�r�lt� modelini do�rulam�yor.

   H2'de kullan�lan `VV-sym` art���, asimetri d�zeltmesinin a��klayabilece�i sinyali de i�erir; tamam�n� g�r�lt� saymak **muhafazak�r olabilir**. Buna kar��l�k ger�ek bile�imsel sapmay� s�f�r ortalamal� ba��ms�z g�r�lt�ye �evirmek iyimser olabilir. Y�n� �nceden belli de�il.

   **D�zeltme:** Ayr�k seed'li g�r�lm�� verilerden Co/bile�en say�s�/hacim fark�na ba�l� art�k senaryolar� kur; sistematik sapmay� koruyan g�� kontrolleri ekle. `truth=old` yaln�z tek bir null senaryosudur; e�it beklenen hata gibi s�n�r durumlar�n� da denetle.

   G��te **1.000**, sonu�ta **4.000** perm�tasyon kullan�l�yor. Ayn� test ayar�n� kullan; 200 sim�lasyonda �l��len g�� 0,80'in standart hatas� yakla��k **0,028**, dolay�s�yla e�ik yak�n�ndaki kay�t karar�n� daha fazla sim�lasyon ve belirsizlik aral���yla ver. `harness/power.py` kullanmak tek ba��na bu varsay�m sorunlar�n� ��zmez.

3. **Bile�im �ekimi, Co oran� ve ?=0,0025**

   [�ekim:52-74](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:52>) hedef de�erlerini kullanm�yor; 27/27/26 bile�en kotas� ve asimetri �art� �nceden sabitlenirse uygundur. Ancak sonu� yaln�z bu kesilmi� da��l�ma genellenebilir; b�t�n �ok bile�enli ala��mlara de�il.

   **Co'nun 40/80 olmas� tek ba��na sorun de�il.** Kotalardan beklenen say� yakla��k **35,44**; 40 ola�and��� g�r�nm�yor. Bilinen hata fark� nedeniyle Co'lu/Co'suz sonu�lar� �nceden tan�mlay�p **ikisini de** raporla. Kod �u anda yaln�z Co'suz altgrubu ayr�ca yazd�r�yor.

   **Seed 100, girdilerle ayr�d�r; b�t�n hedeflerde ayn� olmas� ise ayr� sorun.** [compute.py:49-56](<C:/Users/can02/Projects/AI driven Science/harness/compute.py:49>) yaln�z seed ve h�cre boyutuna ba�l� ortak perm�tasyon kullan�yor. Sat�rlar�n konfig�rasyon hatalar� ba��ml� olabilir; ba��ms�z sat�r i�aret �evirmesi bunu hesaba katm�yor. Her hedefe farkl�, girdilerden ayr�k seed ata. Bunlar ayr�ca optimize edilmi� SQS de�il, rastgele yerle�imler.

   **?=0,0025 uygundur ve muhafazak�rd�r:** iki K' testi i�in Bonferroni toplam s�n�r� 0,005 olur. K44 ve altgruplar do�rulay�c� iddiaya d�n��t�r�lecekse test ailesini yeniden tan�mlamak gerekir.

4. **`k_shear_transfer` import'u yan etkili mi?**

   **Evet, kesinlikle.** [Sat�r 40-41](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_transfer.py:40>) modeli y�kler; �st d�zey b�l�mler eksik ikilileri ve h3 hedeflerini hesaplay�p CSV'ye yazabilir, �n kay�t olu�turabilir ve eski hedef sonu�lar�n� okuyup test eder. `__main__` korumas� yaln�z en sondaki sonu� kayd�n� kaps�yor.

   W1'deki `sys.argv = sys.argv[:1]` bunlar� �nlemez. Fonksiyonlar� yan etkisiz yard�mc� mod�le ay�r; hesap, model y�kleme ve yaz�m ak���n� `main()` i�ine al.

5. **RK, i�aret, spline ve grid**

   | Kontrol | Sonu� |
   |---|---|
   | RK ��z�m� | **Do�ru**, fakat mevcut dallanma hatas� nedeniyle kullan�lm�yor. |
   | `t = x_a - x_b` | **Muggianu i�in do�ru.** `ctx.pairs()` ve ikili anahtarlar alfabetik s�ralamada tutarl�. |
   | Mutlak `ln V` spline ekseni | **Do�ru.** `ln(V/Vref)` ekseninden sabit �telemedir; sorgular da mutlak `ln V`. |
   | Grid kapsam� | **Garanti edilmiyor; sessiz ekstrapolasyon m�mk�n.** |

   [Grid:87-88](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:87>) yaln�z mevcut `[-0,40,+0,40]` listesini kesiyor. �ekim kurallar�na uygun **Au90Co9Ni9** h�cresinde Co-Ni 50:50 girdisi i�in gereken de�er **+0,42985**. `CubicSpline` varsay�lan ekstrapolasyonu bunu sessizce hesaplar. Bu, sabit 80'li �ekimde do�rulanm�� bir ihlal de�il; kapsam garantisinin bulunmad���n� g�steren somut kar�� �rnek.

   Bile�im ekseninde de `t=�0,5` ile fit edilen polinom, izin verilen hedeflerde `|t|=0,75` g�rebilir. Bunu ayr�ca kapsama kontrol�ne kat. �� noktal� ��z�mde
   `L2 = (32/3)(K25+K75) - 16K50`; e�it ba��ms�z giri� g�r�lt�s�nde L2 belirsizli�i yakla��k **22?** olur. Bu tek ba��na tahmin hatas� de�ildir, fakat derece do�rulamas�n�n �nemini g�sterir.

   �ki ek y�r�tme a���� var: [sat�r 191-192](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:191>) hedefleri bile�im anahtar�yla e�le�tirmeden dosya s�ras�yla kar��la�t�r�yor; [sat�r 151-154](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:151>) eski �n kayd� kod/girdi hash'lerini do�rulamadan yeniden kullan�yor. Devam ko�ular�nda ikisi de yanl�� de�erlendirmeye yol a�abilir. Sonu� kayd� ayr�ca ba��ms�z denetimden sonra `ledger.verdict` ile kapat�lmal�.

**VERDICT: NO-GO - mevcut betik i�in.** Hesaptan �nce gerekli d�zeltmeler:

- Asimetrik kol se�imini d�zelt ve d�rt kolun ger�ekten ayr��t���n� kontrol et.
- Import'u yan etkisiz yap.
- Kar��la�t�rman�n kapsam�n� ve ortak g�zlenebilir tan�m�n� sabitle.
- Hedef ba��na ba��ms�z seed; bile�imsel art�klar� koruyan g�� hesab� kullan.
- Hacim/bile�im kapsam�n� do�rula; sessiz ekstrapolasyonu kapat.
- Bile�imle e�le�tirme, tam hassasiyetli kay�t ve �n kay�t/girdi hash kontrol� ekle.

Wu'nun y�ntemini �zg�n PDF'den okudum; Marker'�n ayr�nt�lar� i�in mevcut tam-metin denetim kayd�n� kulland�m, PDF'sini bu tur yeniden a�amad�m. Python ortam� �al��mad���ndan 80'li �ekimi yeniden �retmedim; **40/80 say�s�n� verdi�in bilgi olarak ald�m**.


tokens used
111.692
**Mevcut s�r�m hesap ba�latmaya uygun de�il.** En kritik hata [k_asym_w1.py:124](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:124>): `arm.endswith("sym")`, `"asym"` i�in de `True`. Dolay�s�yla:

- `OV-asym = OV-sym`: H1, belirtilen asimetrik rakibi kar��la�t�rm�yor.
- `VV-asym = VV-sym`: H2'de kazan� **0**, p **1**; g�� **0** olur.
- Yeni 25:75 ve 75:25 hesaplar� yap�l�yor fakat tahminlerde kullan�lm�yor.

Dosya de�i�tirmedim; MACE hesab� veya yan etkili import �al��t�rmad�m.

1. **OV-asym, Wu/Marker'�n adil temsilcisi mi?**

   **Bu haliyle yaln�z bir analog; y�ntemlerin yeniden uygulanmas� de�il.** �� ayr� fark var:

   - **Fit:** �� noktadan �� RK katsay�s� belirlemek cebirsel olarak ge�erli ama doygun interpolasyon: uyum hatas� ve model derecesini do�rulayacak ba��ms�z nokta kalm�yor. Wu, ikilileri `x=0,0.1,,1` �zerinde hesapl�yor; Eq. 5.1 ayr�ca on-site/inter-site yap�s� i�eriyor. �� noktal� Muggianu bunun birebir kar��l��� de�il. Bunu [�zg�n tezde, ss. 43-44](C:/Users/can02/Downloads/etd.pdf) do�rulad�m.
   - **Hacim:** [Sat�r 123](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:123>) ikilinin **Vegard hacmini** kullan�yor; denge hacmini bulmuyor. Bu fark�n rakibi hangi y�nde etkiledi�i hesaplanmadan bilinemez.
   - **G�zlenebilir ve referans:** [curvatures():64](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_transfer.py:64>) ideal konumlarda, ayn� hacimdeki saf referanslar� ��kararak **clamped kar���m e�rili�i** hesapl�yor. Bu, denge hacimlerindeki elastik sabitlerden ve onlar�n saf-element referanslar�ndan farkl�d�r. Taslak da �n-gerilme katk�s�n� a��k�a ay�r�yor: [draft_v5.md:61](<C:/Users/can02/Projects/AI driven Science/paper/draft_v5.md:61>).

   **D�zeltme:** W1'i "ikili Vegard hacmi / hedef Vegard hacmi � simetrik / asimetrik temsil" kar��la�t�rmas� olarak s�n�rland�r; OV ad�n� �rne�in `BV` yap. Wu/Marker'� ge�ti�i iddias� i�in denge hacmi, relaksasyon ve referans tan�mlar� e�le�en ayr� benchmark gerekir. Marker'�n CALPHAD yakla��m�n� kaynak almak makul; mevcut kolu onun tam modeli diye adland�rmak de�il. [Marker 2017](https://www.sciencedirect.com/science/article/abs/pii/S0927025617304597)

   RK derecesini hedeflere bakmadan, ek ikili bile�imler ve ba��ms�z seed kontrolleriyle se�. Ayr�ca H1 hem hacmi hem model esnekli�ini de�i�tiriyor; **hacmin etkisini tek ba��na** g�stermek i�in ayn� derecedeki `VV-asym-BV-asym` kar��la�t�rmas�n� �nceden belirlemek gerekir.

2. **H1/H2 g�� hesab� ger�ek�i mi; s�z�nt� var m�?**

   [Sat�r 137-158](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:137>) gelecekteki W1 hedeflerini okumuyor: bu a��dan do�rudan hedef s�z�nt�s� yok. Fakat g�r�lt� modeli yeterince gerek�elendirilmi� de�il.

   Mevcut CSV'lerden ba��ms�z spline hesab�yla yeniden buldu�um K' art�klar�:

   | hm grubu | n | RMSE |
   |---|---:|---:|
   | T�m� | 94 | 1,892 GPa |
   | Co i�eren | 39 | 2,419 GPa |
   | Co i�ermeyen | 55 | 1,405 GPa |

   **Tek, s�f�r ortalamal� iid Gaussian bu bile�im ba��ml�l���n� siler.** `.orchestra/LESSONS.md:92-96` da art���n b�y�k b�l�m�n�n kompozisyon kaynakl� oldu�unu s�yl�yor.

   Ayr�ca hm hedefleri [seed 0](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_kp_hm.py:77>), girdiler seed 0-2: g�r�lt� kalibrasyonu tarihsel ortak-seed protokol�nden geliyor. Bunun K' g�r�lt�s�n� mutlaka k���ltt���n� s�yleyemem: yaln�z seed 1-2 girdileriyle RMSE **1,880 GPa** ��kt�. Ancak bu kontrol, yeni tasar�m�n g�r�lt� modelini do�rulam�yor.

   H2'de kullan�lan `VV-sym` art���, asimetri d�zeltmesinin a��klayabilece�i sinyali de i�erir; tamam�n� g�r�lt� saymak **muhafazak�r olabilir**. Buna kar��l�k ger�ek bile�imsel sapmay� s�f�r ortalamal� ba��ms�z g�r�lt�ye �evirmek iyimser olabilir. Y�n� �nceden belli de�il.

   **D�zeltme:** Ayr�k seed'li g�r�lm�� verilerden Co/bile�en say�s�/hacim fark�na ba�l� art�k senaryolar� kur; sistematik sapmay� koruyan g�� kontrolleri ekle. `truth=old` yaln�z tek bir null senaryosudur; e�it beklenen hata gibi s�n�r durumlar�n� da denetle.

   G��te **1.000**, sonu�ta **4.000** perm�tasyon kullan�l�yor. Ayn� test ayar�n� kullan; 200 sim�lasyonda �l��len g�� 0,80'in standart hatas� yakla��k **0,028**, dolay�s�yla e�ik yak�n�ndaki kay�t karar�n� daha fazla sim�lasyon ve belirsizlik aral���yla ver. `harness/power.py` kullanmak tek ba��na bu varsay�m sorunlar�n� ��zmez.

3. **Bile�im �ekimi, Co oran� ve ?=0,0025**

   [�ekim:52-74](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:52>) hedef de�erlerini kullanm�yor; 27/27/26 bile�en kotas� ve asimetri �art� �nceden sabitlenirse uygundur. Ancak sonu� yaln�z bu kesilmi� da��l�ma genellenebilir; b�t�n �ok bile�enli ala��mlara de�il.

   **Co'nun 40/80 olmas� tek ba��na sorun de�il.** Kotalardan beklenen say� yakla��k **35,44**; 40 ola�and��� g�r�nm�yor. Bilinen hata fark� nedeniyle Co'lu/Co'suz sonu�lar� �nceden tan�mlay�p **ikisini de** raporla. Kod �u anda yaln�z Co'suz altgrubu ayr�ca yazd�r�yor.

   **Seed 100, girdilerle ayr�d�r; b�t�n hedeflerde ayn� olmas� ise ayr� sorun.** [compute.py:49-56](<C:/Users/can02/Projects/AI driven Science/harness/compute.py:49>) yaln�z seed ve h�cre boyutuna ba�l� ortak perm�tasyon kullan�yor. Sat�rlar�n konfig�rasyon hatalar� ba��ml� olabilir; ba��ms�z sat�r i�aret �evirmesi bunu hesaba katm�yor. Her hedefe farkl�, girdilerden ayr�k seed ata. Bunlar ayr�ca optimize edilmi� SQS de�il, rastgele yerle�imler.

   **?=0,0025 uygundur ve muhafazak�rd�r:** iki K' testi i�in Bonferroni toplam s�n�r� 0,005 olur. K44 ve altgruplar do�rulay�c� iddiaya d�n��t�r�lecekse test ailesini yeniden tan�mlamak gerekir.

4. **`k_shear_transfer` import'u yan etkili mi?**

   **Evet, kesinlikle.** [Sat�r 40-41](<C:/Users/can02/Projects/AI driven Science/scripts/k_shear_transfer.py:40>) modeli y�kler; �st d�zey b�l�mler eksik ikilileri ve h3 hedeflerini hesaplay�p CSV'ye yazabilir, �n kay�t olu�turabilir ve eski hedef sonu�lar�n� okuyup test eder. `__main__` korumas� yaln�z en sondaki sonu� kayd�n� kaps�yor.

   W1'deki `sys.argv = sys.argv[:1]` bunlar� �nlemez. Fonksiyonlar� yan etkisiz yard�mc� mod�le ay�r; hesap, model y�kleme ve yaz�m ak���n� `main()` i�ine al.

5. **RK, i�aret, spline ve grid**

   | Kontrol | Sonu� |
   |---|---|
   | RK ��z�m� | **Do�ru**, fakat mevcut dallanma hatas� nedeniyle kullan�lm�yor. |
   | `t = x_a - x_b` | **Muggianu i�in do�ru.** `ctx.pairs()` ve ikili anahtarlar alfabetik s�ralamada tutarl�. |
   | Mutlak `ln V` spline ekseni | **Do�ru.** `ln(V/Vref)` ekseninden sabit �telemedir; sorgular da mutlak `ln V`. |
   | Grid kapsam� | **Garanti edilmiyor; sessiz ekstrapolasyon m�mk�n.** |

   [Grid:87-88](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:87>) yaln�z mevcut `[-0,40,+0,40]` listesini kesiyor. �ekim kurallar�na uygun **Au90Co9Ni9** h�cresinde Co-Ni 50:50 girdisi i�in gereken de�er **+0,42985**. `CubicSpline` varsay�lan ekstrapolasyonu bunu sessizce hesaplar. Bu, sabit 80'li �ekimde do�rulanm�� bir ihlal de�il; kapsam garantisinin bulunmad���n� g�steren somut kar�� �rnek.

   Bile�im ekseninde de `t=�0,5` ile fit edilen polinom, izin verilen hedeflerde `|t|=0,75` g�rebilir. Bunu ayr�ca kapsama kontrol�ne kat. �� noktal� ��z�mde
   `L2 = (32/3)(K25+K75) - 16K50`; e�it ba��ms�z giri� g�r�lt�s�nde L2 belirsizli�i yakla��k **22?** olur. Bu tek ba��na tahmin hatas� de�ildir, fakat derece do�rulamas�n�n �nemini g�sterir.

   �ki ek y�r�tme a���� var: [sat�r 191-192](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:191>) hedefleri bile�im anahtar�yla e�le�tirmeden dosya s�ras�yla kar��la�t�r�yor; [sat�r 151-154](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:151>) eski �n kayd� kod/girdi hash'lerini do�rulamadan yeniden kullan�yor. Devam ko�ular�nda ikisi de yanl�� de�erlendirmeye yol a�abilir. Sonu� kayd� ayr�ca ba��ms�z denetimden sonra `ledger.verdict` ile kapat�lmal�.

**VERDICT: NO-GO - mevcut betik i�in.** Hesaptan �nce gerekli d�zeltmeler:

- Asimetrik kol se�imini d�zelt ve d�rt kolun ger�ekten ayr��t���n� kontrol et.
- Import'u yan etkisiz yap.
- Kar��la�t�rman�n kapsam�n� ve ortak g�zlenebilir tan�m�n� sabitle.
- Hedef ba��na ba��ms�z seed; bile�imsel art�klar� koruyan g�� hesab� kullan.
- Hacim/bile�im kapsam�n� do�rula; sessiz ekstrapolasyonu kapat.
- Bile�imle e�le�tirme, tam hassasiyetli kay�t ve �n kay�t/girdi hash kontrol� ekle.

Wu'nun y�ntemini �zg�n PDF'den okudum; Marker'�n ayr�nt�lar� i�in mevcut tam-metin denetim kayd�n� kulland�m, PDF'sini bu tur yeniden a�amad�m. Python ortam� �al��mad���ndan 80'li �ekimi yeniden �retmedim; **40/80 say�s�n� verdi�in bilgi olarak ald�m**.


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
# Durum (2 Kas�m 2026)

Tek giri� noktas�. Ayr�nt� ve kan�t defterde (`claims/claims.jsonl`, kimlikler a�a��da), dersler `.orchestra/LESSONS.md` i�inde. `.orchestra/NIGHT_REPORT.md` 31 Ekim sabah�na ait ve eskidir ("iki ba��ms�z holdout" ifadesi d26bd71285 ile d�zeltildi).

## Bulgular

| # | Bulgu | Seviye | Kan�t | A��k olan |
|---|---|---|---|---|
| 1 | **K' hacim transferi.** Rastgele fcc ala��m�n kar���m K' de�eri = ? 4 x_i x_j K'_ij(V0), ikililer ala��m hacminde. �ki k�r sette hata yar�ya iniyor, k 1.08 ve 1.08. | L2 (697c2d6d75) | h3: 4c29d9754c  6e0923b413 (ortak iddia K44 y�z�nden FAIL); hm_fresh: 67a358fc59  d92844787f (PASS) | mpa modelinde k 1.33 [1.11, 1.51] (851aec6883  86767e478d), ama s�z�nt�s�z 150 ala��mda 1.10 [0.94, 1.26] (kay�ts�z; 6bc0e190a8 FAIL, sebep design). Denklik testi 88b9465108 FAIL: 1200 ala��m, k 1.14 [1.10, 1.18], kural yine hatay� 4.81'den 2.21 GPa'ya indiriyor (43370bbb27, verdict 736bcac471, Astra: kod hatas� yok). k kompozisyona ba�l� (ke�ifsel): 3 element 1.00, Cu'suz 1.00, Cu'lu 1.24, max|dlnV| > 0.25 iken 1.41. omat da benzer (1.11). k = 1 iddias� d��t�; b�y�k hacim fark�nda transfer eksik kal�yor. PBE yok. Literat�r (tam metin): k�smen biliniyor; hacim ad�m�, k�r test ve K'/K44 kar��tl��� bulunamad�. "Hacim transferli regular-solution / kesik tens�rel CE kural�" diye yaz�lmal�, Marker 2017 okunmadan yaz�lmamal�. |
| 2 | **Enerji hacim transferi: D��T�.** Standart Muggianu (saf elementler kendi hacminde) ayn� i�i yap�yor, 11.4 ile 11.5 meV, kural 13.3 (S2 denetimi, defterde d�zeltme). Eski metin: E_mix hatas� 36.4  13.1 meV, yaln�z hm_fresh (n 94) ger�ekten k�rd�. Tam hesapta k 0.94 ile 0.98; 0.81 do�rusalla�t�rma etkisi. | L2 (05f01df6ec, d�zeltme d26bd71285) | 1708d0db77, k_direct | Fikrin �z� Zunger 1987-89'da biliniyor (`claims/literature.jsonl`). PBE d�zenli h�cre L3'� FAIL (8541e914ea). |
| 3 | **K44 Co'suz ala��mlarda transfer oluyor** (�n kay�t e410c96a32  d9460850ce, 120 taze ala��m, kazan� 0.51, p 2.5e-4, k 1.23); Co'lularda olmuyor (kazan� 0.11). Eski g�zlem: Ayn� kural K44'te zay�f: kazan� 0.12 ile 0.20, k 0.69 ile 0.86. En k�t� hatalar Co'ca zengin ala��mlarda. | g�zlem | LESSONS 14 ile 16 | Neden a��k; ba��ms�z denetim yap�lmad�. Ke�if bak��� (g�r�lm�� 269 sat�r, kay�t de�il): "E_F'de y�ksek DOS" a��klamas� desteklenmiyor, art�k Pd/Pt/Ni/Rh/Ir/Co oran�yla iki kanalda da benzer b�y�yor (K44/K' rms oran� 1.15 ile 1.4). En b�y�k hatalar iki kanalda da Co'lu ala��mlarda (|r44| ile Co r 0.33): s�radaki ��pheli Co manyetizmas�. K44'�n hacim kaymas� da k���k, kazan� i�in az yer var (a2: pair 3.56  kural 2.66, K' 5.67  1.80). |
| 3b | **Ortak kayma taban�.** Hacim kural�n�n K44 ve K''te ka��rd��� k�s�m ayn� ve kompozisyona ait: K44 - K' kural� ge�iyor (kazan� 0.49), h�creler aras� r 0.75, bilinen �n gerilme �zde�li�i ��kar�l�nca r 0.67, k 0.99. K44'�n "tutmamas�" bu tabandan. | L0, �� �n kay�tl� PASS (b86e0d8a40, fd786169e3, ede47f1d65), ��� de Astra denetimi PLAUSIBLE | `data/k_aniso_s100_clamped.csv`, `k_floor_cells.csv`, `k_floor_stress_*.csv`; LESSONS 20-22 | �kili referanslardan gelen ortak hata d��lanmad� (iki ba��ms�z ikili paneli gerekli). Fiziksel anlam� a��k; MACE only. |
| 4 | **MACE kar���m kayma e�rili�inde L1'den ge�miyor.** 8 d�zenli L1_2 h�crede K' i�areti 8/8 do�ru, K44 i�areti 5/8 (Au3Ir PBE -32.4, MACE +3.2 GPa); medyan sapma K' i�in %47, K44 i�in %56. K' kural� yaln�z MACE i�inde g�sterilmi� say�l�r. | L1 FAIL (b3214734c2, Astra denetimli) | `data/hiso_l12_dft_v2.csv`, `data/hiso_l12_mace.csv` | dense-k ve ecutrho kontrolleri ko�uyor. |
| 5 | **H-iso.** H�cre i�i i�aret okumas�yla PASS (n 6, medyan K44/K' 0.94), tek i�aret okumas�yla FAIL (Pt3Cu pozitif). Ag3Ir 0.54, Ag3Rh 0.39, Pt3Cu 2.61: h�cre baz�nda izotropi yok. | L0, PLAUSIBLE (b3214734c2, sebep numerics, a��k) | `scripts/hiso_l12_v2.py` | 34/78 ko�uda negative rho; ecutrho �1.5 ve kspacing 0.08 kontrolleri bitince kapan�r. |

Yanl��lanan adaylar (A2, H-sm, R3, R3b, HM2-T4, Astra EOS kapan���) ve gerek�eleri defterde `verdict on ...` kay�tlar�nda.

## �al��an i�ler

- **H-iso kontrolleri (PBE, 2 �ekirdek, s�ral�):** dense bitti (`data/hiso_l12_dft_v2_dense.csv`, kspacing 0.08). Cu3Ir de�i�medi (K44 -54.75  -54.71, K' -57.39  -57.42). Ag3Rh K' kararl� (-17.97  -17.44) ama K44 -7.04  -3.64 GPa, oran 0.39  0.21: Ag3Rh K44 k-yak�nsak de�il. Medyan K44/K' 0.942  0.941, i�aretler ayn�, H-iso okumas� de�i�miyor. rho ko�usu 2 Kas�m 13:43'te reboot ile 8/18'de kesildi; 3 Kas�m 12:35'te devam ettirildi (log `data/hiso_l12_dft_v2_rho_resume1.log`, kalan Rh_t+ ve Pt3Cu, yakla��k 3 saat).

## S�radaki ad�mlar

1. Dense ve rho bitince H-iso'yu kapat: oranlar ve MACE fark� �%10 i�inde kal�yorsa verdict b3214734c2'yi kesinle�tir, kalm�yorsa sebep numerics ve yeni ko�u.
2. K' kural� i�in PBE (L3). **Tasar�m uyar�s�:** d�zenli 4 atomlu h�creler enerji kural�nda PBE'de +10 meV'lik sabit hacim �ok cisim terimi ta��d��� i�in yanl�� test ��kt� (d440b9eb7b, 8541e914ea). K' i�in de d�zenli h�cre kullan�lacaksa bu �nce d���n�lmeli; do�ru alan PBE SQS h�creleri (32 atom ve �st�) ve bu laptopta g�nler s�rer, kiral�k sunucu se�ene�i var.
3. PBE h�zland�rma: Cu3Ir'de smearing ve k-a�� gev�etmeyi referansa kar�� test et.
4. ~~Veri d�zeltmesi~~ yap�ld� (2 Kas�m): `scripts/fix_counts2.py`  `data/h1_ev_rows_fixed2.csv`, `h3_fresh_rows_fixed2.csv` (44 ��l�de -0.31 ile -0.71 meV, R ve B_chem yeniden). hm3 ve di�erlerinde 1/3 yok, yeni m�h�r gerekmedi. Enerji analizleri bundan sonra `_fixed2` okumal�.
5. L4 (2 Kas�m): son tarama ve Astra denetimi yap�ld� (`claims/literature.jsonl` sat�r 63 ve 64, `.orchestra/audits/L4_kprime_astra.md`). Karar PARTIALLY KNOWN, KEEP: kural ortak hacimli ikili regular-solution enerjisinin kayma t�revi, �zg�l uygulama bulunmad�. Wu 2021 tezi okundu (sat�r 65): ikili EMTO'dan bcc ��l�lere excess C' ve C44 aktar�m� var, ama her bile�im kendi hacminde; Vegard hacmi ad�m� yok. L4 taramas� kapand� (arama s�n�rl�), en yak�n �nc�l olarak draft_v5'e eklendi. Yeni risk: Soyemi 2026 ve Chong 2026, kural�n MACE i�inde tutmas�n�n model yanl�l��� olabilece�ini d���nd�r�yor; PBE aktar�m testi bu y�zden daha �nemli.
5b. Deney verisi (ajan taramas� 1 Kas�m): bu dokuz elementte �l��lm�� tek kristal ala��m sabitleri yaln�z kapal� eri�imde (Cu-Ni Epstein-Carlson 1965, Schmunk-Smith 1960; Cu-Au Chiarodo 1972, dC/dP ile; Pd-Ag Hoare-Yates 1954; Co-Ni Weston-Granato 1975). 3+ bile�enli �l��m yok. K�t�phane PDF'i gerekli.
5c. ~~nspin hatas�~~ d�zeltildi (2 Kas�m): `extra={'system.nspin': 1}` art�k ba�lang�� momenti koymuyor, Co girdisinde nspin 1 do�ruland�.
6. Makale: `paper/draft_v5.md` (v4 art� model yanl�l��� s�n�r�, madde 6, ve Soyemi, Chong kaynaklar�; ar�iv hen�z v4 ile). v4: Astra v4 incelemesindeki (`.orchestra/audits/draft_v4_astra.md`) b�t�n kapsam ve say� d�zeltmeleri uyguland�. Ar�iv `paper/repro_20261102_2.zip` (v4, requirements.txt, manifest do�ru; ar�ivden `chain.py` ve `fix_counts2.py` birebir �retiyor). G�nderim i�in kalan: yazar�n son okumas�, Zenodo'ya ar�iv y�kleme ve DOI'yi metne yazma, ChemRxiv g�nderimi. Bunlar� yazar yapar. Dense/rho sonucu gelince 5.1'deki "pending" c�mlesi g�ncellenir.

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

 succeeded in 422ms:
   1: """Shear-curvature volume transfer (swarm S1, open front, Opus): a new observable for the champion's mechanism.
   2: 
   3: python scripts/k_shear_transfer.py
   4: Claim: the clamped mixing shear curvatures of random fcc alloys are pair sums of 50:50 binary curvatures taken at the
   5: alloy's own volume, K_alloy(V0) = sum 4 x_i x_j K_ij(V0), with no parameter. Baseline: the same pair sum at each
   6: binary's own Vegard volume V_ij.
   7: Order, so that the test is blind:
   8:  1. binaries: K44, K' of the 50:50 binaries (SQS seeds 0-2) on a ln(V/V_ij) grid -> data/binary_kgrid.csv
   9:  2. predictions on the h3_fresh compositions (comp_actual, n_el >= 3; K never computed there), power by simulation,
  10:     pre-registration in the ledger
  11:  3. targets: the same a2 protocol on those alloys, references at the cell's actual fractions -> data/h3_shear_clamped.csv
  12:  4. test: per channel RMSE(rule) <= 0.9 RMSE(pair at V_ij) and paired sign-flip p < 0.005 (two channels); PASS needs
  13:     both channels. Secondary (reported, not gated): Opus's prior on median dlnK/dlnV of binaries with |K| > 10 GPa,
  14:     K44 in [-5, -1.5], K' in [-6, -2].
  15: """
  16: 
  17: import datetime as dt
  18: import os
  19: import sys
  20: import time
  21: from pathlib import Path
  22: 
  23: ROOT = Path(__file__).resolve().parent.parent
  24: os.environ["HARNESS_MODEL"] = "medium-omat-0"
  25: sys.path.insert(0, str(ROOT))
  26: 
  27: import numpy as np  # noqa: E402
  28: import pandas as pd  # noqa: E402
  29: from ase.build import bulk  # noqa: E402
  30: from scipy.interpolate import CubicSpline  # noqa: E402
  31: 
  32: from harness import compute, ledger  # noqa: E402
  33: from harness.compute import GPA  # noqa: E402
  34: from harness.context import context  # noqa: E402
  35: from harness.features import parse_comp  # noqa: E402
  36: 
  37: AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
  38: GRID = [-0.40, -0.30, -0.20, -0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40]
  39: BIN, TGT = ROOT / "data" / "binary_kgrid.csv", ROOT / "data" / "h3_shear_clamped.csv"
  40: ctx = context()
  41: calc = compute.calculator()
  42: SCRIPT = str(Path(__file__))
  43: 
  44: 
  45: def e_strained(atoms, v_atom, F):
  46:     a = atoms.copy()
  47:     a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
  48:     a.set_cell(a.cell @ F.T, scale_atoms=True)
  49:     a.calc = calc
  50:     t = time.perf_counter()
  51:     e = a.get_potential_energy() / len(a)
  52:     time.sleep(time.perf_counter() - t)  # 50% duty cycle, keeps the laptop cool
  53:     return e
  54: 
  55: 
  56: def F_of(name, s):
  57:     if name == "K44":
  58:         F = np.eye(3)
  59:         F[0, 1] = s
  60:         return F
  61:     return np.diag([np.exp(s), np.exp(-s), 1.0])
  62: 
  63: 
  64: def curvatures(alloy, x, v):
  65:     """K44, Kp (GPa) of E_mix with references at fractions x, all at volume v and the same deformation."""
  66:     pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in x}
  67:     out = {}
  68:     for name in ("K44", "Kp"):
  69:         em = [e_strained(alloy, v, F_of(name, s)) - sum(xi * e_strained(pures[el], v, F_of(name, s))
  70:                                                          for el, xi in x.items()) for s in AMPS]
  71:         c2 = np.polyfit(AMPS, em, 2)[0]
  72:         out[name] = (2 * c2 if name == "K44" else c2 / 2) / v * GPA
  73:     return out
  74: 
  75: 
  76: # 1. binaries
  77: done = set(map(tuple, pd.read_csv(BIN)[["pair", "seed", "dlnV"]].astype(str).values)) if BIN.exists() else set()
  78: for (A, B), p in sorted(ctx.pair.items()):
  79:     for seed in (0, 1, 2):
  80:         alloy = compute.solid_solution({A: 0.5, B: 0.5}, "fcc", reps=3, seed=seed)
  81:         for d in GRID:
  82:             if (f"{A}-{B}", str(seed), str(d)) in done:
  83:                 continue
  84:             v = p["V"] * np.exp(d)
  85:             r = {"pair": f"{A}-{B}", "seed": seed, "dlnV": d, "V": v, **curvatures(alloy, {A: 0.5, B: 0.5}, v)}
  86:             pd.DataFrame([r]).to_csv(BIN, mode="a", header=not BIN.exists(), index=False)
  87:     print("binary", A, B, flush=True)
  88: 
  89: g = pd.read_csv(BIN).groupby(["pair", "dlnV"])[["K44", "Kp"]].mean().reset_index()
  90: spl = {(tuple(k.split("-")), ch): CubicSpline(s.dlnV, s[ch]) for k, s in g.groupby("pair") for ch in ("K44", "Kp")}
  91: 
  92: # 2. predictions, power, pre-registration
  93: h3 = pd.read_csv(ROOT / "data" / "h3_fresh_rows_fixed.csv")
  94: h3 = h3[h3.n_el >= 3].reset_index(drop=True)
  95: comps = [parse_comp(s) for s in h3.comp_actual]
  96: keep = [all(((a, b), "K44") in spl for a, b, _, _ in ctx.pairs(c)) for c in comps]
  97: h3, comps = h3[keep].reset_index(drop=True), [c for c, k in zip(comps, keep) if k]
  98: 
  99: 
 100: def predict(c, ch, at_alloy):
 101:     v0 = ctx.vegard(c)
 102:     return sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v0 / ctx.pair[(a, b)]["V"]) if at_alloy else 0.0))
 103:                for a, b, xa, xb in ctx.pairs(c))
 104: 
 105: 
 106: P = {ch: (np.array([predict(c, ch, True) for c in comps]), np.array([predict(c, ch, False) for c in comps]))
 107:      for ch in ("K44", "Kp")}
 108: 
 109: 
 110: def test(y, rule, pair, n_perm=4000, seed=0):
 111:     e_r, e_p = y - rule, y - pair
 112:     gain = 1 - np.sqrt(np.mean(e_r**2)) / np.sqrt(np.mean(e_p**2))
 113:     d = e_p**2 - e_r**2
 114:     rng = np.random.default_rng(seed)
 115:     null = np.array([(d * rng.choice([-1, 1], len(d))).mean() for _ in range(n_perm)])
 116:     p = (np.sum(null >= d.mean()) + 1) / (n_perm + 1)
 117:     return gain >= 0.10 and p < 0.005, float(gain), float(p)
 118: 
 119: 
 120: # Realistic scatter = the rule's residual on the exploratory a2 rows (h1 compositions, n_el >= 3), the arena's
 121: # convention. A first design used the pair sum's residual there (4 GPa, includes the transfer signal itself) and had
 122: # power 0.45, so it was not registered and no target was computed (ledger design note).
 123: a2 = pd.read_csv(ROOT / "data" / "a2_shear_clamped.csv")
 124: a2c = [parse_comp(s) for s in a2.comp]
 125: a2k = [len(c) >= 3 and all(((a, b), "K44") in spl for a, b, _, _ in ctx.pairs(c)) for c in a2c]
 126: a2, a2c = a2[a2k], [c for c, k in zip(a2c, a2k) if k]
 127: SIG = {ch: float(np.sqrt(np.mean((a2[ch].values - [sum(4 * xa * xb * float(spl[((a, b), ch)](np.log(v / ctx.pair[(a, b)]["V"])))
 128:                                                         for a, b, xa, xb in ctx.pairs(c)) for c, v in zip(a2c, a2.V0)])**2)))
 129:        for ch in ("K44", "Kp")}
 130: regs = [e for e in ledger.entries() if e["claim"].startswith("Shear-curvature volume transfer") and "prereg" in e["notes"]]
 131: if not regs:
 132:     if not any(e["claim"].startswith("Design note, shear-curvature transfer") for e in ledger.entries()):
 133:         ledger.record("Design note, shear-curvature transfer: first design (sigma 4 GPa = pair-sum residual on exploratory "
 134:                       "a2 rows) had power 0.45 and was not registered; no h3 target computed. Exploratory a2 (n 62, "
 135:                       "seen): K44 pair 3.56 -> rule 2.66 GPa, Kp 5.67 -> 1.80, refit k 0.90 / 1.05. Redesign: sigma = "
 136:                       f"rule residual on a2 {SIG}, the arena convention", "L0", [SCRIPT, str(BIN)],
 137:                       notes="design; before registration")
 138:     rng = np.random.default_rng(1)
 139:     sim = lambda truth: np.mean([all(test(P[ch][truth] + rng.normal(0, SIG[ch], len(comps)),  # noqa: E731
 140:                                           *P[ch], 1000, i)[0] for ch in P) for i in range(200)])
 141:     power, fp = sim(0), sim(1)
 142:     print(f"n {len(comps)}, power {power:.3f}, false pass {fp:.3f}", flush=True)
 143:     reg = ledger.register(f"Shear-curvature volume transfer: clamped mixing K44 and K' of random fcc alloys equal "
 144:                           f"sum 4 x_i x_j K_ij(V0) with binary curvatures at the alloy volume (no parameter); PASS if "
 145:                           f"in both channels RMSE <= 0.9 x pair-at-V_ij and sign-flip p < 0.005 on {len(comps)} h3_fresh "
 146:                           f"alloys whose K has never been computed", SCRIPT, {"power": power, "false_pass": fp},
 147:                           notes="proposed by Opus in swarm S1 (open front), critiqued by Astra; binaries computed first")
 148:     print("registered", reg["id"], flush=True)
 149:     regs = [reg]
 150: 
 151: # 3. targets
 152: done = set(pd.read_csv(TGT)["comp"]) if TGT.exists() else set()
 153: for s, c in zip(h3.comp_actual, comps):
 154:     if s in done:
 155:         continue
 156:     alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
 157:     x = compute.actual_fractions(alloy)
 158:     assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
 159:     r = {"comp": s, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
 160:          "time": dt.datetime.now().isoformat(timespec="seconds")}
 161:     pd.DataFrame([r]).to_csv(TGT, mode="a", header=not TGT.exists(), index=False)
 162: print("targets done", flush=True)
 163: 
 164: # 4. test
 165: t = pd.read_csv(TGT).set_index("comp").loc[h3.comp_actual]
 166: res = {}
 167: for ch in ("K44", "Kp"):
 168:     y = t[ch].values
 169:     ok, gain, p = test(y, *P[ch])
 170:     rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
 171:     T = P[ch][0] - P[ch][1]
 172:     k = float(T @ (y - P[ch][1]) / (T @ T))
 173:     res[ch] = ok
 174:     print(f"{ch}: raw {rm(y - y.mean()):.2f}, pair at V_ij {rm(y - P[ch][1]):.2f}, rule {rm(y - P[ch][0]):.2f} GPa, "
 175:           f"gain {gain:.2f}, p {p:.1e}, refit k {k:.2f} -> {'pass' if ok else 'fail'}", flush=True)
 176: sl = {}
 177: for ch in ("K44", "Kp"):
 178:     vals = [float(spl[((tuple(k.split('-'))), ch)](0, 1) / spl[((tuple(k.split('-'))), ch)](0))
 179:             for k in g.pair.unique() if abs(spl[((tuple(k.split('-'))), ch)](0)) > 10]
 180:     sl[ch] = (len(vals), float(np.median(vals)) if vals else float("nan"))
 181: print("secondary: median dlnK/dlnV of binaries with |K| > 10 GPa:", sl, flush=True)
 182: passed = all(res.values())
 183: if __name__ == "__main__":  # k_shear_kp_hm.py imports this file for its splines; the h3 result is recorded once
 184:     ledger.record(f"Shear-curvature volume transfer: {'PASS' if passed else 'FAIL'} on {len(comps)} unseen h3 alloys "
 185:               f"(K44 {'pass' if res['K44'] else 'fail'}, Kp {'pass' if res['Kp'] else 'fail'}); binary slope prior {sl}",
 186:               "L0", [str(BIN), str(TGT), SCRIPT], notes=f"prereg {regs[0]['id']}")
   1: """Append-only claim ledger. Nothing is called a discovery unless it is here at L2 or above.
   2: 
   3: Every entry above L1 names a parent entry one level below, so a claim's chain of evidence
   4: can be walked back to the calibration of the method that produced its data.
   5: """
   6: 
   7: from __future__ import annotations
   8: 
   9: import datetime as dt
  10: import hashlib
  11: import json
  12: from pathlib import Path
  13: 
  14: LEDGER = Path(__file__).resolve().parent.parent / "claims" / "claims.jsonl"
  15: LEVELS = ("L0", "L1", "L2", "L3", "L4")
  16: 
  17: 
  18: def file_hash(path: str | Path) -> str:
  19:     return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]
  20: 
  21: 
  22: def entries() -> list[dict]:
  23:     if not LEDGER.exists():
  24:         return []
  25:     return [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line]
  26: 
  27: 
  28: def record(claim: str, level: str, evidence: list[str], notes: str = "",
  29:            parent: str | None = None) -> dict:
  30:     assert level in LEVELS, level
  31:     if level in ("L2", "L3", "L4"):
  32:         below = LEVELS[LEVELS.index(level) - 1]
  33:         known = {e.get("id"): e["level"] for e in entries()}
  34:         if known.get(parent) != below:
  35:             raise ValueError(f"{level} claim needs a parent entry at {below}, got {parent!r}")
  36:     now = dt.datetime.now().isoformat(timespec="seconds")
  37:     entry = {"id": hashlib.sha256(f"{now}{claim}".encode()).hexdigest()[:10], "time": now,
  38:              "level": level, "claim": claim, "parent": parent,
  39:              "evidence": {str(p): file_hash(p) for p in evidence}, "notes": notes}
  40:     LEDGER.parent.mkdir(exist_ok=True)
  41:     with LEDGER.open("a", encoding="utf-8") as f:
  42:         f.write(json.dumps(entry, ensure_ascii=False) + "\n")
  43:     return entry
  44: 
  45: 
  46: # Pre-registration and verdicts. A test is registered with its measured power (harness/power.py): a design in which
  47: # a correct formula usually fails is not a test. A failed test is closed with a cause; only cause "hypothesis" retires
  48: # the candidate, "design" and "numerics" send it back to the queue.
  49: CAUSES = ("pass", "hypothesis", "design", "numerics")
  50: 
  51: 
  52: def register(claim: str, script: str, power: dict, notes: str = "") -> dict:
  53:     if power.get("power", 0) < 0.8 or power.get("false_pass", 1) > 0.05:
  54:         raise ValueError(f"underpowered or leaky test design, not registered: {power}")
  55:     return record(claim, "L0", [script], notes=f"prereg; power {power}; {notes}".strip("; "))
  56: 
  57: 
  58: def verdict(prereg: str, outcome: str, cause: str, audit: str, evidence: list[str]) -> dict:
  59:     assert cause in CAUSES, cause
  60:     if cause == "hypothesis" and not audit.strip():
  61:         raise ValueError("retiring a candidate needs a post-fail audit (what was checked, by whom)")
  62:     return record(f"verdict on {prereg}: {outcome}", "L0", evidence, notes=f"cause={cause}; audit: {audit}")
  63: 
  64: 
  65: def open_candidates() -> list[dict]:
  66:     """Registered candidates without a verdict, or whose last verdict was a design or numerics failure."""
  67:     es = entries()
  68:     last = {}
  69:     for e in es:
  70:         if e["claim"].startswith("verdict on "):
  71:             last[e["claim"].split()[2].rstrip(":")] = e["notes"]
  72:     return [e for e in es if e["notes"].startswith("prereg")
  73:             and ("cause=pass" not in last.get(e["id"], "") and "cause=hypothesis" not in last.get(e["id"], ""))]

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$i=0; Get-Content harness/context.py | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ }; $i=0; Get-Content harness/compute.py | Select-Object -First 155 | ForEach-Object { $i++; '"'{0,4}: {1}' -f "'$i,$_ }; rg -n "W1|k_asym" claims/claims.jsonl; Get-ChildItem data/w1*, data/binary_k* | Select-Object Name,Length,LastWriteTime; Get-Content -Encoding UTF8 C:'"\\Users\\can02\\.codex\\memories\\rollout_summaries\\2026-10-31T21-44-07-VJVR-validate_k44_shear_transfer_hypotheses.md -TotalCount 70" in C:\Users\can02\Projects\AI driven Science
 succeeded in 743ms:
   1: """What a candidate formula may use: per-element and per-binary inputs, never the alloy's own target.
   2: 
   3: ctx.pure[el]      dict: V (A^3/atom, MACE fcc), B, G, C11, C12, C44 (GPa), r, chi, vec, tm
   4: ctx.pair[(a, b)]  dict for sorted element pairs, 50:50 random clamped binary at its Vegard volume V_ij:
   5:                   E (eV/atom), D = dE/dlnV, D2 = d2E/dlnV2 (eV/atom), V (A^3/atom); mean over SQS seeds 0-2
   6: ctx.vegard(comp)  Vegard volume of a composition
   7: ctx.pairs(comp)   iterator over (a, b, x_a, x_b) for unlike pairs
   8: """
   9: 
  10: from __future__ import annotations
  11: 
  12: from functools import lru_cache
  13: from itertools import combinations
  14: from pathlib import Path
  15: 
  16: import pandas as pd
  17: 
  18: from harness.features import elem, parse_comp
  19: 
  20: ROOT = Path(__file__).resolve().parent.parent
  21: 
  22: 
  23: class Context:
  24:     def __init__(self):
  25:         p = pd.read_csv(ROOT / "data" / "scan_fcc_omat_pure.csv").set_index("el")
  26:         self.pure = {}
  27:         for el, r in p.iterrows():
  28:             self.pure[el] = {"V": r.vol_per_atom, "B": r.B, "G": r.G, "C11": r.C11, "C12": r.C12, "C44": r.C44,
  29:                              **elem(el)}
  30:         h1 = pd.read_csv(ROOT / "data" / "h1_ev_rows.csv")
  31:         h1["c"] = h1.comp.map(parse_comp)
  32:         eq = h1[(h1.n_el == 2) & h1.c.map(lambda c: all(abs(v - 0.5) < 1e-3 for v in c.values()))]
  33:         rows = [eq[["comp", "E_mix", "dE_dlnV", "d2E_dlnV2"]]]
  34:         seeds = ROOT / "data" / "binary_seeds.csv"
  35:         if seeds.exists():
  36:             rows.append(pd.read_csv(seeds)[["comp", "E_mix", "dE_dlnV", "d2E_dlnV2"]])
  37:         b = pd.concat(rows)
  38:         b["pair"] = b.comp.map(lambda s: tuple(sorted(parse_comp(s))))
  39:         m = b.groupby("pair")[["E_mix", "dE_dlnV", "d2E_dlnV2"]].mean()
  40:         self.pair = {k: {"E": r.E_mix, "D": r.dE_dlnV, "D2": r.d2E_dlnV2,
  41:                          "V": 0.5 * (self.pure[k[0]]["V"] + self.pure[k[1]]["V"])} for k, r in m.iterrows()}
  42: 
  43:     def vegard(self, comp: dict) -> float:
  44:         return sum(x * self.pure[e]["V"] for e, x in comp.items())
  45: 
  46:     def pairs(self, comp: dict):
  47:         for a, b in combinations(sorted(comp), 2):
  48:             yield a, b, comp[a], comp[b]
  49: 
  50: 
  51: @lru_cache(maxsize=1)
  52: def context() -> Context:
  53:     return Context()
   1: """Structure generation, relaxation and elastic constants with a universal ML potential."""
   2: 
   3: from __future__ import annotations
   4: 
   5: import datetime as dt
   6: import os
   7: import time
   8: from functools import lru_cache
   9: 
  10: import numpy as np
  11: from ase import Atoms
  12: from ase.build import bulk
  13: from ase.filters import FrechetCellFilter
  14: from ase.optimize import FIRE
  15: 
  16: from harness.reference import ELASTIC_EXP
  17: 
  18: GPA = 160.21766208  # eV/A^3 -> GPa
  19: MODEL = os.environ.get("HARNESS_MODEL", "medium-omat-0")  # mace_mp foundation model name
  20: 
  21: # Rough lattice parameters (A) for the starting guess only; relaxation sets the real value.
  22: A0 = {"fcc": {"Al": 4.05, "Cu": 3.61, "Ni": 3.52, "Ag": 4.09, "Au": 4.08, "Pd": 3.89,
  23:               "Pt": 3.92, "Co": 3.54, "Fe": 3.59, "Cr": 3.60, "Mn": 3.60},
  24:       "bcc": {"Fe": 2.87, "Cr": 2.88, "Mo": 3.15, "W": 3.16, "V": 3.03, "Nb": 3.30,
  25:               "Ta": 3.30, "Ti": 3.28, "Zr": 3.57, "Hf": 3.50, "Al": 3.24}}
  26: 
  27: 
  28: @lru_cache(maxsize=1)
  29: def calculator():
  30:     from mace.calculators import mace_mp
  31:     import torch
  32:     device = "cuda" if torch.cuda.is_available() else "cpu"
  33:     return mace_mp(model=MODEL, device=device, default_dtype="float64")
  34: 
  35: 
  36: def site_counts(comp: dict[str, float], n: int) -> dict[str, int]:
  37:     counts = {el: int(round(x * n)) for el, x in comp.items()}
  38:     counts[max(counts, key=counts.get)] += n - sum(counts.values())
  39:     return counts
  40: 
  41: 
  42: def actual_fractions(atoms: Atoms) -> dict[str, float]:
  43:     """Composition the cell really has. Subtract pure references with these, not the nominal fractions (the
  44:     rounding to whole atoms shifted E_mix by up to ~57 meV/atom before 2026-10-31)."""
  45:     s = atoms.get_chemical_symbols()
  46:     return {el: s.count(el) / len(s) for el in sorted(set(s))}
  47: 
  48: 
  49: def solid_solution(comp: dict[str, float], lattice: str, reps: int, seed: int) -> Atoms:
  50:     """Random solid solution on a cubic conventional supercell (no SQS optimisation). Counts are rounded to whole
  51:     atoms; use actual_fractions() for references."""
  52:     a = sum(x * A0[lattice].get(el, 3.5 if lattice == "fcc" else 3.1) for el, x in comp.items())
  53:     atoms = bulk("X", lattice, a=a, cubic=True).repeat((reps, reps, reps))
  54:     counts = site_counts(comp, len(atoms))
  55:     symbols = [el for el, c in counts.items() for _ in range(c)]
  56:     np.random.default_rng(seed).shuffle(symbols)
  57:     atoms.set_chemical_symbols(symbols)
  58:     return atoms
  59: 
  60: 
  61: # GPU duty cycle in (0, 1]: after each relaxation sleep so the GPU is busy only this fraction
  62: # of the time. Keeps a laptop from overheating on long scans; results are unaffected.
  63: DUTY = float(os.environ.get("HARNESS_DUTY", "1.0"))
  64: 
  65: 
  66: def relax(atoms: Atoms, cell: bool, fmax: float = 1e-3, steps: int = 400) -> int:
  67:     atoms.calc = calculator()
  68:     target = FrechetCellFilter(atoms) if cell else atoms
  69:     opt = FIRE(target, logfile=None)
  70:     t = time.perf_counter()
  71:     opt.run(fmax=fmax, steps=steps)
  72:     if DUTY < 1:
  73:         time.sleep((time.perf_counter() - t) * (1 / DUTY - 1))
  74:     return opt.nsteps
  75: 
  76: 
  77: def elastic_tensor(atoms: Atoms, eps: float = 0.005, relax_ions: bool = True) -> np.ndarray:
  78:     """Full 6x6 Voigt tensor (GPa) from central differences of stress, ions relaxed at each strain."""
  79:     cell0 = atoms.get_cell().array.copy()
  80:     C = np.zeros((6, 6))
  81:     voigt = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
  82:     for j, (k, l) in enumerate(voigt):
  83:         sig = []
  84:         for s in (+eps, -eps):
  85:             e = np.zeros((3, 3))
  86:             if k == l:
  87:                 e[k, k] = s
  88:             else:
  89:                 e[k, l] = e[l, k] = s / 2  # engineering shear strain = s
  90:             strained = atoms.copy()
  91:             strained.set_cell(cell0 @ (np.eye(3) + e), scale_atoms=True)
  92:             strained.calc = calculator()
  93:             if relax_ions and len(strained) > 1:
  94:                 relax(strained, cell=False, fmax=5e-4)
  95:             sig.append(strained.get_stress(voigt=True) * GPA)  # ASE: tensile stress positive
  96:         C[:, j] = (sig[0] - sig[1]) / (2 * eps)
  97:     return 0.5 * (C + C.T)
  98: 
  99: 
 100: def cubic_average(C: np.ndarray) -> tuple[float, float, float]:
 101:     """Project a (noisy, random alloy) 6x6 tensor onto cubic symmetry."""
 102:     c11 = np.mean([C[0, 0], C[1, 1], C[2, 2]])
 103:     c12 = np.mean([C[0, 1], C[0, 2], C[1, 2]])
 104:     c44 = np.mean([C[3, 3], C[4, 4], C[5, 5]])
 105:     return float(c11), float(c12), float(c44)
 106: 
 107: 
 108: def voigt_reuss_hill(c11: float, c12: float, c44: float) -> dict[str, float]:
 109:     B = (c11 + 2 * c12) / 3
 110:     Gv = (c11 - c12 + 3 * c44) / 5
 111:     Gr = 5 * (c11 - c12) * c44 / (4 * c44 + 3 * (c11 - c12))
 112:     G = (Gv + Gr) / 2
 113:     E = 9 * B * G / (3 * B + G)
 114:     nu = (3 * B - 2 * G) / (2 * (3 * B + G))
 115:     return {"B": B, "G": G, "E": E, "nu": nu, "pugh": B / G, "cauchy": c12 - c44,
 116:             "zener": 2 * c44 / (c11 - c12)}
 117: 
 118: 
 119: def run_alloy(comp: dict[str, float], lattice: str, reps: int = 3, seed: int = 0) -> dict:
 120:     atoms = solid_solution(comp, lattice, reps, seed)
 121:     nsteps = relax(atoms, cell=True)
 122:     C = elastic_tensor(atoms)
 123:     c11, c12, c44 = cubic_average(C)
 124:     # Quality flag: spread of the three cubic-equivalent C11 and C44 entries. Large spread means the
 125:     # random cell is too small for its chemistry or the solid solution broke symmetry on relaxing.
 126:     spread = float(max(np.ptp(np.diag(C)[:3]) / c11, np.ptp(np.diag(C)[3:]) / max(c44, 1.0)))
 127:     vol = atoms.get_volume() / len(atoms)
 128:     row = {"formula": atoms.get_chemical_formula(mode="metal"),
 129:            "comp": ";".join(f"{el}:{x:.4f}" for el, x in sorted(comp.items())),
 130:            "lattice": lattice, "natoms": len(atoms), "seed": seed, "model": MODEL,
 131:            "vol_per_atom": vol, "a_eff": (vol * (4 if lattice == "fcc" else 2)) ** (1 / 3),
 132:            "relax_steps": nsteps, "cubic_spread": spread, "C11": c11, "C12": c12, "C44": c44,
 133:            "time": dt.datetime.now().isoformat(timespec="seconds")}
 134:     row.update(voigt_reuss_hill(c11, c12, c44))
 135:     return row
 136: 
 137: 
 138: def calibrate(elements: list[str] | None = None) -> list[dict]:
 139:     rows = []
 140:     for el in elements or list(ELASTIC_EXP):
 141:         lattice, e11, e12, e44 = ELASTIC_EXP[el]
 142:         r = run_alloy({el: 1.0}, lattice, reps=1)
 143:         r["el"] = el
 144:         r.update({"C11_exp": e11, "C12_exp": e12, "C44_exp": e44})
 145:         r.update({f"{k}_exp": v for k, v in voigt_reuss_hill(e11, e12, e44).items()})
 146:         rows.append(r)
 147:     return rows

Name                 Length LastWriteTime      
----                 ------ -------------      
binary_kgrid.csv      98994 31.10.2026 19:06:12
binary_kgrid_mpa.csv  32953 31.10.2026 21:43:39
thread_id: 01a193eb-8431-7393-ae70-82453cb5df2f
updated_at: 2026-10-31T20:57:09+00:00
rollout_path: C:\Users\can02\.codex\sessions\2026\11\01\rollout-2026-11-01T00-44-07-01a193eb-8431-7393-ae70-82453cb5df2f.jsonl
cwd: \\?\C:\Users\can02\Projects\AI driven Science

# Validated two candidate explanations for K44 shear-transfer failure

Rollout context: In `C:\Users\can02\Projects\AI driven Science`, the task was to verify two proposed answers for `.orchestra/fronts/k44.md` against repository data/scripts and literature, then return JSON verdicts.

## Task 1: Evaluate astra_1 composition-asymmetry hypothesis

Outcome: success

Key steps:
- Recomputed binary residuals from `data/a2_shear_clamped.csv` and cubic-spline interpolation of `data/binary_kgrid.csv`.
- Confirmed cited residuals: Co0.75Ir0.25 has K44/Kp residuals about `-7.66/-6.33 GPa`; Co0.25Pt0.75 about `+4.44/+3.60 GPa`.
- Confirmed all three proposed predictions reproduce the stated formula `1.5*K50(V) - K(complement)`.
- Literature search identified the antisymmetric `x(1-x)(1-2x)` Redlich-Kister form as known, with related elastic-property composition models.

Verdict: DROP; prior = KNOWN. The mechanism is physically plausible and numerically supported, but it is a known subregular/Redlich-Kister composition term, affects K44 and Kp similarly rather than explaining the channel-specific failure, is not Co-specific, and relies on noisy seed-0 rows. Large residuals also occur in Cu-Rh, Cu-Ir, Au-Ir, and Au-Rh, while several Co binaries have small K44 residuals.

## Task 2: Evaluate astra_2 sampling/direction-averaging hypothesis

Outcome: success

Key steps:
- Verified `harness/compute.py` randomizes atoms without SQS optimization; `scripts/k_shear_transfer.py` uses only xy simple shear and target calculations use seed 0.
- Recomputed seed scatter. At binary Vegard volumes, the four named pairs reproduce approximately 1.93 GPa K44 SD and 0.45 GPa Kp SD; across the full grid, the four-pair values are about 2.67/1.25 GPa (the proposed 1.93/1.17 values correspond to all-pair averaging).
- Ran an additional 108-atom, 36-pair, 3-seed stress check. Deviatoric stress was only 0.17 GPa RMS; K44 seed variation correlated with cell anisotropy (`r=-0.544` against `d sigma_yy`), supporting directional/cell-anisotropy sampling noise rather than the proposed stress confound.
- Verified that identical seeds produce identical 50:50 site patterns across element pairs, and seed-0 multicomponent patterns are nested/correlated. Seed 0 averages about 0.50 GPa below the three-seed K44 mean.
- Literature search found established work on SQS supercell size/shape effects, cubic projection, and elastic-constant uncertainty: Tasnadi et al. (2012), Tian et al. (2015), Moakher & Norris (2006), and Caro (2014).

Verdict: KEEP; prior = KNOWN. It is a valid numerical/design correction, not a novel physical mechanism. Future K44 tests should vary seeds across rows and average independent shear planes before interpreting the Co/non-Co split. Direction averaging may reduce noise, but cannot by itself explain the full 8-10 GPa residuals or the K44/Kp transfer gap.

No repository claim or ledger files were modified. Temporary stress-check artifacts were written under the Claude scratchpad in `C:\Users\can02\AppData\Local\Temp\claude\...\scratchpad\stress.py` and `stress.csv`.



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$s=Get-Content scripts/k_shear_transfer.py; for ($i=25; $i -lt 88; $i++) { '"'{0}: {1}' -f ("'$i+1),$s[$i] }; $s=Get-Content -Encoding UTF8 .orchestra/LESSONS.md; for ($i=0; $i -lt $s.Count; $i++) { if ($i -lt 30 -or ($i -ge 78 -and $i -le 105)) { '"'{0}: {1}' -f ("'$i+1),$s[$i] } }; Get-Content -Encoding UTF8 STATUS.md -TotalCount 36; Get-Content harness/power.py; Get-Command python,py -ErrorAction SilentlyContinue | Select-Object Name,Source; Get-Item .venv/Scripts/python.exe -ErrorAction SilentlyContinue | Select-Object FullName,Length; Get-FileHash scripts/k_asym_w1.py' in C:\Users\can02\Projects\AI driven Science
 succeeded in 3632ms:
26: 
27: import numpy as np  # noqa: E402
28: import pandas as pd  # noqa: E402
29: from ase.build import bulk  # noqa: E402
30: from scipy.interpolate import CubicSpline  # noqa: E402
31: 
32: from harness import compute, ledger  # noqa: E402
33: from harness.compute import GPA  # noqa: E402
34: from harness.context import context  # noqa: E402
35: from harness.features import parse_comp  # noqa: E402
36: 
37: AMPS = np.array([-0.01, -0.005, 0.0, 0.005, 0.01])
38: GRID = [-0.40, -0.30, -0.20, -0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40]
39: BIN, TGT = ROOT / "data" / "binary_kgrid.csv", ROOT / "data" / "h3_shear_clamped.csv"
40: ctx = context()
41: calc = compute.calculator()
42: SCRIPT = str(Path(__file__))
43: 
44: 
45: def e_strained(atoms, v_atom, F):
46:     a = atoms.copy()
47:     a.set_cell(a.cell * (v_atom * len(a) / a.get_volume()) ** (1 / 3), scale_atoms=True)
48:     a.set_cell(a.cell @ F.T, scale_atoms=True)
49:     a.calc = calc
50:     t = time.perf_counter()
51:     e = a.get_potential_energy() / len(a)
52:     time.sleep(time.perf_counter() - t)  # 50% duty cycle, keeps the laptop cool
53:     return e
54: 
55: 
56: def F_of(name, s):
57:     if name == "K44":
58:         F = np.eye(3)
59:         F[0, 1] = s
60:         return F
61:     return np.diag([np.exp(s), np.exp(-s), 1.0])
62: 
63: 
64: def curvatures(alloy, x, v):
65:     """K44, Kp (GPa) of E_mix with references at fractions x, all at volume v and the same deformation."""
66:     pures = {el: bulk(el, "fcc", a=4.0, cubic=True) for el in x}
67:     out = {}
68:     for name in ("K44", "Kp"):
69:         em = [e_strained(alloy, v, F_of(name, s)) - sum(xi * e_strained(pures[el], v, F_of(name, s))
70:                                                          for el, xi in x.items()) for s in AMPS]
71:         c2 = np.polyfit(AMPS, em, 2)[0]
72:         out[name] = (2 * c2 if name == "K44" else c2 / 2) / v * GPA
73:     return out
74: 
75: 
76: # 1. binaries
77: done = set(map(tuple, pd.read_csv(BIN)[["pair", "seed", "dlnV"]].astype(str).values)) if BIN.exists() else set()
78: for (A, B), p in sorted(ctx.pair.items()):
79:     for seed in (0, 1, 2):
80:         alloy = compute.solid_solution({A: 0.5, B: 0.5}, "fcc", reps=3, seed=seed)
81:         for d in GRID:
82:             if (f"{A}-{B}", str(seed), str(d)) in done:
83:                 continue
84:             v = p["V"] * np.exp(d)
85:             r = {"pair": f"{A}-{B}", "seed": seed, "dlnV": d, "V": v, **curvatures(alloy, {A: 0.5, B: 0.5}, v)}
86:             pd.DataFrame([r]).to_csv(BIN, mode="a", header=not BIN.exists(), index=False)
87:     print("binary", A, B, flush=True)
88: 
1: # Lessons for derivation agents (Astra, Opus)
2: 
3: Read before proposing. Each line is a way a candidate died or nearly died for the wrong reason. Updated 2026-10-31.
4: 
5: 1. Ratios of energies blow up where the denominator crosses zero (R3: n_eff = -3 b/a reached -102 for Cu-Ir). Prefer
6:    predictions linear in measured quantities; if a ratio is essential, say where it is undefined.
7: 2. Compare like with like: clamped with clamped, relaxed with relaxed, random with random. R3 compared a relaxed random
8:    volume with a clamped L1_0 volume; even the exact formula then had slope 0.20.
9: 3. Ordered cells are not random alloys. In PBE, 4-atom ordered cells carry a fixed-volume many-body term (~10 meV/atom)
10:    that random alloys lack. A random-alloy rule must be tested on random (SQS) cells.
11: 4. If your rule's main content is a common shift, a test with a free intercept cannot see it. State the test you expect
12:    to pass, and check its power by simulation (harness/power.py) before data exist.
13: 5. Results that survived so far: volume transfer of binary interactions (L2, refit k = 0.79 on both holdouts, not
14:    input noise); isotropic chemical shear softening K44 ~ K' in Ir/Rh alloys (MACE, PBE pending). Build on these.
15: 6. Results that died for real: A2 (shear from hydrostatic derivatives; even a free 2-term fit has r 0.37), H-sm
16:    (predicted K44/K' = 4, measured 1.05), R3b (exponent sharing). Do not resubmit without a new mechanism.
17: 7. PBE: pure references must share the alloy's cutoff (dft.Settings(ecut_elements=...)). Earlier PBE mixing numbers
18:    carry a cutoff mismatch; its size is being measured (data/ecut_bias.csv).
19: 8. Round R1 (Astra and Opus independently): 108-atom cells round atom counts, but references used nominal fractions,
20:    so every non-integer composition carried up to ~60 meV/atom of bookkeeping error. Fixed in data/*_fixed.csv
21:    (column comp_actual is the real composition) and in the generators. Always reference the composition the cell has.
22: 9. PBE cutoff mismatch corrected (harness/ecutfix.py, validated to 0.002 meV/atom). MACE now PASSES L1 for the
23:    ordered-cell beyond-pair Delta (sign 9/10, r 0.80); PBE quaternary Delta +12.9 meV is real. MACE data on ordered
24:    multicomponent cells can be used.
25: 10. Round R2 (Astra): the arena's permutation count capped the smallest reachable p at 1/501, so after five tests no
26:     candidate could pass however good it was. Fixed: n_perm grows with m. Also open: generators set V0 from nominal
27:     fractions while comp_actual differs (~0.5% in volume, ~0.06 meV RMSE effect, not the cause of k ~ 0.8).
28: 11. k ~ 0.8 was mostly linearisation: E_ij(V) is strongly nonlinear over |ln(V0/V_ij)| up to 0.36. Exact binary
29:     energies at the alloy volume give k 0.94 [0.90, 0.98] and RMSE 10.3 meV with no parameter (data/binary_vgrid.csv).
30: 12. Swarm S1 audit (Astra): (a) scripts/hiso_l12.py did not use ecut_elements, and harness/dft.py picks the k-grid
79:     corr(e44, e') 0.77, joint k 0.91, b 0.94; plain K44 Co-free gain 0.47, Co 0.09. Astra audit: PLAUSIBLE, the
80:     null could not separate a compositional floor from same-cell noise. A shared-channel claim needs targets for the
81:     two channels from different cells. Test fd786169e3.
82: 
83: 21. The shared floor is compositional (fd786169e3 PASS, two cells per composition, unique seeds): cross-cell corr
84:     0.75 vs same-cell 0.79, k 0.92, b 0.95; Astra audit PLAUSIBLE (cell noise ~5% of the shared covariance). Next
85:     doubt is a known identity: clamped curvatures carry the initial stress, K44 = C44 + s_yy, K' = C' + (s_xx+s_yy)/2.
86:     A floor claim must survive subtracting it (k_floor_stress.py). Pre-register every step; one audit, one test.
87: 
88: 22. The floor survives the known pre-stress identity (ede47f1d65 PASS; Astra PLAUSIBLE): corrected cross-cell r
89:     0.67, k 0.99, b 0.79. Mixing pre-stress is 7 GPa rms but pair-additive (rule leaves 0.7 GPa), so it was never the
90:     floor. Remaining doubt: error shared through the binary references (b drops to 0.4-0.5 with single disjoint
91:     seeds). Shared-residual claims need two independent binary panels, as in k_mpa_equiv.py.
92: 23. k = 1 is retired (88b9465108 FAIL, cause hypothesis; Astra found no coding error). Under mpa, 1200 alloys: k 1.14
93:     [1.10, 1.18]; the rule still halves the error (4.81 to 2.21 GPa). k is not a model constant but composition
94:     dependent: 3 elements 1.00, Cu-free 1.00, Cu 1.24, alloys with max|dlnV| > 0.25 1.41; omat shows the same pattern
95:     (1.11). The pair transfer under-predicts at large size mismatch. A power sim that treats the target residual as
96:     cell noise is optimistic: most of it is compositional and does not average out over cells.
# Durum (2 Kas�m 2026)

Tek giri� noktas�. Ayr�nt� ve kan�t defterde (`claims/claims.jsonl`, kimlikler a�a��da), dersler `.orchestra/LESSONS.md` i�inde. `.orchestra/NIGHT_REPORT.md` 31 Ekim sabah�na ait ve eskidir ("iki ba��ms�z holdout" ifadesi d26bd71285 ile d�zeltildi).

## Bulgular

| # | Bulgu | Seviye | Kan�t | A��k olan |
|---|---|---|---|---|
| 1 | **K' hacim transferi.** Rastgele fcc ala��m�n kar���m K' de�eri = ? 4 x_i x_j K'_ij(V0), ikililer ala��m hacminde. �ki k�r sette hata yar�ya iniyor, k 1.08 ve 1.08. | L2 (697c2d6d75) | h3: 4c29d9754c  6e0923b413 (ortak iddia K44 y�z�nden FAIL); hm_fresh: 67a358fc59  d92844787f (PASS) | mpa modelinde k 1.33 [1.11, 1.51] (851aec6883  86767e478d), ama s�z�nt�s�z 150 ala��mda 1.10 [0.94, 1.26] (kay�ts�z; 6bc0e190a8 FAIL, sebep design). Denklik testi 88b9465108 FAIL: 1200 ala��m, k 1.14 [1.10, 1.18], kural yine hatay� 4.81'den 2.21 GPa'ya indiriyor (43370bbb27, verdict 736bcac471, Astra: kod hatas� yok). k kompozisyona ba�l� (ke�ifsel): 3 element 1.00, Cu'suz 1.00, Cu'lu 1.24, max|dlnV| > 0.25 iken 1.41. omat da benzer (1.11). k = 1 iddias� d��t�; b�y�k hacim fark�nda transfer eksik kal�yor. PBE yok. Literat�r (tam metin): k�smen biliniyor; hacim ad�m�, k�r test ve K'/K44 kar��tl��� bulunamad�. "Hacim transferli regular-solution / kesik tens�rel CE kural�" diye yaz�lmal�, Marker 2017 okunmadan yaz�lmamal�. |
| 2 | **Enerji hacim transferi: D��T�.** Standart Muggianu (saf elementler kendi hacminde) ayn� i�i yap�yor, 11.4 ile 11.5 meV, kural 13.3 (S2 denetimi, defterde d�zeltme). Eski metin: E_mix hatas� 36.4  13.1 meV, yaln�z hm_fresh (n 94) ger�ekten k�rd�. Tam hesapta k 0.94 ile 0.98; 0.81 do�rusalla�t�rma etkisi. | L2 (05f01df6ec, d�zeltme d26bd71285) | 1708d0db77, k_direct | Fikrin �z� Zunger 1987-89'da biliniyor (`claims/literature.jsonl`). PBE d�zenli h�cre L3'� FAIL (8541e914ea). |
| 3 | **K44 Co'suz ala��mlarda transfer oluyor** (�n kay�t e410c96a32  d9460850ce, 120 taze ala��m, kazan� 0.51, p 2.5e-4, k 1.23); Co'lularda olmuyor (kazan� 0.11). Eski g�zlem: Ayn� kural K44'te zay�f: kazan� 0.12 ile 0.20, k 0.69 ile 0.86. En k�t� hatalar Co'ca zengin ala��mlarda. | g�zlem | LESSONS 14 ile 16 | Neden a��k; ba��ms�z denetim yap�lmad�. Ke�if bak��� (g�r�lm�� 269 sat�r, kay�t de�il): "E_F'de y�ksek DOS" a��klamas� desteklenmiyor, art�k Pd/Pt/Ni/Rh/Ir/Co oran�yla iki kanalda da benzer b�y�yor (K44/K' rms oran� 1.15 ile 1.4). En b�y�k hatalar iki kanalda da Co'lu ala��mlarda (|r44| ile Co r 0.33): s�radaki ��pheli Co manyetizmas�. K44'�n hacim kaymas� da k���k, kazan� i�in az yer var (a2: pair 3.56  kural 2.66, K' 5.67  1.80). |
| 3b | **Ortak kayma taban�.** Hacim kural�n�n K44 ve K''te ka��rd��� k�s�m ayn� ve kompozisyona ait: K44 - K' kural� ge�iyor (kazan� 0.49), h�creler aras� r 0.75, bilinen �n gerilme �zde�li�i ��kar�l�nca r 0.67, k 0.99. K44'�n "tutmamas�" bu tabandan. | L0, �� �n kay�tl� PASS (b86e0d8a40, fd786169e3, ede47f1d65), ��� de Astra denetimi PLAUSIBLE | `data/k_aniso_s100_clamped.csv`, `k_floor_cells.csv`, `k_floor_stress_*.csv`; LESSONS 20-22 | �kili referanslardan gelen ortak hata d��lanmad� (iki ba��ms�z ikili paneli gerekli). Fiziksel anlam� a��k; MACE only. |
| 4 | **MACE kar���m kayma e�rili�inde L1'den ge�miyor.** 8 d�zenli L1_2 h�crede K' i�areti 8/8 do�ru, K44 i�areti 5/8 (Au3Ir PBE -32.4, MACE +3.2 GPa); medyan sapma K' i�in %47, K44 i�in %56. K' kural� yaln�z MACE i�inde g�sterilmi� say�l�r. | L1 FAIL (b3214734c2, Astra denetimli) | `data/hiso_l12_dft_v2.csv`, `data/hiso_l12_mace.csv` | dense-k ve ecutrho kontrolleri ko�uyor. |
| 5 | **H-iso.** H�cre i�i i�aret okumas�yla PASS (n 6, medyan K44/K' 0.94), tek i�aret okumas�yla FAIL (Pt3Cu pozitif). Ag3Ir 0.54, Ag3Rh 0.39, Pt3Cu 2.61: h�cre baz�nda izotropi yok. | L0, PLAUSIBLE (b3214734c2, sebep numerics, a��k) | `scripts/hiso_l12_v2.py` | 34/78 ko�uda negative rho; ecutrho �1.5 ve kspacing 0.08 kontrolleri bitince kapan�r. |

Yanl��lanan adaylar (A2, H-sm, R3, R3b, HM2-T4, Astra EOS kapan���) ve gerek�eleri defterde `verdict on ...` kay�tlar�nda.

## �al��an i�ler

- **H-iso kontrolleri (PBE, 2 �ekirdek, s�ral�):** dense bitti (`data/hiso_l12_dft_v2_dense.csv`, kspacing 0.08). Cu3Ir de�i�medi (K44 -54.75  -54.71, K' -57.39  -57.42). Ag3Rh K' kararl� (-17.97  -17.44) ama K44 -7.04  -3.64 GPa, oran 0.39  0.21: Ag3Rh K44 k-yak�nsak de�il. Medyan K44/K' 0.942  0.941, i�aretler ayn�, H-iso okumas� de�i�miyor. rho ko�usu 2 Kas�m 13:43'te reboot ile 8/18'de kesildi; 3 Kas�m 12:35'te devam ettirildi (log `data/hiso_l12_dft_v2_rho_resume1.log`, kalan Rh_t+ ve Pt3Cu, yakla��k 3 saat).

## S�radaki ad�mlar

1. Dense ve rho bitince H-iso'yu kapat: oranlar ve MACE fark� �%10 i�inde kal�yorsa verdict b3214734c2'yi kesinle�tir, kalm�yorsa sebep numerics ve yeni ko�u.
2. K' kural� i�in PBE (L3). **Tasar�m uyar�s�:** d�zenli 4 atomlu h�creler enerji kural�nda PBE'de +10 meV'lik sabit hacim �ok cisim terimi ta��d��� i�in yanl�� test ��kt� (d440b9eb7b, 8541e914ea). K' i�in de d�zenli h�cre kullan�lacaksa bu �nce d���n�lmeli; do�ru alan PBE SQS h�creleri (32 atom ve �st�) ve bu laptopta g�nler s�rer, kiral�k sunucu se�ene�i var.
3. PBE h�zland�rma: Cu3Ir'de smearing ve k-a�� gev�etmeyi referansa kar�� test et.
4. ~~Veri d�zeltmesi~~ yap�ld� (2 Kas�m): `scripts/fix_counts2.py`  `data/h1_ev_rows_fixed2.csv`, `h3_fresh_rows_fixed2.csv` (44 ��l�de -0.31 ile -0.71 meV, R ve B_chem yeniden). hm3 ve di�erlerinde 1/3 yok, yeni m�h�r gerekmedi. Enerji analizleri bundan sonra `_fixed2` okumal�.
5. L4 (2 Kas�m): son tarama ve Astra denetimi yap�ld� (`claims/literature.jsonl` sat�r 63 ve 64, `.orchestra/audits/L4_kprime_astra.md`). Karar PARTIALLY KNOWN, KEEP: kural ortak hacimli ikili regular-solution enerjisinin kayma t�revi, �zg�l uygulama bulunmad�. Wu 2021 tezi okundu (sat�r 65): ikili EMTO'dan bcc ��l�lere excess C' ve C44 aktar�m� var, ama her bile�im kendi hacminde; Vegard hacmi ad�m� yok. L4 taramas� kapand� (arama s�n�rl�), en yak�n �nc�l olarak draft_v5'e eklendi. Yeni risk: Soyemi 2026 ve Chong 2026, kural�n MACE i�inde tutmas�n�n model yanl�l��� olabilece�ini d���nd�r�yor; PBE aktar�m testi bu y�zden daha �nemli.
5b. Deney verisi (ajan taramas� 1 Kas�m): bu dokuz elementte �l��lm�� tek kristal ala��m sabitleri yaln�z kapal� eri�imde (Cu-Ni Epstein-Carlson 1965, Schmunk-Smith 1960; Cu-Au Chiarodo 1972, dC/dP ile; Pd-Ag Hoare-Yates 1954; Co-Ni Weston-Granato 1975). 3+ bile�enli �l��m yok. K�t�phane PDF'i gerekli.
5c. ~~nspin hatas�~~ d�zeltildi (2 Kas�m): `extra={'system.nspin': 1}` art�k ba�lang�� momenti koymuyor, Co girdisinde nspin 1 do�ruland�.
6. Makale: `paper/draft_v5.md` (v4 art� model yanl�l��� s�n�r�, madde 6, ve Soyemi, Chong kaynaklar�; ar�iv hen�z v4 ile). v4: Astra v4 incelemesindeki (`.orchestra/audits/draft_v4_astra.md`) b�t�n kapsam ve say� d�zeltmeleri uyguland�. Ar�iv `paper/repro_20261102_2.zip` (v4, requirements.txt, manifest do�ru; ar�ivden `chain.py` ve `fix_counts2.py` birebir �retiyor). G�nderim i�in kalan: yazar�n son okumas�, Zenodo'ya ar�iv y�kleme ve DOI'yi metne yazma, ChemRxiv g�nderimi. Bunlar� yazar yapar. Dense/rho sonucu gelince 5.1'deki "pending" c�mlesi g�ncellenir.

## Harness haritas�

| Par�a | Yer |
|---|---|
"""Power check for a pre-registered test, run before the test data exist.

A test is only informative if (a) data generated with the hypothesis TRUE, at realistic noise, pass it most of the
time and (b) data with the hypothesis FALSE rarely pass. Both are estimated by simulation. Two failures this tool is
meant to catch, from 2026-10-31: the L3 ordered-cell design (an intercept absorbed the rule's main signal) and R3
(the observable compared relaxed with clamped volumes, so even the exact formula had slope 0.20).
"""

from __future__ import annotations

from typing import Callable

import numpy as np


def power(test: Callable[[object], bool], simulate_true: Callable[[np.random.Generator], object],
          simulate_null: Callable[[np.random.Generator], object], n: int = 300, seed: int = 0) -> dict:
    rng = np.random.default_rng(seed)
    p = np.mean([bool(test(simulate_true(rng))) for _ in range(n)])
    f = np.mean([bool(test(simulate_null(rng))) for _ in range(n)])
    return {"power": round(float(p), 3), "false_pass": round(float(f), 3), "n_sims": n}


def near_zero_divisor(x, name: str, frac: float = 0.1) -> list[int]:
    """Indices where a quantity used as a divisor is small relative to its spread (ratio predictions blow up there)."""
    x = np.asarray(x, dtype=float)
    bad = np.flatnonzero(np.abs(x) < frac * np.std(x))
    if len(bad):
        print(f"warning: {name} near zero at rows {bad.tolist()}; a ratio-based prediction is unstable there")
    return bad.tolist()

FullName                                                           Length
--------                                                           ------
C:\Users\can02\Projects\AI driven Science\.venv\Scripts\python.exe 274424
                                                                         



exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command ".\\.venv\\Scripts\\python.exe -B -c \"import sys; import numpy, pandas, scipy; print(sys.version); print(numpy.__version__)\"" in C:\Users\can02\Projects\AI driven Science
 exited 1 in 103ms:
Unable to create process using '"C:\Users\can02\AppData\Local\Programs\Python\Python312\python.exe" -B -c "import sys; import numpy, pandas, scipy; print(sys.version); print(numpy.__version__)"'

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command 'Get-Content data/hm_shear_clamped.csv -TotalCount 4; Get-Content data/binary_kgrid.csv -TotalCount 3; $s=Get-Content scripts/k_shear_kp_hm.py; for ($i=55; $i -lt 88; $i++) { '"'{0}: {1}' -f ("'$i+1),$s[$i] }; (Get-FileHash scripts/k_asym_w1.py).Hash; Get-Content .venv/pyvenv.cfg' in C:\Users\can02\Projects\AI driven Science
 succeeded in 561ms:
comp,n_el,V0,K44,Kp,time
Cu:0.1111;Ir:0.2685;Ni:0.6204,3,11.94978861424134,-54.20079542116013,-55.224767834782185,2026-10-31T19:39:16
Au:0.2037;Ir:0.3611;Pd:0.2407;Rh:0.1944,4,15.213192702943054,-16.375493218240656,-16.950609473613955,2026-10-31T19:39:29
Au:0.4074;Cu:0.2130;Pt:0.3796,3,15.748955644407335,6.078173723678074,6.306101604588543,2026-10-31T19:39:39
pair,seed,dlnV,V,K44,Kp
Ag-Au,0,-0.4,11.985651277317022,8.523430390840046,1.9362738616052462
Ag-Au,0,-0.3,13.246193225887012,6.83273983768061,0.09415509585070463
56: h3 = pd.read_csv(kst.TGT).set_index("comp").loc[kst.h3.comp_actual]
57: SIG = max(kst.SIG["Kp"], float(np.sqrt(np.mean((h3.Kp.values - kst.P["Kp"][0]) ** 2))))
58: regs = [e for e in ledger.entries() if e["claim"].startswith(CLAIM) and "prereg" in e["notes"]]
59: if not regs:
60:     rng = np.random.default_rng(2)
61:     sim = lambda truth: np.mean([test(P["Kp"][truth] + rng.normal(0, SIG, len(comps)), *P["Kp"], 1000, i)[0]  # noqa: E731
62:                                  for i in range(300)])
63:     power, fp = sim(0), sim(1)
64:     print(f"n {len(comps)}, sigma {SIG:.2f}, power {power:.3f}, false pass {fp:.3f}", flush=True)
65:     reg = ledger.register(f"{CLAIM}: clamped mixing K' of random fcc alloys equals sum 4 x_i x_j K'_ij(V0) with binary "
66:                           f"curvatures at the alloy volume (no parameter); PASS if RMSE <= 0.9 x pair-at-V_ij and "
67:                           f"sign-flip p < 0.005 on {len(comps)} hm_fresh alloys whose shear has never been computed",
68:                           SCRIPT, {"power": power, "false_pass": fp},
69:                           notes="fresh test after joint claim 4c29d9754c failed on K44 only (6e0923b413)")
70:     print("registered", reg["id"], flush=True)
71:     regs = [reg]
72: 
73: done = set(pd.read_csv(OUT)["comp"]) if OUT.exists() else set()
74: for s, c in zip(hm.comp_actual, comps):
75:     if s in done:
76:         continue
77:     alloy = compute.solid_solution(c, "fcc", reps=3, seed=0)
78:     x = compute.actual_fractions(alloy)
79:     assert max(abs(x[e] - c[e]) for e in c) < 1e-3, (s, x)
80:     r = {"comp": s, "n_el": len(c), "V0": ctx.vegard(c), **curvatures(alloy, x, ctx.vegard(c)),
81:          "time": dt.datetime.now().isoformat(timespec="seconds")}
82:     pd.DataFrame([r]).to_csv(OUT, mode="a", header=not OUT.exists(), index=False)
83: print("targets done", flush=True)
84: 
85: t = pd.read_csv(OUT).set_index("comp").loc[hm.comp_actual]
86: rm = lambda e: float(np.sqrt(np.mean(np.square(e))))  # noqa: E731
87: out = {}
88: for ch in ("Kp", "K44"):
1643FE6BF036FDCB6B283055CBBCF317F6A259F7C6CB53F50FE66396A3D2664F
home = C:\Users\can02\AppData\Local\Programs\Python\Python312
include-system-site-packages = false
version = 3.12.10
executable = C:\Users\can02\AppData\Local\Programs\Python\Python312\python.exe
command = C:\Users\can02\AppData\Local\Programs\Python\Python312\python.exe -m venv C:\Users\can02\Projects\AI driven Science\.venv

codex
İki önemli açık sürüyor: güç hesabı artıkları Co’ya göre ayırıyor ama rastgele işaret vererek sistematik bileşimsel sapmayı hâlâ siliyor; ön kayıt kontrolü de yalnız betiğin hash’ini doğruluyor, veri girdilerini korumuyor. Ek derece kontrolü için hesaplanan noktalar ise RK tahminiyle karşılaştırılmıyor. Python ortamı başlatılamadı; kalan kontrolleri salt okunur kaynak ve bellek içi sayısal kontrollerle tamamlıyorum.

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$paths=@('"'scripts/k_asym_w1.py','scripts/k_shear_transfer.py','harness/ledger.py','harness/compute.py'); foreach ("'$p in $paths) { $f=Get-Item $p; [pscustomobject]@{Path=$p;Length=$f.Length;Modified=$f.LastWriteTime;SHA256=(Get-FileHash $p).Hash} | ConvertTo-Json -Compress }; $w=Get-Content scripts/k_asym_w1.py; for ($i=235; $i -lt 276; $i++) { '"'{0}: {1}' -f ("'$i+1),$w[$i] }; rg -n "DIAG|diagnostic|extrapolate|CH'"\\[|main__|file_hash|xA_actual\" scripts/k_asym_w1.py; "'$files=@('"'data/w1_compositions.csv','data/w1_shear_clamped.csv','data/binary_kgrid_asym.csv','data/binary_k_asym_diag.csv'); foreach ("'$p in $files) { '"'{0}: exists={1}' -f "'$p,(Test-Path $p) }; $entries=Get-Content claims/claims.jsonl | ConvertFrom-Json; '"'W1 entries: ' + @("'$entries | Where-Object { $_.claim -match '"'"'^W1 |''^Design note, W1 '"' }).Count; "'$m=Get-Content C:'"\\Users\\can02\\.codex\\memories\\MEMORY.md; for ("'$i=133; $i -lt 137; $i++) { '"'{0}: {1}' -f ("'$i+1),$m[$i] }' in C:\Users\can02\Projects\AI driven Science
 succeeded in 672ms:
Cannot convert value "System.Collections.Specialized.OrderedDictionary" to type "System.Management.Automation.LanguageP
rimitives+InternalPSCustomObject". Error: "Cannot convert hashtable to an object of the following type: System.Manageme
nt.Automation.LanguagePrimitives+InternalPSCustomObject. Hashtable-to-Object conversion is not supported in constrained
 language mode, restricted language mode or a Data section."
At line:2 char:147
+ ... et-Item $p; [pscustomobject]@{Path=$p;Length=$f.Length;Modified=$f.La ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : InvalidCastConstructorException
 
Cannot convert value "System.Collections.Specialized.OrderedDictionary" to type "System.Management.Automation.LanguageP
rimitives+InternalPSCustomObject". Error: "Cannot convert hashtable to an object of the following type: System.Manageme
nt.Automation.LanguagePrimitives+InternalPSCustomObject. Hashtable-to-Object conversion is not supported in constrained
 language mode, restricted language mode or a Data section."
At line:2 char:147
+ ... et-Item $p; [pscustomobject]@{Path=$p;Length=$f.Length;Modified=$f.La ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : InvalidCastConstructorException
 
Cannot convert value "System.Collections.Specialized.OrderedDictionary" to type "System.Management.Automation.LanguageP
rimitives+InternalPSCustomObject". Error: "Cannot convert hashtable to an object of the following type: System.Manageme
nt.Automation.LanguagePrimitives+InternalPSCustomObject. Hashtable-to-Object conversion is not supported in constrained
 language mode, restricted language mode or a Data section."
At line:2 char:147
+ ... et-Item $p; [pscustomobject]@{Path=$p;Length=$f.Length;Modified=$f.La ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : InvalidCastConstructorException
 
Cannot convert value "System.Collections.Specialized.OrderedDictionary" to type "System.Management.Automation.LanguageP
rimitives+InternalPSCustomObject". Error: "Cannot convert hashtable to an object of the following type: System.Manageme
nt.Automation.LanguagePrimitives+InternalPSCustomObject. Hashtable-to-Object conversion is not supported in constrained
 language mode, restricted language mode or a Data section."
At line:2 char:147
+ ... et-Item $p; [pscustomobject]@{Path=$p;Length=$f.Length;Modified=$f.La ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [], RuntimeException
    + FullyQualifiedErrorId : InvalidCastConstructorException
 
236:     e = np.empty(len(comps))
237:     for flag in (True, False):
238:         e[co == flag] = rng.choice(pool[flag], (co == flag).sum()) * rng.choice([-1, 1], (co == flag).sum())
239:     return e
240: 
241: 
242: def power(new, old):
243:     rng = np.random.default_rng(7)
244:     run = lambda truth: np.mean([signflip(truth + noise(rng), P["Kp"][new], P["Kp"][old], rng)[0]  # noqa: E731
245:                                  for _ in range(N_SIM)])
246:     pw, fp = run(P["Kp"][new]), run(P["Kp"][old])
247:     fp_mid = run(0.5 * (P["Kp"][new] + P["Kp"][old]))  # equal expected error, the boundary case
248:     return {"power": round(float(pw), 3), "false_pass": round(float(max(fp, fp_mid)), 3), "n_sims": N_SIM,
249:             "power_se": round(float(np.sqrt(pw * (1 - pw) / N_SIM)), 3)}
250: 
251: 
252: regs = {}
253: for h, (new, old) in HYP.items():
254:     tag = f"W1 {h}:"
255:     found = [e for e in ledger.entries() if e["claim"].startswith(tag) and "prereg" in e["notes"]]
256:     if found:
257:         assert found[-1]["evidence"].get(SCRIPT) == ledger.file_hash(SCRIPT), f"{h}: script changed since registration"
258:         regs[h] = found[-1]
259:         continue
260:     if any(e["claim"].startswith(f"Design note, {tag}") for e in ledger.entries()):
261:         continue
262:     pw = power(new, old)
263:     d = P["Kp"][new] - P["Kp"][old]
264:     print(f"{h}: rms(new - old) {np.sqrt(np.mean(d**2)):.2f} GPa, hm residual rms {np.sqrt(np.mean(res_hm**2)):.2f}, "
265:           f"{pw}", flush=True)
266:     claim = (f"{tag} on {len(comps)} fresh off-equiatomic fcc alloys (3-5 of {''.join(ELS)}), clamped mixing K' "
267:              f"RMSE({new}) <= 0.9 RMSE({old}) and paired sign-flip p < {ALPHA:.4f}; MACE medium-omat-0, per-target "
268:              f"SQS seeds 100-{99 + len(comps)}, targets computed after registration")
269:     try:
270:         regs[h] = ledger.register(claim, SCRIPT, pw, notes="literature gap Wu 2021 / Marker 2017 (literature.jsonl "
271:                                   "line 65); design reviewed by Astra (.orchestra/audits/w1_design_astra.md)")
272:         print("registered", h, regs[h]["id"], flush=True)
273:     except ValueError as err:
274:         ledger.record(f"Design note, {tag} not registered: {err}", "L0", [SCRIPT, str(BIN)],
275:                       notes=f"design; effect below detectability at n {len(comps)}")
276:         print(h, "not registered:", err, flush=True)
22:7/8, dlnV = 0, are computed as a reported diagnostic only); targets keep every pairwise |x_a - x_b| <= 0.5 (the fitted
51:DIAG = ROOT / "data" / "binary_k_asym_diag.csv"
57:LNV_MAX = 0.35  # targets may not need binaries beyond this, so splines never extrapolate
94:    for name in CH[::-1]:
157:            r = {"pair": f"{a}-{b}", "xA": xa, "xA_actual": x[a], "seed": seed, "dlnV": d, "V": v,
162:# degree diagnostic (reported only): x = 1/8, 7/8 at the binary's own Vegard volume
163:done = set(map(tuple, pd.read_csv(DIAG)[["pair", "xA", "seed"]].astype(str).values)) if DIAG.exists() else set()
172:            r = {"pair": f"{a}-{b}", "xA": xa, "xA_actual": x[a], "seed": seed, "V": v, **curvatures(alloy, x, v)}
173:            pd.DataFrame([r]).to_csv(DIAG, mode="a", header=not DIAG.exists(), index=False, float_format="%.10g")
174:print("diagnostic binaries done", flush=True)
184:        SPL[(tuple(pair.split("-")), xa, ch)] = CubicSpline(lv, s[ch].values, extrapolate=False)
257:        assert found[-1]["evidence"].get(SCRIPT) == ledger.file_hash(SCRIPT), f"{h}: script changed since registration"
312:                  "L0", [str(BIN), str(DIAG), str(TGT), str(COMPS), SCRIPT],
data/w1_compositions.csv: exists=False
data/w1_shear_clamped.csv: exists=False
data/binary_kgrid_asym.csv: exists=False
data/binary_k_asym_diag.csv: exists=False
W1 entries: 0
134: 
135: - when auditing, the user required errors over new formulas and `file:line`, evidence, and numerical size -> lead with concrete reproducible defects quantified in meV/GPa; keep the investigation read-only and use concise structured proposals when requested. [Task 2]
136: - when proposing alloy rules, the user said �?oDo not edit files. Put your candidates in your answer�?? and prohibited `data/sealed/` access -> use only the `ctx` contract, at most the requested fitted coefficient count, a physical mechanism, numerical prediction, test, falsifier, and cost; do not present cross-source or synthetic estimates as sealed validation. [Task 1]
137: 

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '@{pure=@(Import-Csv data/scan_fcc_omat_pure.csv | Select-Object el,vol_per_atom); binary=@(Import-Csv data/binary_kgrid.csv | Select-Object pair,dlnV,V,Kp); hm=@(Import-Csv data/hm_shear_clamped.csv | Select-Object comp,Kp)} | ConvertTo-Json -Compress -Depth 4' in C:\Users\can02\Projects\AI driven Science
 succeeded in 456ms:
{"hm":[{"comp":"Cu:0.1111;Ir:0.2685;Ni:0.6204","Kp":"-55.224767834782185"},{"comp":"Au:0.2037;Ir:0.3611;Pd:0.2407;Rh:0.1944","Kp":"-16.950609473613955"},{"comp":"Au:0.4074;Cu:0.2130;Pt:0.3796","Kp":"6.306101604588543"},{"comp":"Cu:0.3611;Ni:0.3426;Pd:0.2963","Kp":"3.076496516451004"},{"comp":"Ag:0.1296;Au:0.1667;Co:0.2685;Ir:0.1019;Ni:0.3333","Kp":"-8.941871658244551"},{"comp":"Ag:0.1019;Co:0.1204;Cu:0.5278;Pt:0.1204;Rh:0.1296","Kp":"-7.624265708124541"},{"comp":"Au:0.1204;Co:0.4074;Cu:0.3426;Pt:0.1296","Kp":"6.345689905685805"},{"comp":"Cu:0.4259;Ir:0.4074;Rh:0.1667","Kp":"-66.71825518439655"},{"comp":"Au:0.5926;Ni:0.2870;Rh:0.1204","Kp":"-2.849229106073083"},{"comp":"Ag:0.3056;Au:0.1111;Co:0.1759;Ir:0.4074","Kp":"-23.099352703324385"},{"comp":"Ag:0.3148;Au:0.1204;Co:0.3148;Ir:0.1296;Ni:0.1204","Kp":"-9.930051947608533"},{"comp":"Ag:0.2963;Au:0.1852;Pt:0.5185","Kp":"8.094723680365957"},{"comp":"Au:0.2037;Ni:0.6019;Pd:0.1944","Kp":"5.393755400202467"},{"comp":"Ag:0.1759;Au:0.2778;Rh:0.5463","Kp":"-9.883967873827405"},{"comp":"Ag:0.1111;Ni:0.4537;Pt:0.4352","Kp":"5.81004789185321"},{"comp":"Au:0.5833;Ir:0.2407;Rh:0.1759","Kp":"-12.691758508248007"},{"comp":"Au:0.2407;Co:0.1944;Cu:0.1296;Pt:0.1852;Rh:0.2500","Kp":"-1.1084622699428885"},{"comp":"Au:0.3889;Ir:0.4722;Pt:0.1389","Kp":"-18.552319376616634"},{"comp":"Ag:0.2778;Au:0.2685;Co:0.1111;Ni:0.1389;Pt:0.2037","Kp":"4.719440855002749"},{"comp":"Au:0.2037;Cu:0.3704;Pd:0.3148;Rh:0.1111","Kp":"-0.6747471580819249"},{"comp":"Ag:0.2315;Au:0.1111;Co:0.3611;Rh:0.2963","Kp":"-8.133301288611072"},{"comp":"Ag:0.1944;Au:0.2500;Pd:0.1759;Pt:0.3796","Kp":"7.588615980526209"},{"comp":"Co:0.2315;Ir:0.6111;Rh:0.1574","Kp":"-18.362858592009825"},{"comp":"Co:0.3241;Cu:0.3519;Pt:0.2037;Rh:0.1204","Kp":"-6.94213050458972"},{"comp":"Ag:0.2870;Co:0.3704;Pd:0.3426","Kp":"6.383593812427618"},{"comp":"Au:0.4537;Ni:0.2593;Pt:0.2870","Kp":"3.7369106903739904"},{"comp":"Cu:0.1759;Ir:0.2130;Pt:0.6111","Kp":"-1.826143784890575"},{"comp":"Ag:0.1111;Co:0.1111;Ir:0.6667;Rh:0.1111","Kp":"-18.06691590975176"},{"comp":"Cu:0.1204;Pd:0.2685;Pt:0.1389;Rh:0.4722","Kp":"-6.455602510789042"},{"comp":"Au:0.1759;Co:0.5833;Cu:0.1204;Pd:0.1204","Kp":"9.52296580567938"},{"comp":"Ag:0.2870;Co:0.1944;Ni:0.3426;Pt:0.1759","Kp":"4.425343635414349"},{"comp":"Ag:0.2407;Cu:0.3056;Ni:0.1204;Rh:0.3333","Kp":"-18.31605031725299"},{"comp":"Ag:0.6574;Ni:0.1019;Pd:0.2407","Kp":"3.526043198716264"},{"comp":"Au:0.3981;Ir:0.2778;Pt:0.3241","Kp":"-9.591039976554729"},{"comp":"Cu:0.7593;Ni:0.1389;Pd:0.1019","Kp":"0.47470426321767284"},{"comp":"Au:0.1574;Co:0.4352;Ir:0.2685;Pd:0.1389","Kp":"-14.370143888282472"},{"comp":"Au:0.4537;Ni:0.1667;Pd:0.3796","Kp":"4.47295282520855"},{"comp":"Ag:0.1204;Cu:0.1019;Ir:0.7778","Kp":"-26.080064028817976"},{"comp":"Au:0.2963;Cu:0.1204;Rh:0.5833","Kp":"-13.247171883325294"},{"comp":"Co:0.4815;Ir:0.2500;Pt:0.2685","Kp":"-6.878134752155616"},{"comp":"Au:0.2037;Co:0.2407;Pt:0.1019;Rh:0.4537","Kp":"-3.587714457953573"},{"comp":"Ag:0.2222;Ir:0.3611;Ni:0.1759;Pd:0.2407","Kp":"-21.39973790267062"},{"comp":"Ag:0.2500;Cu:0.3056;Ni:0.1296;Rh:0.3148","Kp":"-17.289050168034684"},{"comp":"Au:0.2037;Co:0.2315;Ni:0.2315;Rh:0.3333","Kp":"-8.881783265385744"},{"comp":"Ag:0.3148;Co:0.2685;Ni:0.2130;Rh:0.2037","Kp":"-9.786082086410156"},{"comp":"Ag:0.2315;Co:0.1389;Pd:0.1296;Pt:0.5000","Kp":"10.972941440433937"},{"comp":"Cu:0.3889;Ni:0.3148;Pd:0.1111;Pt:0.1852","Kp":"3.012538399470321"},{"comp":"Au:0.1574;Co:0.2130;Cu:0.3333;Ni:0.2963","Kp":"1.7745711110523228"},{"comp":"Au:0.3611;Cu:0.2778;Pd:0.3611","Kp":"5.4471274742874565"},{"comp":"Cu:0.4074;Ni:0.4907;Pd:0.1019","Kp":"-2.688693648185914"},{"comp":"Au:0.4167;Ir:0.3056;Pd:0.2778","Kp":"-11.903833066597429"},{"comp":"Co:0.4815;Cu:0.3611;Pd:0.1574","Kp":"3.3269316385972547"},{"comp":"Ni:0.2870;Pt:0.4537;Rh:0.2593","Kp":"1.6804231297388492"},{"comp":"Ag:0.1389;Co:0.2407;Ni:0.1481;Rh:0.4722","Kp":"-16.186336984051966"},{"comp":"Ir:0.1111;Pt:0.1111;Rh:0.7778","Kp":"1.826505596258236"},{"comp":"Au:0.2222;Ir:0.3519;Pd:0.3148;Rh:0.1111","Kp":"-16.19328065026759"},{"comp":"Co:0.1852;Cu:0.2315;Pd:0.5833","Kp":"6.544704482639729"},{"comp":"Cu:0.5370;Ni:0.2870;Pd:0.1759","Kp":"-0.2592138192415616"},{"comp":"Ag:0.4537;Au:0.3981;Pt:0.1481","Kp":"4.080003988957273"},{"comp":"Co:0.2407;Pd:0.3796;Pt:0.3796","Kp":"14.667435456472155"},{"comp":"Ag:0.1944;Co:0.4815;Ni:0.3241","Kp":"3.0462083192676803"},{"comp":"Ni:0.5370;Pd:0.2963;Rh:0.1667","Kp":"-8.680275996547959"},{"comp":"Ag:0.4815;Ir:0.3704;Ni:0.1481","Kp":"-23.490377338103514"},{"comp":"Cu:0.1019;Ni:0.6296;Pt:0.2685","Kp":"-2.9965278081402538"},{"comp":"Au:0.3333;Cu:0.3704;Ni:0.2963","Kp":"2.4674148472660162"},{"comp":"Au:0.2222;Pd:0.4537;Rh:0.3241","Kp":"-5.195379951353661"},{"comp":"Ag:0.1111;Au:0.1296;Ni:0.3796;Pt:0.3796","Kp":"4.678820445495399"},{"comp":"Au:0.2870;Pt:0.3148;Rh:0.3981","Kp":"-3.2359944221008163"},{"comp":"Au:0.2500;Co:0.1111;Cu:0.6389","Kp":"0.7120158478585924"},{"comp":"Ag:0.2593;Ni:0.1204;Pd:0.1759;Pt:0.4444","Kp":"7.514155738784122"},{"comp":"Co:0.1111;Pt:0.7778;Rh:0.1111","Kp":"10.193960382253579"},{"comp":"Au:0.2685;Co:0.2870;Ni:0.3333;Pt:0.1111","Kp":"12.620431225866739"},{"comp":"Ag:0.2500;Co:0.1667;Ir:0.2870;Rh:0.2963","Kp":"-21.15172769264694"},{"comp":"Ag:0.1667;Au:0.2407;Rh:0.5926","Kp":"-10.280602429803825"},{"comp":"Ag:0.1944;Cu:0.5833;Pt:0.2222","Kp":"1.6891714790996668"},{"comp":"Cu:0.3241;Pt:0.3519;Rh:0.3241","Kp":"-4.28007748897066"},{"comp":"Ag:0.4444;Au:0.3056;Cu:0.1019;Pd:0.1481","Kp":"3.9349100936126393"},{"comp":"Co:0.5556;Cu:0.1574;Ni:0.1574;Rh:0.1296","Kp":"-7.978993807893352"},{"comp":"Au:0.4352;Co:0.1667;Pt:0.3981","Kp":"7.38666770432032"},{"comp":"Ag:0.1759;Co:0.2500;Ir:0.3148;Ni:0.1111;Pd:0.1481","Kp":"-20.172766489138848"},{"comp":"Co:0.1389;Ni:0.2870;Pd:0.5741","Kp":"6.438861887201654"},{"comp":"Co:0.3519;Cu:0.2407;Ir:0.4074","Kp":"-68.4705416585423"},{"comp":"Ag:0.3333;Au:0.1667;Co:0.1944;Cu:0.3056","Kp":"0.6945048060258269"},{"comp":"Cu:0.3889;Pt:0.2778;Rh:0.3333","Kp":"-9.392649074663327"},{"comp":"Ag:0.1019;Cu:0.4630;Rh:0.4352","Kp":"-26.908136511732273"},{"comp":"Ag:0.3704;Cu:0.4074;Pd:0.2222","Kp":"2.7830293745589336"},{"comp":"Co:0.1019;Pd:0.5278;Pt:0.1481;Rh:0.2222","Kp":"2.340867716058475"},{"comp":"Ag:0.4259;Cu:0.3519;Pt:0.2222","Kp":"3.566908035328897"},{"comp":"Ag:0.3796;Ni:0.4259;Rh:0.1944","Kp":"-10.823611985144817"},{"comp":"Co:0.7500;Pt:0.1389;Rh:0.1111","Kp":"5.7751530270011875"},{"comp":"Co:0.2500;Cu:0.1296;Ni:0.3056;Pd:0.3148","Kp":"5.730620155640041"},{"comp":"Ag:0.2778;Au:0.6111;Ni:0.1111","Kp":"1.7659057920313026"},{"comp":"Ag:0.1019;Au:0.1019;Ni:0.4352;Pd:0.1574;Rh:0.2037","Kp":"-8.704307888424399"},{"comp":"Ag:0.1759;Ni:0.1667;Pt:0.5556;Rh:0.1019","Kp":"5.555867884582994"}],"pure":[{"el":"Ni","vol_per_atom":"10.92074197468201"},{"el":"Cu","vol_per_atom":"11.991099263282468"},{"el":"Pd","vol_per_atom":"15.351033412517511"},{"el":"Pt","vol_per_atom":"15.527451675555266"},{"el":"Ag","vol_per_atom":"17.840925109818457"},{"el":"Au","vol_per_atom":"17.920056075815886"},{"el":"Al","vol_per_atom":"16.410446749313255"},{"el":"Rh","vol_per_atom":"13.890889916682202"},{"el":"Ir","vol_per_atom":"14.310425195523056"},{"el":"Co","vol_per_atom":"10.874016237580149"}],"binary":[{"pair":"Ag-Au","dlnV":"-0.4","V":"11.985651277317022","Kp":"1.9362738616052462"},{"pair":"Ag-Au","dlnV":"-0.3","V":"13.246193225887012","Kp":"0.09415509585070463"},{"pair":"Ag-Au","dlnV":"-0.2","V":"14.639307528460971","Kp":"2.6990438579393303"},{"pair":"Ag-Au","dlnV":"-0.15","V":"15.38988087563095","Kp":"2.1356376618991746"},{"pair":"Ag-Au","dlnV":"-0.1","V":"16.178936941220954","Kp":"1.9898373827310942"},{"pair":"Ag-Au","dlnV":"-0.05","V":"17.00844877639591","Kp":"1.946720865512062"},{"pair":"Ag-Au","dlnV":"0.0","V":"17.88049059281717","Kp":"1.7798757634797238"},{"pair":"Ag-Au","dlnV":"0.05","V":"18.797242949252094","Kp":"1.7808857592210035"},{"pair":"Ag-Au","dlnV":"0.1","V":"19.760998204106734","Kp":"1.5734154289391575"},{"pair":"Ag-Au","dlnV":"0.15","V":"20.77416624751593","Kp":"1.3973225282539112"},{"pair":"Ag-Au","dlnV":"0.2","V":"21.839280527323865","Kp":"1.15149137106347"},{"pair":"Ag-Au","dlnV":"0.3","V":"24.13613771049413","Kp":"0.8575641169194845"},{"pair":"Ag-Au","dlnV":"0.4","V":"26.674557472307054","Kp":"0.7134472384184474"},{"pair":"Ag-Au","dlnV":"-0.4","V":"11.985651277317022","Kp":"2.254808545871703"},{"pair":"Ag-Au","dlnV":"-0.3","V":"13.246193225887012","Kp":"0.4482872038349287"},{"pair":"Ag-Au","dlnV":"-0.2","V":"14.639307528460971","Kp":"2.8583455691456847"},{"pair":"Ag-Au","dlnV":"-0.15","V":"15.38988087563095","Kp":"2.2767500291228955"},{"pair":"Ag-Au","dlnV":"-0.1","V":"16.178936941220954","Kp":"2.123048028973297"},{"pair":"Ag-Au","dlnV":"-0.05","V":"17.00844877639591","Kp":"2.0792319986674554"},{"pair":"Ag-Au","dlnV":"0.0","V":"17.88049059281717","Kp":"1.8842681922670375"},{"pair":"Ag-Au","dlnV":"0.05","V":"18.797242949252094","Kp":"1.8797155515969928"},{"pair":"Ag-Au","dlnV":"0.1","V":"19.760998204106734","Kp":"1.6579547611232113"},{"pair":"Ag-Au","dlnV":"0.15","V":"20.77416624751593","Kp":"1.462407068358507"},{"pair":"Ag-Au","dlnV":"0.2","V":"21.839280527323865","Kp":"1.195528043137594"},{"pair":"Ag-Au","dlnV":"0.3","V":"24.13613771049413","Kp":"0.8502807958698667"},{"pair":"Ag-Au","dlnV":"0.4","V":"26.674557472307054","Kp":"0.6547912724291621"},{"pair":"Ag-Au","dlnV":"-0.4","V":"11.985651277317022","Kp":"1.7866460866998817"},{"pair":"Ag-Au","dlnV":"-0.3","V":"13.246193225887012","Kp":"0.24997877366951796"},{"pair":"Ag-Au","dlnV":"-0.2","V":"14.639307528460971","Kp":"2.570481968250618"},{"pair":"Ag-Au","dlnV":"-0.15","V":"15.38988087563095","Kp":"2.0085070659370072"},{"pair":"Ag-Au","dlnV":"-0.1","V":"16.178936941220954","Kp":"1.8517790175740367"},{"pair":"Ag-Au","dlnV":"-0.05","V":"17.00844877639591","Kp":"1.7930632706069423"},{"pair":"Ag-Au","dlnV":"0.0","V":"17.88049059281717","Kp":"1.6436061615487179"},{"pair":"Ag-Au","dlnV":"0.05","V":"18.797242949252094","Kp":"1.6442031984365513"},{"pair":"Ag-Au","dlnV":"0.1","V":"19.760998204106734","Kp":"1.4372416422893122"},{"pair":"Ag-Au","dlnV":"0.15","V":"20.77416624751593","Kp":"1.2631924605535443"},{"pair":"Ag-Au","dlnV":"0.2","V":"21.839280527323865","Kp":"1.017062411331121"},{"pair":"Ag-Au","dlnV":"0.3","V":"24.13613771049413","Kp":"0.7153120668527495"},{"pair":"Ag-Au","dlnV":"0.4","V":"26.674557472307054","Kp":"0.5845910707241538"},{"pair":"Ag-Co","dlnV":"-0.4","V":"9.624100402949459","Kp":"0.695990676526331"},{"pair":"Ag-Co","dlnV":"-0.3","V":"10.636275877979863","Kp":"-8.749758128700783"},{"pair":"Ag-Co","dlnV":"-0.2","V":"11.75490277697287","Kp":"-2.4291001114429602"},{"pair":"Ag-Co","dlnV":"-0.15","V":"12.357589530141839","Kp":"0.55266699231023"},{"pair":"Ag-Co","dlnV":"-0.1","V":"12.991176693917087","Kp":"4.501391514338048"},{"pair":"Ag-Co","dlnV":"-0.05","V":"13.657248566228867","Kp":"0.9232744392182411"},{"pair":"Ag-Co","dlnV":"0.0","V":"14.357470673699304","Kp":"-0.002739685202876314"},{"pair":"Ag-Co","dlnV":"0.05","V":"15.09359393632648","Kp":"-0.4348806738875199"},{"pair":"Ag-Co","dlnV":"0.1","V":"15.867459045696448","Kp":"-0.5658879790730131"},{"pair":"Ag-Co","dlnV":"0.15","V":"16.681001067670962","Kp":"-0.4122075001993553"},{"pair":"Ag-Co","dlnV":"0.2","V":"17.53625428106008","Kp":"0.06411785923362738"},{"pair":"Ag-Co","dlnV":"0.3","V":"19.380558243407176","Kp":"0.43129565248635576"},{"pair":"Ag-Co","dlnV":"0.4","V":"21.41882934668487","Kp":"0.453160576432347"},{"pair":"Ag-Co","dlnV":"-0.4","V":"9.624100402949459","Kp":"-0.9721603196609429"},{"pair":"Ag-Co","dlnV":"-0.3","V":"10.636275877979863","Kp":"-9.194404946867175"},{"pair":"Ag-Co","dlnV":"-0.2","V":"11.75490277697287","Kp":"-2.0666227962679966"},{"pair":"Ag-Co","dlnV":"-0.15","V":"12.357589530141839","Kp":"0.9667515983584143"},{"pair":"Ag-Co","dlnV":"-0.1","V":"12.991176693917087","Kp":"4.801130098849259"},{"pair":"Ag-Co","dlnV":"-0.05","V":"13.657248566228867","Kp":"1.2655852757261943"},{"pair":"Ag-Co","dlnV":"0.0","V":"14.357470673699304","Kp":"0.32719767107938547"},{"pair":"Ag-Co","dlnV":"0.05","V":"15.09359393632648","Kp":"-0.11505376491551365"},{"pair":"Ag-Co","dlnV":"0.1","V":"15.867459045696448","Kp":"-0.23998752320960237"},{"pair":"Ag-Co","dlnV":"0.15","V":"16.681001067670962","Kp":"-0.07634992843063443"},{"pair":"Ag-Co","dlnV":"0.2","V":"17.53625428106008","Kp":"0.4092764606165694"},{"pair":"Ag-Co","dlnV":"0.3","V":"19.380558243407176","Kp":"0.7892889823223943"},{"pair":"Ag-Co","dlnV":"0.4","V":"21.41882934668487","Kp":"0.7755958979005785"},{"pair":"Ag-Co","dlnV":"-0.4","V":"9.624100402949459","Kp":"0.8455636951130344"},{"pair":"Ag-Co","dlnV":"-0.3","V":"10.636275877979863","Kp":"-8.55584251123511"},{"pair":"Ag-Co","dlnV":"-0.2","V":"11.75490277697287","Kp":"-2.31247144245902"},{"pair":"Ag-Co","dlnV":"-0.15","V":"12.357589530141839","Kp":"0.5205096925773093"},{"pair":"Ag-Co","dlnV":"-0.1","V":"12.991176693917087","Kp":"4.354091574645194"},{"pair":"Ag-Co","dlnV":"-0.05","V":"13.657248566228867","Kp":"0.7942919865260074"},{"pair":"Ag-Co","dlnV":"0.0","V":"14.357470673699304","Kp":"-0.17412081412144348"},{"pair":"Ag-Co","dlnV":"0.05","V":"15.09359393632648","Kp":"-0.6168873584132318"},{"pair":"Ag-Co","dlnV":"0.1","V":"15.867459045696448","Kp":"-0.7439946749495603"},{"pair":"Ag-Co","dlnV":"0.15","V":"16.681001067670962","Kp":"-0.5265353588768928"},{"pair":"Ag-Co","dlnV":"0.2","V":"17.53625428106008","Kp":"-0.050157827968965486"},{"pair":"Ag-Co","dlnV":"0.3","V":"19.380558243407176","Kp":"0.42828522666798463"},{"pair":"Ag-Co","dlnV":"0.4","V":"21.41882934668487","Kp":"0.5145229499922556"},{"pair":"Ag-Cu","dlnV":"-0.4","V":"9.998501975556664","Kp":"-1.8785985624049022"},{"pair":"Ag-Cu","dlnV":"-0.3","V":"11.050053607707135","Kp":"-1.716668595725932"},{"pair":"Ag-Cu","dlnV":"-0.2","V":"12.212197890414814","Kp":"-0.9934222981686766"},{"pair":"Ag-Cu","dlnV":"-0.15","V":"12.83833066541735","Kp":"-1.25452857776691"},{"pair":"Ag-Cu","dlnV":"-0.1","V":"13.496565954271228","Kp":"-1.3448196194779223"},{"pair":"Ag-Cu","dlnV":"-0.05","V":"14.188549688058034","Kp":"-1.1399896224421098"},{"pair":"Ag-Cu","dlnV":"0.0","V":"14.916012186550462","Kp":"-0.9247395764669046"},{"pair":"Ag-Cu","dlnV":"0.05","V":"15.680772484913042","Kp":"-0.7677165455991796"},{"pair":"Ag-Cu","dlnV":"0.1","V":"16.484742882237523","Kp":"-0.7337263213200531"},{"pair":"Ag-Cu","dlnV":"0.15","V":"17.329933723286697","Kp":"-0.7180736994348027"},{"pair":"Ag-Cu","dlnV":"0.2","V":"18.21845842540344","Kp":"-0.621397744797998"},{"pair":"Ag-Cu","dlnV":"0.3","V":"20.134510423926137","Kp":"-0.397169847247745"},{"pair":"Ag-Cu","dlnV":"0.4","V":"22.252075370214147","Kp":"-0.22353881045545396"},{"pair":"Ag-Cu","dlnV":"-0.4","V":"9.998501975556664","Kp":"-3.540700568701248"},{"pair":"Ag-Cu","dlnV":"-0.3","V":"11.050053607707135","Kp":"-2.969717652402929"},{"pair":"Ag-Cu","dlnV":"-0.2","V":"12.212197890414814","Kp":"-2.0350967249785397"},{"pair":"Ag-Cu","dlnV":"-0.15","V":"12.83833066541735","Kp":"-2.129663346201434"},{"pair":"Ag-Cu","dlnV":"-0.1","V":"13.496565954271228","Kp":"-2.068332839787424"},{"pair":"Ag-Cu","dlnV":"-0.05","V":"14.188549688058034","Kp":"-1.7421883252494015"},{"pair":"Ag-Cu","dlnV":"0.0","V":"14.916012186550462","Kp":"-1.4228030104241767"},{"pair":"Ag-Cu","dlnV":"0.05","V":"15.680772484913042","Kp":"-1.179885483203537"},{"pair":"Ag-Cu","dlnV":"0.1","V":"16.484742882237523","Kp":"-1.0602996995688914"},{"pair":"Ag-Cu","dlnV":"0.15","V":"17.329933723286697","Kp":"-0.9808094698373722"},{"pair":"Ag-Cu","dlnV":"0.2","V":"18.21845842540344","Kp":"-0.8316479522128154"},{"pair":"Ag-Cu","dlnV":"0.3","V":"20.134510423926137","Kp":"-0.5097807816336474"},{"pair":"Ag-Cu","dlnV":"0.4","V":"22.252075370214147","Kp":"-0.2759718140498414"},{"pair":"Ag-Cu","dlnV":"-0.4","V":"9.998501975556664","Kp":"-1.8925025374487086"},{"pair":"Ag-Cu","dlnV":"-0.3","V":"11.050053607707135","Kp":"-1.7582498835982252"},{"pair":"Ag-Cu","dlnV":"-0.2","V":"12.212197890414814","Kp":"-1.0974960787386672"},{"pair":"Ag-Cu","dlnV":"-0.15","V":"12.83833066541735","Kp":"-1.2316493119292207"},{"pair":"Ag-Cu","dlnV":"-0.1","V":"13.496565954271228","Kp":"-1.318055224123552"},{"pair":"Ag-Cu","dlnV":"-0.05","V":"14.188549688058034","Kp":"-1.1291837022689013"},{"pair":"Ag-Cu","dlnV":"0.0","V":"14.916012186550462","Kp":"-0.9162193001005803"},{"pair":"Ag-Cu","dlnV":"0.05","V":"15.680772484913042","Kp":"-0.7623131450308139"},{"pair":"Ag-Cu","dlnV":"0.1","V":"16.484742882237523","Kp":"-0.7269909650919292"},{"pair":"Ag-Cu","dlnV":"0.15","V":"17.329933723286697","Kp":"-0.7143121715569248"},{"pair":"Ag-Cu","dlnV":"0.2","V":"18.21845842540344","Kp":"-0.6212628054680411"},{"pair":"Ag-Cu","dlnV":"0.3","V":"20.134510423926137","Kp":"-0.39170309545559645"},{"pair":"Ag-Cu","dlnV":"0.4","V":"22.252075370214147","Kp":"-0.21499576284753671"},{"pair":"Ag-Ir","dlnV":"-0.4","V":"10.775847308392244","Kp":"-83.00760164836812"},{"pair":"Ag-Ir","dlnV":"-0.3","V":"11.909153062858852","Kp":"-89.28934706036709"},{"pair":"Ag-Ir","dlnV":"-0.2","V":"13.161649623983127","Kp":"-67.54417123438357"},{"pair":"Ag-Ir","dlnV":"-0.15","V":"13.836461830321827","Kp":"-41.41174988266926"},{"pair":"Ag-Ir","dlnV":"-0.1","V":"14.545872398327434","Kp":"-34.98825987022931"},{"pair":"Ag-Ir","dlnV":"-0.05","V":"15.29165522393543","Kp":"-29.200955996377015"},{"pair":"Ag-Ir","dlnV":"0.0","V":"16.075675152670755","Kp":"-23.191055529509736"},{"pair":"Ag-Ir","dlnV":"0.05","V":"16.899892642732993","Kp":"-16.447465108277974"},{"pair":"Ag-Ir","dlnV":"0.1","V":"17.766368667163015","Kp":"-12.972048037499507"},{"pair":"Ag-Ir","dlnV":"0.15","V":"18.677269867349104","Kp":"-9.226436347200176"},{"pair":"Ag-Ir","dlnV":"0.2","V":"19.63487397075897","Kp":"-5.635005034174954"},{"pair":"Ag-Ir","dlnV":"0.3","V":"21.699891692563327","Kp":"-2.387675611194178"},{"pair":"Ag-Ir","dlnV":"0.4","V":"23.98208922401233","Kp":"-0.9639711207422199"},{"pair":"Ag-Ir","dlnV":"-0.4","V":"10.775847308392244","Kp":"-83.19136096581725"},{"pair":"Ag-Ir","dlnV":"-0.3","V":"11.909153062858852","Kp":"-88.19621306175718"},{"pair":"Ag-Ir","dlnV":"-0.2","V":"13.161649623983127","Kp":"-66.71258989463634"},{"pair":"Ag-Ir","dlnV":"-0.15","V":"13.836461830321827","Kp":"-39.798434867999255"},{"pair":"Ag-Ir","dlnV":"-0.1","V":"14.545872398327434","Kp":"-33.42911065468347"},{"pair":"Ag-Ir","dlnV":"-0.05","V":"15.29165522393543","Kp":"-27.811157964314514"},{"pair":"Ag-Ir","dlnV":"0.0","V":"16.075675152670755","Kp":"-21.97471940421335"},{"pair":"Ag-Ir","dlnV":"0.05","V":"16.899892642732993","Kp":"-15.22717437411702"},{"pair":"Ag-Ir","dlnV":"0.1","V":"17.766368667163015","Kp":"-11.889783571803283"},{"pair":"Ag-Ir","dlnV":"0.15","V":"18.677269867349104","Kp":"-8.084807345294504"},{"pair":"Ag-Ir","dlnV":"0.2","V":"19.63487397075897","Kp":"-4.404170921809648"},{"pair":"Ag-Ir","dlnV":"0.3","V":"21.699891692563327","Kp":"-1.2543150324655803"},{"pair":"Ag-Ir","dlnV":"0.4","V":"23.98208922401233","Kp":"0.03075387601353437"},{"pair":"Ag-Ir","dlnV":"-0.4","V":"10.775847308392244","Kp":"-80.88933954063404"},{"pair":"Ag-Ir","dlnV":"-0.3","V":"11.909153062858852","Kp":"-86.85238028245537"},{"pair":"Ag-Ir","dlnV":"-0.2","V":"13.161649623983127","Kp":"-66.01003644581056"},{"pair":"Ag-Ir","dlnV":"-0.15","V":"13.836461830321827","Kp":"-39.07312448498367"},{"pair":"Ag-Ir","dlnV":"-0.1","V":"14.545872398327434","Kp":"-32.94163376718516"},{"pair":"Ag-Ir","dlnV":"-0.05","V":"15.29165522393543","Kp":"-27.483447167118104"},{"pair":"Ag-Ir","dlnV":"0.0","V":"16.075675152670755","Kp":"-21.848214574053426"},{"pair":"Ag-Ir","dlnV":"0.05","V":"16.899892642732993","Kp":"-15.390632999521463"},{"pair":"Ag-Ir","dlnV":"0.1","V":"17.766368667163015","Kp":"-12.126371816987497"},{"pair":"Ag-Ir","dlnV":"0.15","V":"18.677269867349104","Kp":"-8.534755291926526"},{"pair":"Ag-Ir","dlnV":"0.2","V":"19.63487397075897","Kp":"-5.10015189071934"},{"pair":"Ag-Ir","dlnV":"0.3","V":"21.699891692563327","Kp":"-2.1676192302219053"},{"pair":"Ag-Ir","dlnV":"0.4","V":"23.98208922401233","Kp":"-0.8501509292077886"},{"pair":"Ag-Ni","dlnV":"-0.4","V":"9.639761002072042","Kp":"-5.52665088262394"},{"pair":"Ag-Ni","dlnV":"-0.3","V":"10.653583516689784","Kp":"-10.944370812602362"},{"pair":"Ag-Ni","dlnV":"-0.2","V":"11.774030675935634","Kp":"-7.211611906453585"},{"pair":"Ag-Ni","dlnV":"-0.15","V":"12.377698137455795","Kp":"-2.6616551483353663"},{"pair":"Ag-Ni","dlnV":"-0.1","V":"13.012316291574622","Kp":"7.688251059638802"},{"pair":"Ag-Ni","dlnV":"-0.05","V":"13.679472014235253","Kp":"-0.7182104068562775"},{"pair":"Ag-Ni","dlnV":"0.0","V":"14.380833542250233","Kp":"-2.0071503212726465"},{"pair":"Ag-Ni","dlnV":"0.05","V":"15.118154644762505","Kp":"-1.6582353903360834"},{"pair":"Ag-Ni","dlnV":"0.1","V":"15.893279008581759","Kp":"-0.7408230829486399"},{"pair":"Ag-Ni","dlnV":"0.15","V":"16.70814484836179","Kp":"-0.6133971474030392"},{"pair":"Ag-Ni","dlnV":"0.2","V":"17.56478975314672","Kp":"0.33203991321327014"},{"pair":"Ag-Ni","dlnV":"0.3","V":"19.41209481729089","Kp":"0.16634123442337448"},{"pair":"Ag-Ni","dlnV":"0.4","V":"21.453682650996893","Kp":"0.1295544333484683"},{"pair":"Ag-Ni","dlnV":"-0.4","V":"9.639761002072042","Kp":"-7.509795928133263"},{"pair":"Ag-Ni","dlnV":"-0.3","V":"10.653583516689784","Kp":"-12.396606801634944"},{"pair":"Ag-Ni","dlnV":"-0.2","V":"11.774030675935634","Kp":"-8.08050936199243"},{"pair":"Ag-Ni","dlnV":"-0.15","V":"12.377698137455795","Kp":"-3.399715777526191"},{"pair":"Ag-Ni","dlnV":"-0.1","V":"13.012316291574622","Kp":"7.270585505761568"},{"pair":"Ag-Ni","dlnV":"-0.05","V":"13.679472014235253","Kp":"-1.0840973965196494"},{"pair":"Ag-Ni","dlnV":"0.0","V":"14.380833542250233","Kp":"-2.2834549615798627"},{"pair":"Ag-Ni","dlnV":"0.05","V":"15.118154644762505","Kp":"-1.8429917380016554"},{"pair":"Ag-Ni","dlnV":"0.1","V":"15.893279008581759","Kp":"-0.832534651285223"},{"pair":"Ag-Ni","dlnV":"0.15","V":"16.70814484836179","Kp":"-0.623334950803632"},{"pair":"Ag-Ni","dlnV":"0.2","V":"17.56478975314672","Kp":"0.35817837313497075"},{"pair":"Ag-Ni","dlnV":"0.3","V":"19.41209481729089","Kp":"0.22332935370928264"},{"pair":"Ag-Ni","dlnV":"0.4","V":"21.453682650996893","Kp":"0.18178461556514325"},{"pair":"Ag-Ni","dlnV":"-0.4","V":"9.639761002072042","Kp":"-5.750902984873687"},{"pair":"Ag-Ni","dlnV":"-0.3","V":"10.653583516689784","Kp":"-10.896137350074746"},{"pair":"Ag-Ni","dlnV":"-0.2","V":"11.774030675935634","Kp":"-7.0484831956245815"},{"pair":"Ag-Ni","dlnV":"-0.15","V":"12.377698137455795","Kp":"-2.592178563271748"},{"pair":"Ag-Ni","dlnV":"-0.1","V":"13.012316291574622","Kp":"7.450963240848004"},{"pair":"Ag-Ni","dlnV":"-0.05","V":"13.679472014235253","Kp":"-0.6669801717838623"},{"pair":"Ag-Ni","dlnV":"0.0","V":"14.380833542250233","Kp":"-1.9124820379264862"},{"pair":"Ag-Ni","dlnV":"0.05","V":"15.118154644762505","Kp":"-1.5744186891477236"},{"pair":"Ag-Ni","dlnV":"0.1","V":"15.893279008581759","Kp":"-0.6793100502011661"},{"pair":"Ag-Ni","dlnV":"0.15","V":"16.70814484836179","Kp":"-0.5261531600014377"},{"pair":"Ag-Ni","dlnV":"0.2","V":"17.56478975314672","Kp":"0.3684036012388182"},{"pair":"Ag-Ni","dlnV":"0.3","V":"19.41209481729089","Kp":"0.15569800558238953"},{"pair":"Ag-Ni","dlnV":"0.4","V":"21.453682650996893","Kp":"0.08632562736220628"},{"pair":"Ag-Pd","dlnV":"-0.4","V":"11.124617582352638","Kp":"-3.553062827195927"},{"pair":"Ag-Pd","dlnV":"-0.3","V":"12.294603826729157","Kp":"2.51836811366293"},{"pair":"Ag-Pd","dlnV":"-0.2","V":"13.58763859856263","Kp":"2.3441755596083627"},{"pair":"Ag-Pd","dlnV":"-0.15","V":"14.284291726672121","Kp":"4.866976883725856"},{"pair":"Ag-Pd","dlnV":"-0.1","V":"15.01666302445357","Kp":"5.501095374350757"},{"pair":"Ag-Pd","dlnV":"-0.05","V":"15.786583801626605","Kp":"5.093010822406915"},{"pair":"Ag-Pd","dlnV":"0.0","V":"16.595979261167983","Kp":"6.288358355472664"},{"pair":"Ag-Pd","dlnV":"0.05","V":"17.446873313321824","Kp":"5.007086391212225"},{"pair":"Ag-Pd","dlnV":"0.1","V":"18.34139363642943","Kp":"3.31607938721704"},{"pair":"Ag-Pd","dlnV":"0.15","V":"19.281776997233393","Kp":"3.7491266482418584"},{"pair":"Ag-Pd","dlnV":"0.2","V":"20.27037484395955","Kp":"2.444435923665261"},{"pair":"Ag-Pd","dlnV":"0.3","V":"22.402228776036292","Kp":"1.0528554618623696"},{"pair":"Ag-Pd","dlnV":"0.4","V":"24.758291743352718","Kp":"1.0036102966982525"},{"pair":"Ag-Pd","dlnV":"-0.4","V":"11.124617582352638","Kp":"-3.553289447512142"},{"pair":"Ag-Pd","dlnV":"-0.3","V":"12.294603826729157","Kp":"2.8931371339332044"},{"pair":"Ag-Pd","dlnV":"-0.2","V":"13.58763859856263","Kp":"2.818765458787873"},{"pair":"Ag-Pd","dlnV":"-0.15","V":"14.284291726672121","Kp":"5.224697854877776"},{"pair":"Ag-Pd","dlnV":"-0.1","V":"15.01666302445357","Kp":"5.762344994984988"},{"pair":"Ag-Pd","dlnV":"-0.05","V":"15.786583801626605","Kp":"5.27141408575929"},{"pair":"Ag-Pd","dlnV":"0.0","V":"16.595979261167983","Kp":"6.407968742767025"},{"pair":"Ag-Pd","dlnV":"0.05","V":"17.446873313321824","Kp":"5.0726406542167135"},{"pair":"Ag-Pd","dlnV":"0.1","V":"18.34139363642943","Kp":"3.335976089950893"},{"pair":"Ag-Pd","dlnV":"0.15","V":"19.281776997233393","Kp":"3.7512732248080316"},{"pair":"Ag-Pd","dlnV":"0.2","V":"20.27037484395955","Kp":"2.4076558649541253"},{"pair":"Ag-Pd","dlnV":"0.3","V":"22.402228776036292","Kp":"0.9393234213921073"},{"pair":"Ag-Pd","dlnV":"0.4","V":"24.758291743352718","Kp":"0.8677842860407637"},{"pair":"Ag-Pd","dlnV":"-0.4","V":"11.124617582352638","Kp":"-3.221695901747962"},{"pair":"Ag-Pd","dlnV":"-0.3","V":"12.294603826729157","Kp":"2.463690295945853"},{"pair":"Ag-Pd","dlnV":"-0.2","V":"13.58763859856263","Kp":"2.779654144665604"},{"pair":"Ag-Pd","dlnV":"-0.15","V":"14.284291726672121","Kp":"5.067624942805699"},{"pair":"Ag-Pd","dlnV":"-0.1","V":"15.01666302445357","Kp":"5.63247382077092"},{"pair":"Ag-Pd","dlnV":"-0.05","V":"15.786583801626605","Kp":"5.1935837254255155"},{"pair":"Ag-Pd","dlnV":"0.0","V":"16.595979261167983","Kp":"6.332146792774403"},{"pair":"Ag-Pd","dlnV":"0.05","V":"17.446873313321824","Kp":"5.050518166920367"},{"pair":"Ag-Pd","dlnV":"0.1","V":"18.34139363642943","Kp":"3.3523591143108327"},{"pair":"Ag-Pd","dlnV":"0.15","V":"19.281776997233393","Kp":"3.770614530857385"},{"pair":"Ag-Pd","dlnV":"0.2","V":"20.27037484395955","Kp":"2.4509531993111326"},{"pair":"Ag-Pd","dlnV":"0.3","V":"22.402228776036292","Kp":"1.0329533972659775"},{"pair":"Ag-Pd","dlnV":"0.4","V":"24.758291743352718","Kp":"0.896698761558132"},{"pair":"Ag-Pt","dlnV":"-0.4","V":"11.183745931453137","Kp":"-7.115627615054192"},{"pair":"Ag-Pt","dlnV":"-0.3","V":"12.359950758588852","Kp":"-3.467526154737155"},{"pair":"Ag-Pt","dlnV":"-0.2","V":"13.659858127239438","Kp":"7.872540782684801"},{"pair":"Ag-Pt","dlnV":"-0.15","V":"14.360214029763949","Kp":"8.227675454441362"},{"pair":"Ag-Pt","dlnV":"-0.1","V":"15.096477947264306","Kp":"8.682711721996506"},{"pair":"Ag-Pt","dlnV":"-0.05","V":"15.870490923037018","Kp":"8.463931876528736"},{"pair":"Ag-Pt","dlnV":"0.0","V":"16.684188392686863","Kp":"8.487554607306745"},{"pair":"Ag-Pt","dlnV":"0.05","V":"17.539605023724054","Kp":"7.202396408165608"},{"pair":"Ag-Pt","dlnV":"0.1","V":"18.438879803292807","Kp":"6.208942811497761"},{"pair":"Ag-Pt","dlnV":"0.15","V":"19.38426138675335","Kp":"4.9790101716738215"},{"pair":"Ag-Pt","dlnV":"0.2","V":"20.378113720491626","Kp":"3.9494617575626996"},{"pair":"Ag-Pt","dlnV":"0.3","V":"22.521298649125683","Kp":"2.1107828688100523"},{"pair":"Ag-Pt","dlnV":"0.4","V":"24.889884304310073","Kp":"2.2605253735206547"},{"pair":"Ag-Pt","dlnV":"-0.4","V":"11.183745931453137","Kp":"-6.375608941490749"},{"pair":"Ag-Pt","dlnV":"-0.3","V":"12.359950758588852","Kp":"-2.2067742478348595"},{"pair":"Ag-Pt","dlnV":"-0.2","V":"13.659858127239438","Kp":"8.949152751109528"},{"pair":"Ag-Pt","dlnV":"-0.15","V":"14.360214029763949","Kp":"9.282162992461256"},{"pair":"Ag-Pt","dlnV":"-0.1","V":"15.096477947264306","Kp":"9.650221909714118"},{"pair":"Ag-Pt","dlnV":"-0.05","V":"15.870490923037018","Kp":"9.342613130775058"},{"pair":"Ag-Pt","dlnV":"0.0","V":"16.684188392686863","Kp":"9.249790549454161"},{"pair":"Ag-Pt","dlnV":"0.05","V":"17.539605023724054","Kp":"7.94437387723498"},{"pair":"Ag-Pt","dlnV":"0.1","V":"18.438879803292807","Kp":"6.896090909193165"},{"pair":"Ag-Pt","dlnV":"0.15","V":"19.38426138675335","Kp":"5.58555256798956"},{"pair":"Ag-Pt","dlnV":"0.2","V":"20.378113720491626","Kp":"4.478033317500866"},{"pair":"Ag-Pt","dlnV":"0.3","V":"22.521298649125683","Kp":"2.549784561386002"},{"pair":"Ag-Pt","dlnV":"0.4","V":"24.889884304310073","Kp":"2.644386556986444"},{"pair":"Ag-Pt","dlnV":"-0.4","V":"11.183745931453137","Kp":"-6.818669318214101"},{"pair":"Ag-Pt","dlnV":"-0.3","V":"12.359950758588852","Kp":"-3.413099172608392"},{"pair":"Ag-Pt","dlnV":"-0.2","V":"13.659858127239438","Kp":"8.811339570342517"},{"pair":"Ag-Pt","dlnV":"-0.15","V":"14.360214029763949","Kp":"8.914222818778207"},{"pair":"Ag-Pt","dlnV":"-0.1","V":"15.096477947264306","Kp":"9.236951996455028"},{"pair":"Ag-Pt","dlnV":"-0.05","V":"15.870490923037018","Kp":"8.92034840492265"},{"pair":"Ag-Pt","dlnV":"0.0","V":"16.684188392686863","Kp":"8.771094621808137"},{"pair":"Ag-Pt","dlnV":"0.05","V":"17.539605023724054","Kp":"7.476124009055109"},{"pair":"Ag-Pt","dlnV":"0.1","V":"18.438879803292807","Kp":"6.410647702340642"},{"pair":"Ag-Pt","dlnV":"0.15","V":"19.38426138675335","Kp":"5.112107301908095"},{"pair":"Ag-Pt","dlnV":"0.2","V":"20.378113720491626","Kp":"4.035031302875107"},{"pair":"Ag-Pt","dlnV":"0.3","V":"22.521298649125683","Kp":"2.160495526684136"},{"pair":"Ag-Pt","dlnV":"0.4","V":"24.889884304310073","Kp":"2.2674836140351164"},{"pair":"Ag-Rh","dlnV":"-0.4","V":"10.635235854679157","Kp":"-50.674350406120205"},{"pair":"Ag-Rh","dlnV":"-0.3","V":"11.753753373466807","Kp":"-55.339334237569254"},{"pair":"Ag-Rh","dlnV":"-0.2","V":"12.989906406589052","Kp":"-25.63845799203684"},{"pair":"Ag-Rh","dlnV":"-0.15","V":"13.655913149876811","Kp":"-22.179672159209005"},{"pair":"Ag-Rh","dlnV":"-0.1","V":"14.356066789086759","Kp":"-18.05700235713572"},{"pair":"Ag-Rh","dlnV":"-0.05","V":"15.092118073010665","Kp":"-13.891283611968092"},{"pair":"Ag-Rh","dlnV":"0.0","V":"15.86590751325033","Kp":"-10.367103815260949"},{"pair":"Ag-Rh","dlnV":"0.05","V":"16.67936998645527","Kp":"-6.368445993718866"},{"pair":"Ag-Rh","dlnV":"0.1","V":"17.534539572522185","Kp":"-3.9899148006140734"},{"pair":"Ag-Rh","dlnV":"0.15","V":"18.433554640854172","Kp":"-2.0368295086640718"},{"pair":"Ag-Rh","dlnV":"0.2","V":"19.378663197398115","Kp":"0.5835815195657124"},{"pair":"Ag-Rh","dlnV":"0.3","V":"21.41673499694724","Kp":"0.8525665646995836"},{"pair":"Ag-Rh","dlnV":"0.4","V":"23.669152678759033","Kp":"0.9965167471015663"},{"pair":"Ag-Rh","dlnV":"-0.4","V":"10.635235854679157","Kp":"-49.71352039884912"},{"pair":"Ag-Rh","dlnV":"-0.3","V":"11.753753373466807","Kp":"-53.97868718903312"},{"pair":"Ag-Rh","dlnV":"-0.2","V":"12.989906406589052","Kp":"-24.93985963715416"},{"pair":"Ag-Rh","dlnV":"-0.15","V":"13.655913149876811","Kp":"-21.00712076327114"},{"pair":"Ag-Rh","dlnV":"-0.1","V":"14.356066789086759","Kp":"-16.88894775363446"},{"pair":"Ag-Rh","dlnV":"-0.05","V":"15.092118073010665","Kp":"-12.846394967984361"},{"pair":"Ag-Rh","dlnV":"0.0","V":"15.86590751325033","Kp":"-9.474625556506137"},{"pair":"Ag-Rh","dlnV":"0.05","V":"16.67936998645527","Kp":"-5.518184434318221"},{"pair":"Ag-Rh","dlnV":"0.1","V":"17.534539572522185","Kp":"-3.2554805152187045"},{"pair":"Ag-Rh","dlnV":"0.15","V":"18.433554640854172","Kp":"-1.374943676146134"},{"pair":"Ag-Rh","dlnV":"0.2","V":"19.378663197398115","Kp":"1.2701287728284754"},{"pair":"Ag-Rh","dlnV":"0.3","V":"21.41673499694724","Kp":"1.3677020328569829"},{"pair":"Ag-Rh","dlnV":"0.4","V":"23.669152678759033","Kp":"1.367550200970614"},{"pair":"Ag-Rh","dlnV":"-0.4","V":"10.635235854679157","Kp":"-49.27753964951638"},{"pair":"Ag-Rh","dlnV":"-0.3","V":"11.753753373466807","Kp":"-53.97936417425305"},{"pair":"Ag-Rh","dlnV":"-0.2","V":"12.989906406589052","Kp":"-24.697047789706218"},{"pair":"Ag-Rh","dlnV":"-0.15","V":"13.655913149876811","Kp":"-21.03942805098529"},{"pair":"Ag-Rh","dlnV":"-0.1","V":"14.356066789086759","Kp":"-17.037775412736334"},{"pair":"Ag-Rh","dlnV":"-0.05","V":"15.092118073010665","Kp":"-13.081367590933365"},{"pair":"Ag-Rh","dlnV":"0.0","V":"15.86590751325033","Kp":"-9.765425305564975"},{"pair":"Ag-Rh","dlnV":"0.05","V":"16.67936998645527","Kp":"-5.9024460863159485"},{"pair":"Ag-Rh","dlnV":"0.1","V":"17.534539572522185","Kp":"-3.6453723412739567"},{"pair":"Ag-Rh","dlnV":"0.15","V":"18.433554640854172","Kp":"-1.7823144533955797"},{"pair":"Ag-Rh","dlnV":"0.2","V":"19.378663197398115","Kp":"0.8076031405838985"},{"pair":"Ag-Rh","dlnV":"0.3","V":"21.41673499694724","Kp":"0.9465448518889864"},{"pair":"Ag-Rh","dlnV":"0.4","V":"23.669152678759033","Kp":"1.0375513108780905"},{"pair":"Au-Co","dlnV":"-0.4","V":"9.65062193933458","Kp":"-1.1779677511689095"},{"pair":"Au-Co","dlnV":"-0.3","V":"10.665586708695384","Kp":"0.5496766495752997"},{"pair":"Au-Co","dlnV":"-0.2","V":"11.787296254664302","Kp":"10.189577174720732"},{"pair":"Au-Co","dlnV":"-0.15","V":"12.391643856949942","Kp":"12.444647409878172"},{"pair":"Au-Co","dlnV":"-0.1","V":"13.026977023396988","Kp":"16.72644574898928"},{"pair":"Au-Co","dlnV":"-0.05","V":"13.694884417851828","Kp":"9.360089448359432"},{"pair":"Au-Co","dlnV":"0.0","V":"14.397036156698018","Kp":"6.1068010106242285"},{"pair":"Au-Co","dlnV":"0.05","V":"15.135187985017186","Kp":"4.167443623448709"},{"pair":"Au-Co","dlnV":"0.1","V":"15.911185666866244","Kp":"3.2334394946695277"},{"pair":"Au-Co","dlnV":"0.15","V":"16.726969600648953","Kp":"2.372939719418844"},{"pair":"Au-Co","dlnV":"0.2","V":"17.58457967112265","Kp":"2.571366743426348"},{"pair":"Au-Co","dlnV":"0.3","V":"19.43396605910899","Kp":"1.8292149934186845"},{"pair":"Au-Co","dlnV":"0.4","V":"21.477854111396457","Kp":"1.7660360479500952"},{"pair":"Au-Co","dlnV":"-0.4","V":"9.65062193933458","Kp":"-6.740551615941894"},{"pair":"Au-Co","dlnV":"-0.3","V":"10.665586708695384","Kp":"-2.254669148130843"},{"pair":"Au-Co","dlnV":"-0.2","V":"11.787296254664302","Kp":"9.354171871986967"},{"pair":"Au-Co","dlnV":"-0.15","V":"12.391643856949942","Kp":"11.913025653671138"},{"pair":"Au-Co","dlnV":"-0.1","V":"13.026977023396988","Kp":"15.763835136657184"},{"pair":"Au-Co","dlnV":"-0.05","V":"13.694884417851828","Kp":"8.841119333422528"},{"pair":"Au-Co","dlnV":"0.0","V":"14.397036156698018","Kp":"5.739747345299876"},{"pair":"Au-Co","dlnV":"0.05","V":"15.135187985017186","Kp":"3.9865414255297957"},{"pair":"Au-Co","dlnV":"0.1","V":"15.911185666866244","Kp":"3.2426940232369956"},{"pair":"Au-Co","dlnV":"0.15","V":"16.726969600648953","Kp":"2.3591819361313004"},{"pair":"Au-Co","dlnV":"0.2","V":"17.58457967112265","Kp":"2.7976412408382965"},{"pair":"Au-Co","dlnV":"0.3","V":"19.43396605910899","Kp":"1.9991119492143092"},{"pair":"Au-Co","dlnV":"0.4","V":"21.477854111396457","Kp":"1.9367138227098735"},{"pair":"Au-Co","dlnV":"-0.4","V":"9.65062193933458","Kp":"-2.284459373806714"},{"pair":"Au-Co","dlnV":"-0.3","V":"10.665586708695384","Kp":"-1.2436227631003012"},{"pair":"Au-Co","dlnV":"-0.2","V":"11.787296254664302","Kp":"9.099523044340167"},{"pair":"Au-Co","dlnV":"-0.15","V":"12.391643856949942","Kp":"11.706663498562111"},{"pair":"Au-Co","dlnV":"-0.1","V":"13.026977023396988","Kp":"16.960966734393256"},{"pair":"Au-Co","dlnV":"-0.05","V":"13.694884417851828","Kp":"8.811179654057165"},{"pair":"Au-Co","dlnV":"0.0","V":"14.397036156698018","Kp":"5.468514852212455"},{"pair":"Au-Co","dlnV":"0.05","V":"15.135187985017186","Kp":"3.6004589888774223"},{"pair":"Au-Co","dlnV":"0.1","V":"15.911185666866244","Kp":"2.7738013069429903"},{"pair":"Au-Co","dlnV":"0.15","V":"16.726969600648953","Kp":"1.926489043691946"},{"pair":"Au-Co","dlnV":"0.2","V":"17.58457967112265","Kp":"2.272417895779954"},{"pair":"Au-Co","dlnV":"0.3","V":"19.43396605910899","Kp":"1.6224775072656836"},{"pair":"Au-Co","dlnV":"0.4","V":"21.477854111396457","Kp":"1.7152358582807499"},{"pair":"Au-Cu","dlnV":"-0.4","V":"10.025023511941784","Kp":"-11.224419312821116"},{"pair":"Au-Cu","dlnV":"-0.3","V":"11.079364438422655","Kp":"-5.8629979369887595"},{"pair":"Au-Cu","dlnV":"-0.2","V":"12.244591368106246","Kp":"-2.055748079171486"},{"pair":"Au-Cu","dlnV":"-0.15","V":"12.872384992225454","Kp":"-2.819267467118179"},{"pair":"Au-Cu","dlnV":"-0.1","V":"13.532366283751129","Kp":"1.3138769468383211"},{"pair":"Au-Cu","dlnV":"-0.05","V":"14.226185539680992","Kp":"1.7395660851089314"},{"pair":"Au-Cu","dlnV":"0.0","V":"14.955577669549177","Kp":"1.1104913220639159"},{"pair":"Au-Cu","dlnV":"0.05","V":"15.722366533603747","Kp":"0.8754002141839397"},{"pair":"Au-Cu","dlnV":"0.1","V":"16.52846950340732","Kp":"0.7714593649356204"},{"pair":"Au-Cu","dlnV":"0.15","V":"17.375902256264688","Kp":"0.7524909000791885"},{"pair":"Au-Cu","dlnV":"0.2","V":"18.26678381546601","Kp":"1.1118672187683973"},{"pair":"Au-Cu","dlnV":"0.3","V":"20.18791823962795","Kp":"0.8484670891174569"},{"pair":"Au-Cu","dlnV":"0.4","V":"22.311100134925734","Kp":"0.32519509165557453"},{"pair":"Au-Cu","dlnV":"-0.4","V":"10.025023511941784","Kp":"-15.599731672017032"},{"pair":"Au-Cu","dlnV":"-0.3","V":"11.079364438422655","Kp":"-8.737203965736771"},{"pair":"Au-Cu","dlnV":"-0.2","V":"12.244591368106246","Kp":"-3.964998280599793"},{"pair":"Au-Cu","dlnV":"-0.15","V":"12.872384992225454","Kp":"-4.419370341816148"},{"pair":"Au-Cu","dlnV":"-0.1","V":"13.532366283751129","Kp":"-0.026115069230334093"},{"pair":"Au-Cu","dlnV":"-0.05","V":"14.226185539680992","Kp":"0.6206905796200597"},{"pair":"Au-Cu","dlnV":"0.0","V":"14.955577669549177","Kp":"0.2106513270065992"},{"pair":"Au-Cu","dlnV":"0.05","V":"15.722366533603747","Kp":"0.17882408197811372"},{"pair":"Au-Cu","dlnV":"0.1","V":"16.52846950340732","Kp":"0.2426189351447772"},{"pair":"Au-Cu","dlnV":"0.15","V":"17.375902256264688","Kp":"0.3742992154912997"},{"pair":"Au-Cu","dlnV":"0.2","V":"18.26678381546601","Kp":"0.859971321592617"},{"pair":"Au-Cu","dlnV":"0.3","V":"20.18791823962795","Kp":"0.7213511316723519"},{"pair":"Au-Cu","dlnV":"0.4","V":"22.311100134925734","Kp":"0.25834790787959405"},{"pair":"Au-Cu","dlnV":"-0.4","V":"10.025023511941784","Kp":"-11.476952591850427"},{"pair":"Au-Cu","dlnV":"-0.3","V":"11.079364438422655","Kp":"-6.126773789005163"},{"pair":"Au-Cu","dlnV":"-0.2","V":"12.244591368106246","Kp":"-2.5618252890348825"},{"pair":"Au-Cu","dlnV":"-0.15","V":"12.872384992225454","Kp":"-2.7391259773988383"},{"pair":"Au-Cu","dlnV":"-0.1","V":"13.532366283751129","Kp":"1.2850208986352774"},{"pair":"Au-Cu","dlnV":"-0.05","V":"14.226185539680992","Kp":"1.6385720521221565"},{"pair":"Au-Cu","dlnV":"0.0","V":"14.955577669549177","Kp":"1.0163219296178432"},{"pair":"Au-Cu","dlnV":"0.05","V":"15.722366533603747","Kp":"0.8071199776784573"},{"pair":"Au-Cu","dlnV":"0.1","V":"16.52846950340732","Kp":"0.6962259862090754"},{"pair":"Au-Cu","dlnV":"0.15","V":"17.375902256264688","Kp":"0.6882961986077922"},{"pair":"Au-Cu","dlnV":"0.2","V":"18.26678381546601","Kp":"1.0808082490107505"},{"pair":"Au-Cu","dlnV":"0.3","V":"20.18791823962795","Kp":"0.8193187938771208"},{"pair":"Au-Cu","dlnV":"0.4","V":"22.311100134925734","Kp":"0.2733670146664954"},{"pair":"Au-Ir","dlnV":"-0.4","V":"10.802368844777366","Kp":"-45.324265113138615"},{"pair":"Au-Ir","dlnV":"-0.3","V":"11.938463893574374","Kp":"-61.514948769874984"},{"pair":"Au-Ir","dlnV":"-0.2","V":"13.194043101674561","Kp":"-55.42524080719944"},{"pair":"Au-Ir","dlnV":"-0.15","V":"13.870516157129934","Kp":"-36.508051145708095"},{"pair":"Au-Ir","dlnV":"-0.1","V":"14.58167272780734","Kp":"-31.978680538810362"},{"pair":"Au-Ir","dlnV":"-0.05","V":"15.329291075558393","Kp":"-27.69250435602604"},{"pair":"Au-Ir","dlnV":"0.0","V":"16.115240635669473","Kp":"-22.321266820454344"},{"pair":"Au-Ir","dlnV":"0.05","V":"16.9414866914237","Kp":"-16.06499992312018"},{"pair":"Au-Ir","dlnV":"0.1","V":"17.810095288332814","Kp":"-13.146169994551054"},{"pair":"Au-Ir","dlnV":"0.15","V":"18.723238400327098","Kp":"-9.905262310794166"},{"pair":"Au-Ir","dlnV":"0.2","V":"19.683199360821543","Kp":"-6.766877266064425"},{"pair":"Au-Ir","dlnV":"0.3","V":"21.753299508265147","Kp":"-3.429570119086198"},{"pair":"Au-Ir","dlnV":"0.4","V":"24.041113988723925","Kp":"-1.1278859091649671"},{"pair":"Au-Ir","dlnV":"-0.4","V":"10.802368844777366","Kp":"-48.170449305023645"},{"pair":"Au-Ir","dlnV":"-0.3","V":"11.938463893574374","Kp":"-63.068407179030004"},{"pair":"Au-Ir","dlnV":"-0.2","V":"13.194043101674561","Kp":"-56.25494085626303"},{"pair":"Au-Ir","dlnV":"-0.15","V":"13.870516157129934","Kp":"-36.663243814546554"},{"pair":"Au-Ir","dlnV":"-0.1","V":"14.58167272780734","Kp":"-31.875200119191582"},{"pair":"Au-Ir","dlnV":"-0.05","V":"15.329291075558393","Kp":"-27.449656561707705"},{"pair":"Au-Ir","dlnV":"0.0","V":"16.115240635669473","Kp":"-22.041569839440875"},{"pair":"Au-Ir","dlnV":"0.05","V":"16.9414866914237","Kp":"-15.68912164629337"},{"pair":"Au-Ir","dlnV":"0.1","V":"17.810095288332814","Kp":"-12.775289142647306"},{"pair":"Au-Ir","dlnV":"0.15","V":"18.723238400327098","Kp":"-9.48226102010666"},{"pair":"Au-Ir","dlnV":"0.2","V":"19.683199360821543","Kp":"-6.296517692755996"},{"pair":"Au-Ir","dlnV":"0.3","V":"21.753299508265147","Kp":"-2.9929424997102934"},{"pair":"Au-Ir","dlnV":"0.4","V":"24.041113988723925","Kp":"-0.7713337060832434"},{"pair":"Au-Ir","dlnV":"-0.4","V":"10.802368844777366","Kp":"-43.713695002434505"},{"pair":"Au-Ir","dlnV":"-0.3","V":"11.938463893574374","Kp":"-59.12333763278241"},{"pair":"Au-Ir","dlnV":"-0.2","V":"13.194043101674561","Kp":"-54.00968259784161"},{"pair":"Au-Ir","dlnV":"-0.15","V":"13.870516157129934","Kp":"-34.381529627093144"},{"pair":"Au-Ir","dlnV":"-0.1","V":"14.58167272780734","Kp":"-30.02946238827485"},{"pair":"Au-Ir","dlnV":"-0.05","V":"15.329291075558393","Kp":"-26.02758891550491"},{"pair":"Au-Ir","dlnV":"0.0","V":"16.115240635669473","Kp":"-20.99874133716815"},{"pair":"Au-Ir","dlnV":"0.05","V":"16.9414866914237","Kp":"-14.936828496730339"},{"pair":"Au-Ir","dlnV":"0.1","V":"17.810095288332814","Kp":"-12.314012534651807"},{"pair":"Au-Ir","dlnV":"0.15","V":"18.723238400327098","Kp":"-9.179644362209642"},{"pair":"Au-Ir","dlnV":"0.2","V":"19.683199360821543","Kp":"-6.140421247996524"},{"pair":"Au-Ir","dlnV":"0.3","V":"21.753299508265147","Kp":"-3.117805479495416"},{"pair":"Au-Ir","dlnV":"0.4","V":"24.041113988723925","Kp":"-0.9937454593757844"},{"pair":"Au-Ni","dlnV":"-0.4","V":"9.666282538457162","Kp":"-23.393668802153492"},{"pair":"Au-Ni","dlnV":"-0.3","V":"10.682894347405304","Kp":"-18.287086361578243"},{"pair":"Au-Ni","dlnV":"-0.2","V":"11.806424153627066","Kp":"-8.370503008835167"},{"pair":"Au-Ni","dlnV":"-0.15","V":"12.411752464263898","Kp":"-0.6677773785634216"},{"pair":"Au-Ni","dlnV":"-0.1","V":"13.048116621054525","Kp":"11.558130338008139"},{"pair":"Au-Ni","dlnV":"-0.05","V":"13.717107865858214","Kp":"2.13211002005592"},{"pair":"Au-Ni","dlnV":"0.0","V":"14.420399025248948","Kp":"0.010326079711762774"},{"pair":"Au-Ni","dlnV":"0.05","V":"15.15974869345321","Kp":"-0.13005124673815105"},{"pair":"Au-Ni","dlnV":"0.1","V":"15.937005629751555","Kp":"0.5596941196570019"},{"pair":"Au-Ni","dlnV":"0.15","V":"16.75411338133978","Kp":"0.392723226307557"},{"pair":"Au-Ni","dlnV":"0.2","V":"17.61311514320929","Kp":"1.2063186410762432"},{"pair":"Au-Ni","dlnV":"0.3","V":"19.465502632992703","Kp":"0.6846883965208767"},{"pair":"Au-Ni","dlnV":"0.4","V":"21.51270741570848","Kp":"0.7698093930166071"},{"pair":"Au-Ni","dlnV":"-0.4","V":"9.666282538457162","Kp":"-29.092062733509657"},{"pair":"Au-Ni","dlnV":"-0.3","V":"10.682894347405304","Kp":"-22.042186168196633"},{"pair":"Au-Ni","dlnV":"-0.2","V":"11.806424153627066","Kp":"-10.712946780334564"},{"pair":"Au-Ni","dlnV":"-0.15","V":"12.411752464263898","Kp":"-2.500825023846633"},{"pair":"Au-Ni","dlnV":"-0.1","V":"13.048116621054525","Kp":"10.371167212721886"},{"pair":"Au-Ni","dlnV":"-0.05","V":"13.717107865858214","Kp":"0.9786967432313736"},{"pair":"Au-Ni","dlnV":"0.0","V":"14.420399025248948","Kp":"-0.9266782670530809"},{"pair":"Au-Ni","dlnV":"0.05","V":"15.15974869345321","Kp":"-0.8128355222908968"},{"pair":"Au-Ni","dlnV":"0.1","V":"15.937005629751555","Kp":"0.09894845479758421"},{"pair":"Au-Ni","dlnV":"0.15","V":"16.75411338133978","Kp":"0.0607462457482826"},{"pair":"Au-Ni","dlnV":"0.2","V":"17.61311514320929","Kp":"1.010273201717056"},{"pair":"Au-Ni","dlnV":"0.3","V":"19.465502632992703","Kp":"0.5556714334197913"},{"pair":"Au-Ni","dlnV":"0.4","V":"21.51270741570848","Kp":"0.7156052863144156"},{"pair":"Au-Ni","dlnV":"-0.4","V":"9.666282538457162","Kp":"-24.153782912756583"},{"pair":"Au-Ni","dlnV":"-0.3","V":"10.682894347405304","Kp":"-19.139262464800453"},{"pair":"Au-Ni","dlnV":"-0.2","V":"11.806424153627066","Kp":"-9.098545061354164"},{"pair":"Au-Ni","dlnV":"-0.15","V":"12.411752464263898","Kp":"-1.2289865664725175"},{"pair":"Au-Ni","dlnV":"-0.1","V":"13.048116621054525","Kp":"11.48847683931598"},{"pair":"Au-Ni","dlnV":"-0.05","V":"13.717107865858214","Kp":"1.8556862141800325"},{"pair":"Au-Ni","dlnV":"0.0","V":"14.420399025248948","Kp":"-0.2570958894274756"},{"pair":"Au-Ni","dlnV":"0.05","V":"15.15974869345321","Kp":"-0.3591464728350277"},{"pair":"Au-Ni","dlnV":"0.1","V":"15.937005629751555","Kp":"0.37273510102386975"},{"pair":"Au-Ni","dlnV":"0.15","V":"16.75411338133978","Kp":"0.24748079434967962"},{"pair":"Au-Ni","dlnV":"0.2","V":"17.61311514320929","Kp":"1.0976949632498991"},{"pair":"Au-Ni","dlnV":"0.3","V":"19.465502632992703","Kp":"0.6113521159134522"},{"pair":"Au-Ni","dlnV":"0.4","V":"21.51270741570848","Kp":"0.6866230208169859"},{"pair":"Au-Pd","dlnV":"-0.4","V":"11.151139118737758","Kp":"-8.222782309221321"},{"pair":"Au-Pd","dlnV":"-0.3","V":"12.323914657444677","Kp":"0.1714611846124756"},{"pair":"Au-Pd","dlnV":"-0.2","V":"13.620032076254063","Kp":"-0.2178973382932842"},{"pair":"Au-Pd","dlnV":"-0.15","V":"14.318346053480225","Kp":"3.0611847732358757"},{"pair":"Au-Pd","dlnV":"-0.1","V":"15.05246335393347","Kp":"4.2783887169645105"},{"pair":"Au-Pd","dlnV":"-0.05","V":"15.824219653249566","Kp":"4.62346378993705"},{"pair":"Au-Pd","dlnV":"0.0","V":"16.635544744166697","Kp":"6.838855313504039"},{"pair":"Au-Pd","dlnV":"0.05","V":"17.48846736201253","Kp":"5.526934982679326"},{"pair":"Au-Pd","dlnV":"0.1","V":"18.385120257599226","Kp":"4.076416270693741"},{"pair":"Au-Pd","dlnV":"0.15","V":"19.327745530211384","Kp":"4.303694446836186"},{"pair":"Au-Pd","dlnV":"0.2","V":"20.31870023402212","Kp":"2.8329909206012873"},{"pair":"Au-Pd","dlnV":"0.3","V":"22.455636591738106","Kp":"1.131043658953108"},{"pair":"Au-Pd","dlnV":"0.4","V":"24.81731650806431","Kp":"1.4881559997976805"},{"pair":"Au-Pd","dlnV":"-0.4","V":"11.151139118737758","Kp":"-8.356485578024635"},{"pair":"Au-Pd","dlnV":"-0.3","V":"12.323914657444677","Kp":"0.5219428199439715"},{"pair":"Au-Pd","dlnV":"-0.2","V":"13.620032076254063","Kp":"-0.013087528808066401"},{"pair":"Au-Pd","dlnV":"-0.15","V":"14.318346053480225","Kp":"3.2509710516456574"},{"pair":"Au-Pd","dlnV":"-0.1","V":"15.05246335393347","Kp":"4.447330078159461"},{"pair":"Au-Pd","dlnV":"-0.05","V":"15.824219653249566","Kp":"4.760035445375603"},{"pair":"Au-Pd","dlnV":"0.0","V":"16.635544744166697","Kp":"6.979620550511252"},{"pair":"Au-Pd","dlnV":"0.05","V":"17.48846736201253","Kp":"5.620259136696921"},{"pair":"Au-Pd","dlnV":"0.1","V":"18.385120257599226","Kp":"4.10470235957806"},{"pair":"Au-Pd","dlnV":"0.15","V":"19.327745530211384","Kp":"4.316426842812029"},{"pair":"Au-Pd","dlnV":"0.2","V":"20.31870023402212","Kp":"2.812678766335934"},{"pair":"Au-Pd","dlnV":"0.3","V":"22.455636591738106","Kp":"1.0292019669259147"},{"pair":"Au-Pd","dlnV":"0.4","V":"24.81731650806431","Kp":"1.3805758282258012"},{"pair":"Au-Pd","dlnV":"-0.4","V":"11.151139118737758","Kp":"-7.9903106801021755"},{"pair":"Au-Pd","dlnV":"-0.3","V":"12.323914657444677","Kp":"0.17832996903275442"},{"pair":"Au-Pd","dlnV":"-0.2","V":"13.620032076254063","Kp":"0.004642306923407328"},{"pair":"Au-Pd","dlnV":"-0.15","V":"14.318346053480225","Kp":"3.0829264592275054"},{"pair":"Au-Pd","dlnV":"-0.1","V":"15.05246335393347","Kp":"4.2178104909712175"},{"pair":"Au-Pd","dlnV":"-0.05","V":"15.824219653249566","Kp":"4.528432372673083"},{"pair":"Au-Pd","dlnV":"0.0","V":"16.635544744166697","Kp":"6.684058366346062"},{"pair":"Au-Pd","dlnV":"0.05","V":"17.48846736201253","Kp":"5.398912525998326"},{"pair":"Au-Pd","dlnV":"0.1","V":"18.385120257599226","Kp":"3.9613052093934473"},{"pair":"Au-Pd","dlnV":"0.15","V":"19.327745530211384","Kp":"4.209581389398381"},{"pair":"Au-Pd","dlnV":"0.2","V":"20.31870023402212","Kp":"2.749555684380334"},{"pair":"Au-Pd","dlnV":"0.3","V":"22.455636591738106","Kp":"1.0501870505752073"},{"pair":"Au-Pd","dlnV":"0.4","V":"24.81731650806431","Kp":"1.3070327405224256"},{"pair":"Au-Pt","dlnV":"-0.4","V":"11.210267467838255","Kp":"-16.721556560624546"},{"pair":"Au-Pt","dlnV":"-0.3","V":"12.38926158930437","Kp":"-9.26049744176824"},{"pair":"Au-Pt","dlnV":"-0.2","V":"13.692251604930867","Kp":"-0.5993277712063136"},{"pair":"Au-Pt","dlnV":"-0.15","V":"14.394268356572049","Kp":"1.008599373343365"},{"pair":"Au-Pt","dlnV":"-0.1","V":"15.132278276744206","Kp":"2.581862670621954"},{"pair":"Au-Pt","dlnV":"-0.05","V":"15.908126774659975","Kp":"3.5134133017519886"},{"pair":"Au-Pt","dlnV":"0.0","V":"16.723753875685574","Kp":"4.724449526061585"},{"pair":"Au-Pt","dlnV":"0.05","V":"17.581199072414755","Kp":"4.314100301477891"},{"pair":"Au-Pt","dlnV":"0.1","V":"18.4826064244626","Kp":"3.8230220885585458"},{"pair":"Au-Pt","dlnV":"0.15","V":"19.43022991973134","Kp":"2.9356013261406724"},{"pair":"Au-Pt","dlnV":"0.2","V":"20.426439110554192","Kp":"2.2540202206730595"},{"pair":"Au-Pt","dlnV":"0.3","V":"22.57470646482749","Kp":"0.9739990629114011"},{"pair":"Au-Pt","dlnV":"0.4","V":"24.948909069021656","Kp":"1.4956185679597578"},{"pair":"Au-Pt","dlnV":"-0.4","V":"11.210267467838255","Kp":"-16.396673145265893"},{"pair":"Au-Pt","dlnV":"-0.3","V":"12.38926158930437","Kp":"-8.252601661284483"},{"pair":"Au-Pt","dlnV":"-0.2","V":"13.692251604930867","Kp":"0.002906427912766326"},{"pair":"Au-Pt","dlnV":"-0.15","V":"14.394268356572049","Kp":"1.5604530072358227"},{"pair":"Au-Pt","dlnV":"-0.1","V":"15.132278276744206","Kp":"3.0652291660064246"},{"pair":"Au-Pt","dlnV":"-0.05","V":"15.908126774659975","Kp":"3.9091644547922324"},{"pair":"Au-Pt","dlnV":"0.0","V":"16.723753875685574","Kp":"5.049715554745848"},{"pair":"Au-Pt","dlnV":"0.05","V":"17.581199072414755","Kp":"4.580823048702611"},{"pair":"Au-Pt","dlnV":"0.1","V":"18.4826064244626","Kp":"4.032759548615097"},{"pair":"Au-Pt","dlnV":"0.15","V":"19.43022991973134","Kp":"3.104653062985903"},{"pair":"Au-Pt","dlnV":"0.2","V":"20.426439110554192","Kp":"2.3758099112797826"},{"pair":"Au-Pt","dlnV":"0.3","V":"22.57470646482749","Kp":"1.0213487825597591"},{"pair":"Au-Pt","dlnV":"0.4","V":"24.948909069021656","Kp":"1.5149455118471369"},{"pair":"Au-Pt","dlnV":"-0.4","V":"11.210267467838255","Kp":"-15.701369022188144"},{"pair":"Au-Pt","dlnV":"-0.3","V":"12.38926158930437","Kp":"-8.314147216803448"},{"pair":"Au-Pt","dlnV":"-0.2","V":"13.692251604930867","Kp":"0.4055085788680644"},{"pair":"Au-Pt","dlnV":"-0.15","V":"14.394268356572049","Kp":"1.710390955479097"},{"pair":"Au-Pt","dlnV":"-0.1","V":"15.132278276744206","Kp":"3.11415292320936"},{"pair":"Au-Pt","dlnV":"-0.05","V":"15.908126774659975","Kp":"3.9126099020824308"},{"pair":"Au-Pt","dlnV":"0.0","V":"16.723753875685574","Kp":"4.945990388981478"},{"pair":"Au-Pt","dlnV":"0.05","V":"17.581199072414755","Kp":"4.51392933536713"},{"pair":"Au-Pt","dlnV":"0.1","V":"18.4826064244626","Kp":"3.9485866785224957"},{"pair":"Au-Pt","dlnV":"0.15","V":"19.43022991973134","Kp":"3.017330329222689"},{"pair":"Au-Pt","dlnV":"0.2","V":"20.426439110554192","Kp":"2.29147443881997"},{"pair":"Au-Pt","dlnV":"0.3","V":"22.57470646482749","Kp":"0.9795294191405993"},{"pair":"Au-Pt","dlnV":"0.4","V":"24.948909069021656","Kp":"1.4514402321479718"},{"pair":"Au-Rh","dlnV":"-0.4","V":"10.661757391064278","Kp":"-34.07454594383723"},{"pair":"Au-Rh","dlnV":"-0.3","V":"11.78306420418233","Kp":"-44.47369792571055"},{"pair":"Au-Rh","dlnV":"-0.2","V":"13.022299884280484","Kp":"-17.21144700908858"},{"pair":"Au-Rh","dlnV":"-0.15","V":"13.689967476684915","Kp":"-18.218535764675327"},{"pair":"Au-Rh","dlnV":"-0.1","V":"14.391867118566662","Kp":"-15.397978392185312"},{"pair":"Au-Rh","dlnV":"-0.05","V":"15.129753924633626","Kp":"-12.107016086375856"},{"pair":"Au-Rh","dlnV":"0.0","V":"15.905472996249044","Kp":"-8.882907621600033"},{"pair":"Au-Rh","dlnV":"0.05","V":"16.72096403514598","Kp":"-4.631311839913992"},{"pair":"Au-Rh","dlnV":"0.1","V":"17.578266193691977","Kp":"-2.7830149999340312"},{"pair":"Au-Rh","dlnV":"0.15","V":"18.479523173832163","Kp":"-1.257799463616109"},{"pair":"Au-Rh","dlnV":"0.2","V":"19.426988587460684","Kp":"0.9052831397101959"},{"pair":"Au-Rh","dlnV":"0.3","V":"21.47014281264905","Kp":"0.7444253660336367"},{"pair":"Au-Rh","dlnV":"0.4","V":"23.72817744347062","Kp":"1.2508125370005874"},{"pair":"Au-Rh","dlnV":"-0.4","V":"10.661757391064278","Kp":"-34.77673196671893"},{"pair":"Au-Rh","dlnV":"-0.3","V":"11.78306420418233","Kp":"-44.23712116821884"},{"pair":"Au-Rh","dlnV":"-0.2","V":"13.022299884280484","Kp":"-16.88677560434092"},{"pair":"Au-Rh","dlnV":"-0.15","V":"13.689967476684915","Kp":"-17.612492362391613"},{"pair":"Au-Rh","dlnV":"-0.1","V":"14.391867118566662","Kp":"-14.725059367363903"},{"pair":"Au-Rh","dlnV":"-0.05","V":"15.129753924633626","Kp":"-11.464320778695383"},{"pair":"Au-Rh","dlnV":"0.0","V":"15.905472996249044","Kp":"-8.327111613313212"},{"pair":"Au-Rh","dlnV":"0.05","V":"16.72096403514598","Kp":"-4.092479832545515"},{"pair":"Au-Rh","dlnV":"0.1","V":"17.578266193691977","Kp":"-2.353119152195792"},{"pair":"Au-Rh","dlnV":"0.15","V":"18.479523173832163","Kp":"-0.9048966769135225"},{"pair":"Au-Rh","dlnV":"0.2","V":"19.426988587460684","Kp":"1.2669033823858913"},{"pair":"Au-Rh","dlnV":"0.3","V":"21.47014281264905","Kp":"0.9820790985860998"},{"pair":"Au-Rh","dlnV":"0.4","V":"23.72817744347062","Kp":"1.3754004518706358"},{"pair":"Au-Rh","dlnV":"-0.4","V":"10.661757391064278","Kp":"-33.09437754245651"},{"pair":"Au-Rh","dlnV":"-0.3","V":"11.78306420418233","Kp":"-43.4141818243128"},{"pair":"Au-Rh","dlnV":"-0.2","V":"13.022299884280484","Kp":"-16.626557081376554"},{"pair":"Au-Rh","dlnV":"-0.15","V":"13.689967476684915","Kp":"-17.244665470899612"},{"pair":"Au-Rh","dlnV":"-0.1","V":"14.391867118566662","Kp":"-14.509277803229303"},{"pair":"Au-Rh","dlnV":"-0.05","V":"15.129753924633626","Kp":"-11.423171648357362"},{"pair":"Au-Rh","dlnV":"0.0","V":"15.905472996249044","Kp":"-8.41476104809165"},{"pair":"Au-Rh","dlnV":"0.05","V":"16.72096403514598","Kp":"-4.287144146591842"},{"pair":"Au-Rh","dlnV":"0.1","V":"17.578266193691977","Kp":"-2.5449364186291206"},{"pair":"Au-Rh","dlnV":"0.15","V":"18.479523173832163","Kp":"-1.0906263699851073"},{"pair":"Au-Rh","dlnV":"0.2","V":"19.426988587460684","Kp":"1.0649268815419948"},{"pair":"Au-Rh","dlnV":"0.3","V":"21.47014281264905","Kp":"0.8088106447728167"},{"pair":"Au-Rh","dlnV":"0.4","V":"23.72817744347062","Kp":"1.214985984400681"},{"pair":"Co-Cu","dlnV":"-0.4","V":"7.663472637574219","Kp":"-7.955213776606281"},{"pair":"Co-Cu","dlnV":"-0.3","V":"8.469447090515505","Kp":"-4.977666718079002"},{"pair":"Co-Cu","dlnV":"-0.2","V":"9.360186616618142","Kp":"-2.030697743896875"},{"pair":"Co-Cu","dlnV":"-0.15","V":"9.840093646736342","Kp":"-3.411932295270192"},{"pair":"Co-Cu","dlnV":"-0.1","V":"10.344606036447262","Kp":"-6.197485527112476"},{"pair":"Co-Cu","dlnV":"-0.05","V":"10.874985329513951","Kp":"-5.572658123169522"},{"pair":"Co-Cu","dlnV":"0.0","V":"11.432557750431307","Kp":"-2.3347027286819153"},{"pair":"Co-Cu","dlnV":"0.05","V":"12.018717520678132","Kp":"1.5992767877050462"},{"pair":"Co-Cu","dlnV":"0.1","V":"12.634930344997029","Kp":"-0.5663834128272781"},{"pair":"Co-Cu","dlnV":"0.15","V":"13.282737076419721","Kp":"-1.3477983617688063"},{"pair":"Co-Cu","dlnV":"0.2","V":"13.963757569202226","Kp":"0.40219768043024645"},{"pair":"Co-Cu","dlnV":"0.3","V":"15.432338772540998","Kp":"-0.5530905462489756"},{"pair":"Co-Cu","dlnV":"0.4","V":"17.055372009303547","Kp":"-0.053493540436201824"},{"pair":"Co-Cu","dlnV":"-0.4","V":"7.663472637574219","Kp":"-7.659403957575167"},{"pair":"Co-Cu","dlnV":"-0.3","V":"8.469447090515505","Kp":"-4.54622323433208"},{"pair":"Co-Cu","dlnV":"-0.2","V":"9.360186616618142","Kp":"-1.2586057026686632"},{"pair":"Co-Cu","dlnV":"-0.15","V":"9.840093646736342","Kp":"-2.4790727041391722"},{"pair":"Co-Cu","dlnV":"-0.1","V":"10.344606036447262","Kp":"-5.087222401061771"},{"pair":"Co-Cu","dlnV":"-0.05","V":"10.874985329513951","Kp":"-4.648286927481893"},{"pair":"Co-Cu","dlnV":"0.0","V":"11.432557750431307","Kp":"-1.5270643855662829"},{"pair":"Co-Cu","dlnV":"0.05","V":"12.018717520678132","Kp":"2.6725765375155532"},{"pair":"Co-Cu","dlnV":"0.1","V":"12.634930344997029","Kp":"0.20272994012706602"},{"pair":"Co-Cu","dlnV":"0.15","V":"13.282737076419721","Kp":"-0.7014491117602208"},{"pair":"Co-Cu","dlnV":"0.2","V":"13.963757569202226","Kp":"1.1294145886203464"},{"pair":"Co-Cu","dlnV":"0.3","V":"15.432338772540998","Kp":"0.021975652189896257"},{"pair":"Co-Cu","dlnV":"0.4","V":"17.055372009303547","Kp":"0.31786950252575585"},{"pair":"Co-Cu","dlnV":"-0.4","V":"7.663472637574219","Kp":"-7.7362190096255325"},{"pair":"Co-Cu","dlnV":"-0.3","V":"8.469447090515505","Kp":"-3.9710874911909317"},{"pair":"Co-Cu","dlnV":"-0.2","V":"9.360186616618142","Kp":"-0.8648181471755642"},{"pair":"Co-Cu","dlnV":"-0.15","V":"9.840093646736342","Kp":"-2.3275797194057755"},{"pair":"Co-Cu","dlnV":"-0.1","V":"10.344606036447262","Kp":"-5.207119403747388"},{"pair":"Co-Cu","dlnV":"-0.05","V":"10.874985329513951","Kp":"-5.05148195320708"},{"pair":"Co-Cu","dlnV":"0.0","V":"11.432557750431307","Kp":"-2.130359297656944"},{"pair":"Co-Cu","dlnV":"0.05","V":"12.018717520678132","Kp":"1.8019052495067585"},{"pair":"Co-Cu","dlnV":"0.1","V":"12.634930344997029","Kp":"-0.610933909019846"},{"pair":"Co-Cu","dlnV":"0.15","V":"13.282737076419721","Kp":"-1.3464465632624592"},{"pair":"Co-Cu","dlnV":"0.2","V":"13.963757569202226","Kp":"0.43903133153365614"},{"pair":"Co-Cu","dlnV":"0.3","V":"15.432338772540998","Kp":"-0.5747495933611954"},{"pair":"Co-Cu","dlnV":"0.4","V":"17.055372009303547","Kp":"-0.08745186398802661"},{"pair":"Co-Ir","dlnV":"-0.4","V":"8.440817970409801","Kp":"-29.97296732335801"},{"pair":"Co-Ir","dlnV":"-0.3","V":"9.328546545667225","Kp":"-78.08765343117311"},{"pair":"Co-Ir","dlnV":"-0.2","V":"10.309638350186457","Kp":"-52.45948427367589"},{"pair":"Co-Ir","dlnV":"-0.15","V":"10.83822481164082","Kp":"-38.772798685066306"},{"pair":"Co-Ir","dlnV":"-0.1","V":"11.39391248050347","Kp":"-37.38081453909426"},{"pair":"Co-Ir","dlnV":"-0.05","V":"11.978090865391348","Kp":"-27.872891597320834"},{"pair":"Co-Ir","dlnV":"0.0","V":"12.592220716551601","Kp":"-47.152198112215025"},{"pair":"Co-Ir","dlnV":"0.05","V":"13.237837678498085","Kp":"-40.67550066490232"},{"pair":"Co-Ir","dlnV":"0.1","V":"13.916556129922524","Kp":"-20.468871006071648"},{"pair":"Co-Ir","dlnV":"0.15","V":"14.630073220482128","Kp":"-17.421656302555466"},{"pair":"Co-Ir","dlnV":"0.2","V":"15.380173114557756","Kp":"-14.45707570245645"},{"pair":"Co-Ir","dlnV":"0.3","V":"16.997720041178187","Kp":"-6.878543802124714"},{"pair":"Co-Ir","dlnV":"0.4","V":"18.785385863101734","Kp":"-2.672559669352239"},{"pair":"Co-Ir","dlnV":"-0.4","V":"8.440817970409801","Kp":"-39.89836755447518"},{"pair":"Co-Ir","dlnV":"-0.3","V":"9.328546545667225","Kp":"-85.05977759824606"},{"pair":"Co-Ir","dlnV":"-0.2","V":"10.309638350186457","Kp":"-56.81500305288882"},{"pair":"Co-Ir","dlnV":"-0.15","V":"10.83822481164082","Kp":"-41.796591304687745"},{"pair":"Co-Ir","dlnV":"-0.1","V":"11.39391248050347","Kp":"-39.292972029700294"},{"pair":"Co-Ir","dlnV":"-0.05","V":"11.978090865391348","Kp":"-29.60683997065689"},{"pair":"Co-Ir","dlnV":"0.0","V":"12.592220716551601","Kp":"-48.72683217872358"},{"pair":"Co-Ir","dlnV":"0.05","V":"13.237837678498085","Kp":"-41.912843746728605"},{"pair":"Co-Ir","dlnV":"0.1","V":"13.916556129922524","Kp":"-21.752720983625554"},{"pair":"Co-Ir","dlnV":"0.15","V":"14.630073220482128","Kp":"-18.52165812448334"},{"pair":"Co-Ir","dlnV":"0.2","V":"15.380173114557756","Kp":"-15.32593490816341"},{"pair":"Co-Ir","dlnV":"0.3","V":"16.997720041178187","Kp":"-7.367394536813352"},{"pair":"Co-Ir","dlnV":"0.4","V":"18.785385863101734","Kp":"-2.7455220377304443"},{"pair":"Co-Ir","dlnV":"-0.4","V":"8.440817970409801","Kp":"-31.112392554598085"},{"pair":"Co-Ir","dlnV":"-0.3","V":"9.328546545667225","Kp":"-78.26597097284635"},{"pair":"Co-Ir","dlnV":"-0.2","V":"10.309638350186457","Kp":"-51.91920463496502"},{"pair":"Co-Ir","dlnV":"-0.15","V":"10.83822481164082","Kp":"-37.884072825307044"},{"pair":"Co-Ir","dlnV":"-0.1","V":"11.39391248050347","Kp":"-36.3098098820908"},{"pair":"Co-Ir","dlnV":"-0.05","V":"11.978090865391348","Kp":"-27.353358761836596"},{"pair":"Co-Ir","dlnV":"0.0","V":"12.592220716551601","Kp":"-46.017772421900915"},{"pair":"Co-Ir","dlnV":"0.05","V":"13.237837678498085","Kp":"-38.96655141199022"},{"pair":"Co-Ir","dlnV":"0.1","V":"13.916556129922524","Kp":"-19.384415525668082"},{"pair":"Co-Ir","dlnV":"0.15","V":"14.630073220482128","Kp":"-16.507042757616315"},{"pair":"Co-Ir","dlnV":"0.2","V":"15.380173114557756","Kp":"-13.577622410676017"},{"pair":"Co-Ir","dlnV":"0.3","V":"16.997720041178187","Kp":"-6.510430960267014"},{"pair":"Co-Ir","dlnV":"0.4","V":"18.785385863101734","Kp":"-2.3173797989471794"},{"pair":"Co-Ni","dlnV":"-0.4","V":"7.3047316640896","Kp":"11.970304992700042"},{"pair":"Co-Ni","dlnV":"-0.3","V":"8.072976999498156","Kp":"11.984947953495583"},{"pair":"Co-Ni","dlnV":"-0.2","V":"8.922019402138963","Kp":"10.16085794694266"},{"pair":"Co-Ni","dlnV":"-0.15","V":"9.379461118774786","Kp":"8.62000701299186"},{"pair":"Co-Ni","dlnV":"-0.1","V":"9.860356373750658","Kp":"7.461989118002209"},{"pair":"Co-Ni","dlnV":"-0.05","V":"10.365907655691172","Kp":"7.53403503144171"},{"pair":"Co-Ni","dlnV":"0.0","V":"10.89737910613108","Kp":"6.83259062928939"},{"pair":"Co-Ni","dlnV":"0.05","V":"11.456099680527599","Kp":"7.093494888905692"},{"pair":"Co-Ni","dlnV":"0.1","V":"12.043466471341267","Kp":"7.662087731217587"},{"pair":"Co-Ni","dlnV":"0.15","V":"12.660948201494817","Kp":"5.234708863086703"},{"pair":"Co-Ni","dlnV":"0.2","V":"13.310088896945507","Kp":"3.6896064086319873"},{"pair":"Co-Ni","dlnV":"0.3","V":"14.709923165905751","Kp":"2.6612085321139625"},{"pair":"Co-Ni","dlnV":"0.4","V":"16.256979290086296","Kp":"1.7762635731947352"},{"pair":"Co-Ni","dlnV":"-0.4","V":"7.3047316640896","Kp":"12.487879320809377"},{"pair":"Co-Ni","dlnV":"-0.3","V":"8.072976999498156","Kp":"12.454382459957996"},{"pair":"Co-Ni","dlnV":"-0.2","V":"8.922019402138963","Kp":"10.515242631039682"},{"pair":"Co-Ni","dlnV":"-0.15","V":"9.379461118774786","Kp":"8.93671926474313"},{"pair":"Co-Ni","dlnV":"-0.1","V":"9.860356373750658","Kp":"7.752760430670337"},{"pair":"Co-Ni","dlnV":"-0.05","V":"10.365907655691172","Kp":"7.873494711896246"},{"pair":"Co-Ni","dlnV":"0.0","V":"10.89737910613108","Kp":"7.136082106539789"},{"pair":"Co-Ni","dlnV":"0.05","V":"11.456099680527599","Kp":"7.433011222929272"},{"pair":"Co-Ni","dlnV":"0.1","V":"12.043466471341267","Kp":"8.073744314882621"},{"pair":"Co-Ni","dlnV":"0.15","V":"12.660948201494817","Kp":"5.456248459432615"},{"pair":"Co-Ni","dlnV":"0.2","V":"13.310088896945507","Kp":"3.8976836624179065"},{"pair":"Co-Ni","dlnV":"0.3","V":"14.709923165905751","Kp":"2.8018033556192226"},{"pair":"Co-Ni","dlnV":"0.4","V":"16.256979290086296","Kp":"1.858180673110641"},{"pair":"Co-Ni","dlnV":"-0.4","V":"7.3047316640896","Kp":"12.199287386069187"},{"pair":"Co-Ni","dlnV":"-0.3","V":"8.072976999498156","Kp":"11.906888406216195"},{"pair":"Co-Ni","dlnV":"-0.2","V":"8.922019402138963","Kp":"10.127399146783999"},{"pair":"Co-Ni","dlnV":"-0.15","V":"9.379461118774786","Kp":"8.480675581898696"},{"pair":"Co-Ni","dlnV":"-0.1","V":"9.860356373750658","Kp":"7.223520451025385"},{"pair":"Co-Ni","dlnV":"-0.05","V":"10.365907655691172","Kp":"7.391728919653546"},{"pair":"Co-Ni","dlnV":"0.0","V":"10.89737910613108","Kp":"6.486730055423283"},{"pair":"Co-Ni","dlnV":"0.05","V":"11.456099680527599","Kp":"6.648553444899856"},{"pair":"Co-Ni","dlnV":"0.1","V":"12.043466471341267","Kp":"7.495714707148786"},{"pair":"Co-Ni","dlnV":"0.15","V":"12.660948201494817","Kp":"4.682532345570093"},{"pair":"Co-Ni","dlnV":"0.2","V":"13.310088896945507","Kp":"3.2772484515464937"},{"pair":"Co-Ni","dlnV":"0.3","V":"14.709923165905751","Kp":"2.557287893692682"},{"pair":"Co-Ni","dlnV":"0.4","V":"16.256979290086296","Kp":"1.6972282498129148"},{"pair":"Co-Pd","dlnV":"-0.4","V":"8.789588244370195","Kp":"9.484018415893276"},{"pair":"Co-Pd","dlnV":"-0.3","V":"9.713997309537529","Kp":"11.39754102792128"},{"pair":"Co-Pd","dlnV":"-0.2","V":"10.73562732476596","Kp":"17.59148320384459"},{"pair":"Co-Pd","dlnV":"-0.15","V":"11.286054707991113","Kp":"21.144348389018337"},{"pair":"Co-Pd","dlnV":"-0.1","V":"11.864703106629605","Kp":"21.316368305380458"},{"pair":"Co-Pd","dlnV":"-0.05","V":"12.473019443082524","Kp":"17.336462840287112"},{"pair":"Co-Pd","dlnV":"0.0","V":"13.11252482504883","Kp":"12.210320406533853"},{"pair":"Co-Pd","dlnV":"0.05","V":"13.784818349086917","Kp":"12.842273798950727"},{"pair":"Co-Pd","dlnV":"0.1","V":"14.491581099188936","Kp":"11.60463394946179"},{"pair":"Co-Pd","dlnV":"0.15","V":"15.23458035036642","Kp":"9.992990069280062"},{"pair":"Co-Pd","dlnV":"0.2","V":"16.01567398775834","Kp":"8.192467989436173"},{"pair":"Co-Pd","dlnV":"0.3","V":"17.700057124651153","Kp":"4.499492357941698"},{"pair":"Co-Pd","dlnV":"0.4","V":"19.56158838244212","Kp":"2.4435468842156194"},{"pair":"Co-Pd","dlnV":"-0.4","V":"8.789588244370195","Kp":"6.902750208952693"},{"pair":"Co-Pd","dlnV":"-0.3","V":"9.713997309537529","Kp":"9.873813340631084"},{"pair":"Co-Pd","dlnV":"-0.2","V":"10.73562732476596","Kp":"16.67397111645339"},{"pair":"Co-Pd","dlnV":"-0.15","V":"11.286054707991113","Kp":"20.750710344676612"},{"pair":"Co-Pd","dlnV":"-0.1","V":"11.864703106629605","Kp":"20.61722784667211"},{"pair":"Co-Pd","dlnV":"-0.05","V":"12.473019443082524","Kp":"16.8879521393138"},{"pair":"Co-Pd","dlnV":"0.0","V":"13.11252482504883","Kp":"12.305877581183612"},{"pair":"Co-Pd","dlnV":"0.05","V":"13.784818349086917","Kp":"12.224013195725401"},{"pair":"Co-Pd","dlnV":"0.1","V":"14.491581099188936","Kp":"10.996116223331237"},{"pair":"Co-Pd","dlnV":"0.15","V":"15.23458035036642","Kp":"9.427663264571798"},{"pair":"Co-Pd","dlnV":"0.2","V":"16.01567398775834","Kp":"7.69115014649497"},{"pair":"Co-Pd","dlnV":"0.3","V":"17.700057124651153","Kp":"4.101267916182326"},{"pair":"Co-Pd","dlnV":"0.4","V":"19.56158838244212","Kp":"2.2297262252977545"},{"pair":"Co-Pd","dlnV":"-0.4","V":"8.789588244370195","Kp":"9.287265130312075"},{"pair":"Co-Pd","dlnV":"-0.3","V":"9.713997309537529","Kp":"11.194972182956095"},{"pair":"Co-Pd","dlnV":"-0.2","V":"10.73562732476596","Kp":"17.221857462018185"},{"pair":"Co-Pd","dlnV":"-0.15","V":"11.286054707991113","Kp":"20.686076804037068"},{"pair":"Co-Pd","dlnV":"-0.1","V":"11.864703106629605","Kp":"20.77919095259793"},{"pair":"Co-Pd","dlnV":"-0.05","V":"12.473019443082524","Kp":"16.7325064966026"},{"pair":"Co-Pd","dlnV":"0.0","V":"13.11252482504883","Kp":"11.981117973268432"},{"pair":"Co-Pd","dlnV":"0.05","V":"13.784818349086917","Kp":"12.582747240367908"},{"pair":"Co-Pd","dlnV":"0.1","V":"14.491581099188936","Kp":"11.323164954797628"},{"pair":"Co-Pd","dlnV":"0.15","V":"15.23458035036642","Kp":"9.724970038648802"},{"pair":"Co-Pd","dlnV":"0.2","V":"16.01567398775834","Kp":"7.964018515353549"},{"pair":"Co-Pd","dlnV":"0.3","V":"17.700057124651153","Kp":"4.386788345131325"},{"pair":"Co-Pd","dlnV":"0.4","V":"19.56158838244212","Kp":"2.444620419831328"},{"pair":"Co-Pt","dlnV":"-0.4","V":"8.848716593470693","Kp":"-12.799100169057562"},{"pair":"Co-Pt","dlnV":"-0.3","V":"9.779344241397222","Kp":"-3.389572910746041"},{"pair":"Co-Pt","dlnV":"-0.2","V":"10.807846853442765","Kp":"34.05852915936448"},{"pair":"Co-Pt","dlnV":"-0.15","V":"11.361977011082937","Kp":"42.10788277658241"},{"pair":"Co-Pt","dlnV":"-0.1","V":"11.94451802944034","Kp":"39.26707413231709"},{"pair":"Co-Pt","dlnV":"-0.05","V":"12.556926564492933","Kp":"34.43499643928375"},{"pair":"Co-Pt","dlnV":"0.0","V":"13.200733956567706","Kp":"33.24971454631742"},{"pair":"Co-Pt","dlnV":"0.05","V":"13.877550059489144","Kp":"24.76621280445244"},{"pair":"Co-Pt","dlnV":"0.1","V":"14.589067266052309","Kp":"20.978144745883437"},{"pair":"Co-Pt","dlnV":"0.15","V":"15.337064739886372","Kp":"18.62402567904017"},{"pair":"Co-Pt","dlnV":"0.2","V":"16.123412864290408","Kp":"15.771033444699343"},{"pair":"Co-Pt","dlnV":"0.3","V":"17.81912699774054","Kp":"10.713389660427369"},{"pair":"Co-Pt","dlnV":"0.4","V":"19.69318094339947","Kp":"5.605325835661524"},{"pair":"Co-Pt","dlnV":"-0.4","V":"8.848716593470693","Kp":"-20.17794236021182"},{"pair":"Co-Pt","dlnV":"-0.3","V":"9.779344241397222","Kp":"-7.399677896408269"},{"pair":"Co-Pt","dlnV":"-0.2","V":"10.807846853442765","Kp":"31.890175402783694"},{"pair":"Co-Pt","dlnV":"-0.15","V":"11.361977011082937","Kp":"40.817739178861636"},{"pair":"Co-Pt","dlnV":"-0.1","V":"11.94451802944034","Kp":"37.6897611238387"},{"pair":"Co-Pt","dlnV":"-0.05","V":"12.556926564492933","Kp":"33.40241674127073"},{"pair":"Co-Pt","dlnV":"0.0","V":"13.200733956567706","Kp":"32.75314394836096"},{"pair":"Co-Pt","dlnV":"0.05","V":"13.877550059489144","Kp":"23.835190710795803"},{"pair":"Co-Pt","dlnV":"0.1","V":"14.589067266052309","Kp":"20.248419093960724"},{"pair":"Co-Pt","dlnV":"0.15","V":"15.337064739886372","Kp":"18.045448295446057"},{"pair":"Co-Pt","dlnV":"0.2","V":"16.123412864290408","Kp":"15.33577729547351"},{"pair":"Co-Pt","dlnV":"0.3","V":"17.81912699774054","Kp":"10.463965757703942"},{"pair":"Co-Pt","dlnV":"0.4","V":"19.69318094339947","Kp":"5.566845377357981"},{"pair":"Co-Pt","dlnV":"-0.4","V":"8.848716593470693","Kp":"-12.747149600315536"},{"pair":"Co-Pt","dlnV":"-0.3","V":"9.779344241397222","Kp":"-3.987655016993581"},{"pair":"Co-Pt","dlnV":"-0.2","V":"10.807846853442765","Kp":"32.10006844525481"},{"pair":"Co-Pt","dlnV":"-0.15","V":"11.361977011082937","Kp":"40.560659925928135"},{"pair":"Co-Pt","dlnV":"-0.1","V":"11.94451802944034","Kp":"36.95191074184284"},{"pair":"Co-Pt","dlnV":"-0.05","V":"12.556926564492933","Kp":"33.53894133454024"},{"pair":"Co-Pt","dlnV":"0.0","V":"13.200733956567706","Kp":"33.556035898423254"},{"pair":"Co-Pt","dlnV":"0.05","V":"13.877550059489144","Kp":"24.28445365361013"},{"pair":"Co-Pt","dlnV":"0.1","V":"14.589067266052309","Kp":"20.563741482530418"},{"pair":"Co-Pt","dlnV":"0.15","V":"15.337064739886372","Kp":"18.2845505729048"},{"pair":"Co-Pt","dlnV":"0.2","V":"16.123412864290408","Kp":"15.508283238370819"},{"pair":"Co-Pt","dlnV":"0.3","V":"17.81912699774054","Kp":"10.507621735965197"},{"pair":"Co-Pt","dlnV":"0.4","V":"19.69318094339947","Kp":"5.437491930549915"},{"pair":"Co-Rh","dlnV":"-0.4","V":"8.300206516696713","Kp":"-7.563367155996036"},{"pair":"Co-Rh","dlnV":"-0.3","V":"9.17314685627518","Kp":"-31.334911473609562"},{"pair":"Co-Rh","dlnV":"-0.2","V":"10.13789513279238","Kp":"-20.200011125021355"},{"pair":"Co-Rh","dlnV":"-0.15","V":"10.657676131195803","Kp":"-10.623353957958425"},{"pair":"Co-Rh","dlnV":"-0.1","V":"11.204106871262793","Kp":"-3.8956568684629236"},{"pair":"Co-Rh","dlnV":"-0.05","V":"11.778553714466582","Kp":"-11.214527317982913"},{"pair":"Co-Rh","dlnV":"0.0","V":"12.382453077131174","Kp":"-17.099257446165737"},{"pair":"Co-Rh","dlnV":"0.05","V":"13.017315022220362","Kp":"-12.32515104273233"},{"pair":"Co-Rh","dlnV":"0.1","V":"13.68472703528169","Kp":"-9.719509023304743"},{"pair":"Co-Rh","dlnV":"0.15","V":"14.386357993987197","Kp":"-7.276907276721113"},{"pair":"Co-Rh","dlnV":"0.2","V":"15.123962341196899","Kp":"-4.639637272004274"},{"pair":"Co-Rh","dlnV":"0.3","V":"16.714563345562098","Kp":"-0.5634655090715142"},{"pair":"Co-Rh","dlnV":"0.4","V":"18.472449317848433","Kp":"1.9381521165635438"},{"pair":"Co-Rh","dlnV":"-0.4","V":"8.300206516696713","Kp":"-13.43246964143941"},{"pair":"Co-Rh","dlnV":"-0.3","V":"9.17314685627518","Kp":"-35.2899535818047"},{"pair":"Co-Rh","dlnV":"-0.2","V":"10.13789513279238","Kp":"-22.397261563867893"},{"pair":"Co-Rh","dlnV":"-0.15","V":"10.657676131195803","Kp":"-12.14708568886572"},{"pair":"Co-Rh","dlnV":"-0.1","V":"11.204106871262793","Kp":"-4.607791669860618"},{"pair":"Co-Rh","dlnV":"-0.05","V":"11.778553714466582","Kp":"-12.003032542991075"},{"pair":"Co-Rh","dlnV":"0.0","V":"12.382453077131174","Kp":"-17.92568620998429"},{"pair":"Co-Rh","dlnV":"0.05","V":"13.017315022220362","Kp":"-12.566974033621419"},{"pair":"Co-Rh","dlnV":"0.1","V":"13.68472703528169","Kp":"-10.199488316196499"},{"pair":"Co-Rh","dlnV":"0.15","V":"14.386357993987197","Kp":"-7.757856231855545"},{"pair":"Co-Rh","dlnV":"0.2","V":"15.123962341196899","Kp":"-5.0697630686366"},{"pair":"Co-Rh","dlnV":"0.3","V":"16.714563345562098","Kp":"-0.9613895301842491"},{"pair":"Co-Rh","dlnV":"0.4","V":"18.472449317848433","Kp":"1.7381460002117142"},{"pair":"Co-Rh","dlnV":"-0.4","V":"8.300206516696713","Kp":"-9.71326521635944"},{"pair":"Co-Rh","dlnV":"-0.3","V":"9.17314685627518","Kp":"-31.901898832252012"},{"pair":"Co-Rh","dlnV":"-0.2","V":"10.13789513279238","Kp":"-20.124594915255397"},{"pair":"Co-Rh","dlnV":"-0.15","V":"10.657676131195803","Kp":"-10.1497030824839"},{"pair":"Co-Rh","dlnV":"-0.1","V":"11.204106871262793","Kp":"-3.3293435114600314"},{"pair":"Co-Rh","dlnV":"-0.05","V":"11.778553714466582","Kp":"-10.586793804048986"},{"pair":"Co-Rh","dlnV":"0.0","V":"12.382453077131174","Kp":"-16.551859665695634"},{"pair":"Co-Rh","dlnV":"0.05","V":"13.017315022220362","Kp":"-11.31602321981971"},{"pair":"Co-Rh","dlnV":"0.1","V":"13.68472703528169","Kp":"-8.956026884533468"},{"pair":"Co-Rh","dlnV":"0.15","V":"14.386357993987197","Kp":"-6.663544593354488"},{"pair":"Co-Rh","dlnV":"0.2","V":"15.123962341196899","Kp":"-4.123661874189543"},{"pair":"Co-Rh","dlnV":"0.3","V":"16.714563345562098","Kp":"-0.3635039518643919"},{"pair":"Co-Rh","dlnV":"0.4","V":"18.472449317848433","Kp":"2.136483085395237"},{"pair":"Cu-Ir","dlnV":"-0.4","V":"8.815219543017006","Kp":"-72.83165010244068"},{"pair":"Cu-Ir","dlnV":"-0.3","V":"9.742324275394495","Kp":"-99.19301541152856"},{"pair":"Cu-Ir","dlnV":"-0.2","V":"10.766933463628403","Kp":"-94.4111982927611"},{"pair":"Cu-Ir","dlnV":"-0.15","V":"11.318965946916332","Kp":"-107.67713734105334"},{"pair":"Cu-Ir","dlnV":"-0.1","V":"11.899301740857615","Kp":"-94.03614053748488"},{"pair":"Cu-Ir","dlnV":"-0.05","V":"12.509391987220516","Kp":"-97.79408977652099"},{"pair":"Cu-Ir","dlnV":"0.0","V":"13.150762229402762","Kp":"-82.72188737360392"},{"pair":"Cu-Ir","dlnV":"0.05","V":"13.82501622708465","Kp":"-48.19899722749975"},{"pair":"Cu-Ir","dlnV":"0.1","V":"14.533839966463603","Kp":"-40.15136112128353"},{"pair":"Cu-Ir","dlnV":"0.15","V":"15.279005876097866","Kp":"-33.526269201875174"},{"pair":"Cu-Ir","dlnV":"0.2","V":"16.06237725890112","Kp":"-26.868212100650066"},{"pair":"Cu-Ir","dlnV":"0.3","V":"17.751672221697152","Kp":"-15.895666389934306"},{"pair":"Cu-Ir","dlnV":"0.4","V":"19.618631886631015","Kp":"-7.624731669880611"},{"pair":"Cu-Ir","dlnV":"-0.4","V":"8.815219543017006","Kp":"-81.1814690741639"},{"pair":"Cu-Ir","dlnV":"-0.3","V":"9.742324275394495","Kp":"-105.23378085000421"},{"pair":"Cu-Ir","dlnV":"-0.2","V":"10.766933463628403","Kp":"-98.66495021621023"},{"pair":"Cu-Ir","dlnV":"-0.15","V":"11.318965946916332","Kp":"-110.55389091346242"},{"pair":"Cu-Ir","dlnV":"-0.1","V":"11.899301740857615","Kp":"-96.32602039972099"},{"pair":"Cu-Ir","dlnV":"-0.05","V":"12.509391987220516","Kp":"-99.46714561215204"},{"pair":"Cu-Ir","dlnV":"0.0","V":"13.150762229402762","Kp":"-83.62431759900082"},{"pair":"Cu-Ir","dlnV":"0.05","V":"13.82501622708465","Kp":"-48.673563216285636"},{"pair":"Cu-Ir","dlnV":"0.1","V":"14.533839966463603","Kp":"-40.43143929724504"},{"pair":"Cu-Ir","dlnV":"0.15","V":"15.279005876097866","Kp":"-33.7101658599106"},{"pair":"Cu-Ir","dlnV":"0.2","V":"16.06237725890112","Kp":"-26.979856204930904"},{"pair":"Cu-Ir","dlnV":"0.3","V":"17.751672221697152","Kp":"-15.712060471176411"},{"pair":"Cu-Ir","dlnV":"0.4","V":"19.618631886631015","Kp":"-7.109164555297976"},{"pair":"Cu-Ir","dlnV":"-0.4","V":"8.815219543017006","Kp":"-68.54800326192588"},{"pair":"Cu-Ir","dlnV":"-0.3","V":"9.742324275394495","Kp":"-95.53497985626407"},{"pair":"Cu-Ir","dlnV":"-0.2","V":"10.766933463628403","Kp":"-91.33836591663255"},{"pair":"Cu-Ir","dlnV":"-0.15","V":"11.318965946916332","Kp":"-104.1296189318415"},{"pair":"Cu-Ir","dlnV":"-0.1","V":"11.899301740857615","Kp":"-90.72242179416935"},{"pair":"Cu-Ir","dlnV":"-0.05","V":"12.509391987220516","Kp":"-94.52316214774015"},{"pair":"Cu-Ir","dlnV":"0.0","V":"13.150762229402762","Kp":"-79.51566247460093"},{"pair":"Cu-Ir","dlnV":"0.05","V":"13.82501622708465","Kp":"-45.11621089774171"},{"pair":"Cu-Ir","dlnV":"0.1","V":"14.533839966463603","Kp":"-37.467473665780226"},{"pair":"Cu-Ir","dlnV":"0.15","V":"15.279005876097866","Kp":"-31.24963921083924"},{"pair":"Cu-Ir","dlnV":"0.2","V":"16.06237725890112","Kp":"-25.006781490290766"},{"pair":"Cu-Ir","dlnV":"0.3","V":"17.751672221697152","Kp":"-14.682495367955033"},{"pair":"Cu-Ir","dlnV":"0.4","V":"19.618631886631015","Kp":"-6.858717361400684"},{"pair":"Cu-Ni","dlnV":"-0.4","V":"7.679133236696804","Kp":"-10.520240288718837"},{"pair":"Cu-Ni","dlnV":"-0.3","V":"8.486754729225426","Kp":"-8.181943205016694"},{"pair":"Cu-Ni","dlnV":"-0.2","V":"9.379314515580909","Kp":"-5.166049935524128"},{"pair":"Cu-Ni","dlnV":"-0.15","V":"9.860202254050298","Kp":"-4.674340039033512"},{"pair":"Cu-Ni","dlnV":"-0.1","V":"10.3657456341048","Kp":"-6.654794315735708"},{"pair":"Cu-Ni","dlnV":"-0.05","V":"10.897208777520339","Kp":"-3.9272547423753275"},{"pair":"Cu-Ni","dlnV":"0.0","V":"11.455920618982239","Kp":"0.07417020758608579"},{"pair":"Cu-Ni","dlnV":"0.05","V":"12.04327822911416","Kp":"-3.2543410437501654"},{"pair":"Cu-Ni","dlnV":"0.1","V":"12.660750307882344","Kp":"7.0911252414433"},{"pair":"Cu-Ni","dlnV":"0.15","V":"13.309880857110553","Kp":"6.398886226476426"},{"pair":"Cu-Ni","dlnV":"0.2","V":"13.992293041288866","Kp":"-0.5582212886988144"},{"pair":"Cu-Ni","dlnV":"0.3","V":"15.463875346424713","Kp":"-0.41703025972641944"},{"pair":"Cu-Ni","dlnV":"0.4","V":"17.090225313615573","Kp":"-0.23410058829286834"},{"pair":"Cu-Ni","dlnV":"-0.4","V":"7.679133236696804","Kp":"-10.827708852889518"},{"pair":"Cu-Ni","dlnV":"-0.3","V":"8.486754729225426","Kp":"-8.35340662105909"},{"pair":"Cu-Ni","dlnV":"-0.2","V":"9.379314515580909","Kp":"-5.267662237740186"},{"pair":"Cu-Ni","dlnV":"-0.15","V":"9.860202254050298","Kp":"-4.7233553662173495"},{"pair":"Cu-Ni","dlnV":"-0.1","V":"10.3657456341048","Kp":"-6.735189703410525"},{"pair":"Cu-Ni","dlnV":"-0.05","V":"10.897208777520339","Kp":"-3.8443041714254655"},{"pair":"Cu-Ni","dlnV":"0.0","V":"11.455920618982239","Kp":"0.2890069467726501"},{"pair":"Cu-Ni","dlnV":"0.05","V":"12.04327822911416","Kp":"-3.2075081145311968"},{"pair":"Cu-Ni","dlnV":"0.1","V":"12.660750307882344","Kp":"7.235572740915568"},{"pair":"Cu-Ni","dlnV":"0.15","V":"13.309880857110553","Kp":"6.578849043092864"},{"pair":"Cu-Ni","dlnV":"0.2","V":"13.992293041288866","Kp":"-0.41754551932428197"},{"pair":"Cu-Ni","dlnV":"0.3","V":"15.463875346424713","Kp":"-0.30134143253345785"},{"pair":"Cu-Ni","dlnV":"0.4","V":"17.090225313615573","Kp":"-0.1619137438971086"},{"pair":"Cu-Ni","dlnV":"-0.4","V":"7.679133236696804","Kp":"-10.548555295824746"},{"pair":"Cu-Ni","dlnV":"-0.3","V":"8.486754729225426","Kp":"-7.710414961600995"},{"pair":"Cu-Ni","dlnV":"-0.2","V":"9.379314515580909","Kp":"-4.5369760627124105"},{"pair":"Cu-Ni","dlnV":"-0.15","V":"9.860202254050298","Kp":"-4.106045038397277"},{"pair":"Cu-Ni","dlnV":"-0.1","V":"10.3657456341048","Kp":"-6.224648646880844"},{"pair":"Cu-Ni","dlnV":"-0.05","V":"10.897208777520339","Kp":"-3.6378759947986774"},{"pair":"Cu-Ni","dlnV":"0.0","V":"11.455920618982239","Kp":"0.21685937933410038"},{"pair":"Cu-Ni","dlnV":"0.05","V":"12.04327822911416","Kp":"-3.209404609948338"},{"pair":"Cu-Ni","dlnV":"0.1","V":"12.660750307882344","Kp":"6.963498122972273"},{"pair":"Cu-Ni","dlnV":"0.15","V":"13.309880857110553","Kp":"6.368004061852575"},{"pair":"Cu-Ni","dlnV":"0.2","V":"13.992293041288866","Kp":"-0.45256322975078833"},{"pair":"Cu-Ni","dlnV":"0.3","V":"15.463875346424713","Kp":"-0.3507548377067865"},{"pair":"Cu-Ni","dlnV":"0.4","V":"17.090225313615573","Kp":"-0.2190901754601608"},{"pair":"Cu-Pd","dlnV":"-0.4","V":"9.1639898169774","Kp":"-5.485499453454357"},{"pair":"Cu-Pd","dlnV":"-0.3","V":"10.1277750392648","Kp":"-6.75200343543685"},{"pair":"Cu-Pd","dlnV":"-0.2","V":"11.192922438207907","Kp":"-4.522286776031484"},{"pair":"Cu-Pd","dlnV":"-0.15","V":"11.766795843266626","Kp":"0.33477419959950416"},{"pair":"Cu-Pd","dlnV":"-0.1","V":"12.370092366983748","Kp":"2.199826162353193"},{"pair":"Cu-Pd","dlnV":"-0.05","V":"13.004320564911692","Kp":"-3.6212953484213504"},{"pair":"Cu-Pd","dlnV":"0.0","V":"13.67106633789999","Kp":"3.2810775624219244"},{"pair":"Cu-Pd","dlnV":"0.05","V":"14.37199689767348","Kp":"4.848756702574902"},{"pair":"Cu-Pd","dlnV":"0.1","V":"15.108864935730015","Kp":"5.173109125038239"},{"pair":"Cu-Pd","dlnV":"0.15","V":"15.883513005982158","Kp":"4.781063201959534"},{"pair":"Cu-Pd","dlnV":"0.2","V":"16.6978781321017","Kp":"5.610170838346461"},{"pair":"Cu-Pd","dlnV":"0.3","V":"18.454009305170118","Kp":"1.9824995271633095"},{"pair":"Cu-Pd","dlnV":"0.4","V":"20.3948344059714","Kp":"0.183617371493584"},{"pair":"Cu-Pd","dlnV":"-0.4","V":"9.1639898169774","Kp":"-8.3817375417961"},{"pair":"Cu-Pd","dlnV":"-0.3","V":"10.1277750392648","Kp":"-8.846545090818623"},{"pair":"Cu-Pd","dlnV":"-0.2","V":"11.192922438207907","Kp":"-5.7973119404813405"},{"pair":"Cu-Pd","dlnV":"-0.15","V":"11.766795843266626","Kp":"-0.9300778373687564"},{"pair":"Cu-Pd","dlnV":"-0.1","V":"12.370092366983748","Kp":"1.135367435645846"},{"pair":"Cu-Pd","dlnV":"-0.05","V":"13.004320564911692","Kp":"-3.9193832739506305"},{"pair":"Cu-Pd","dlnV":"0.0","V":"13.67106633789999","Kp":"2.6997189439669866"},{"pair":"Cu-Pd","dlnV":"0.05","V":"14.37199689767348","Kp":"4.247879571181148"},{"pair":"Cu-Pd","dlnV":"0.1","V":"15.108864935730015","Kp":"4.587000966310749"},{"pair":"Cu-Pd","dlnV":"0.15","V":"15.883513005982158","Kp":"4.217424774027196"},{"pair":"Cu-Pd","dlnV":"0.2","V":"16.6978781321017","Kp":"5.086656897442922"},{"pair":"Cu-Pd","dlnV":"0.3","V":"18.454009305170118","Kp":"1.5460382902036593"},{"pair":"Cu-Pd","dlnV":"0.4","V":"20.3948344059714","Kp":"-0.18042821255529432"},{"pair":"Cu-Pd","dlnV":"-0.4","V":"9.1639898169774","Kp":"-5.030218353101323"},{"pair":"Cu-Pd","dlnV":"-0.3","V":"10.1277750392648","Kp":"-5.945777887984735"},{"pair":"Cu-Pd","dlnV":"-0.2","V":"11.192922438207907","Kp":"-3.634971929221147"},{"pair":"Cu-Pd","dlnV":"-0.15","V":"11.766795843266626","Kp":"0.5644374057925424"},{"pair":"Cu-Pd","dlnV":"-0.1","V":"12.370092366983748","Kp":"2.3437466885053206"},{"pair":"Cu-Pd","dlnV":"-0.05","V":"13.004320564911692","Kp":"-2.445707563604459"},{"pair":"Cu-Pd","dlnV":"0.0","V":"13.67106633789999","Kp":"3.804986615459029"},{"pair":"Cu-Pd","dlnV":"0.05","V":"14.37199689767348","Kp":"5.182066989979675"},{"pair":"Cu-Pd","dlnV":"0.1","V":"15.108864935730015","Kp":"5.412642972532003"},{"pair":"Cu-Pd","dlnV":"0.15","V":"15.883513005982158","Kp":"4.959250015091362"},{"pair":"Cu-Pd","dlnV":"0.2","V":"16.6978781321017","Kp":"5.705350410160156"},{"pair":"Cu-Pd","dlnV":"0.3","V":"18.454009305170118","Kp":"2.0601445094312556"},{"pair":"Cu-Pd","dlnV":"0.4","V":"20.3948344059714","Kp":"0.21814843519012508"},{"pair":"Cu-Pt","dlnV":"-0.4","V":"9.223118166077898","Kp":"-22.41547411030023"},{"pair":"Cu-Pt","dlnV":"-0.3","V":"10.193121971124494","Kp":"-26.690983432626282"},{"pair":"Cu-Pt","dlnV":"-0.2","V":"11.26514196688471","Kp":"-7.6647006416812715"},{"pair":"Cu-Pt","dlnV":"-0.15","V":"11.84271814635845","Kp":"-3.131743544829156"},{"pair":"Cu-Pt","dlnV":"-0.1","V":"12.449907289794483","Kp":"-1.0204244816321824"},{"pair":"Cu-Pt","dlnV":"-0.05","V":"13.088227686322101","Kp":"2.9178394645193837"},{"pair":"Cu-Pt","dlnV":"0.0","V":"13.759275469418867","Kp":"7.05440877096798"},{"pair":"Cu-Pt","dlnV":"0.05","V":"14.464728608075706","Kp":"7.587150800192992"},{"pair":"Cu-Pt","dlnV":"0.1","V":"15.206351102593388","Kp":"7.9930693583819235"},{"pair":"Cu-Pt","dlnV":"0.15","V":"15.98599739550211","Kp":"7.734014588970775"},{"pair":"Cu-Pt","dlnV":"0.2","V":"16.80561700863377","Kp":"7.191848078212868"},{"pair":"Cu-Pt","dlnV":"0.3","V":"18.573079178259505","Kp":"4.4291163912608456"},{"pair":"Cu-Pt","dlnV":"0.4","V":"20.52642696692875","Kp":"1.8757390454616898"},{"pair":"Cu-Pt","dlnV":"-0.4","V":"9.223118166077898","Kp":"-28.473704879323876"},{"pair":"Cu-Pt","dlnV":"-0.3","V":"10.193121971124494","Kp":"-30.922147158182643"},{"pair":"Cu-Pt","dlnV":"-0.2","V":"11.26514196688471","Kp":"-10.30969719657001"},{"pair":"Cu-Pt","dlnV":"-0.15","V":"11.84271814635845","Kp":"-5.191640090920636"},{"pair":"Cu-Pt","dlnV":"-0.1","V":"12.449907289794483","Kp":"-2.863884560072588"},{"pair":"Cu-Pt","dlnV":"-0.05","V":"13.088227686322101","Kp":"1.7197553382603488"},{"pair":"Cu-Pt","dlnV":"0.0","V":"13.759275469418867","Kp":"6.131871224486475"},{"pair":"Cu-Pt","dlnV":"0.05","V":"14.464728608075706","Kp":"6.865908795201261"},{"pair":"Cu-Pt","dlnV":"0.1","V":"15.206351102593388","Kp":"7.422217622048235"},{"pair":"Cu-Pt","dlnV":"0.15","V":"15.98599739550211","Kp":"7.289023621716338"},{"pair":"Cu-Pt","dlnV":"0.2","V":"16.80561700863377","Kp":"6.866798704132685"},{"pair":"Cu-Pt","dlnV":"0.3","V":"18.573079178259505","Kp":"4.301600267967938"},{"pair":"Cu-Pt","dlnV":"0.4","V":"20.52642696692875","Kp":"1.8443702065313947"},{"pair":"Cu-Pt","dlnV":"-0.4","V":"9.223118166077898","Kp":"-19.944115532745762"},{"pair":"Cu-Pt","dlnV":"-0.3","V":"10.193121971124494","Kp":"-25.693622653120872"},{"pair":"Cu-Pt","dlnV":"-0.2","V":"11.26514196688471","Kp":"-6.7471945352056135"},{"pair":"Cu-Pt","dlnV":"-0.15","V":"11.84271814635845","Kp":"-3.446028361129611"},{"pair":"Cu-Pt","dlnV":"-0.1","V":"12.449907289794483","Kp":"-0.7093407896530276"},{"pair":"Cu-Pt","dlnV":"-0.05","V":"13.088227686322101","Kp":"5.042575330797804"},{"pair":"Cu-Pt","dlnV":"0.0","V":"13.759275469418867","Kp":"8.187794215617552"},{"pair":"Cu-Pt","dlnV":"0.05","V":"14.464728608075706","Kp":"8.506782608289042"},{"pair":"Cu-Pt","dlnV":"0.1","V":"15.206351102593388","Kp":"8.733242803042433"},{"pair":"Cu-Pt","dlnV":"0.15","V":"15.98599739550211","Kp":"8.310272206372622"},{"pair":"Cu-Pt","dlnV":"0.2","V":"16.80561700863377","Kp":"7.644325491408062"},{"pair":"Cu-Pt","dlnV":"0.3","V":"18.573079178259505","Kp":"4.678173922945561"},{"pair":"Cu-Pt","dlnV":"0.4","V":"20.52642696692875","Kp":"2.0266900879624523"},{"pair":"Cu-Rh","dlnV":"-0.4","V":"8.674608089303918","Kp":"-40.11555234356552"},{"pair":"Cu-Rh","dlnV":"-0.3","V":"9.58692458600245","Kp":"-50.72468702044379"},{"pair":"Cu-Rh","dlnV":"-0.2","V":"10.595190246234326","Kp":"-52.02545826472819"},{"pair":"Cu-Rh","dlnV":"-0.15","V":"11.138417266471317","Kp":"-48.30732186748997"},{"pair":"Cu-Rh","dlnV":"-0.1","V":"11.709496131616936","Kp":"-53.43264721402689"},{"pair":"Cu-Rh","dlnV":"-0.05","V":"12.30985483629575","Kp":"-51.94185167462829"},{"pair":"Cu-Rh","dlnV":"0.0","V":"12.940994589982335","Kp":"-37.85776987953348"},{"pair":"Cu-Rh","dlnV":"0.05","V":"13.604493570806925","Kp":"-26.996145936191883"},{"pair":"Cu-Rh","dlnV":"0.1","V":"14.302010871822768","Kp":"-20.927418251870886"},{"pair":"Cu-Rh","dlnV":"0.15","V":"15.035290649602935","Kp":"-16.06884017872528"},{"pair":"Cu-Rh","dlnV":"0.2","V":"15.80616648554026","Kp":"-12.176061330519161"},{"pair":"Cu-Rh","dlnV":"0.3","V":"17.468515526081063","Kp":"-5.304878155411007"},{"pair":"Cu-Rh","dlnV":"0.4","V":"19.305695341377714","Kp":"-1.1661671617609886"},{"pair":"Cu-Rh","dlnV":"-0.4","V":"8.674608089303918","Kp":"-45.466451565908365"},{"pair":"Cu-Rh","dlnV":"-0.3","V":"9.58692458600245","Kp":"-53.91691121436861"},{"pair":"Cu-Rh","dlnV":"-0.2","V":"10.595190246234326","Kp":"-54.09108911990049"},{"pair":"Cu-Rh","dlnV":"-0.15","V":"11.138417266471317","Kp":"-49.77772234711169"},{"pair":"Cu-Rh","dlnV":"-0.1","V":"11.709496131616936","Kp":"-54.506323962790724"},{"pair":"Cu-Rh","dlnV":"-0.05","V":"12.30985483629575","Kp":"-52.68693009046761"},{"pair":"Cu-Rh","dlnV":"0.0","V":"12.940994589982335","Kp":"-38.104518280282925"},{"pair":"Cu-Rh","dlnV":"0.05","V":"13.604493570806925","Kp":"-27.10108507658386"},{"pair":"Cu-Rh","dlnV":"0.1","V":"14.302010871822768","Kp":"-20.941698309350063"},{"pair":"Cu-Rh","dlnV":"0.15","V":"15.035290649602935","Kp":"-16.057146544568628"},{"pair":"Cu-Rh","dlnV":"0.2","V":"15.80616648554026","Kp":"-12.191048236459048"},{"pair":"Cu-Rh","dlnV":"0.3","V":"17.468515526081063","Kp":"-5.291154443642999"},{"pair":"Cu-Rh","dlnV":"0.4","V":"19.305695341377714","Kp":"-1.0645162220315167"},{"pair":"Cu-Rh","dlnV":"-0.4","V":"8.674608089303918","Kp":"-38.58099604025175"},{"pair":"Cu-Rh","dlnV":"-0.3","V":"9.58692458600245","Kp":"-48.49394060426106"},{"pair":"Cu-Rh","dlnV":"-0.2","V":"10.595190246234326","Kp":"-49.97732052161318"},{"pair":"Cu-Rh","dlnV":"-0.15","V":"11.138417266471317","Kp":"-45.99401844489237"},{"pair":"Cu-Rh","dlnV":"-0.1","V":"11.709496131616936","Kp":"-51.440579551363804"},{"pair":"Cu-Rh","dlnV":"-0.05","V":"12.30985483629575","Kp":"-50.151093004184034"},{"pair":"Cu-Rh","dlnV":"0.0","V":"12.940994589982335","Kp":"-35.85759581184193"},{"pair":"Cu-Rh","dlnV":"0.05","V":"13.604493570806925","Kp":"-25.383842552284683"},{"pair":"Cu-Rh","dlnV":"0.1","V":"14.302010871822768","Kp":"-19.586592411885572"},{"pair":"Cu-Rh","dlnV":"0.15","V":"15.035290649602935","Kp":"-14.991752797540936"},{"pair":"Cu-Rh","dlnV":"0.2","V":"15.80616648554026","Kp":"-11.331473295682702"},{"pair":"Cu-Rh","dlnV":"0.3","V":"17.468515526081063","Kp":"-4.806780520087393"},{"pair":"Cu-Rh","dlnV":"0.4","V":"19.305695341377714","Kp":"-0.8476987560149947"},{"pair":"Ir-Ni","dlnV":"-0.4","V":"8.456478569532386","Kp":"-24.878009828557605"},{"pair":"Ir-Ni","dlnV":"-0.3","V":"9.345854184377146","Kp":"-79.76461572549424"},{"pair":"Ir-Ni","dlnV":"-0.2","V":"10.328766249149222","Kp":"-74.81227298268564"},{"pair":"Ir-Ni","dlnV":"-0.15","V":"10.858333418954777","Kp":"-78.45796453700129"},{"pair":"Ir-Ni","dlnV":"-0.1","V":"11.41505207816101","Kp":"-81.18992555573652"},{"pair":"Ir-Ni","dlnV":"-0.05","V":"12.000314313397737","Kp":"-69.51702877039573"},{"pair":"Ir-Ni","dlnV":"0.0","V":"12.615583585102533","Kp":"-74.05201104361208"},{"pair":"Ir-Ni","dlnV":"0.05","V":"13.262398386934112","Kp":"-58.836320557578375"},{"pair":"Ir-Ni","dlnV":"0.1","V":"13.942376092807837","Kp":"-37.74383065294266"},{"pair":"Ir-Ni","dlnV":"0.15","V":"14.65721700117296","Kp":"-32.196210020488884"},{"pair":"Ir-Ni","dlnV":"0.2","V":"15.408708586644398","Kp":"-26.788022293205955"},{"pair":"Ir-Ni","dlnV":"0.3","V":"17.029256615061904","Kp":"-14.043802128355344"},{"pair":"Ir-Ni","dlnV":"0.4","V":"18.82023916741376","Kp":"-8.406969019146421"},{"pair":"Ir-Ni","dlnV":"-0.4","V":"8.456478569532386","Kp":"-36.034331149529265"},{"pair":"Ir-Ni","dlnV":"-0.3","V":"9.345854184377146","Kp":"-88.16371463511928"},{"pair":"Ir-Ni","dlnV":"-0.2","V":"10.328766249149222","Kp":"-80.94988282601706"},{"pair":"Ir-Ni","dlnV":"-0.15","V":"10.858333418954777","Kp":"-83.18078217287649"},{"pair":"Ir-Ni","dlnV":"-0.1","V":"11.41505207816101","Kp":"-84.44360639111888"},{"pair":"Ir-Ni","dlnV":"-0.05","V":"12.000314313397737","Kp":"-72.39317558516682"},{"pair":"Ir-Ni","dlnV":"0.0","V":"12.615583585102533","Kp":"-76.27232983955857"},{"pair":"Ir-Ni","dlnV":"0.05","V":"13.262398386934112","Kp":"-60.17302854679505"},{"pair":"Ir-Ni","dlnV":"0.1","V":"13.942376092807837","Kp":"-38.96372232259728"},{"pair":"Ir-Ni","dlnV":"0.15","V":"14.65721700117296","Kp":"-33.204853569353105"},{"pair":"Ir-Ni","dlnV":"0.2","V":"15.408708586644398","Kp":"-27.472766459690387"},{"pair":"Ir-Ni","dlnV":"0.3","V":"17.029256615061904","Kp":"-14.425673386121165"},{"pair":"Ir-Ni","dlnV":"0.4","V":"18.82023916741376","Kp":"-8.647918964215231"},{"pair":"Ir-Ni","dlnV":"-0.4","V":"8.456478569532386","Kp":"-23.669596471384427"},{"pair":"Ir-Ni","dlnV":"-0.3","V":"9.345854184377146","Kp":"-78.10206761166471"},{"pair":"Ir-Ni","dlnV":"-0.2","V":"10.328766249149222","Kp":"-72.66125272944835"},{"pair":"Ir-Ni","dlnV":"-0.15","V":"10.858333418954777","Kp":"-76.15216940532804"},{"pair":"Ir-Ni","dlnV":"-0.1","V":"11.41505207816101","Kp":"-78.94772386013311"},{"pair":"Ir-Ni","dlnV":"-0.05","V":"12.000314313397737","Kp":"-67.26134356969764"},{"pair":"Ir-Ni","dlnV":"0.0","V":"12.615583585102533","Kp":"-72.60026912568448"},{"pair":"Ir-Ni","dlnV":"0.05","V":"13.262398386934112","Kp":"-57.447896609884125"},{"pair":"Ir-Ni","dlnV":"0.1","V":"13.942376092807837","Kp":"-36.476481933923715"},{"pair":"Ir-Ni","dlnV":"0.15","V":"14.65721700117296","Kp":"-31.21042810908768"},{"pair":"Ir-Ni","dlnV":"0.2","V":"15.408708586644398","Kp":"-25.907806931607684"},{"pair":"Ir-Ni","dlnV":"0.3","V":"17.029256615061904","Kp":"-13.467009984321482"},{"pair":"Ir-Ni","dlnV":"0.4","V":"18.82023916741376","Kp":"-8.003171496010273"},{"pair":"Ir-Pd","dlnV":"-0.4","V":"9.941335149812982","Kp":"-44.16462842403102"},{"pair":"Ir-Pd","dlnV":"-0.3","V":"10.986874494416519","Kp":"-37.194113627375756"},{"pair":"Ir-Pd","dlnV":"-0.2","V":"12.14237417177622","Kp":"-28.324068753137485"},{"pair":"Ir-Pd","dlnV":"-0.15","V":"12.764927008171105","Kp":"-50.105619485687455"},{"pair":"Ir-Pd","dlnV":"-0.1","V":"13.419398811039956","Kp":"-30.076302294622987"},{"pair":"Ir-Pd","dlnV":"-0.05","V":"14.10742610078909","Kp":"-16.82511029171996"},{"pair":"Ir-Pd","dlnV":"0.0","V":"14.830729304020284","Kp":"-15.685465457126226"},{"pair":"Ir-Pd","dlnV":"0.05","V":"15.591117055493433","Kp":"-15.157023900913108"},{"pair":"Ir-Pd","dlnV":"0.1","V":"16.39049072065551","Kp":"-12.396515424012708"},{"pair":"Ir-Pd","dlnV":"0.15","V":"17.230849150044563","Kp":"-10.119994091645328"},{"pair":"Ir-Pd","dlnV":"0.2","V":"18.11429367745723","Kp":"-10.126423553810286"},{"pair":"Ir-Pd","dlnV":"0.3","V":"20.019390573807307","Kp":"-5.747997165635324"},{"pair":"Ir-Pd","dlnV":"0.4","V":"22.12484825976959","Kp":"-3.650811531833361"},{"pair":"Ir-Pd","dlnV":"-0.4","V":"9.941335149812982","Kp":"-44.41581850132767"},{"pair":"Ir-Pd","dlnV":"-0.3","V":"10.986874494416519","Kp":"-37.13341969915339"},{"pair":"Ir-Pd","dlnV":"-0.2","V":"12.14237417177622","Kp":"-28.023202909185382"},{"pair":"Ir-Pd","dlnV":"-0.15","V":"12.764927008171105","Kp":"-51.436747867383914"},{"pair":"Ir-Pd","dlnV":"-0.1","V":"13.419398811039956","Kp":"-30.90502145687114"},{"pair":"Ir-Pd","dlnV":"-0.05","V":"14.10742610078909","Kp":"-17.190087274033388"},{"pair":"Ir-Pd","dlnV":"0.0","V":"14.830729304020284","Kp":"-16.026424119239127"},{"pair":"Ir-Pd","dlnV":"0.05","V":"15.591117055493433","Kp":"-15.347783203725271"},{"pair":"Ir-Pd","dlnV":"0.1","V":"16.39049072065551","Kp":"-12.560602566235897"},{"pair":"Ir-Pd","dlnV":"0.15","V":"17.230849150044563","Kp":"-10.228125963123261"},{"pair":"Ir-Pd","dlnV":"0.2","V":"18.11429367745723","Kp":"-10.179025669924883"},{"pair":"Ir-Pd","dlnV":"0.3","V":"20.019390573807307","Kp":"-5.79839655007648"},{"pair":"Ir-Pd","dlnV":"0.4","V":"22.12484825976959","Kp":"-3.639275697603093"},{"pair":"Ir-Pd","dlnV":"-0.4","V":"9.941335149812982","Kp":"-42.15204675578133"},{"pair":"Ir-Pd","dlnV":"-0.3","V":"10.986874494416519","Kp":"-35.897339827040554"},{"pair":"Ir-Pd","dlnV":"-0.2","V":"12.14237417177622","Kp":"-26.695280765097454"},{"pair":"Ir-Pd","dlnV":"-0.15","V":"12.764927008171105","Kp":"-50.25330657628356"},{"pair":"Ir-Pd","dlnV":"-0.1","V":"13.419398811039956","Kp":"-29.823309333541864"},{"pair":"Ir-Pd","dlnV":"-0.05","V":"14.10742610078909","Kp":"-16.141387346027482"},{"pair":"Ir-Pd","dlnV":"0.0","V":"14.830729304020284","Kp":"-15.135494648422764"},{"pair":"Ir-Pd","dlnV":"0.05","V":"15.591117055493433","Kp":"-14.771924617087572"},{"pair":"Ir-Pd","dlnV":"0.1","V":"16.39049072065551","Kp":"-12.102721905173961"},{"pair":"Ir-Pd","dlnV":"0.15","V":"17.230849150044563","Kp":"-9.874354122038891"},{"pair":"Ir-Pd","dlnV":"0.2","V":"18.11429367745723","Kp":"-9.957586516623053"},{"pair":"Ir-Pd","dlnV":"0.3","V":"20.019390573807307","Kp":"-5.513921635777139"},{"pair":"Ir-Pd","dlnV":"0.4","V":"22.12484825976959","Kp":"-3.4996806968361507"},{"pair":"Ir-Pt","dlnV":"-0.4","V":"10.00046349891348","Kp":"4.011764692007472"},{"pair":"Ir-Pt","dlnV":"-0.3","V":"11.052221426276214","Kp":"5.08193090247967"},{"pair":"Ir-Pt","dlnV":"-0.2","V":"12.214593700453026","Kp":"7.145653051387462"},{"pair":"Ir-Pt","dlnV":"-0.15","V":"12.840849311262929","Kp":"-9.255573566327831"},{"pair":"Ir-Pt","dlnV":"-0.1","V":"13.499213733850691","Kp":"-2.3373448328788013"},{"pair":"Ir-Pt","dlnV":"-0.05","V":"14.191333222199498","Kp":"-1.2282899118900157"},{"pair":"Ir-Pt","dlnV":"0.0","V":"14.918938435539161","Kp":"-3.321855383690063"},{"pair":"Ir-Pt","dlnV":"0.05","V":"15.68384876589566","Kp":"-4.906975819364116"},{"pair":"Ir-Pt","dlnV":"0.1","V":"16.487976887518883","Kp":"-5.405670709923194"},{"pair":"Ir-Pt","dlnV":"0.15","V":"17.333333539564517","Kp":"-5.574598641912791"},{"pair":"Ir-Pt","dlnV":"0.2","V":"18.2220325539893","Kp":"-5.481002306359524"},{"pair":"Ir-Pt","dlnV":"0.3","V":"20.138460446896694","Kp":"-4.157021903010061"},{"pair":"Ir-Pt","dlnV":"0.4","V":"22.256440820726937","Kp":"-2.534718900051752"},{"pair":"Ir-Pt","dlnV":"-0.4","V":"10.00046349891348","Kp":"4.4367695888540775"},{"pair":"Ir-Pt","dlnV":"-0.3","V":"11.052221426276214","Kp":"5.524330452159186"},{"pair":"Ir-Pt","dlnV":"-0.2","V":"12.214593700453026","Kp":"7.489453722163997"},{"pair":"Ir-Pt","dlnV":"-0.15","V":"12.840849311262929","Kp":"-8.807223441425728"},{"pair":"Ir-Pt","dlnV":"-0.1","V":"13.499213733850691","Kp":"-2.1854061232290336"},{"pair":"Ir-Pt","dlnV":"-0.05","V":"14.191333222199498","Kp":"-1.18517144455071"},{"pair":"Ir-Pt","dlnV":"0.0","V":"14.918938435539161","Kp":"-3.3815493040578435"},{"pair":"Ir-Pt","dlnV":"0.05","V":"15.68384876589566","Kp":"-5.0065039699377625"},{"pair":"Ir-Pt","dlnV":"0.1","V":"16.487976887518883","Kp":"-5.565256400639364"},{"pair":"Ir-Pt","dlnV":"0.15","V":"17.333333539564517","Kp":"-5.711684383503662"},{"pair":"Ir-Pt","dlnV":"0.2","V":"18.2220325539893","Kp":"-5.606502430014647"},{"pair":"Ir-Pt","dlnV":"0.3","V":"20.138460446896694","Kp":"-4.322370444458979"},{"pair":"Ir-Pt","dlnV":"0.4","V":"22.256440820726937","Kp":"-2.6339273129454304"},{"pair":"Ir-Pt","dlnV":"-0.4","V":"10.00046349891348","Kp":"5.227799861928096"},{"pair":"Ir-Pt","dlnV":"-0.3","V":"11.052221426276214","Kp":"4.94533679265325"},{"pair":"Ir-Pt","dlnV":"-0.2","V":"12.214593700453026","Kp":"7.2182204345571215"},{"pair":"Ir-Pt","dlnV":"-0.15","V":"12.840849311262929","Kp":"-9.816876325275542"},{"pair":"Ir-Pt","dlnV":"-0.1","V":"13.499213733850691","Kp":"-2.640474587316186"},{"pair":"Ir-Pt","dlnV":"-0.05","V":"14.191333222199498","Kp":"-1.2101464712072019"},{"pair":"Ir-Pt","dlnV":"0.0","V":"14.918938435539161","Kp":"-3.2607377587624278"},{"pair":"Ir-Pt","dlnV":"0.05","V":"15.68384876589566","Kp":"-4.89084181835709"},{"pair":"Ir-Pt","dlnV":"0.1","V":"16.487976887518883","Kp":"-5.27309724977013"},{"pair":"Ir-Pt","dlnV":"0.15","V":"17.333333539564517","Kp":"-5.437606834227175"},{"pair":"Ir-Pt","dlnV":"0.2","V":"18.2220325539893","Kp":"-5.433035325814702"},{"pair":"Ir-Pt","dlnV":"0.3","V":"20.138460446896694","Kp":"-3.9768795317081094"},{"pair":"Ir-Pt","dlnV":"0.4","V":"22.256440820726937","Kp":"-2.4151228181005036"},{"pair":"Ir-Rh","dlnV":"-0.4","V":"9.4519534221395","Kp":"5.266769255629187"},{"pair":"Ir-Rh","dlnV":"-0.3","V":"10.44602404115417","Kp":"3.7535587491937776"},{"pair":"Ir-Rh","dlnV":"-0.2","V":"11.54464197980264","Kp":"1.5765939732972003"},{"pair":"Ir-Rh","dlnV":"-0.15","V":"12.136548431375795","Kp":"7.848167303357005"},{"pair":"Ir-Rh","dlnV":"-0.1","V":"12.758802575673146","Kp":"-8.754827856577345"},{"pair":"Ir-Rh","dlnV":"-0.05","V":"13.412960372173147","Kp":"-4.718416814052785"},{"pair":"Ir-Rh","dlnV":"0.0","V":"14.100657556102629","Kp":"-0.5676501052467016"},{"pair":"Ir-Rh","dlnV":"0.05","V":"14.82361372862688","Kp":"-0.540258936457541"},{"pair":"Ir-Rh","dlnV":"0.1","V":"15.583636656748261","Kp":"-0.7433215558422636"},{"pair":"Ir-Rh","dlnV":"0.15","V":"16.38262679366534","Kp":"0.025449259640155146"},{"pair":"Ir-Rh","dlnV":"0.2","V":"17.22258203089579","Kp":"0.5516394815531044"},{"pair":"Ir-Rh","dlnV":"0.3","V":"19.033896794718252","Kp":"0.32612999700706563"},{"pair":"Ir-Rh","dlnV":"0.4","V":"21.035709195175897","Kp":"-0.09235711222765458"},{"pair":"Ir-Rh","dlnV":"-0.4","V":"9.4519534221395","Kp":"5.8086845217901475"},{"pair":"Ir-Rh","dlnV":"-0.3","V":"10.44602404115417","Kp":"4.686922705538234"},{"pair":"Ir-Rh","dlnV":"-0.2","V":"11.54464197980264","Kp":"2.0874767446214286"},{"pair":"Ir-Rh","dlnV":"-0.15","V":"12.136548431375795","Kp":"8.459687031090164"},{"pair":"Ir-Rh","dlnV":"-0.1","V":"12.758802575673146","Kp":"-9.0740929475464"},{"pair":"Ir-Rh","dlnV":"-0.05","V":"13.412960372173147","Kp":"-4.906509537375983"},{"pair":"Ir-Rh","dlnV":"0.0","V":"14.100657556102629","Kp":"-0.6350789292136065"},{"pair":"Ir-Rh","dlnV":"0.05","V":"14.82361372862688","Kp":"-0.632872079772702"},{"pair":"Ir-Rh","dlnV":"0.1","V":"15.583636656748261","Kp":"-0.8347379312868082"},{"pair":"Ir-Rh","dlnV":"0.15","V":"16.38262679366534","Kp":"-0.06312114817758442"},{"pair":"Ir-Rh","dlnV":"0.2","V":"17.22258203089579","Kp":"0.4749575629537919"},{"pair":"Ir-Rh","dlnV":"0.3","V":"19.033896794718252","Kp":"0.27842825705543006"},{"pair":"Ir-Rh","dlnV":"0.4","V":"21.035709195175897","Kp":"-0.10792711841566936"},{"pair":"Ir-Rh","dlnV":"-0.4","V":"9.4519534221395","Kp":"4.613087841807541"},{"pair":"Ir-Rh","dlnV":"-0.3","V":"10.44602404115417","Kp":"3.2957842172475504"},{"pair":"Ir-Rh","dlnV":"-0.2","V":"11.54464197980264","Kp":"1.4003844193217627"},{"pair":"Ir-Rh","dlnV":"-0.15","V":"12.136548431375795","Kp":"7.205423236804491"},{"pair":"Ir-Rh","dlnV":"-0.1","V":"12.758802575673146","Kp":"-8.446549599975523"},{"pair":"Ir-Rh","dlnV":"-0.05","V":"13.412960372173147","Kp":"-4.450217872252756"},{"pair":"Ir-Rh","dlnV":"0.0","V":"14.100657556102629","Kp":"-0.6086427276814882"},{"pair":"Ir-Rh","dlnV":"0.05","V":"14.82361372862688","Kp":"-0.6170632232160151"},{"pair":"Ir-Rh","dlnV":"0.1","V":"15.583636656748261","Kp":"-0.8381687564904736"},{"pair":"Ir-Rh","dlnV":"0.15","V":"16.38262679366534","Kp":"-0.11023243167621194"},{"pair":"Ir-Rh","dlnV":"0.2","V":"17.22258203089579","Kp":"0.40286256584358"},{"pair":"Ir-Rh","dlnV":"0.3","V":"19.033896794718252","Kp":"0.234295883671833"},{"pair":"Ir-Rh","dlnV":"0.4","V":"21.035709195175897","Kp":"-0.12524816434200298"},{"pair":"Ni-Pd","dlnV":"-0.4","V":"8.805248843492778","Kp":"-6.968440349296511"},{"pair":"Ni-Pd","dlnV":"-0.3","V":"9.731304948247448","Kp":"-3.863272280781007"},{"pair":"Ni-Pd","dlnV":"-0.2","V":"10.754755223728724","Kp":"-5.916642051589142"},{"pair":"Ni-Pd","dlnV":"-0.15","V":"11.306163315305069","Kp":"-1.4493207557173142"},{"pair":"Ni-Pd","dlnV":"-0.1","V":"11.88584270428714","Kp":"-3.162649805962711"},{"pair":"Ni-Pd","dlnV":"-0.05","V":"12.49524289108891","Kp":"1.100875974696786"},{"pair":"Ni-Pd","dlnV":"0.0","V":"13.13588769359976","Kp":"4.908375251514339"},{"pair":"Ni-Pd","dlnV":"0.05","V":"13.809379057522941","Kp":"3.088099302361483"},{"pair":"Ni-Pd","dlnV":"0.1","V":"14.51740106207425","Kp":"3.098680806137177"},{"pair":"Ni-Pd","dlnV":"0.15","V":"15.26172413105725","Kp":"3.475161071460554"},{"pair":"Ni-Pd","dlnV":"0.2","V":"16.04420945984498","Kp":"3.48426163149195"},{"pair":"Ni-Pd","dlnV":"0.3","V":"17.731593698534866","Kp":"2.13448599938965"},{"pair":"Ni-Pd","dlnV":"0.4","V":"19.596441686754144","Kp":"1.1140558295591576"},{"pair":"Ni-Pd","dlnV":"-0.4","V":"8.805248843492778","Kp":"-9.883789402555356"},{"pair":"Ni-Pd","dlnV":"-0.3","V":"9.731304948247448","Kp":"-5.764275516225519"},{"pair":"Ni-Pd","dlnV":"-0.2","V":"10.754755223728724","Kp":"-7.660059016740398"},{"pair":"Ni-Pd","dlnV":"-0.15","V":"11.306163315305069","Kp":"-2.599140434175154"},{"pair":"Ni-Pd","dlnV":"-0.1","V":"11.88584270428714","Kp":"-4.660094082794948"},{"pair":"Ni-Pd","dlnV":"-0.05","V":"12.49524289108891","Kp":"0.09241133028629749"},{"pair":"Ni-Pd","dlnV":"0.0","V":"13.13588769359976","Kp":"4.562753774539531"},{"pair":"Ni-Pd","dlnV":"0.05","V":"13.809379057522941","Kp":"2.4083383144345927"},{"pair":"Ni-Pd","dlnV":"0.1","V":"14.51740106207425","Kp":"2.478368103831177"},{"pair":"Ni-Pd","dlnV":"0.15","V":"15.26172413105725","Kp":"2.930753846256082"},{"pair":"Ni-Pd","dlnV":"0.2","V":"16.04420945984498","Kp":"3.0071516035429924"},{"pair":"Ni-Pd","dlnV":"0.3","V":"17.731593698534866","Kp":"1.7687540730454956"},{"pair":"Ni-Pd","dlnV":"0.4","V":"19.596441686754144","Kp":"0.8441635562246051"},{"pair":"Ni-Pd","dlnV":"-0.4","V":"8.805248843492778","Kp":"-6.598717333380955"},{"pair":"Ni-Pd","dlnV":"-0.3","V":"9.731304948247448","Kp":"-3.421182557435256"},{"pair":"Ni-Pd","dlnV":"-0.2","V":"10.754755223728724","Kp":"-5.849338540564297"},{"pair":"Ni-Pd","dlnV":"-0.15","V":"11.306163315305069","Kp":"-1.298025511944314"},{"pair":"Ni-Pd","dlnV":"-0.1","V":"11.88584270428714","Kp":"-3.3147345862896467"},{"pair":"Ni-Pd","dlnV":"-0.05","V":"12.49524289108891","Kp":"1.0142702400416803"},{"pair":"Ni-Pd","dlnV":"0.0","V":"13.13588769359976","Kp":"5.000508736101006"},{"pair":"Ni-Pd","dlnV":"0.05","V":"13.809379057522941","Kp":"3.064446091500076"},{"pair":"Ni-Pd","dlnV":"0.1","V":"14.51740106207425","Kp":"3.0231766211774986"},{"pair":"Ni-Pd","dlnV":"0.15","V":"15.26172413105725","Kp":"3.3925795562815586"},{"pair":"Ni-Pd","dlnV":"0.2","V":"16.04420945984498","Kp":"3.408619522236033"},{"pair":"Ni-Pd","dlnV":"0.3","V":"17.731593698534866","Kp":"2.1044200166012295"},{"pair":"Ni-Pd","dlnV":"0.4","V":"19.596441686754144","Kp":"1.0950487332527101"},{"pair":"Ni-Pt","dlnV":"-0.4","V":"8.864377192593277","Kp":"-31.879644204545798"},{"pair":"Ni-Pt","dlnV":"-0.3","V":"9.796651880107143","Kp":"-29.996630427940616"},{"pair":"Ni-Pt","dlnV":"-0.2","V":"10.826974752405532","Kp":"-9.702355409506206"},{"pair":"Ni-Pt","dlnV":"-0.15","V":"11.382085618396895","Kp":"-1.1059011511407741"},{"pair":"Ni-Pt","dlnV":"-0.1","V":"11.965657627097878","Kp":"-0.25522106958144486"},{"pair":"Ni-Pt","dlnV":"-0.05","V":"12.579150012499321","Kp":"5.505081863646287"},{"pair":"Ni-Pt","dlnV":"0.0","V":"13.224096825118638","Kp":"10.222893573014737"},{"pair":"Ni-Pt","dlnV":"0.05","V":"13.90211076792517","Kp":"6.886659143140209"},{"pair":"Ni-Pt","dlnV":"0.1","V":"14.614887228937622","Kp":"6.5559407883873835"},{"pair":"Ni-Pt","dlnV":"0.15","V":"15.364208520577204","Kp":"7.223590378201224"},{"pair":"Ni-Pt","dlnV":"0.2","V":"16.15194833637705","Kp":"6.994497506969158"},{"pair":"Ni-Pt","dlnV":"0.3","V":"17.850663571624253","Kp":"4.755232453804971"},{"pair":"Ni-Pt","dlnV":"0.4","V":"19.728034247711495","Kp":"2.1578600813222404"},{"pair":"Ni-Pt","dlnV":"-0.4","V":"8.864377192593277","Kp":"-40.3300160388979"},{"pair":"Ni-Pt","dlnV":"-0.3","V":"9.796651880107143","Kp":"-34.75039474111878"},{"pair":"Ni-Pt","dlnV":"-0.2","V":"10.826974752405532","Kp":"-13.641960462979812"},{"pair":"Ni-Pt","dlnV":"-0.15","V":"11.382085618396895","Kp":"-3.7576245044995606"},{"pair":"Ni-Pt","dlnV":"-0.1","V":"11.965657627097878","Kp":"-3.644779368657482"},{"pair":"Ni-Pt","dlnV":"-0.05","V":"12.579150012499321","Kp":"3.913296247314613"},{"pair":"Ni-Pt","dlnV":"0.0","V":"13.224096825118638","Kp":"9.943428394417449"},{"pair":"Ni-Pt","dlnV":"0.05","V":"13.90211076792517","Kp":"5.858968613665202"},{"pair":"Ni-Pt","dlnV":"0.1","V":"14.614887228937622","Kp":"5.815014481054659"},{"pair":"Ni-Pt","dlnV":"0.15","V":"15.364208520577204","Kp":"6.655887745516214"},{"pair":"Ni-Pt","dlnV":"0.2","V":"16.15194833637705","Kp":"6.5908958357566085"},{"pair":"Ni-Pt","dlnV":"0.3","V":"17.850663571624253","Kp":"4.545975860833835"},{"pair":"Ni-Pt","dlnV":"0.4","V":"19.728034247711495","Kp":"2.121051011180881"},{"pair":"Ni-Pt","dlnV":"-0.4","V":"8.864377192593277","Kp":"-29.949560065892097"},{"pair":"Ni-Pt","dlnV":"-0.3","V":"9.796651880107143","Kp":"-29.375529308847934"},{"pair":"Ni-Pt","dlnV":"-0.2","V":"10.826974752405532","Kp":"-10.39223251383926"},{"pair":"Ni-Pt","dlnV":"-0.15","V":"11.382085618396895","Kp":"-1.4451057533525844"},{"pair":"Ni-Pt","dlnV":"-0.1","V":"11.965657627097878","Kp":"-1.5601674624710595"},{"pair":"Ni-Pt","dlnV":"-0.05","V":"12.579150012499321","Kp":"5.511969604570851"},{"pair":"Ni-Pt","dlnV":"0.0","V":"13.224096825118638","Kp":"11.235353026628959"},{"pair":"Ni-Pt","dlnV":"0.05","V":"13.90211076792517","Kp":"6.936947007355636"},{"pair":"Ni-Pt","dlnV":"0.1","V":"14.614887228937622","Kp":"6.581907839260563"},{"pair":"Ni-Pt","dlnV":"0.15","V":"15.364208520577204","Kp":"7.203565616899587"},{"pair":"Ni-Pt","dlnV":"0.2","V":"16.15194833637705","Kp":"6.981510214448113"},{"pair":"Ni-Pt","dlnV":"0.3","V":"17.850663571624253","Kp":"4.728573696570143"},{"pair":"Ni-Pt","dlnV":"0.4","V":"19.728034247711495","Kp":"2.171244486730349"},{"pair":"Ni-Rh","dlnV":"-0.4","V":"8.315867115819298","Kp":"-8.109429940718519"},{"pair":"Ni-Rh","dlnV":"-0.3","V":"9.1904544949851","Kp":"-42.376170777499766"},{"pair":"Ni-Rh","dlnV":"-0.2","V":"10.157023031755145","Kp":"-40.43186734791174"},{"pair":"Ni-Rh","dlnV":"-0.15","V":"10.677784738509759","Kp":"-40.761477764006024"},{"pair":"Ni-Rh","dlnV":"-0.1","V":"11.225246468920332","Kp":"-33.41101761164301"},{"pair":"Ni-Rh","dlnV":"-0.05","V":"11.80077716247297","Kp":"-41.35625969488578"},{"pair":"Ni-Rh","dlnV":"0.0","V":"12.405815945682106","Kp":"-35.94363352817949"},{"pair":"Ni-Rh","dlnV":"0.05","V":"13.04187573065639","Kp":"-21.334268840578453"},{"pair":"Ni-Rh","dlnV":"0.1","V":"13.710546998167002","Kp":"-19.928456334471655"},{"pair":"Ni-Rh","dlnV":"0.15","V":"14.413501774678029","Kp":"-16.204513163822327"},{"pair":"Ni-Rh","dlnV":"0.2","V":"15.15249781328354","Kp":"-11.832658524835818"},{"pair":"Ni-Rh","dlnV":"0.3","V":"16.746099919445815","Kp":"-4.810717513733241"},{"pair":"Ni-Rh","dlnV":"0.4","V":"18.507302622160456","Kp":"-1.3297811754860778"},{"pair":"Ni-Rh","dlnV":"-0.4","V":"8.315867115819298","Kp":"-14.262979324179902"},{"pair":"Ni-Rh","dlnV":"-0.3","V":"9.1904544949851","Kp":"-46.22180022888343"},{"pair":"Ni-Rh","dlnV":"-0.2","V":"10.157023031755145","Kp":"-42.860687499139495"},{"pair":"Ni-Rh","dlnV":"-0.15","V":"10.677784738509759","Kp":"-42.86269367487779"},{"pair":"Ni-Rh","dlnV":"-0.1","V":"11.225246468920332","Kp":"-34.83018470269476"},{"pair":"Ni-Rh","dlnV":"-0.05","V":"11.80077716247297","Kp":"-42.713666947541036"},{"pair":"Ni-Rh","dlnV":"0.0","V":"12.405815945682106","Kp":"-37.02009621367784"},{"pair":"Ni-Rh","dlnV":"0.05","V":"13.04187573065639","Kp":"-21.792775802542344"},{"pair":"Ni-Rh","dlnV":"0.1","V":"13.710546998167002","Kp":"-20.450922869796624"},{"pair":"Ni-Rh","dlnV":"0.15","V":"14.413501774678029","Kp":"-16.67367163680125"},{"pair":"Ni-Rh","dlnV":"0.2","V":"15.15249781328354","Kp":"-12.242440553069747"},{"pair":"Ni-Rh","dlnV":"0.3","V":"16.746099919445815","Kp":"-5.182191368303732"},{"pair":"Ni-Rh","dlnV":"0.4","V":"18.507302622160456","Kp":"-1.538183639781703"},{"pair":"Ni-Rh","dlnV":"-0.4","V":"8.315867115819298","Kp":"-7.620262714553684"},{"pair":"Ni-Rh","dlnV":"-0.3","V":"9.1904544949851","Kp":"-40.607738014356656"},{"pair":"Ni-Rh","dlnV":"-0.2","V":"10.157023031755145","Kp":"-38.700810486884755"},{"pair":"Ni-Rh","dlnV":"-0.15","V":"10.677784738509759","Kp":"-38.82246883834688"},{"pair":"Ni-Rh","dlnV":"-0.1","V":"11.225246468920332","Kp":"-31.858859430946534"},{"pair":"Ni-Rh","dlnV":"-0.05","V":"11.80077716247297","Kp":"-39.68390740507361"},{"pair":"Ni-Rh","dlnV":"0.0","V":"12.405815945682106","Kp":"-34.72615990844918"},{"pair":"Ni-Rh","dlnV":"0.05","V":"13.04187573065639","Kp":"-20.91758820244723"},{"pair":"Ni-Rh","dlnV":"0.1","V":"13.710546998167002","Kp":"-19.150362493191086"},{"pair":"Ni-Rh","dlnV":"0.15","V":"14.413501774678029","Kp":"-15.509361439530586"},{"pair":"Ni-Rh","dlnV":"0.2","V":"15.15249781328354","Kp":"-11.269415014134253"},{"pair":"Ni-Rh","dlnV":"0.3","V":"16.746099919445815","Kp":"-4.531516317211947"},{"pair":"Ni-Rh","dlnV":"0.4","V":"18.507302622160456","Kp":"-1.1338593549791052"},{"pair":"Pd-Pt","dlnV":"-0.4","V":"10.349233772873873","Kp":"0.05998826806732331"},{"pair":"Pd-Pt","dlnV":"-0.3","V":"11.437672190146516","Kp":"-1.2241720532385707"},{"pair":"Pd-Pt","dlnV":"-0.2","V":"12.64058267503253","Kp":"-3.7602532350397353"},{"pair":"Pd-Pt","dlnV":"-0.15","V":"13.288679207613223","Kp":"-0.5847989539989429"},{"pair":"Pd-Pt","dlnV":"-0.1","V":"13.970004359976826","Kp":"3.736681692635135"},{"pair":"Pd-Pt","dlnV":"-0.05","V":"14.686261799890675","Kp":"3.4943080637507915"},{"pair":"Pd-Pt","dlnV":"0.0","V":"15.43924254403639","Kp":"3.1299689316272845"},{"pair":"Pd-Pt","dlnV":"0.05","V":"16.23082943648449","Kp":"3.0098759265779917"},{"pair":"Pd-Pt","dlnV":"0.1","V":"17.063001856785295","Kp":"2.770066359158721"},{"pair":"Pd-Pt","dlnV":"0.15","V":"17.93784066944881","Kp":"1.6385865047235189"},{"pair":"Pd-Pt","dlnV":"0.2","V":"18.857533427189885","Kp":"1.3292751090229715"},{"pair":"Pd-Pt","dlnV":"0.3","V":"20.84079753036966","Kp":"0.5283156248122033"},{"pair":"Pd-Pt","dlnV":"0.4","V":"23.032643340067324","Kp":"0.33252341403435315"},{"pair":"Pd-Pt","dlnV":"-0.4","V":"10.349233772873873","Kp":"-0.4813173935534769"},{"pair":"Pd-Pt","dlnV":"-0.3","V":"11.437672190146516","Kp":"-1.7272436708000083"},{"pair":"Pd-Pt","dlnV":"-0.2","V":"12.64058267503253","Kp":"-4.2268374954199315"},{"pair":"Pd-Pt","dlnV":"-0.15","V":"13.288679207613223","Kp":"-0.9674179586692904"},{"pair":"Pd-Pt","dlnV":"-0.1","V":"13.970004359976826","Kp":"3.8034010075653972"},{"pair":"Pd-Pt","dlnV":"-0.05","V":"14.686261799890675","Kp":"3.648719488532899"},{"pair":"Pd-Pt","dlnV":"0.0","V":"15.43924254403639","Kp":"3.338542815887255"},{"pair":"Pd-Pt","dlnV":"0.05","V":"16.23082943648449","Kp":"3.2592978951686042"},{"pair":"Pd-Pt","dlnV":"0.1","V":"17.063001856785295","Kp":"3.0304073635097755"},{"pair":"Pd-Pt","dlnV":"0.15","V":"17.93784066944881","Kp":"1.8980819598806178"},{"pair":"Pd-Pt","dlnV":"0.2","V":"18.857533427189885","Kp":"1.5743271535143037"},{"pair":"Pd-Pt","dlnV":"0.3","V":"20.84079753036966","Kp":"0.719747344516407"},{"pair":"Pd-Pt","dlnV":"0.4","V":"23.032643340067324","Kp":"0.5050670113427894"},{"pair":"Pd-Pt","dlnV":"-0.4","V":"10.349233772873873","Kp":"-0.3826949554546281"},{"pair":"Pd-Pt","dlnV":"-0.3","V":"11.437672190146516","Kp":"-1.680873208192"},{"pair":"Pd-Pt","dlnV":"-0.2","V":"12.64058267503253","Kp":"-4.04024701533224"},{"pair":"Pd-Pt","dlnV":"-0.15","V":"13.288679207613223","Kp":"-0.7868926223188549"},{"pair":"Pd-Pt","dlnV":"-0.1","V":"13.970004359976826","Kp":"3.607403104502879"},{"pair":"Pd-Pt","dlnV":"-0.05","V":"14.686261799890675","Kp":"3.385898652570924"},{"pair":"Pd-Pt","dlnV":"0.0","V":"15.43924254403639","Kp":"3.0187380672365483"},{"pair":"Pd-Pt","dlnV":"0.05","V":"16.23082943648449","Kp":"2.9152138191893915"},{"pair":"Pd-Pt","dlnV":"0.1","V":"17.063001856785295","Kp":"2.698795063073044"},{"pair":"Pd-Pt","dlnV":"0.15","V":"17.93784066944881","Kp":"1.5658881321546287"},{"pair":"Pd-Pt","dlnV":"0.2","V":"18.857533427189885","Kp":"1.2811384274496622"},{"pair":"Pd-Pt","dlnV":"0.3","V":"20.84079753036966","Kp":"0.5043107342062134"},{"pair":"Pd-Pt","dlnV":"0.4","V":"23.032643340067324","Kp":"0.32374404820723574"},{"pair":"Pd-Rh","dlnV":"-0.4","V":"9.800723696099894","Kp":"-23.08154756979195"},{"pair":"Pd-Rh","dlnV":"-0.3","V":"10.831474805024474","Kp":"-15.155377450837916"},{"pair":"Pd-Rh","dlnV":"-0.2","V":"11.970630954382143","Kp":"-21.435915870524315"},{"pair":"Pd-Rh","dlnV":"-0.15","V":"12.584378327726087","Kp":"-15.468228009363449"},{"pair":"Pd-Rh","dlnV":"-0.1","V":"13.229593201799279","Kp":"-9.859576922068605"},{"pair":"Pd-Rh","dlnV":"-0.05","V":"13.907888949864324","Kp":"-7.504277270775159"},{"pair":"Pd-Rh","dlnV":"0.0","V":"14.620961664599857","Kp":"-6.797496650823985"},{"pair":"Pd-Rh","dlnV":"0.05","V":"15.37059439921571","Kp":"-5.712744941517464"},{"pair":"Pd-Rh","dlnV":"0.1","V":"16.158661626014673","Kp":"-4.767636506094518"},{"pair":"Pd-Rh","dlnV":"0.15","V":"16.98713392354963","Kp":"-3.8779983146279537"},{"pair":"Pd-Rh","dlnV":"0.2","V":"17.858082904096374","Kp":"-2.9931944352760564"},{"pair":"Pd-Rh","dlnV":"0.3","V":"19.736233878191218","Kp":"-1.7041061216918898"},{"pair":"Pd-Rh","dlnV":"0.4","V":"21.811911714516288","Kp":"-0.9727194677335769"},{"pair":"Pd-Rh","dlnV":"-0.4","V":"9.800723696099894","Kp":"-23.135014676779385"},{"pair":"Pd-Rh","dlnV":"-0.3","V":"10.831474805024474","Kp":"-15.12191469506648"},{"pair":"Pd-Rh","dlnV":"-0.2","V":"11.970630954382143","Kp":"-21.480557411674177"},{"pair":"Pd-Rh","dlnV":"-0.15","V":"12.584378327726087","Kp":"-15.279813661824194"},{"pair":"Pd-Rh","dlnV":"-0.1","V":"13.229593201799279","Kp":"-9.671533651236846"},{"pair":"Pd-Rh","dlnV":"-0.05","V":"13.907888949864324","Kp":"-7.558850469162353"},{"pair":"Pd-Rh","dlnV":"0.0","V":"14.620961664599857","Kp":"-6.865308300901736"},{"pair":"Pd-Rh","dlnV":"0.05","V":"15.37059439921571","Kp":"-5.737975208445635"},{"pair":"Pd-Rh","dlnV":"0.1","V":"16.158661626014673","Kp":"-4.75776668813945"},{"pair":"Pd-Rh","dlnV":"0.15","V":"16.98713392354963","Kp":"-3.84782394602338"},{"pair":"Pd-Rh","dlnV":"0.2","V":"17.858082904096374","Kp":"-2.900437255029457"},{"pair":"Pd-Rh","dlnV":"0.3","V":"19.736233878191218","Kp":"-1.5723702544372264"},{"pair":"Pd-Rh","dlnV":"0.4","V":"21.811911714516288","Kp":"-0.8280484651898168"},{"pair":"Pd-Rh","dlnV":"-0.4","V":"9.800723696099894","Kp":"-22.10925698554054"},{"pair":"Pd-Rh","dlnV":"-0.3","V":"10.831474805024474","Kp":"-14.950905555575167"},{"pair":"Pd-Rh","dlnV":"-0.2","V":"11.970630954382143","Kp":"-20.977673887361796"},{"pair":"Pd-Rh","dlnV":"-0.15","V":"12.584378327726087","Kp":"-15.579041546270924"},{"pair":"Pd-Rh","dlnV":"-0.1","V":"13.229593201799279","Kp":"-10.157413548055034"},{"pair":"Pd-Rh","dlnV":"-0.05","V":"13.907888949864324","Kp":"-7.371195916688116"},{"pair":"Pd-Rh","dlnV":"0.0","V":"14.620961664599857","Kp":"-6.6724189498477635"},{"pair":"Pd-Rh","dlnV":"0.05","V":"15.37059439921571","Kp":"-5.664354036646686"},{"pair":"Pd-Rh","dlnV":"0.1","V":"16.158661626014673","Kp":"-4.746700470111837"},{"pair":"Pd-Rh","dlnV":"0.15","V":"16.98713392354963","Kp":"-3.8144703139697693"},{"pair":"Pd-Rh","dlnV":"0.2","V":"17.858082904096374","Kp":"-2.991901099909537"},{"pair":"Pd-Rh","dlnV":"0.3","V":"19.736233878191218","Kp":"-1.5989122151778514"},{"pair":"Pd-Rh","dlnV":"0.4","V":"21.811911714516288","Kp":"-0.8847787150057446"},{"pair":"Pt-Rh","dlnV":"-0.4","V":"9.859852045200391","Kp":"-2.297123145969615"},{"pair":"Pt-Rh","dlnV":"-0.3","V":"10.896821736884169","Kp":"13.602218625812638"},{"pair":"Pt-Rh","dlnV":"-0.2","V":"12.042850483058949","Kp":"5.122576327828488"},{"pair":"Pt-Rh","dlnV":"-0.15","V":"12.660300630817911","Kp":"10.716460562886335"},{"pair":"Pt-Rh","dlnV":"-0.1","V":"13.309408124610014","Kp":"12.315060438741497"},{"pair":"Pt-Rh","dlnV":"-0.05","V":"13.991796071274733","Kp":"7.284304020707654"},{"pair":"Pt-Rh","dlnV":"0.0","V":"14.709170796118734","Kp":"5.350644335191342"},{"pair":"Pt-Rh","dlnV":"0.05","V":"15.463326109617936","Kp":"4.3356905573101745"},{"pair":"Pt-Rh","dlnV":"0.1","V":"16.256147792878046","Kp":"2.9630256819875984"},{"pair":"Pt-Rh","dlnV":"0.15","V":"17.089618313069586","Kp":"1.5968157460351364"},{"pair":"Pt-Rh","dlnV":"0.2","V":"17.965821780628442","Kp":"1.7693444657237276"},{"pair":"Pt-Rh","dlnV":"0.3","V":"19.855303751280605","Kp":"0.45472326732433543"},{"pair":"Pt-Rh","dlnV":"0.4","V":"21.943504275473636","Kp":"0.6284406576649421"},{"pair":"Pt-Rh","dlnV":"-0.4","V":"9.859852045200391","Kp":"-2.309548599812124"},{"pair":"Pt-Rh","dlnV":"-0.3","V":"10.896821736884169","Kp":"13.907521310047816"},{"pair":"Pt-Rh","dlnV":"-0.2","V":"12.042850483058949","Kp":"5.25682987125323"},{"pair":"Pt-Rh","dlnV":"-0.15","V":"12.660300630817911","Kp":"11.312076074141475"},{"pair":"Pt-Rh","dlnV":"-0.1","V":"13.309408124610014","Kp":"12.949883066715511"},{"pair":"Pt-Rh","dlnV":"-0.05","V":"13.991796071274733","Kp":"7.782299805374014"},{"pair":"Pt-Rh","dlnV":"0.0","V":"14.709170796118734","Kp":"5.80689547068625"},{"pair":"Pt-Rh","dlnV":"0.05","V":"15.463326109617936","Kp":"4.749995290258106"},{"pair":"Pt-Rh","dlnV":"0.1","V":"16.256147792878046","Kp":"3.329253023869651"},{"pair":"Pt-Rh","dlnV":"0.15","V":"17.089618313069586","Kp":"1.9168046734703392"},{"pair":"Pt-Rh","dlnV":"0.2","V":"17.965821780628442","Kp":"2.0319267109883494"},{"pair":"Pt-Rh","dlnV":"0.3","V":"19.855303751280605","Kp":"0.6686878796909914"},{"pair":"Pt-Rh","dlnV":"0.4","V":"21.943504275473636","Kp":"0.7986038453907146"},{"pair":"Pt-Rh","dlnV":"-0.4","V":"9.859852045200391","Kp":"-2.167902655622681"},{"pair":"Pt-Rh","dlnV":"-0.3","V":"10.896821736884169","Kp":"13.16383161365344"},{"pair":"Pt-Rh","dlnV":"-0.2","V":"12.042850483058949","Kp":"4.614079558984605"},{"pair":"Pt-Rh","dlnV":"-0.15","V":"12.660300630817911","Kp":"10.087888591896709"},{"pair":"Pt-Rh","dlnV":"-0.1","V":"13.309408124610014","Kp":"11.841663546273866"},{"pair":"Pt-Rh","dlnV":"-0.05","V":"13.991796071274733","Kp":"6.9424418871502045"},{"pair":"Pt-Rh","dlnV":"0.0","V":"14.709170796118734","Kp":"5.089584412526836"},{"pair":"Pt-Rh","dlnV":"0.05","V":"15.463326109617936","Kp":"4.110912510408177"},{"pair":"Pt-Rh","dlnV":"0.1","V":"16.256147792878046","Kp":"2.803166929792184"},{"pair":"Pt-Rh","dlnV":"0.15","V":"17.089618313069586","Kp":"1.517925223096464"},{"pair":"Pt-Rh","dlnV":"0.2","V":"17.965821780628442","Kp":"1.6896516619649533"},{"pair":"Pt-Rh","dlnV":"0.3","V":"19.855303751280605","Kp":"0.479130272429511"},{"pair":"Pt-Rh","dlnV":"0.4","V":"21.943504275473636","Kp":"0.6630296797524189"}]}

codex
Mevcut hm verisinde bağımsız spline hesabı K′ artık RMSE’sini 1,892 GPa olarak yeniden üretti. Co’lu grubun ortalama artığı −0,577 GPa; yeni gürültü üreticisi bu ortalamayı beklenen değerde sıfırlıyor. Kanal sırası matematiksel sonucu değiştirmiyor; ancak sıra değiştirildikten sonra eski başlıklı CSV’ye ekleme yapılırsa K44/K′ sütunları sessizce yer değiştirebilir.

exec
"C:\\Users\\can02\\AppData\\Local\\Microsoft\\WindowsApps\\pwsh.exe" -Command '$p='"'C:\\Users\\can02\\.codex\\memories\\rollout_summaries\\2026-10-31T21-44-07-VJVR-validate_k44_shear_transfer_hypotheses.md'; "'$s=Get-Content $p; for ($i=21; $i -lt 34; $i++) { '"'{0}: {1}' -f ("'$i+1),$s[$i] }; (Get-FileHash scripts/k_asym_w1.py).Hash; Get-Item scripts/k_asym_w1.py | Select-Object Length,LastWriteTime' in C:\Users\can02\Projects\AI driven Science
 succeeded in 456ms:
22: ## Task 2: Evaluate astra_2 sampling/direction-averaging hypothesis
23: 
24: Outcome: success
25: 
26: Key steps:
27: - Verified `harness/compute.py` randomizes atoms without SQS optimization; `scripts/k_shear_transfer.py` uses only xy simple shear and target calculations use seed 0.
28: - Recomputed seed scatter. At binary Vegard volumes, the four named pairs reproduce approximately 1.93 GPa K44 SD and 0.45 GPa Kp SD; across the full grid, the four-pair values are about 2.67/1.25 GPa (the proposed 1.93/1.17 values correspond to all-pair averaging).
29: - Ran an additional 108-atom, 36-pair, 3-seed stress check. Deviatoric stress was only 0.17 GPa RMS; K44 seed variation correlated with cell anisotropy (`r=-0.544` against `d sigma_yy`), supporting directional/cell-anisotropy sampling noise rather than the proposed stress confound.
30: - Verified that identical seeds produce identical 50:50 site patterns across element pairs, and seed-0 multicomponent patterns are nested/correlated. Seed 0 averages about 0.50 GPa below the three-seed K44 mean.
31: - Literature search found established work on SQS supercell size/shape effects, cubic projection, and elastic-constant uncertainty: Tasnadi et al. (2012), Tian et al. (2015), Moakher & Norris (2006), and Caro (2014).
32: 
33: Verdict: KEEP; prior = KNOWN. It is a valid numerical/design correction, not a novel physical mechanism. Future K44 tests should vary seeds across rows and average independent shear planes before interpreting the Co/non-Co split. Direction averaging may reduce noise, but cannot by itself explain the full 8�?"10 GPa residuals or the K44/Kp transfer gap.
34: 
1643FE6BF036FDCB6B283055CBBCF317F6A259F7C6CB53F50FE66396A3D2664F

Length LastWriteTime     
------ -------------     
 15456 3.11.2026 13:01:01



codex
**Önceki kritik kol hatası düzelmiş; ancak güç modeli ve ön kayıt bütünlüğü hâlâ eksik.** Denetlediğim betiğin SHA256 başlangıcı `1643fe6bf036fdcb`. Dosya değiştirmedim.

| Önceki madde | Durum | Kanıt ve değerlendirme |
|---|---|---|
| **Kol seçimi** | **Düzeldi** | `arm.split("-")` ve `rep == "sym"` kullanılıyor; `asym` artık simetrik dala girmiyor. Dört kolun ayrışması da kontrol ediliyor. [Satır 199–217](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:199>) |
| **Yan etkili import** | **W1 açısından düzeldi** | `k_shear_transfer` import’u kaldırılmış; hesaplayıcı ilk enerji çağrısında yükleniyor. Ancak W1’in kendisi hâlâ üst düzey hesap/yazım içeriyor; yardımcı modül olarak import edilmeye uygun değil. [Satır 65–79](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:65>) |
| **Kapsam/adlandırma: BV** | **Düzeldi** | İkili **Vegard** hacmi, clamped gözlenebilir ve Wu/Marker’ın yeniden uygulanmadığı açık. H3, aynı asimetrik temsil altında hacim adımını karşılaştırıyor. [Satır 5–24](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:5>) |
| **Hedef başına seed** | **Yeni üretimde düzeldi** | `100+i` kaydedilip hedef üretiminde kullanılıyor. Mevcut COMPS/TGT dosyaları yeniden kullanılırken seed benzersizliği, ≥100 şartı ve kayıtla uyumu doğrulanmıyor. [Satır 132](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:132>), [satır 284](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:284>) |
| **Bileşimsel gürültü ve sınır null’u** | **Kısmen düzeldi; engel sürüyor** | Co/Co-free havuzları ve eşit beklenen hatalı orta-nokta null’u eklenmiş. Fakat artıkların rastgele yeniden dağıtılması ve **±1 ile çarpılması**, sistematik bileşimsel sapmayı siliyor. [Satır 219–249](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:219>) |
| **Ekstrapolasyon ve t aralığı** | **Yeni çekimde düzeldi** | `spread ≤ 0.5`, gerekli hacim farkında `≤0.35`, `extrapolate=False` ve aralık kontrolü mevcut. Eski COMPS okunurken bileşim kısıtları tekrar doğrulanmıyor. [Satır 109–129](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:109>), [satır 176–190](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:176>) |
| **Bileşimle eşleştirme** | **Düzeldi** | Hedefler artık `set_index("comp").loc[...]` ile tahmin sırasına getiriliyor. [Satır 296–298](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:296>) |
| **Ön kayıt hash kontrolü** | **Kısmen düzeldi; engel sürüyor** | Betik hash’i karşılaştırılıyor; **girdi hash’leri kaydedilmiyor/doğrulanmıyor**. `ledger.register()` yalnız betiği hash’liyor. [Satır 252–270](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:252>), [ledger.py:52](<C:/Users/can02/Projects/AI driven Science/harness/ledger.py:52>) |
| **Alt grup raporu** | **Düzeldi** | İki kanalda da all/Co/Co-free için örneklem sayısı ve dört kolun RMSE’si yazdırılıyor. K44 ikincil; üç ana hipotez için `α=0.005/3`. [Satır 300–309](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:300>) |

**Kalan iki önemli engelin somut etkisi:**

- **Gürültü modeli:** Mevcut CSV’lerden bağımsız spline hesabıyla K′ artık RMSE’sini **1,892 GPa** buldum. Co grubunda RMSE **2,419**, ortalama artık **−0,577 GPa**. Satır 238 bu ortalamayı beklenen değerde sıfıra çekiyor; bileşen sayısı/hacim farkıyla ilişkisini de korumuyor. Ayrıca hm hedefleri hâlâ seed 0 kökenli; ikili panel 0–2. Dolayısıyla yeni tasarımın gerçekçi güç koşulu doğrulanmış değil. Sistematik sapmayı koruyan, ayrık seed’li kalibrasyon senaryosu gerekli. Sınır null’unun eklenmesi bu sorunu tek başına çözmüyor.
- **Ön kayıt bütünlüğü:** Ön kayıttan sonra `COMPS`, ikili CSV’ler veya saf-element hacimleri değişirse, betik aynı kaldığı için eski kayıt kabul ediliyor; hedefler ve tahminler değişebiliyor. Girdiler, seed eşlemesi ve ilgili hesap kodu kayıt sırasında sabitlenmeli; devam koşusunda hesap/yazımdan **önce** doğrulanmalı.

**Ek bulgu:** Derece tanısı tamamlanmamış. `x=1/8,7/8` noktaları hesaplanıp CSV’ye yazılıyor; fakat RK tahminiyle karşılaştırılmıyor, tanısal hata raporlanmıyor. [Satır 162–174](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:162>) Üstelik 108 atomda gerçek oranlar yaklaşık **0,12963/0,87037**; gelecekteki karşılaştırma nominal oranlar yerine `xA_actual` kullanmalı.

**Kanal sırası sorusu:** İncelediğim sürümde fark artık yok: `CH=("Kp","K44")`, döngü `CH[::-1]`; dolayısıyla **K44 → Kp**, özgün fonksiyonla aynı. [Satır 94](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:94>)

Sıra ters olsaydı da her deformasyon kopya atomlardan hesaplandığı ve sonuçlar kanal adıyla tutulduğu için matematiksel sonuç değişmezdi. **Ancak CSV’ye devam yazımında değişebilir:** eski başlık `K44,Kp`, yeni sözlük sırası `Kp,K44` olursa `header=False` eklemesi değerleri ters sütunlara yazar. Yazımda açık sütun sırası kullanılmalı. Mevcut çalışma alanında W1 çıktı dosyaları bulunmadığından gerçekleşmiş bir karışma saptamadım.

Python ortamı başlatılamadı; MACE veya uçtan uca W1 çalıştırmadım. Kaynak denetimi ve mevcut hm/ikili verilerinin bellek içi sayısal kontrolünü yaptım.

**VERDICT: NO-GO — ön kayıt ve hedef testine geçmeden önce gürültü modeli ile girdi bütünlüğü tamamlanmalı.**


tokens used
85.546
**Önceki kritik kol hatası düzelmiş; ancak güç modeli ve ön kayıt bütünlüğü hâlâ eksik.** Denetlediğim betiğin SHA256 başlangıcı `1643fe6bf036fdcb`. Dosya değiştirmedim.

| Önceki madde | Durum | Kanıt ve değerlendirme |
|---|---|---|
| **Kol seçimi** | **Düzeldi** | `arm.split("-")` ve `rep == "sym"` kullanılıyor; `asym` artık simetrik dala girmiyor. Dört kolun ayrışması da kontrol ediliyor. [Satır 199–217](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:199>) |
| **Yan etkili import** | **W1 açısından düzeldi** | `k_shear_transfer` import’u kaldırılmış; hesaplayıcı ilk enerji çağrısında yükleniyor. Ancak W1’in kendisi hâlâ üst düzey hesap/yazım içeriyor; yardımcı modül olarak import edilmeye uygun değil. [Satır 65–79](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:65>) |
| **Kapsam/adlandırma: BV** | **Düzeldi** | İkili **Vegard** hacmi, clamped gözlenebilir ve Wu/Marker’ın yeniden uygulanmadığı açık. H3, aynı asimetrik temsil altında hacim adımını karşılaştırıyor. [Satır 5–24](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:5>) |
| **Hedef başına seed** | **Yeni üretimde düzeldi** | `100+i` kaydedilip hedef üretiminde kullanılıyor. Mevcut COMPS/TGT dosyaları yeniden kullanılırken seed benzersizliği, ≥100 şartı ve kayıtla uyumu doğrulanmıyor. [Satır 132](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:132>), [satır 284](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:284>) |
| **Bileşimsel gürültü ve sınır null’u** | **Kısmen düzeldi; engel sürüyor** | Co/Co-free havuzları ve eşit beklenen hatalı orta-nokta null’u eklenmiş. Fakat artıkların rastgele yeniden dağıtılması ve **±1 ile çarpılması**, sistematik bileşimsel sapmayı siliyor. [Satır 219–249](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:219>) |
| **Ekstrapolasyon ve t aralığı** | **Yeni çekimde düzeldi** | `spread ≤ 0.5`, gerekli hacim farkında `≤0.35`, `extrapolate=False` ve aralık kontrolü mevcut. Eski COMPS okunurken bileşim kısıtları tekrar doğrulanmıyor. [Satır 109–129](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:109>), [satır 176–190](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:176>) |
| **Bileşimle eşleştirme** | **Düzeldi** | Hedefler artık `set_index("comp").loc[...]` ile tahmin sırasına getiriliyor. [Satır 296–298](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:296>) |
| **Ön kayıt hash kontrolü** | **Kısmen düzeldi; engel sürüyor** | Betik hash’i karşılaştırılıyor; **girdi hash’leri kaydedilmiyor/doğrulanmıyor**. `ledger.register()` yalnız betiği hash’liyor. [Satır 252–270](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:252>), [ledger.py:52](<C:/Users/can02/Projects/AI driven Science/harness/ledger.py:52>) |
| **Alt grup raporu** | **Düzeldi** | İki kanalda da all/Co/Co-free için örneklem sayısı ve dört kolun RMSE’si yazdırılıyor. K44 ikincil; üç ana hipotez için `α=0.005/3`. [Satır 300–309](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:300>) |

**Kalan iki önemli engelin somut etkisi:**

- **Gürültü modeli:** Mevcut CSV’lerden bağımsız spline hesabıyla K′ artık RMSE’sini **1,892 GPa** buldum. Co grubunda RMSE **2,419**, ortalama artık **−0,577 GPa**. Satır 238 bu ortalamayı beklenen değerde sıfıra çekiyor; bileşen sayısı/hacim farkıyla ilişkisini de korumuyor. Ayrıca hm hedefleri hâlâ seed 0 kökenli; ikili panel 0–2. Dolayısıyla yeni tasarımın gerçekçi güç koşulu doğrulanmış değil. Sistematik sapmayı koruyan, ayrık seed’li kalibrasyon senaryosu gerekli. Sınır null’unun eklenmesi bu sorunu tek başına çözmüyor.
- **Ön kayıt bütünlüğü:** Ön kayıttan sonra `COMPS`, ikili CSV’ler veya saf-element hacimleri değişirse, betik aynı kaldığı için eski kayıt kabul ediliyor; hedefler ve tahminler değişebiliyor. Girdiler, seed eşlemesi ve ilgili hesap kodu kayıt sırasında sabitlenmeli; devam koşusunda hesap/yazımdan **önce** doğrulanmalı.

**Ek bulgu:** Derece tanısı tamamlanmamış. `x=1/8,7/8` noktaları hesaplanıp CSV’ye yazılıyor; fakat RK tahminiyle karşılaştırılmıyor, tanısal hata raporlanmıyor. [Satır 162–174](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:162>) Üstelik 108 atomda gerçek oranlar yaklaşık **0,12963/0,87037**; gelecekteki karşılaştırma nominal oranlar yerine `xA_actual` kullanmalı.

**Kanal sırası sorusu:** İncelediğim sürümde fark artık yok: `CH=("Kp","K44")`, döngü `CH[::-1]`; dolayısıyla **K44 → Kp**, özgün fonksiyonla aynı. [Satır 94](<C:/Users/can02/Projects/AI driven Science/scripts/k_asym_w1.py:94>)

Sıra ters olsaydı da her deformasyon kopya atomlardan hesaplandığı ve sonuçlar kanal adıyla tutulduğu için matematiksel sonuç değişmezdi. **Ancak CSV’ye devam yazımında değişebilir:** eski başlık `K44,Kp`, yeni sözlük sırası `Kp,K44` olursa `header=False` eklemesi değerleri ters sütunlara yazar. Yazımda açık sütun sırası kullanılmalı. Mevcut çalışma alanında W1 çıktı dosyaları bulunmadığından gerçekleşmiş bir karışma saptamadım.

Python ortamı başlatılamadı; MACE veya uçtan uca W1 çalıştırmadım. Kaynak denetimi ve mevcut hm/ikili verilerinin bellek içi sayısal kontrolünü yaptım.

**VERDICT: NO-GO — ön kayıt ve hedef testine geçmeden önce gürültü modeli ile girdi bütünlüğü tamamlanmalı.**


