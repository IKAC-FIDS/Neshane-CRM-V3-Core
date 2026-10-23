# Historical V2 source evidence recovery

## 1. Document control

| Field | Value |
| --- | --- |
| Task | V3-002A — Historical V2 Source Evidence Recovery & Inventory Reconciliation |
| Parent | V3-002 |
| Architecture | `NESHANE-V3-ARCH-P00-002` |
| Governance | `NESHANE-V3-GOV-P00-000A` |
| Historical repository | `https://github.com/IKAC-FIDS/iam-crm-backend` |
| Required commit | `9b918ba8972812c129c8b073e1ac4991023ccbbb` |
| Evidence index | `E:\Neshane-CRM-V2\docs\skill-audit\legacy-evidence.json` |
| Inspection date | 2026-10-23 |
| Verified local source | `E:\nodejs\iam-crm-backend` |
| Outcome | **Historical Source Verified — Inventory Reconciled; Owner Review Pending** |

## 2. Source discovery and revision provenance

Bounded Source Folder discovery inspected the registered Core/V2 projects and relevant locally registered repositories. It found the required repository at `E:\nodejs\iam-crm-backend`. Read-only Git metadata establishes:

- origin: `https://github.com/IKAC-FIDS/iam-crm-backend.git`;
- required object: commit `9b918ba8972812c129c8b073e1ac4991023ccbbb`;
- commit tree: `cebb86260d849e543664c2b894c17ee2460900c3`;
- parent: `ae6f0648844d8aa521dad072dc376be513f45480`;
- subject: `change customer needs config 01`.

The working tree remained on `main` at `c91fb58b98d836ba17c627751c52421a8ba625a2`; it was clean and was not checked out, switched, reset, fetched, pulled, cloned, or modified. Every historical body was read from the required commit with exact-revision Git object access. `E:\nodejs\content-intelligence-backend` was also identified, but its repository identity differs, it does not contain the required object, and it was not used as a substitute. No network access occurred.

## 3. Hash method and verification result

The index field is named `sha256`, and the prior report calls the values content hashes. For every indexed path, SHA-256 was computed over the exact raw bytes returned for `<commit>:<path>` from the local Git object database. No text decoding, newline normalization, checkout conversion, or Git blob-object hashing was used. The observed result empirically establishes that the index algorithm is ordinary SHA-256 over the stored file bytes: all 106 results equal their expected values.

## 4. Coverage summary

| Measure | Count | Meaning |
| --- | ---: | --- |
| Indexed entries | 106 | Entries present in the historical evidence index |
| Available indexed source bodies | 106 | Every indexed path exists at the pinned revision |
| Hash matches | 106 | Expected and observed content SHA-256 are equal |
| Hash mismatches | 0 | No discrepancy found |
| Confirmed missing paths in pinned revision | 0 | Every indexed path resolves in the pinned tree |
| Inaccessible / unverifiable entries | 0 | Every indexed entry was compared |
| Pinned-tree files | 838 | Complete Git tree enumeration at the required commit |
| Unindexed tree files | 732 | Present in the pinned tree but absent from the 106-entry index; grouped in the reconciled inventory |

## 5. 106-entry coverage and hash-verification matrix

Every indexed entry is individually accounted for below. Observed SHA-256 values were computed from exact pinned-revision blob bytes; `Match` is content verification, not a filename-only result.

| # | Indexed path | Expected SHA-256 | Observed SHA-256 | Hash verification | Provenance |
| ---: | --- | --- | --- | --- | --- |
| 1 | `.dockerignore` | `6c46e4e82e91f927773048605bb250603e1bb6cb7b6c30915240edf51538939a` | `6c46e4e82e91f927773048605bb250603e1bb6cb7b6c30915240edf51538939a` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 2 | `docker-compose.yml` | `a0c9b3dfc041a6017fa51abebe3a245f500b2d8d3668aa9961d804fb88b93253` | `a0c9b3dfc041a6017fa51abebe3a245f500b2d8d3668aa9961d804fb88b93253` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 3 | `Dockerfile` | `ea4bf52eb0ca2c4dd46c4ebb5e6077cadb97b3d82534b3cceff5f812d5ffb642` | `ea4bf52eb0ca2c4dd46c4ebb5e6077cadb97b3d82534b3cceff5f812d5ffb642` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 4 | `package.json` | `6230e112f4981355474c985b5d4d70bb2affb6364674fa1413b66c6a6a451d35` | `6230e112f4981355474c985b5d4d70bb2affb6364674fa1413b66c6a6a451d35` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 5 | `prisma/schema.prisma` | `6c49e606e14c38a2814c62c7955734598580b595ef4c3b3636cad30aa7bf19d4` | `6c49e606e14c38a2814c62c7955734598580b595ef4c3b3636cad30aa7bf19d4` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 6 | `src/app.module.ts` | `330068337e2ffd6589c623f3fc5280b62eb415939043555a1a76e6ef0695becf` | `330068337e2ffd6589c623f3fc5280b62eb415939043555a1a76e6ef0695becf` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 7 | `.github/workflows/backend-ci.yml` | `735f726c2eff452d87a883340a4d65262e0f83992bf065bfa8161c8015c86040` | `735f726c2eff452d87a883340a4d65262e0f83992bf065bfa8161c8015c86040` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 8 | `src/audit-log/audit-log.service.ts` | `6ed78056b3348f635bc0d54abd2a98eee49b6c174b71571003bbbcad90fe9ca5` | `6ed78056b3348f635bc0d54abd2a98eee49b6c174b71571003bbbcad90fe9ca5` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 9 | `src/audit-log/audit-request-context.service.ts` | `ddf782be9c9ffdf8e4a6e2f4ae813202d7bfb3a46756ddc51d024535e17bcec3` | `ddf782be9c9ffdf8e4a6e2f4ae813202d7bfb3a46756ddc51d024535e17bcec3` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 10 | `src/auth/account-security.service.ts` | `b70afc0d634b639ebaebef99c82656c721488bc0d79077682b5db83206c66311` | `b70afc0d634b639ebaebef99c82656c721488bc0d79077682b5db83206c66311` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 11 | `src/auth/auth.service.ts` | `2277ffc06524e67508f78e4cbfacb94e3c93a70656e65b3e2155c1b3f8f3cd91` | `2277ffc06524e67508f78e4cbfacb94e3c93a70656e65b3e2155c1b3f8f3cd91` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 12 | `src/auth/refresh-token.service.ts` | `e2a73754d1b1ffee8c05846a8498bfce7008cdb2f64d4aca28d0f4b7bf45c4ac` | `e2a73754d1b1ffee8c05846a8498bfce7008cdb2f64d4aca28d0f4b7bf45c4ac` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 13 | `src/auth/sessions.service.ts` | `a6691ef70bcbf15c19b0a0b1c739b5ede73ff67d5183a1e697031ba366fe9519` | `a6691ef70bcbf15c19b0a0b1c739b5ede73ff67d5183a1e697031ba366fe9519` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 14 | `src/companies/company-registry-lookup.service.ts` | `73f191f6153c434bcedc5233d925502dd152ba1cff9e7262545554917e6d47f7` | `73f191f6153c434bcedc5233d925502dd152ba1cff9e7262545554917e6d47f7` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 15 | `src/crm-assistant/crm-assistant-actions.service.spec.ts` | `4a4685ddcc3abcc7d3cc06289b046af3f09a2cf2c4c7fcc803618580efd00ad3` | `4a4685ddcc3abcc7d3cc06289b046af3f09a2cf2c4c7fcc803618580efd00ad3` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 16 | `src/crm-assistant/crm-assistant-actions.service.ts` | `e12bd1c8bbb17992f5806b0f7699acbef8af0374cde6335e6be2fdaedd8b430a` | `e12bd1c8bbb17992f5806b0f7699acbef8af0374cde6335e6be2fdaedd8b430a` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 17 | `src/crm-assistant/crm-assistant-tools.service.spec.ts` | `8590e4cdcc3d7aa66a5e0eed170aefdde1920ff9c23eea34db307a10016c8cc4` | `8590e4cdcc3d7aa66a5e0eed170aefdde1920ff9c23eea34db307a10016c8cc4` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 18 | `src/crm-assistant/crm-assistant-tools.service.ts` | `644f77b8dc8dead160ac9e7525b7bc7a856ee5c733421290bb0b15643a9875d1` | `644f77b8dc8dead160ac9e7525b7bc7a856ee5c733421290bb0b15643a9875d1` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 19 | `src/crm-assistant/crm-assistant.controller.ts` | `7768f473071c83c86c45dd7a58301171860e8c9c0f1bb5e4151b8e832ac91b36` | `7768f473071c83c86c45dd7a58301171860e8c9c0f1bb5e4151b8e832ac91b36` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 20 | `src/crm-assistant/crm-assistant.module.ts` | `2396acf676917493531e03d0c38100dcceb61a8808b7e69f8c2f27157a29c003` | `2396acf676917493531e03d0c38100dcceb61a8808b7e69f8c2f27157a29c003` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 21 | `src/crm-assistant/crm-assistant.service.spec.ts` | `6af11ec7cdad47103807bf002e7243e0b2de6f72290d4e654ef1ea89a79fa87c` | `6af11ec7cdad47103807bf002e7243e0b2de6f72290d4e654ef1ea89a79fa87c` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 22 | `src/crm-assistant/crm-assistant.service.ts` | `66ce8e3aac042e18aa9a37aa30637b520ac602b4167f3493d871fb905768237c` | `66ce8e3aac042e18aa9a37aa30637b520ac602b4167f3493d871fb905768237c` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 23 | `src/crm-assistant/crm-mcp-gateway.service.spec.ts` | `afae11e80f1f93d42bac7942cc68661d7e257b115d4ad4d511953bfad01d67df` | `afae11e80f1f93d42bac7942cc68661d7e257b115d4ad4d511953bfad01d67df` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 24 | `src/crm-assistant/crm-mcp-gateway.service.ts` | `2efea2c039cbcaa75a84ad34bffcf3511f554c013e4f5364f15bf508bc008573` | `2efea2c039cbcaa75a84ad34bffcf3511f554c013e4f5364f15bf508bc008573` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 25 | `src/crm-assistant/crm-mcp.controller.ts` | `a60bdcc76210c69e0f9d0524690bf1f48fb3c5f80e8dc2bc1158642f1dde2086` | `a60bdcc76210c69e0f9d0524690bf1f48fb3c5f80e8dc2bc1158642f1dde2086` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 26 | `src/customer-requests/customer-request-operations.service.ts` | `d98acdd64d4d177d4b3380cf2c30ef04dbf0d14f653554b1db6819d083ae747d` | `d98acdd64d4d177d4b3380cf2c30ef04dbf0d14f653554b1db6819d083ae747d` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 27 | `src/customer-requests/customer-requests.service.ts` | `3fcea5f065e1a5849602cb82fc027d10c385c529872dcb4f1b9db1c0946a6e63` | `3fcea5f065e1a5849602cb82fc027d10c385c529872dcb4f1b9db1c0946a6e63` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 28 | `src/entitlements/entitlement.service.ts` | `b90a8ef442bd7602e8e484d5be8b52ff8ade20c8cb397938a07e93a28145d1f0` | `b90a8ef442bd7602e8e484d5be8b52ff8ade20c8cb397938a07e93a28145d1f0` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 29 | `src/entitlements/platform-entitlements.service.ts` | `66159dad717c97a09f3c5bc6af433ba3b4602cff9118bfbd76975cb1748d2708` | `66159dad717c97a09f3c5bc6af433ba3b4602cff9118bfbd76975cb1748d2708` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 30 | `src/notification-core/index.ts` | `6c094e2e84ae8337710e2b7871bd0e11a91e203cce486ff5f67be79b9b906399` | `6c094e2e84ae8337710e2b7871bd0e11a91e203cce486ff5f67be79b9b906399` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 31 | `src/notification-core/notification-admin.controller.ts` | `44537103638ea762caf002662587b67ca2bd3bd472018252734e418a7da7c030` | `44537103638ea762caf002662587b67ca2bd3bd472018252734e418a7da7c030` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 32 | `src/notification-core/notification-admin.service.ts` | `1213adc30769588e440325ae985577e7b9f5e20440a453f57a209f7516b90480` | `1213adc30769588e440325ae985577e7b9f5e20440a453f57a209f7516b90480` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 33 | `src/notification-core/notification-channel-handler.ts` | `0c3e5d4f3a34b5acf05657013d4ee74b352624d26698d3c05348e9ac5a8e36e7` | `0c3e5d4f3a34b5acf05657013d4ee74b352624d26698d3c05348e9ac5a8e36e7` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 34 | `src/notification-core/notification-core.catalog.ts` | `631daa2267683bfb21e22fe67b39fa439000537e98c50fe63e6545dde70d7c0c` | `631daa2267683bfb21e22fe67b39fa439000537e98c50fe63e6545dde70d7c0c` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 35 | `src/notification-core/notification-core.module.ts` | `114464a9472eed8551233a742c414c1546de5cb53bb3a357cf7bc2104dd778df` | `114464a9472eed8551233a742c414c1546de5cb53bb3a357cf7bc2104dd778df` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 36 | `src/notification-core/notification-core.service.ts` | `048685bb34caea8d88407f18cc21f16499b740459bf14411bc9f92940b7596f4` | `048685bb34caea8d88407f18cc21f16499b740459bf14411bc9f92940b7596f4` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 37 | `src/notification-core/notification-core.types.ts` | `1384059665796262b98c5f7826aef7334bf9eab0ebd901955ad1497e4bc3f640` | `1384059665796262b98c5f7826aef7334bf9eab0ebd901955ad1497e4bc3f640` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 38 | `src/notification-core/notification-delivery-dispatcher.service.ts` | `4dcfefb51f0f4eb9cf2ed9186d610c7bcd6180ba23d3cddfb4c604cc6fb99bdf` | `4dcfefb51f0f4eb9cf2ed9186d610c7bcd6180ba23d3cddfb4c604cc6fb99bdf` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 39 | `src/notification-core/notification-rule-engine.service.ts` | `9eed8f9f509d55390d83dc44a839a7a92190e2848fc3e643dd8944642f723da4` | `9eed8f9f509d55390d83dc44a839a7a92190e2848fc3e643dd8944642f723da4` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 40 | `src/notification-core/notification-rules.controller.ts` | `4c309b20278b89deb36befa7e37ad14dc5b0f73d78c913b6071ef3078081d84e` | `4c309b20278b89deb36befa7e37ad14dc5b0f73d78c913b6071ef3078081d84e` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 41 | `src/notification-core/notification-rules.service.ts` | `4625735a7021675153d8ae72c56cc28c5cdd3657ec1f04ce7204891fcc795564` | `4625735a7021675153d8ae72c56cc28c5cdd3657ec1f04ce7204891fcc795564` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 42 | `src/notification-core/notification-template-engine.service.ts` | `06f3f285cb5cc22c468205d8ed5b0b3166fab15c752030fe8fa9cab44602b95f` | `06f3f285cb5cc22c468205d8ed5b0b3166fab15c752030fe8fa9cab44602b95f` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 43 | `src/organization-memberships/organization-memberships.service.ts` | `986e7416fb00409d2e4109edf238f48f5c9335c7846b574e3e703d50dd3e22d4` | `986e7416fb00409d2e4109edf238f48f5c9335c7846b574e3e703d50dd3e22d4` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 44 | `src/organization-memberships/tenant-rbac.service.ts` | `0f0fd616b4d9ee3e7bb2d4ef1cc7d213bc03017c65bee3a0bf67a3e118e21888` | `0f0fd616b4d9ee3e7bb2d4ef1cc7d213bc03017c65bee3a0bf67a3e118e21888` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 45 | `src/organization-memberships/tenant-resolver.service.ts` | `3654722d8f4d46fe0ab49d8ddf495f875772b0131221cc150377055cd1ef82e1` | `3654722d8f4d46fe0ab49d8ddf495f875772b0131221cc150377055cd1ef82e1` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 46 | `src/organizations/organization-configuration.service.ts` | `a91add37c1c5782af80c9e4765f1815a06ff6375a6ca851622e53ed3f9003f23` | `a91add37c1c5782af80c9e4765f1815a06ff6375a6ca851622e53ed3f9003f23` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 47 | `src/organizations/organization-domain-verification.service.ts` | `390e8f88352d2563f7f1b468c26e1979be4b7eacdeb7fc30bf82f6ecdf74478b` | `390e8f88352d2563f7f1b468c26e1979be4b7eacdeb7fc30bf82f6ecdf74478b` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 48 | `src/organizations/organizations.service.ts` | `ef3aea08081b462e4d756ff1feae386cb906e7027ee80727c8f312c71ed5b216` | `ef3aea08081b462e4d756ff1feae386cb906e7027ee80727c8f312c71ed5b216` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 49 | `src/prisma/prisma.service.ts` | `0b47af43a2d7a35b0c9748bf10dca859646691a0618c015a7480351fd8e3cf59` | `0b47af43a2d7a35b0c9748bf10dca859646691a0618c015a7480351fd8e3cf59` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 50 | `src/quota/platform-quota.service.ts` | `f8657bd7cc16e2334d9c51fba0077221d15208c32301675cd350f7c0b141c48b` | `f8657bd7cc16e2334d9c51fba0077221d15208c32301675cd350f7c0b141c48b` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 51 | `src/quota/quota-resolver.service.ts` | `ca2aa250ec586b1de515692c68c1332266f210566be02ada3a625fe03b37de9c` | `ca2aa250ec586b1de515692c68c1332266f210566be02ada3a625fe03b37de9c` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 52 | `src/quota/quota-scheduler.service.ts` | `ebcaa8b7ce2f0565babc90e236d1752da9bd1a9c44d53ae0ceca6fd58cbd2f85` | `ebcaa8b7ce2f0565babc90e236d1752da9bd1a9c44d53ae0ceca6fd58cbd2f85` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 53 | `src/quota/quota.service.ts` | `69b59c2d5caf2cd3422f09b1bb8c3192953db7a5430099ec1d0cd4222346791a` | `69b59c2d5caf2cd3422f09b1bb8c3192953db7a5430099ec1d0cd4222346791a` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 54 | `src/quota/usage-reconciliation.service.ts` | `ab8f27bc22a7ffd3c298616930efb1d7374ef06504e83ff4d255dd82d072ea30` | `ab8f27bc22a7ffd3c298616930efb1d7374ef06504e83ff4d255dd82d072ea30` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 55 | `src/auth/passkeys/passkeys.service.ts` | `65bc468829dd80a74099e3a241b6b66cefbeb8dd8ac1427acde9d4fc0c28a299` | `65bc468829dd80a74099e3a241b6b66cefbeb8dd8ac1427acde9d4fc0c28a299` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 56 | `src/auth/sso/oidc.service.ts` | `d41753f8563fa9ddbc2c18ee59242c8ba4e2eef9701dede3d685e99b936d8fb9` | `d41753f8563fa9ddbc2c18ee59242c8ba4e2eef9701dede3d685e99b936d8fb9` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 57 | `src/auth/sso/saml.service.ts` | `d23518cf7cb584e0446e6159bd2213cb06c90d0765ce32f069b5b0d91d0bf010` | `d23518cf7cb584e0446e6159bd2213cb06c90d0765ce32f069b5b0d91d0bf010` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 58 | `src/auth/sso/sso-network-security.service.ts` | `bb5eaf53a1888278372875c423d0c576ff6da22fd0a1b30cdce151f2f8ce39ab` | `bb5eaf53a1888278372875c423d0c576ff6da22fd0a1b30cdce151f2f8ce39ab` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 59 | `src/auth/sso/sso-provider.service.ts` | `70264203eaac7b0a7f96d4a306f7685521a02b81ef816a13ddcbdaa7113e88c6` | `70264203eaac7b0a7f96d4a306f7685521a02b81ef816a13ddcbdaa7113e88c6` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 60 | `src/auth/sso/sso-secret.service.ts` | `43a90af64d146ae05c80219902f7352ca4827ed0e72e09e0df93df2578044401` | `43a90af64d146ae05c80219902f7352ca4827ed0e72e09e0df93df2578044401` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 61 | `src/auth/sso/sso-ticket.service.ts` | `f6bf29db5e915914e7a30c34dce43b5179366689aad43a69c79778e74ad5adbe` | `f6bf29db5e915914e7a30c34dce43b5179366689aad43a69c79778e74ad5adbe` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 62 | `src/auth/sso/crypto/secret-encryption.service.ts` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 63 | `src/crm-assistant/dto/ask-crm-assistant.dto.ts` | `54919a034bae4475f4de5d17fce72e5dd2835acf96930bf3e1f4d3876bced1f7` | `54919a034bae4475f4de5d17fce72e5dd2835acf96930bf3e1f4d3876bced1f7` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 64 | `src/crm-assistant/dto/confirm-crm-assistant-action.dto.ts` | `27dad6ade93e2f80112b25e5b5bdcd9fb84f789b8b2e94fd6b3591082b565d2c` | `27dad6ade93e2f80112b25e5b5bdcd9fb84f789b8b2e94fd6b3591082b565d2c` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 65 | `src/notification-core/audit/notification-delivery-audit.service.ts` | `893a928a1c26d3de95015d7f2671bac983698e8b8d4f6d28908626962386342a` | `893a928a1c26d3de95015d7f2671bac983698e8b8d4f6d28908626962386342a` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 66 | `src/notification-core/deduplication/notification-deduplication-key.service.ts` | `0fd397336601ff77e020110daeb3b334cb90d8277fc8c2d2e05f6af232f0f534` | `0fd397336601ff77e020110daeb3b334cb90d8277fc8c2d2e05f6af232f0f534` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 67 | `src/notification-core/deduplication/notification-delivery.service.ts` | `b715aef62306574712af35f642acd5b378a2d206edbbacf09540177f6ad310e4` | `b715aef62306574712af35f642acd5b378a2d206edbbacf09540177f6ad310e4` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 68 | `src/notification-core/dto/notification-admin.dto.ts` | `c4348cd67a1536666a0823bd3b3ee48487f93c32b313615ab080f12ad3bce22d` | `c4348cd67a1536666a0823bd3b3ee48487f93c32b313615ab080f12ad3bce22d` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 69 | `src/notification-core/dto/notification-orchestration.dto.ts` | `86168d698c2630c9d8d0571f73c45a0f365ceb2c96ed20f85a54ba72d612ce7f` | `86168d698c2630c9d8d0571f73c45a0f365ceb2c96ed20f85a54ba72d612ce7f` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 70 | `src/notification-core/dto/notification-rule.dto.ts` | `98348634e3c7c75c1c75fa0ea37f363996b390dfdec76bf5c6c31aa8998539fd` | `98348634e3c7c75c1c75fa0ea37f363996b390dfdec76bf5c6c31aa8998539fd` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 71 | `src/notification-core/email/email-notification-channel.handler.ts` | `402827bfcd09e25f70e038f19a1f4eb90cf53979bd9cde70b0ed9a42d6d3e5a2` | `402827bfcd09e25f70e038f19a1f4eb90cf53979bd9cde70b0ed9a42d6d3e5a2` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 72 | `src/notification-core/in-app/in-app-notification-channel.handler.ts` | `5049bdba4e6397e04779653f12705ee134628acd5b80dbad43e680ed0c4f25d4` | `5049bdba4e6397e04779653f12705ee134628acd5b80dbad43e680ed0c4f25d4` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 73 | `src/notification-core/in-app/notification-action-url.resolver.ts` | `c25a60501aa5683265efc4aac1bcb7fb53695a0e78db871c14e24d1a4a2cb9de` | `c25a60501aa5683265efc4aac1bcb7fb53695a0e78db871c14e24d1a4a2cb9de` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 74 | `src/notification-core/in-app/notification-tenant-context.ts` | `f1ee25bd19375b17d4ee9e57953f29254a8cdc7c528a82311ca29814485a44b0` | `f1ee25bd19375b17d4ee9e57953f29254a8cdc7c528a82311ca29814485a44b0` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 75 | `src/notification-core/orchestration/notification-digest-renderer.service.ts` | `46aa3c4f2f237d17fee0b941dfca6e2e23597848f80867c4e47515195b3bcb2b` | `46aa3c4f2f237d17fee0b941dfca6e2e23597848f80867c4e47515195b3bcb2b` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 76 | `src/notification-core/orchestration/notification-escalation.service.ts` | `1969be4afab48cb21bd372306a59f050505463d33854f09f244bad1dcf08c702` | `1969be4afab48cb21bd372306a59f050505463d33854f09f244bad1dcf08c702` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 77 | `src/notification-core/orchestration/notification-orchestration.service.ts` | `d1f12b3153a4c65bd03d7bd211a3dc68359283aec2c418773761c756ff81aea0` | `d1f12b3153a4c65bd03d7bd211a3dc68359283aec2c418773761c756ff81aea0` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 78 | `src/notification-core/orchestration/notification-policy-admin.controller.ts` | `4f19097f3f1fc05cde02229a7cfddbd011967f4c6d9790031a7d5e3abf254b44` | `4f19097f3f1fc05cde02229a7cfddbd011967f4c6d9790031a7d5e3abf254b44` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 79 | `src/notification-core/orchestration/notification-policy-admin.service.ts` | `a67c4b2c69edd05d380da6d95c7086060a42820a5c749796689fcb72d61b446b` | `a67c4b2c69edd05d380da6d95c7086060a42820a5c749796689fcb72d61b446b` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 80 | `src/notification-core/orchestration/notification-time-window.ts` | `69fd872c5633bfec725b0d0f96132774252290eb41453f44fcf77f3bc356376c` | `69fd872c5633bfec725b0d0f96132774252290eb41453f44fcf77f3bc356376c` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 81 | `src/notification-core/policy/notification-condition.catalog.ts` | `961dbd4407f67443272d0d6a134214cf04018960e401934dbd24e55d7f35b1da` | `961dbd4407f67443272d0d6a134214cf04018960e401934dbd24e55d7f35b1da` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 82 | `src/notification-core/policy/notification-policy-condition-validator.service.ts` | `7cb2774a118955553d86fe2645d184a2991213e15e40ac46b829d54c8554930c` | `7cb2774a118955553d86fe2645d184a2991213e15e40ac46b829d54c8554930c` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 83 | `src/notification-core/policy/notification-policy-context-builder.service.ts` | `7b2888b549405af3f539341366604590938d4b81ffc55a2533174c062c8af90a` | `7b2888b549405af3f539341366604590938d4b81ffc55a2533174c062c8af90a` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 84 | `src/notification-core/policy/notification-policy-evaluator.service.ts` | `22e9ff49fc5c3079ff2eb599916db429f1cd1ad99c44e9c9f4a6328b668b8b73` | `22e9ff49fc5c3079ff2eb599916db429f1cd1ad99c44e9c9f4a6328b668b8b73` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 85 | `src/notification-core/policy/notification-policy-field-resolver.ts` | `6cba2d6659bcf8dd0e45397b2d3af34389a68cc2f4b99de0e5f4dabc2af92f40` | `6cba2d6659bcf8dd0e45397b2d3af34389a68cc2f4b99de0e5f4dabc2af92f40` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 86 | `src/notification-core/policy/notification-policy.types.ts` | `2a4ea782c76927016e5576bb11dcfe9da09cd81cc6b08ac8e8964e350f45da89` | `2a4ea782c76927016e5576bb11dcfe9da09cd81cc6b08ac8e8964e350f45da89` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 87 | `src/notification-core/push/push-notification-channel.handler.ts` | `6bb29c3fd6196e2007793b61771fd3142a762eaef4ba954904235e52481cc2c3` | `6bb29c3fd6196e2007793b61771fd3142a762eaef4ba954904235e52481cc2c3` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 88 | `src/notification-core/push/push-provider.registry.ts` | `9a912bc75eb7bc0e4f626fdb1108b9d0bb61ca648b85976e72b4ff937efafc5d` | `9a912bc75eb7bc0e4f626fdb1108b9d0bb61ca648b85976e72b4ff937efafc5d` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 89 | `src/notification-core/push/push-settings.service.ts` | `96383e845f82f7589902b0ae1993ffc5edf35d460bead5ff1de81582d07e97a4` | `96383e845f82f7589902b0ae1993ffc5edf35d460bead5ff1de81582d07e97a4` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 90 | `src/notification-core/push/push.controller.ts` | `abb4e5222d8b048baf195e195fe1833e6cacde8c475670885086d2a0ea2abdd7` | `abb4e5222d8b048baf195e195fe1833e6cacde8c475670885086d2a0ea2abdd7` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 91 | `src/notification-core/push/push.types.ts` | `ff53717822f75b437e0e489537480d979763223e223414dd1678b0a1e84134a0` | `ff53717822f75b437e0e489537480d979763223e223414dd1678b0a1e84134a0` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 92 | `src/notification-core/push/web-push.provider.ts` | `4ae1a67e3f52d0c61dd76e1c312a3f09c32b90d2906df640885f769ab3a1f2da` | `4ae1a67e3f52d0c61dd76e1c312a3f09c32b90d2906df640885f769ab3a1f2da` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 93 | `src/notification-core/queue/notification-delivery-queue.service.ts` | `6ae0949cb79a9aabfac6f2b509d0804aa668763d29573c1521da7009f91e8a1c` | `6ae0949cb79a9aabfac6f2b509d0804aa668763d29573c1521da7009f91e8a1c` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 94 | `src/notification-core/queue/notification-delivery-worker.service.ts` | `d9edecd659bdc6fd8c1f47bb7cd232ad5cfc9f23b76274bba4be9f288c02b81d` | `d9edecd659bdc6fd8c1f47bb7cd232ad5cfc9f23b76274bba4be9f288c02b81d` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 95 | `src/notification-core/schedule/notification-schedule-validator.service.ts` | `f3eadeb82d9dd6e59627268e711da0dc4ee990dcf86b264a14ee6400ad0eb5ba` | `f3eadeb82d9dd6e59627268e711da0dc4ee990dcf86b264a14ee6400ad0eb5ba` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 96 | `src/notification-core/schedule/notification-schedule.catalog.ts` | `7b9dba85e09fdd1a84a1bedf9bfdcd09b016e0abe4aa25207b21f86178b76d54` | `7b9dba85e09fdd1a84a1bedf9bfdcd09b016e0abe4aa25207b21f86178b76d54` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 97 | `src/notification-core/schedule/notification-scheduler.service.ts` | `ede7080445e6fd2f762a83dee88bd99d04a64a7dcf00cd69950528aa0e1fdbc6` | `ede7080445e6fd2f762a83dee88bd99d04a64a7dcf00cd69950528aa0e1fdbc6` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 98 | `src/notification-core/sms/generic-http-sms.provider.ts` | `2a3791cb305115f22ad3419927ff220d3f9b5398ff1c2ec2659fff600b1bfd30` | `2a3791cb305115f22ad3419927ff220d3f9b5398ff1c2ec2659fff600b1bfd30` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 99 | `src/notification-core/sms/sms-admin.controller.ts` | `06c5906362312af5d014b41966e34ef5a531ef910590eb6431afb3af1feb596f` | `06c5906362312af5d014b41966e34ef5a531ef910590eb6431afb3af1feb596f` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 100 | `src/notification-core/sms/sms-notification-channel.handler.ts` | `fcc97d66f65dfc9c9ea2744d8dd33389e48435fc3faec972486ad599dbdd2691` | `fcc97d66f65dfc9c9ea2744d8dd33389e48435fc3faec972486ad599dbdd2691` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 101 | `src/notification-core/sms/sms-provider.registry.ts` | `11913bb33c8ca18af11cd13694fa697ba54e9a5d412e78f2a1abd97a959248ea` | `11913bb33c8ca18af11cd13694fa697ba54e9a5d412e78f2a1abd97a959248ea` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 102 | `src/notification-core/sms/sms-recipient-resolver.service.ts` | `ce92bb75728d33cfb50f2b3ba4c94199264966775b62e4319f2cd5110b33ae9e` | `ce92bb75728d33cfb50f2b3ba4c94199264966775b62e4319f2cd5110b33ae9e` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 103 | `src/notification-core/sms/sms-settings.service.ts` | `2c89dcac7f693de07fe815a1baaab02d4eff37b74d5c6a2e3a30070c90c911ec` | `2c89dcac7f693de07fe815a1baaab02d4eff37b74d5c6a2e3a30070c90c911ec` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 104 | `src/notification-core/sms/sms.types.ts` | `429f8532b79fb616ced1b50955a34d029a0a25b0214022fd55ce7c801a458aba` | `429f8532b79fb616ced1b50955a34d029a0a25b0214022fd55ce7c801a458aba` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 105 | `src/notification-core/push/dto/push.dto.ts` | `2982f505bcf967015ef36471f4bf15884750fa51e82272c99d0d14e119244ab8` | `2982f505bcf967015ef36471f4bf15884750fa51e82272c99d0d14e119244ab8` | Match | Exact Git blob at pinned commit; compared with V2 index |
| 106 | `src/notification-core/sms/dto/sms-settings.dto.ts` | `227b06536d12c834378637e124b2b22b34bf2b3f7e94337b23c71e0dfec42ab8` | `227b06536d12c834378637e124b2b22b34bf2b3f7e94337b23c71e0dfec42ab8` | Match | Exact Git blob at pinned commit; compared with V2 index |

## 6. Historical capability assessment

The following are static findings from the pinned source, not runtime validation:

| Capability | Confirmed historical implementation evidence | Assessment |
| --- | --- | --- |
| Identity, sessions and tenant switching | Password login/lockout/audit, tenant-aware JWT payloads, refresh-session lookup/rotation/revocation and tenant-switch rotation (`src/auth/auth.service.ts:69-209,259-280,333-423`; `src/auth/refresh-token.service.ts:75-203,448-491`) | Business/security semantics are salvage candidates; implementation must be rewritten for V3 trust decisions. |
| OIDC, SAML and SSO | Persisted one-time OIDC transactions with nonce/PKCE, provider-organization binding, membership checks and public-URL validation; SAML issuer/audience and transaction consumption; tenant-scoped provider administration (`src/auth/sso/oidc.service.ts:68-122,170-249,298-333`; `src/auth/sso/saml.service.ts:223-245,512-548`; `src/auth/sso/sso-provider.service.ts:62-84,260-320,398-444`) | Confirmed source design; provider configuration and production protocol behavior remain unverified. |
| Passkeys | WebAuthn challenge flow exists, but challenge state uses process-local `NodeCache` (`src/auth/passkeys/passkeys.service.ts:11,28,170`) | Probable multi-instance/restart weakness; rewrite challenge lifecycle. |
| Tenant, Organization and Membership | Active membership is resolved into tenant context; tenant RBAC and organization-scoped queries are implemented (`src/organization-memberships/tenant-resolver.service.ts`; `src/organization-memberships/tenant-rbac.service.ts`; `src/organization-memberships/organization-memberships.service.ts`) | Semantics are useful, but shared NestJS/Prisma composition is not a V3 ownership model. |
| Notification | Tenant-scoped templates/rules, policy evaluation, schedules, digest/escalation, email/SMS/push/in-app channels, idempotent events, deduplicated deliveries, queue retry and delivery audit exist (`src/notification-core/notification-core.service.ts:24-56`; `src/notification-core/notification-delivery-dispatcher.service.ts:20-37`; `src/notification-core/notification-admin.service.ts:38-265`) | Rich behavior is confirmed; provider behavior, delivery guarantees and operations remain runtime-unverified. |
| Linka/external registry | Company registry lookup and reviewed-draft/provenance path exist (`src/companies/company-registry-lookup.service.ts`; `src/companies/companies.controller.ts:89-104`) | Keep NEEDS_REVIEW until sanitized provider contract, retention and failure semantics are available. |
| Customer requests | Tenant-scoped request workflow and history are implemented (`src/customer-requests/customer-requests.service.ts`; `src/customer-requests/customer-requests.controller.ts`) | Source confirms a workflow candidate; aggregate ownership remains an owner decision. |
| Audit | Tenant/platform scopes, request context, permissioned admin routes, export and retention/archive maintenance are present (`src/audit-log/audit-log.service.ts:51-169,266-344`; `src/audit-log/audit-log-maintenance.ts:6-77`) | Useful semantics; runtime immutability, retention and privileged access are not proved. |
| Quota and entitlement | Resolution, reservation/reconciliation/scheduling and entitlement evaluation services are present (`src/quota/quota.service.ts`; `src/quota/quota-resolver.service.ts`; `src/quota/usage-reconciliation.service.ts`; `src/entitlements/entitlement.service.ts`) | Source confirms behavior, but policy ownership and V3 service placement remain open. |
| AI and reporting | Permission-aware CRM tools, deterministic report paths, proposal/confirmation actions and report modules exist (`src/crm-assistant/crm-assistant-tools.service.ts`; `src/crm-assistant/crm-assistant-actions.service.ts`; `src/reports/`) | Product scope and approval/replay model remain owner decisions; no model quality or runtime claim. |
| Other business capabilities | Companies/people, opportunities/product catalog, tasks/meetings/timesheets/collaboration, attachments/artifacts, portal access, technical center, administration/lookups and operations are present under their corresponding `src/` roots | Newly established first-party historical assets are grouped as V2-AST-037 through V2-AST-046 in the parent inventory. |

The pinned tree contains 838 files: 542 under `src/`, 101 under `prisma/` (including 97 SQL migrations), 126 under `test/`, 31 under `docs/`, and 38 other repository/configuration files. The 106-entry index is therefore a curated evidence subset, not a complete repository manifest. The additional 732 paths were enumerated and classified by first-party root/capability; they were not all subjected to the per-file hash comparison because no expected index values exist for them.

## 7. Security and architecture review result

- Source confirms refresh-token hashing/rotation/revocation and tenant re-resolution, but static inspection cannot prove race safety or production revocation behavior (`src/auth/refresh-token.service.ts:75-203`).
- JWT validation requires expiration and audience and re-resolves membership; the inspected strategy does not visibly pin issuer or an algorithm allowlist, which is a **probable static gap**, not an exploitability claim (`src/auth/jwt.strategy.ts:41-70`).
- Passkey challenges are process-local, so restart/multi-instance correctness requires redesign (`src/auth/passkeys/passkeys.service.ts:11,28`).
- OIDC URL validation and tenant/provider/membership binding are directly present; tests statically cover HTTP, loopback, link-local, private-address and userinfo denial (`test/tenant-scoped-sso.spec.ts:62-218`).
- Tenant-scoped tests cover missing context, spoofing resistance, non-enumerating cross-tenant access and denial before object storage (`test/tenant-scope-enforcement.spec.ts:25-229`). Tests were read, not run.
- The historical application is a shared NestJS/TypeScript/Prisma repository with broad shared schema/module coupling. It is implementation-incompatible with ADR-V3-001 and cannot establish ADR-V3-002 service/data ownership merely from directory names.
- Source patterns for tenant context, domain checks, delivery idempotency and audit are candidate requirements only. They do not establish PostgreSQL RLS effectiveness, outbox/inbox runtime guarantees, production security, any mandatory deployment profile, or readiness.
- ADR-V3-001 through ADR-V3-012 remain authoritative and unchanged. OD-001 through OD-023 remain Open.

## 8. Reconciliation with existing Asset IDs

| Asset ID | V3-002 state | V3-002A reconciliation | Confidence change | Disposition change |
| --- | --- | --- | --- | --- |
| V2-AST-030 | RETAIN; metadata index confirmed | 106/106 paths and content hashes verified at exact commit | Metadata-only → source-verified index | None |
| V2-AST-031 | NEEDS_REVIEW; Identity source unverified | Identity/session/SSO/passkey bodies and tests inspected | Unverified → Confirmed static source | NEEDS_REVIEW → REWRITE |
| V2-AST-032 | NEEDS_REVIEW; Notification source unverified | Notification core, channels, policy, queue/dedup and audit inspected | Unverified → Confirmed static source | NEEDS_REVIEW → REWRITE |
| V2-AST-033 | NEEDS_REVIEW; Linka/provider source unverified | Adapter/draft source found; live provider contract absent | Unverified → Partial confirmed source | None |
| V2-AST-034 | NEEDS_REVIEW; AI source unverified | Assistant tools/actions and tests inspected | Unverified → Confirmed static source | None; product scope still open |
| V2-AST-035 | NEEDS_REVIEW; mixed capability source unverified | Customer Request, Audit, Quota and Entitlement implementations found | Unverified → Confirmed static source | None; split ownership still open |
| V2-AST-036 | NEEDS_REVIEW; broader capability map unverified | Full 838-file tree enumerated; implementation roots confirmed | Unverified → Confirmed tree/capability coverage | None; detailed assets added |

Ten new stable groups, V2-AST-037 through V2-AST-046, cover the newly discovered CRM, Sales, Work, Content, Knowledge, Portal, schema/migrations, tests, contracts and administration/reporting assets. Updated proposed totals are RETAIN 13, REWRITE 19, RETIRE 3 and NEEDS_REVIEW 11; total 46. Every disposition remains Proposed and pending project-owner review.

## 9. Remaining evidence gaps and owner decisions

- Owner approval is required for every proposed disposition and for V3 product scope/bounded-context ownership.
- Sanitized provider contracts/fixtures are still needed for Linka, notification providers, OIDC/SAML and other external integrations.
- Production-neutral schema/data dictionaries, volumes, retention/legal constraints and migration reconciliation requirements remain unavailable.
- Runtime/build/test/CI/operational evidence was intentionally not produced; static source and test bodies are not proof of effectiveness or readiness.
- Frontend, plugin platform, production deployment profiles, Sovereign-local authority, backup/restore and operating evidence remain outside this historical backend source.

## 10. Acceptance and outcome

| Criterion | Result |
| --- | --- |
| Historical availability objectively established | Met — local repository identity and exact commit object verified |
| Every index entry accounted for | Met — 106/106 present at exact revision |
| Hash coverage accurately reported | Met — 106 matches, 0 mismatches, 0 unverifiable |
| Available capability source analyzed | Met — required capabilities and additional first-party roots assessed statically |
| Existing inventory reconciled without provenance loss | Met — V2-AST-030–036 updated and V2-AST-037–046 added |
| Unsupported claims remain unverified | Met |
| Owner approvals remain pending | Met |
| V3 architecture/Open Decisions unchanged | Met |
| Only authorized Core documentation modified | Met, subject to final manual status review |

**Final outcome: Historical Source Verified — Inventory Reconciled; Owner Review Pending.**

Precise next action: the project owner reviews and approves/revises the 46 proposed dispositions and decides V3 capability scope/ownership. Provider contracts, production-neutral data evidence and later authorized runtime verification remain separate follow-ups. No implementation or other roadmap task begins from this record.

