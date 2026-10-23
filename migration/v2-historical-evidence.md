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
| Outcome | **Historical Source Access Blocked** |

## 2. Access method and exact blocker

The task permits only a pre-existing local checkout or explicitly provided read-only snapshot. No network acquisition was authorized, and no clone, fetch, pull, archive download, branch change, worktree change, remote change, or Git metadata modification was performed.

Bounded local discovery checked the expected workspace/sibling locations, common local repository locations, the V2 root, the V3 migration area, FIDS-related roots, and user-profile folders named for IAM CRM. No checkout or source snapshot for `IKAC-FIDS/iam-crm-backend` was found, and no local Git worktree was found at the required commit.

Related timestamped folders contained database dumps, environment files, resolved Compose material, or safety/restore artifacts rather than a historical source snapshot. Their contents were outside the authorized source-recovery need and potentially sensitive, so they were not read. The accessible V2 workspace contains only the 106-entry metadata index and the prior narrative report.

**Exact blocker:** the source bodies for commit `9b918ba8972812c129c8b073e1ac4991023ccbbb` are not locally available, and network acquisition is prohibited without separate explicit authorization. Consequently, Phase B capability inspection and Phase C source-based security review cannot proceed.

## 3. Hash method and verification limitation

The index labels each expected value `sha256`, and `docs/architecture/legacy-review.md` calls them content hashes. No document found in the accessible workspace specifies byte normalization, encoding, line-ending handling, or the exact hashing command used. No source body is available to hash. Therefore:

- no indexed hash was recomputed;
- no Git blob SHA was treated as equivalent to a plain SHA-256 content hash;
- all 106 hash checks are `Unverifiable`; and
- zero mismatches or missing paths are asserted, because the pinned source tree itself is inaccessible.

## 4. Coverage summary

| Measure | Count | Meaning |
| --- | ---: | --- |
| Indexed entries | 106 | Entries present in the historical evidence index |
| Available source bodies | 0 | No pinned-revision file body is locally accessible |
| Hash matches | 0 | No comparison could be performed |
| Hash mismatches | 0 | No comparison could be performed; this is not a clean verification result |
| Confirmed missing paths in pinned revision | 0 | Path existence cannot be tested without the revision |
| Inaccessible / unverifiable entries | 106 | Every indexed entry is blocked by the same missing-source condition |
| Unindexed first-party assets discovered | 0 assessable | No historical source tree exists to enumerate |

## 5. 106-entry coverage and hash-verification matrix

Every indexed entry is individually accounted for below. `Inaccessible` means the expected path is known from the index, not that the file is absent from the pinned Git revision.

| # | Indexed path | Expected SHA-256 | Source body | Hash verification | Provenance |
| ---: | --- | --- | --- | --- | --- |
| 1 | `.dockerignore` | `6c46e4e82e91f927773048605bb250603e1bb6cb7b6c30915240edf51538939a` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 2 | `docker-compose.yml` | `a0c9b3dfc041a6017fa51abebe3a245f500b2d8d3668aa9961d804fb88b93253` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 3 | `Dockerfile` | `ea4bf52eb0ca2c4dd46c4ebb5e6077cadb97b3d82534b3cceff5f812d5ffb642` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 4 | `package.json` | `6230e112f4981355474c985b5d4d70bb2affb6364674fa1413b66c6a6a451d35` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 5 | `prisma/schema.prisma` | `6c49e606e14c38a2814c62c7955734598580b595ef4c3b3636cad30aa7bf19d4` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 6 | `src/app.module.ts` | `330068337e2ffd6589c623f3fc5280b62eb415939043555a1a76e6ef0695becf` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 7 | `.github/workflows/backend-ci.yml` | `735f726c2eff452d87a883340a4d65262e0f83992bf065bfa8161c8015c86040` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 8 | `src/audit-log/audit-log.service.ts` | `6ed78056b3348f635bc0d54abd2a98eee49b6c174b71571003bbbcad90fe9ca5` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 9 | `src/audit-log/audit-request-context.service.ts` | `ddf782be9c9ffdf8e4a6e2f4ae813202d7bfb3a46756ddc51d024535e17bcec3` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 10 | `src/auth/account-security.service.ts` | `b70afc0d634b639ebaebef99c82656c721488bc0d79077682b5db83206c66311` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 11 | `src/auth/auth.service.ts` | `2277ffc06524e67508f78e4cbfacb94e3c93a70656e65b3e2155c1b3f8f3cd91` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 12 | `src/auth/refresh-token.service.ts` | `e2a73754d1b1ffee8c05846a8498bfce7008cdb2f64d4aca28d0f4b7bf45c4ac` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 13 | `src/auth/sessions.service.ts` | `a6691ef70bcbf15c19b0a0b1c739b5ede73ff67d5183a1e697031ba366fe9519` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 14 | `src/companies/company-registry-lookup.service.ts` | `73f191f6153c434bcedc5233d925502dd152ba1cff9e7262545554917e6d47f7` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 15 | `src/crm-assistant/crm-assistant-actions.service.spec.ts` | `4a4685ddcc3abcc7d3cc06289b046af3f09a2cf2c4c7fcc803618580efd00ad3` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 16 | `src/crm-assistant/crm-assistant-actions.service.ts` | `e12bd1c8bbb17992f5806b0f7699acbef8af0374cde6335e6be2fdaedd8b430a` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 17 | `src/crm-assistant/crm-assistant-tools.service.spec.ts` | `8590e4cdcc3d7aa66a5e0eed170aefdde1920ff9c23eea34db307a10016c8cc4` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 18 | `src/crm-assistant/crm-assistant-tools.service.ts` | `644f77b8dc8dead160ac9e7525b7bc7a856ee5c733421290bb0b15643a9875d1` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 19 | `src/crm-assistant/crm-assistant.controller.ts` | `7768f473071c83c86c45dd7a58301171860e8c9c0f1bb5e4151b8e832ac91b36` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 20 | `src/crm-assistant/crm-assistant.module.ts` | `2396acf676917493531e03d0c38100dcceb61a8808b7e69f8c2f27157a29c003` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 21 | `src/crm-assistant/crm-assistant.service.spec.ts` | `6af11ec7cdad47103807bf002e7243e0b2de6f72290d4e654ef1ea89a79fa87c` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 22 | `src/crm-assistant/crm-assistant.service.ts` | `66ce8e3aac042e18aa9a37aa30637b520ac602b4167f3493d871fb905768237c` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 23 | `src/crm-assistant/crm-mcp-gateway.service.spec.ts` | `afae11e80f1f93d42bac7942cc68661d7e257b115d4ad4d511953bfad01d67df` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 24 | `src/crm-assistant/crm-mcp-gateway.service.ts` | `2efea2c039cbcaa75a84ad34bffcf3511f554c013e4f5364f15bf508bc008573` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 25 | `src/crm-assistant/crm-mcp.controller.ts` | `a60bdcc76210c69e0f9d0524690bf1f48fb3c5f80e8dc2bc1158642f1dde2086` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 26 | `src/customer-requests/customer-request-operations.service.ts` | `d98acdd64d4d177d4b3380cf2c30ef04dbf0d14f653554b1db6819d083ae747d` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 27 | `src/customer-requests/customer-requests.service.ts` | `3fcea5f065e1a5849602cb82fc027d10c385c529872dcb4f1b9db1c0946a6e63` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 28 | `src/entitlements/entitlement.service.ts` | `b90a8ef442bd7602e8e484d5be8b52ff8ade20c8cb397938a07e93a28145d1f0` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 29 | `src/entitlements/platform-entitlements.service.ts` | `66159dad717c97a09f3c5bc6af433ba3b4602cff9118bfbd76975cb1748d2708` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 30 | `src/notification-core/index.ts` | `6c094e2e84ae8337710e2b7871bd0e11a91e203cce486ff5f67be79b9b906399` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 31 | `src/notification-core/notification-admin.controller.ts` | `44537103638ea762caf002662587b67ca2bd3bd472018252734e418a7da7c030` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 32 | `src/notification-core/notification-admin.service.ts` | `1213adc30769588e440325ae985577e7b9f5e20440a453f57a209f7516b90480` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 33 | `src/notification-core/notification-channel-handler.ts` | `0c3e5d4f3a34b5acf05657013d4ee74b352624d26698d3c05348e9ac5a8e36e7` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 34 | `src/notification-core/notification-core.catalog.ts` | `631daa2267683bfb21e22fe67b39fa439000537e98c50fe63e6545dde70d7c0c` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 35 | `src/notification-core/notification-core.module.ts` | `114464a9472eed8551233a742c414c1546de5cb53bb3a357cf7bc2104dd778df` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 36 | `src/notification-core/notification-core.service.ts` | `048685bb34caea8d88407f18cc21f16499b740459bf14411bc9f92940b7596f4` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 37 | `src/notification-core/notification-core.types.ts` | `1384059665796262b98c5f7826aef7334bf9eab0ebd901955ad1497e4bc3f640` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 38 | `src/notification-core/notification-delivery-dispatcher.service.ts` | `4dcfefb51f0f4eb9cf2ed9186d610c7bcd6180ba23d3cddfb4c604cc6fb99bdf` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 39 | `src/notification-core/notification-rule-engine.service.ts` | `9eed8f9f509d55390d83dc44a839a7a92190e2848fc3e643dd8944642f723da4` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 40 | `src/notification-core/notification-rules.controller.ts` | `4c309b20278b89deb36befa7e37ad14dc5b0f73d78c913b6071ef3078081d84e` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 41 | `src/notification-core/notification-rules.service.ts` | `4625735a7021675153d8ae72c56cc28c5cdd3657ec1f04ce7204891fcc795564` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 42 | `src/notification-core/notification-template-engine.service.ts` | `06f3f285cb5cc22c468205d8ed5b0b3166fab15c752030fe8fa9cab44602b95f` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 43 | `src/organization-memberships/organization-memberships.service.ts` | `986e7416fb00409d2e4109edf238f48f5c9335c7846b574e3e703d50dd3e22d4` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 44 | `src/organization-memberships/tenant-rbac.service.ts` | `0f0fd616b4d9ee3e7bb2d4ef1cc7d213bc03017c65bee3a0bf67a3e118e21888` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 45 | `src/organization-memberships/tenant-resolver.service.ts` | `3654722d8f4d46fe0ab49d8ddf495f875772b0131221cc150377055cd1ef82e1` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 46 | `src/organizations/organization-configuration.service.ts` | `a91add37c1c5782af80c9e4765f1815a06ff6375a6ca851622e53ed3f9003f23` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 47 | `src/organizations/organization-domain-verification.service.ts` | `390e8f88352d2563f7f1b468c26e1979be4b7eacdeb7fc30bf82f6ecdf74478b` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 48 | `src/organizations/organizations.service.ts` | `ef3aea08081b462e4d756ff1feae386cb906e7027ee80727c8f312c71ed5b216` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 49 | `src/prisma/prisma.service.ts` | `0b47af43a2d7a35b0c9748bf10dca859646691a0618c015a7480351fd8e3cf59` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 50 | `src/quota/platform-quota.service.ts` | `f8657bd7cc16e2334d9c51fba0077221d15208c32301675cd350f7c0b141c48b` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 51 | `src/quota/quota-resolver.service.ts` | `ca2aa250ec586b1de515692c68c1332266f210566be02ada3a625fe03b37de9c` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 52 | `src/quota/quota-scheduler.service.ts` | `ebcaa8b7ce2f0565babc90e236d1752da9bd1a9c44d53ae0ceca6fd58cbd2f85` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 53 | `src/quota/quota.service.ts` | `69b59c2d5caf2cd3422f09b1bb8c3192953db7a5430099ec1d0cd4222346791a` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 54 | `src/quota/usage-reconciliation.service.ts` | `ab8f27bc22a7ffd3c298616930efb1d7374ef06504e83ff4d255dd82d072ea30` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 55 | `src/auth/passkeys/passkeys.service.ts` | `65bc468829dd80a74099e3a241b6b66cefbeb8dd8ac1427acde9d4fc0c28a299` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 56 | `src/auth/sso/oidc.service.ts` | `d41753f8563fa9ddbc2c18ee59242c8ba4e2eef9701dede3d685e99b936d8fb9` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 57 | `src/auth/sso/saml.service.ts` | `d23518cf7cb584e0446e6159bd2213cb06c90d0765ce32f069b5b0d91d0bf010` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 58 | `src/auth/sso/sso-network-security.service.ts` | `bb5eaf53a1888278372875c423d0c576ff6da22fd0a1b30cdce151f2f8ce39ab` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 59 | `src/auth/sso/sso-provider.service.ts` | `70264203eaac7b0a7f96d4a306f7685521a02b81ef816a13ddcbdaa7113e88c6` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 60 | `src/auth/sso/sso-secret.service.ts` | `43a90af64d146ae05c80219902f7352ca4827ed0e72e09e0df93df2578044401` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 61 | `src/auth/sso/sso-ticket.service.ts` | `f6bf29db5e915914e7a30c34dce43b5179366689aad43a69c79778e74ad5adbe` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 62 | `src/auth/sso/crypto/secret-encryption.service.ts` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 63 | `src/crm-assistant/dto/ask-crm-assistant.dto.ts` | `54919a034bae4475f4de5d17fce72e5dd2835acf96930bf3e1f4d3876bced1f7` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 64 | `src/crm-assistant/dto/confirm-crm-assistant-action.dto.ts` | `27dad6ade93e2f80112b25e5b5bdcd9fb84f789b8b2e94fd6b3591082b565d2c` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 65 | `src/notification-core/audit/notification-delivery-audit.service.ts` | `893a928a1c26d3de95015d7f2671bac983698e8b8d4f6d28908626962386342a` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 66 | `src/notification-core/deduplication/notification-deduplication-key.service.ts` | `0fd397336601ff77e020110daeb3b334cb90d8277fc8c2d2e05f6af232f0f534` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 67 | `src/notification-core/deduplication/notification-delivery.service.ts` | `b715aef62306574712af35f642acd5b378a2d206edbbacf09540177f6ad310e4` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 68 | `src/notification-core/dto/notification-admin.dto.ts` | `c4348cd67a1536666a0823bd3b3ee48487f93c32b313615ab080f12ad3bce22d` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 69 | `src/notification-core/dto/notification-orchestration.dto.ts` | `86168d698c2630c9d8d0571f73c45a0f365ceb2c96ed20f85a54ba72d612ce7f` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 70 | `src/notification-core/dto/notification-rule.dto.ts` | `98348634e3c7c75c1c75fa0ea37f363996b390dfdec76bf5c6c31aa8998539fd` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 71 | `src/notification-core/email/email-notification-channel.handler.ts` | `402827bfcd09e25f70e038f19a1f4eb90cf53979bd9cde70b0ed9a42d6d3e5a2` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 72 | `src/notification-core/in-app/in-app-notification-channel.handler.ts` | `5049bdba4e6397e04779653f12705ee134628acd5b80dbad43e680ed0c4f25d4` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 73 | `src/notification-core/in-app/notification-action-url.resolver.ts` | `c25a60501aa5683265efc4aac1bcb7fb53695a0e78db871c14e24d1a4a2cb9de` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 74 | `src/notification-core/in-app/notification-tenant-context.ts` | `f1ee25bd19375b17d4ee9e57953f29254a8cdc7c528a82311ca29814485a44b0` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 75 | `src/notification-core/orchestration/notification-digest-renderer.service.ts` | `46aa3c4f2f237d17fee0b941dfca6e2e23597848f80867c4e47515195b3bcb2b` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 76 | `src/notification-core/orchestration/notification-escalation.service.ts` | `1969be4afab48cb21bd372306a59f050505463d33854f09f244bad1dcf08c702` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 77 | `src/notification-core/orchestration/notification-orchestration.service.ts` | `d1f12b3153a4c65bd03d7bd211a3dc68359283aec2c418773761c756ff81aea0` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 78 | `src/notification-core/orchestration/notification-policy-admin.controller.ts` | `4f19097f3f1fc05cde02229a7cfddbd011967f4c6d9790031a7d5e3abf254b44` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 79 | `src/notification-core/orchestration/notification-policy-admin.service.ts` | `a67c4b2c69edd05d380da6d95c7086060a42820a5c749796689fcb72d61b446b` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 80 | `src/notification-core/orchestration/notification-time-window.ts` | `69fd872c5633bfec725b0d0f96132774252290eb41453f44fcf77f3bc356376c` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 81 | `src/notification-core/policy/notification-condition.catalog.ts` | `961dbd4407f67443272d0d6a134214cf04018960e401934dbd24e55d7f35b1da` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 82 | `src/notification-core/policy/notification-policy-condition-validator.service.ts` | `7cb2774a118955553d86fe2645d184a2991213e15e40ac46b829d54c8554930c` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 83 | `src/notification-core/policy/notification-policy-context-builder.service.ts` | `7b2888b549405af3f539341366604590938d4b81ffc55a2533174c062c8af90a` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 84 | `src/notification-core/policy/notification-policy-evaluator.service.ts` | `22e9ff49fc5c3079ff2eb599916db429f1cd1ad99c44e9c9f4a6328b668b8b73` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 85 | `src/notification-core/policy/notification-policy-field-resolver.ts` | `6cba2d6659bcf8dd0e45397b2d3af34389a68cc2f4b99de0e5f4dabc2af92f40` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 86 | `src/notification-core/policy/notification-policy.types.ts` | `2a4ea782c76927016e5576bb11dcfe9da09cd81cc6b08ac8e8964e350f45da89` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 87 | `src/notification-core/push/push-notification-channel.handler.ts` | `6bb29c3fd6196e2007793b61771fd3142a762eaef4ba954904235e52481cc2c3` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 88 | `src/notification-core/push/push-provider.registry.ts` | `9a912bc75eb7bc0e4f626fdb1108b9d0bb61ca648b85976e72b4ff937efafc5d` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 89 | `src/notification-core/push/push-settings.service.ts` | `96383e845f82f7589902b0ae1993ffc5edf35d460bead5ff1de81582d07e97a4` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 90 | `src/notification-core/push/push.controller.ts` | `abb4e5222d8b048baf195e195fe1833e6cacde8c475670885086d2a0ea2abdd7` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 91 | `src/notification-core/push/push.types.ts` | `ff53717822f75b437e0e489537480d979763223e223414dd1678b0a1e84134a0` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 92 | `src/notification-core/push/web-push.provider.ts` | `4ae1a67e3f52d0c61dd76e1c312a3f09c32b90d2906df640885f769ab3a1f2da` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 93 | `src/notification-core/queue/notification-delivery-queue.service.ts` | `6ae0949cb79a9aabfac6f2b509d0804aa668763d29573c1521da7009f91e8a1c` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 94 | `src/notification-core/queue/notification-delivery-worker.service.ts` | `d9edecd659bdc6fd8c1f47bb7cd232ad5cfc9f23b76274bba4be9f288c02b81d` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 95 | `src/notification-core/schedule/notification-schedule-validator.service.ts` | `f3eadeb82d9dd6e59627268e711da0dc4ee990dcf86b264a14ee6400ad0eb5ba` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 96 | `src/notification-core/schedule/notification-schedule.catalog.ts` | `7b9dba85e09fdd1a84a1bedf9bfdcd09b016e0abe4aa25207b21f86178b76d54` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 97 | `src/notification-core/schedule/notification-scheduler.service.ts` | `ede7080445e6fd2f762a83dee88bd99d04a64a7dcf00cd69950528aa0e1fdbc6` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 98 | `src/notification-core/sms/generic-http-sms.provider.ts` | `2a3791cb305115f22ad3419927ff220d3f9b5398ff1c2ec2659fff600b1bfd30` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 99 | `src/notification-core/sms/sms-admin.controller.ts` | `06c5906362312af5d014b41966e34ef5a531ef910590eb6431afb3af1feb596f` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 100 | `src/notification-core/sms/sms-notification-channel.handler.ts` | `fcc97d66f65dfc9c9ea2744d8dd33389e48435fc3faec972486ad599dbdd2691` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 101 | `src/notification-core/sms/sms-provider.registry.ts` | `11913bb33c8ca18af11cd13694fa697ba54e9a5d412e78f2a1abd97a959248ea` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 102 | `src/notification-core/sms/sms-recipient-resolver.service.ts` | `ce92bb75728d33cfb50f2b3ba4c94199264966775b62e4319f2cd5110b33ae9e` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 103 | `src/notification-core/sms/sms-settings.service.ts` | `2c89dcac7f693de07fe815a1baaab02d4eff37b74d5c6a2e3a30070c90c911ec` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 104 | `src/notification-core/sms/sms.types.ts` | `429f8532b79fb616ced1b50955a34d029a0a25b0214022fd55ce7c801a458aba` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 105 | `src/notification-core/push/dto/push.dto.ts` | `2982f505bcf967015ef36471f4bf15884750fa51e82272c99d0d14e119244ab8` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |
| 106 | `src/notification-core/sms/dto/sms-settings.dto.ts` | `227b06536d12c834378637e124b2b22b34bf2b3f7e94337b23c71e0dfec42ab8` | Inaccessible — no local pinned snapshot | Unverifiable | V2 historical index metadata |

## 6. Historical capability assessment

No historical source body was recovered, so no capability received new Directly Observed evidence under V3-002A. Identity/session/OIDC/SAML/Passkey, Tenant/Organization/Membership, Notification, Linka/external integration, Customer Requests, Audit, Quota/Entitlement, AI, and other CRM capability claims retain their V3-002 labels of Documentation-Reported or Unverified.

The prior report in `E:\Neshane-CRM-V2\docs\architecture\legacy-review.md` remains secondary evidence. Its claims were neither confirmed nor contradicted by V3-002A. No runtime behavior, domain invariant, public/internal contract, persistence ownership, authorization boundary, recovery behavior, or test result was newly verified.

## 7. Security and architecture review result

No new source-based security or architecture finding is justified. The only confirmed V3-002A finding is the evidence-access gap itself:

- historical content cannot be independently checked against its indexed hashes;
- no claim about token validation, refresh rotation, tenant isolation, provider trust, audit integrity, idempotency, or authorization can be promoted from Documentation-Reported to Confirmed;
- historical V2 choices remain non-authoritative for V3; and
- ADR-V3-001 through ADR-V3-012 and OD-001 through OD-023 are unchanged.

Source inspection would still not prove runtime effectiveness or exploitability if access were later provided.

## 8. Reconciliation with existing Asset IDs

| Asset ID | V3-002 state | V3-002A reconciliation | Confidence change | Disposition change |
| --- | --- | --- | --- | --- |
| V2-AST-030 | RETAIN; metadata index confirmed | All 106 metadata entries accounted for; source bodies unavailable | None — metadata remains confirmed, content remains unavailable | None |
| V2-AST-031 | NEEDS_REVIEW; Identity source unverified | Indexed paths accounted for but not inspected | None | None |
| V2-AST-032 | NEEDS_REVIEW; Notification source unverified | Indexed paths accounted for but not inspected | None | None |
| V2-AST-033 | NEEDS_REVIEW; Linka/provider source unverified | Indexed path accounted for but not inspected | None | None |
| V2-AST-034 | NEEDS_REVIEW; AI source unverified | Indexed paths accounted for but not inspected | None | None |
| V2-AST-035 | NEEDS_REVIEW; Customer Request/Audit/Quota source unverified | Indexed paths accounted for but not inspected | None | None |
| V2-AST-036 | NEEDS_REVIEW; broader capability map unverified | No historical tree available to discover additional implementations | None | None |

No prior evidence was erased, no contradictory source was available, no new first-party historical asset could be established, and no new Asset ID was assigned.

Disposition totals remain unchanged: RETAIN 11, REWRITE 10, RETIRE 3, NEEDS_REVIEW 12; total 36. Every disposition remains Proposed and pending project-owner review.

## 9. Remaining evidence gaps and owner decisions

- A read-only snapshot or checkout containing the exact pinned commit is required to continue source verification.
- The snapshot should be placed outside the V2, V3 Core, Backend, and Frontend repositories and should include enough provenance to establish the exact commit.
- If source is provided, the hashing method must be documented or approved before comparing bytes with the indexed SHA-256 values.
- The owner must decide whether to provide such a snapshot or issue a separate explicit authorization for external acquisition. This task grants neither.
- Capability scope, V3 mappings, bounded contexts, service splits, migration/retirement decisions, and all open technical selections remain unapproved.

## 10. Acceptance and outcome

| Criterion | Result |
| --- | --- |
| Historical availability objectively established | Met — no authorized local source body is available |
| Every index entry accounted for | Met — 106/106 listed as inaccessible/unverifiable |
| Hash coverage accurately reported | Met — 0 comparisons; no fabricated match/mismatch/missing result |
| Available capability source analyzed | Not applicable — no source body available |
| Existing inventory reconciled without provenance loss | Met — affected Asset IDs unchanged and linked to this record |
| Unsupported claims remain unverified | Met |
| Owner approvals remain pending | Met |
| V3 architecture/Open Decisions unchanged | Met |
| Only authorized Core documentation modified | Met, subject to final manual status review |

**Final outcome: Historical Source Access Blocked.**

Precise next action: the project owner provides an explicitly authorized read-only snapshot/check-out of `IKAC-FIDS/iam-crm-backend` at commit `9b918ba8972812c129c8b073e1ac4991023ccbbb` outside the repositories, together with the content-hashing method if known. V3-002A can then resume with per-file verification. No implementation or other roadmap task should begin from this record.

