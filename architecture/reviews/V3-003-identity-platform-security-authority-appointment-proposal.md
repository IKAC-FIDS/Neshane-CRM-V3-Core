# V3-003 — پیشنهاد حاکمیت انتصاب Identity/Platform Security Authority

## A. هدف، محدوده و شکاف حاکمیتی فعلی

این سند یک **Governance Proposal** مستنداتی برای تعریف روش نامزدی، احراز، انتصاب، تفویض، بازبینی، تعلیق، انقضا و لغو `Identity/Platform Security Authority` است. این سند Governance Standard نهایی، Appointment Record یا Delegation مؤثر نیست.

```text
IDENTITY_PLATFORM_SECURITY_AUTHORITY = UNASSIGNED
APPOINTING_AUTHORITY = NOT_VERIFIED
FORMAL_DELEGATION = NOT_ISSUED
IDENTITY_PLATFORM_SECURITY_APPROVAL = PENDING
```

هیچ فرد، تیم یا سازمانی در این سند نامزد یا منصوب نمی‌شود. نقش Project Owner، Domain Owner، Coordinator، Operator یا Independent Security Reviewer به‌صورت خودکار اختیار انتصاب یا اختیار Identity/Platform Security ایجاد نمی‌کند.

### A.1 کنترل سند و خط مبنا

| فیلد | مقدار تأییدشده |
| --- | --- |
| Repository | `E:\Neshane-CRM-V3` |
| Branch | `main` |
| Git HEAD در زمان تهیه Proposal | `ffcc793ce96842b0ca7d60a369a1c2e3b5b933a8` |
| وضعیت Index/Worktree پیش از ایجاد سند | Clean |
| نوع سند | `DRAFT — ORGANIZATIONAL GOVERNANCE APPROVAL REQUIRED` |
| اثر اجرایی | None؛ هیچ Appointment یا Delegation صادر نمی‌شود |
| V3-003 | `IN PROGRESS` |

| سند مرجع | SHA-256 تأییدشده | وضعیت |
| --- | --- | --- |
| `architecture/reviews/V3-003-specialist-review-tracking-register.md` | `c3a4b6c04bc31589d7d6e485c747e31f865805aadca8d8708064450d436c296e` | Committed؛ منطبق با HEAD |
| `architecture/reviews/V3-003-identity-platform-security-review-request.md` | `99f64d857ee22b3090bf9ad07fc270c903dab0c620190fba7ac3590c8631cc1e` | Committed؛ منطبق با HEAD |
| `architecture/reviews/V3-003-consolidated-security-design-review-manifest.md` | `9592b9e9190d2182132d5eebefbd9fdcb7c802f7f8a8e305b8209db699b90c3e` | Committed؛ منطبق با HEAD |
| `architecture/reviews/V3-003-decision-record.md` | `178d447fc642a385c20fecd866de5e87e518944da3f65a005fc6118034000e18` | Committed؛ منطبق با HEAD |

## B. مرزهای تأییدشده اختیار موجود

شواهد Repository فقط مسئولیت‌های role-based و نیاز به یک Authority احرازشده را تعیین می‌کنند؛ هیچ Appointing Authority یا دارنده واقعی `AUTH-IP` ثبت نشده است.

| نقش یا اختیار | وضعیت تأییدشده | مرز |
| --- | --- | --- |
| Project Owner | تصمیم‌های Project Owner ثبت شده‌اند | هیچ شاهدی برای اختیار انتصاب Security Authority وجود ندارد |
| Customer/Audit/Messaging-Operations Owners | Bounded dispositions ثبت شده‌اند | Specialist Security Approval ایجاد نمی‌کنند |
| Identity/Platform Security Authority | `UNASSIGNED / PENDING` | فقط پس از Appointment و Delegation معتبر می‌تواند disposition محدود صادر کند |
| Security Architecture | `PENDING` | جایگزین Identity/Platform، Tenant، Contract یا Independent Review نیست |
| Tenant Security | `PENDING` | مالک تصمیم‌های Tenant Context، Delegation و Isolation در محدوده خود است |
| Sovereign-specific Security | `PENDING` | مالک بررسی امنیتی اختصاصی Sovereign در محدوده خود است |
| Contract Governance | `PENDING` | مالک semantic contract و compatibility در محدوده خود است |
| Messaging/API Event Architecture | `PENDING` | مالک envelope، delivery و recovery architecture در محدوده خود است |
| Operational Policy Governance | `PENDING` | مالک policy عملیات privileged، monitoring و restoration در محدوده خود است |
| Independent Security Reviewer | `UNASSIGNED / NOT_SIGNED_OFF` | مستقل از Appointment و Specialist disposition است |
| Operational Executor | هیچ اختیار ضمنی | اجرای عملیات، مالکیت evidence یا اختیار Security decision ایجاد نمی‌کند |

تمایزهای زیر الزامی‌اند:

- **Organizational appointing authority:** اختیار حقوقی/سازمانی برای ایجاد یا تفویض نقش؛ فعلاً `NOT_VERIFIED`.
- **Technical competence:** توانایی تخصصی؛ به‌تنهایی Authority ایجاد نمی‌کند.
- **Security decision authority:** محدوده تصمیم فنی که فقط از Appointment معتبر ناشی می‌شود.
- **Project coordination:** گردآوری و ارسال بسته؛ فاقد اختیار Approval.
- **Domain ownership:** اختیار Business Fact و Resource/Action همان Domain؛ قابل انتقال ضمنی نیست.
- **Independent security review:** ارزیابی مستقل بعدی؛ با Specialist Authority یکی نیست.
- **Operational execution:** اجرای کنترل‌شده؛ حق self-authorization یا policy ownership ایجاد نمی‌کند.

## C. الزامات احراز Appointing Authority

پیش از انتخاب هر مدل، سازمان باید مرجعی را که مجاز به انتصاب است با شواهد authenticated احراز کند. این Proposal چنین مرجعی را تعیین نمی‌کند.

| الزام | شاهد پیشنهادی لازم | وضعیت فعلی |
| --- | --- | --- |
| هویت مرجع انتصاب | Organizational identity یا authenticated reference | `UNASSIGNED` |
| مبنای اختیار | Charter، corporate resolution، policy، contract یا delegation معتبر | `NOT_VERIFIED` |
| محدوده جغرافیایی/سازمانی | Entity، business unit و Deployment Profile تحت پوشش | `NOT_VERIFIED` |
| اختیار تفویض Security decision | عبارت صریح درباره انتصاب یا delegation | `NOT_VERIFIED` |
| محدودیت‌ها | Conflict rules، duration، revocation و non-delegable powers | `NOT_VERIFIED` |
| تمامیت شاهد | Immutable reference، custodian و retention rule | `NOT_VERIFIED` |
| سازگاری با Governance پروژه | عدم تعارض با ADRها، Domain ownership و Independent Review | `NOT_VERIFIED` |

تا زمان احراز همه موارد لازم، هیچ Nomination نباید به `APPOINTED_EVIDENCE_VERIFIED` تبدیل شود. Project Owner فقط در صورتی می‌تواند Appointing Authority باشد که اختیار سازمانی او برای این کار با شاهد مستقل و صریح احراز شود.

## D. گزینه‌های پیشنهادی مدل انتصاب

همه گزینه‌ها Candidate هستند و هیچ‌کدام تصویب نشده‌اند.

| مدل | Competence | Organizational authorization | Independence / conflict | Accountability و continuity | Revocation و auditability | مرز میان تخصص‌ها |
| --- | --- | --- | --- | --- | --- | --- |
| A — Internal named Security Authority | شواهد تجربه و تخصص فردی لازم | Appointment داخلی صریح لازم | تعارض با delivery/ownership باید ارزیابی شود | فرد accountable؛ deputy/continuity باید جداگانه تعریف شود | لغو یا تعلیق داخلی با record authenticated | فقط delegation مصوب IP؛ سایر authorities مستقل |
| B — External formally delegated Security Authority | رزومه، references و domain competence لازم | Contract و delegation سازمانی صریح لازم | استقلال بالقوه بیشتر؛ conflict تجاری و vendor bias باید بررسی شود | SLA/continuity فقط در صورت قرارداد مصوب؛ هیچ عددی اینجا تصویب نمی‌شود | termination، replacement و evidence custody باید تعریف شود | delegation نباید Contract، Tenant، Sovereign یا risk acceptance را جذب کند |
| C — Security Review Committee | ترکیب مهارت‌ها و حد نصاب competence لازم | Charter، membership authority و decision rules لازم | conflict declaration، recusal و quorum ضروری | continuity بهتر؛ مسئولیت هر تصمیم و dissent باید traceable باشد | membership change، quorum loss و charter revocation باید ثبت شود | هر رأی فقط در scope تفویض‌شده معتبر است |
| D — Internal authority with external advisors | Internal appointee باید competence و Authority کافی داشته باشد | Appointment داخلی و advisory contract جدا لازم | Advisor تصمیم‌گیر نیست؛ conflict هر دو طرف بررسی می‌شود | Authority داخلی accountable؛ advisor فقط evidence/recommendation می‌دهد | تعویض advisor Appointment را خودکار تغییر نمی‌دهد | advisor هیچ Specialist یا Independent Approval صادر نمی‌کند |

انتخاب مدل باید صریحاً موارد competence، accountability، continuity، independence، delegation، sub-delegation، suspension، revocation، retention و cross-specialist boundaries را تعیین کند.

## E. معیارهای صلاحیت و استقلال Candidate

### E.1 Competence پیشنهادی

- تجربه قابل‌اثبات در workload identity، service-to-service trust و authorization boundaries.
- توانایی ارزیابی issuer/audience/validity/revocation و credential lifecycle بدون وابستگی به یک فناوری خاص.
- تجربه در producer provenance، messaging trust، replay و confused-deputy risks.
- شناخت Tenant Context، Domain-owned authorization و fail-closed behavior.
- توانایی بررسی Audit confirmation trust و تفکیک broker ACK از durable Audit evidence.
- تجربه در Sovereign-local authority، disconnected operation و reconnect trust conflicts.
- توانایی خواندن ADR، threat/abuse catalogs، evidence gaps و negative-test requirements.

هیچ گواهی، سابقه یا عنوان شغلی مشخص در این Proposal به‌تنهایی کافی یا مصوب اعلام نمی‌شود؛ کف شواهد competence باید توسط Governance مصوب آینده تعیین شود.

### E.2 Independence و Conflict-of-Interest

- رابطه Candidate با طراح، implementer، operator، vendor و risk owner باید افشا شود.
- Candidate نباید implementation خودش را بدون کنترل تعارض مناسب به‌تنهایی تصویب کند.
- منافع مالی، vendor incentives و مسئولیت delivery باید ارزیابی شوند.
- Committee member یا advisor دارای conflict باید طبق policy آینده recuse شود.
- استقلال Specialist Review به معنی Independent Security Review نیست.

### E.3 Accountability و Evidence

- هر disposition باید به هویت، Appointment reference، baseline و scope متصل باشد.
- محدودیت‌ها، dissent، required evidence و amendments باید حفظ شوند.
- عدم پاسخ، سکوت یا recommendation تحلیلگر Approval محسوب نمی‌شود.

## F. محدوده Delegation و اختیارات ممنوع

### F.1 محدوده اولیه Candidate

Delegation اولیه فقط می‌تواند تصمیم‌های زیر را، هر کدام به‌صورت مستقل، پوشش دهد:

| Working label | محدوده تصمیم |
| --- | --- |
| `IP-01` | Workload Identity Trust Model |
| `IP-02` | Producer Provenance Validation |
| `IP-03` | Audit Confirmation Trust |
| `IP-04` | Credential Lifecycle and Revocation |
| `IP-05` | Sovereign-local Identity Validation |

در صورت Appointment معتبر، Reviewer می‌تواند در محدوده تفویض‌شده:

- شواهد Security Architecture مربوط به IP را بررسی کند؛
- Amendment یا evidence تکمیلی درخواست کند؛
- design evidence ناکافی را رد یا Block کند؛
- constraints امنیتی در scope خود مشخص کند؛
- برای هر IP یک bounded disposition معتبر صادر کند.

### F.2 اختیاراتی که خودکار ایجاد نمی‌شوند

Identity/Platform Security Authority مجاز نیست صرفاً به اتکای این نقش:

- Tenant Security، RLS یا Domain authorization را تصویب کند؛
- Contract Governance یا Messaging/API Event Architecture را تصویب کند؛
- Sovereign-specific Security یا Operational Policy را تصویب کند؛
- Eligibility Policy Authority را تعیین کند؛
- Independent Security Review sign-off صادر کند؛
- `EXECUTABLE_DURABLE_DEFER` را مجاز کند؛
- Production deployment یا Production Readiness را تصویب کند؛
- organizational residual risk را خارج از delegation صریح بپذیرد؛
- فناوری، provider، protocol، cryptography، KMS/HSM یا secret manager را بدون اختیار جداگانه انتخاب کند؛
- اختیار خود را بدون اجازه صریح sub-delegate کند.

## G. Lifecycle پیشنهادی Appointment و ماتریس شواهد

این State Model پیشنهادی است؛ هیچ Transition با ایجاد این سند اجرا نمی‌شود.

| State | Entry condition و evidence | Actor مجاز برای Transition | اقدامات مجاز | اقدامات ممنوع | Exit condition |
| --- | --- | --- | --- | --- | --- |
| `UNASSIGNED` | هیچ Appointment معتبر وجود ندارد؛ وضعیت فعلی Repository | N/A؛ وضعیت پایه | تحلیل شکاف و آماده‌سازی Proposal | Review، disposition، assignment یا submission به نام Authority | Nomination مستند توسط actor مجاز در مدل تصویب‌شده |
| `NOMINATED` | Candidate identity و nomination reference authenticated؛ nominator authority verified | Nominator مجاز طبق Governance مصوب | ارائه competence، role و conflict evidence | Specialist decision یا نمایش خود به‌عنوان appointed | پذیرش Candidate برای verification یا withdrawal معتبر |
| `AUTHORITY_VERIFICATION_PENDING` | بسته Evidence کامل برای بررسی؛ identity و provenance قابل‌ردیابی | Verifier مستقل یا governance custodian مصوب | بررسی identity، competence، appointing authority و conflict | صدور Appointment یا IP disposition | Verified findings و انتقال به approval؛ یا بازگشت/رد |
| `APPOINTMENT_APPROVAL_PENDING` | Verification موفق، delegation draft و limitations آماده | فقط `APPOINTING_AUTHORITY` احرازشده | تصمیم درباره مدل، scope، مدت، restrictions و revocation terms | Specialist disposition پیش از effective appointment | Approval authenticated + acceptance؛ یا reject/withdraw |
| `APPOINTED_EVIDENCE_VERIFIED` | Appointment approval، appointee acceptance، scope و effective condition همگی احراز شده‌اند | Appointing Authority احرازشده؛ activation طبق record مصوب | bounded IP review، amendment request و decision-specific disposition | اختیار خارج scope، risk acceptance یا sign-off سایر authorities | Suspension، expiration، revocation یا authorized review/renewal |
| `SUSPENDED` | Suspension record authenticated یا trigger مصوب فعال؛ scope و effective condition روشن | Appointing Authority یا emergency actor فقط در صورت delegation صریح | حفظ evidence، همکاری در impact assessment | صدور disposition جدید یا استفاده از Authority معلق | Reinstatement صریح با verification جدید؛ expiration یا revocation |
| `EXPIRED` | Expiration date یا review condition مصوب محقق شده | Transition شرطی ثبت‌شده؛ verification توسط governance custodian | حفظ record و انجام impact review در صورت نیاز | تصمیم جدید یا ادامه ضمنی Authority | Appointment جدید/renewal با evidence کامل؛ یا باقی‌ماندن expired |
| `REVOKED` | Revocation record authenticated با scope و effective condition | Appointing Authority احرازشده یا actor صریحاً مجاز | حفظ evidence و impact assessment | تصمیم جدید، sub-delegation یا ادعای Authority | فقط Appointment جدید و مستقل؛ Revoked record حذف نمی‌شود |

### G.1 Evidence Record پیشنهادی

| فیلد لازم | مقدار فعلی |
| --- | --- |
| Appointment reference | `UNASSIGNED` |
| Appointing authority identity | `UNASSIGNED` |
| Evidence of appointing authority | `NOT_VERIFIED` |
| Candidate identity reference | `UNASSIGNED` |
| Technical competence and experience evidence | `NOT_VERIFIED` |
| Organizational role or external contract | `NOT_VERIFIED` |
| Independence/conflict assessment | `NOT_VERIFIED` |
| Exact delegated decision scope | `NOT_ISSUED` |
| Effective date | `UNASSIGNED` |
| Expiration date or review condition | `UNASSIGNED` |
| Sub-delegation restrictions | `NOT_APPROVED` |
| Suspension/revocation conditions | `NOT_APPROVED` |
| Appointment approval reference | `UNASSIGNED` |
| Appointee acceptance reference | `UNASSIGNED` |
| Evidence integrity/retention rule | `NOT_APPROVED` |

## H. اعتبار تصمیم Authorized Reviewer

یک disposition فقط زمانی Candidate معتبر برای ثبت است که همه شروط زیر احراز شوند:

1. Reviewer identity با authenticated reference تأیید شده باشد.
2. Appointment در زمان صدور تصمیم `APPOINTED_EVIDENCE_VERIFIED` و مؤثر باشد.
3. تصمیم دقیقاً در delegation scope قرار گیرد.
4. Reviewer path، SHA-256 و baseline بررسی‌شده را تأیید کرده باشد.
5. disposition برای یک Working label مشخص و از vocabulary مجاز صادر شده باشد.
6. accepted/rejected boundaries، limitations و evidence requirements ثبت شده باشند.
7. authenticated decision record با integrity و retention مناسب حفظ شده باشد.
8. Conflict-of-interest، suspension و expiration constraints نقض نشده باشند.
9. cross-specialist dependencies به‌عنوان حل‌شده جعل نشده باشند.

گزینه‌های disposition بدون انتخاب قبلی:

```text
APPROVE_WITH_BOUNDARIES
AMEND
REJECT
BLOCKED
EVIDENCE_REQUIRED
```

Appointment به‌تنهایی Specialist Approval نیست. پاسخ Track-level نیز `IP-01..05` را خودکار تصویب نمی‌کند؛ هر تصمیم باید disposition و scope مستقل داشته باشد.

## I. تعلیق، انقضا و لغو

### I.1 Triggerهای پیشنهادی

- پایان مدت یا تحقق review condition؛
- تغییر نقش سازمانی یا خاتمه قرارداد؛
- کشف Conflict-of-Interest مؤثر؛
- compromise شدن credential یا authenticated decision channel؛
- sub-delegation غیرمجاز؛
- material architecture rebaseline خارج از baseline پذیرفته‌شده؛
- جایگزینی Reviewer؛
- failure در authenticity یا integrity شواهد Appointment/Decision.

### I.2 اثر آینده‌نگر

- پس از Suspension، Expiration یا Revocation هیچ disposition جدیدی معتبر نیست.
- Assignment و Submissionهای آینده باید Authority state را در زمان اقدام دوباره بررسی کنند.
- Replacement هیچ تصمیم قبلی را خودکار adopt یا reject نمی‌کند.
- material rebaseline نیازمند تعیین Scope تأثیر و احتمال re-review است.

### I.3 اثر بر تصمیم‌های قبلی

تصمیم‌های قبلی نه خودکار حذف می‌شوند و نه خودکار معتبر باقی می‌مانند. یک impact assessment صریح باید بررسی کند:

- آیا Authority در زمان تصمیم معتبر بوده است؛
- آیا trigger به provenance یا integrity همان تصمیم لطمه می‌زند؛
- آیا baseline مادی تغییر کرده است؛
- آیا re-review، suspension of reliance یا superseding disposition لازم است.

نتیجه impact assessment نیازمند اختیار و record مستقل است؛ این Proposal هیچ تصمیم قبلی را لغو نمی‌کند.

## J. پیشنهاد Integration با Tracking Register

این بخش فقط mapping آینده را پیشنهاد می‌کند و فایل Tracking Register را تغییر نمی‌دهد.

| Appointment evidence | فیلد پیشنهادی در Register | شرط ثبت آینده |
| --- | --- | --- |
| Appointment reference + accepted identity | `Assigned reviewer identity` | فقط پس از `APPOINTED_EVIDENCE_VERIFIED` |
| Authority proof و delegation scope | `Verified authority evidence` و `Authority scope and limitations` | authenticated evidence و scope دقیق |
| Package delivery evidence | `Submission date/reference` | فقط پس از ارسال واقعی؛ Appointment معادل Submission نیست |
| Reviewer acknowledgement | `UNDER_REVIEW — EVIDENCE VERIFIED` | baseline و scope پذیرفته شده باشد |
| Authenticated per-IP response | `Reviewer disposition` و boundaries | فقط برای همان IP و همان scope |
| Suspension/expiration/revocation | future authority-state evidence | نیازمند schema/change action جداگانه؛ هیچ تغییر خودکار اینجا نیست |

وضعیت فعلی باید بدون تغییر باقی بماند:

```text
COORDINATION_STATUS = NOT_SUBMITTED
ASSIGNED_REVIEWER_IDENTITY = UNASSIGNED
VERIFIED_AUTHORITY_EVIDENCE = NOT_VERIFIED
REVIEWER_DISPOSITION = <intentionally empty>
```

مقدار literal فیلد disposition نباید بدون schema change مصوب به `NOT_RECEIVED` تبدیل شود. این Proposal نه Reviewer assignment است و نه Submission evidence.

## K. مرزهای Cross-specialist و Independent Review

| موضوع | Authority اصلی مرتبط | اثر Appointment IP |
| --- | --- | --- |
| Workload identity و ProducerAuthority | Identity/Platform Security | امکان bounded IP disposition پس از Appointment معتبر |
| Tenant Context، delegation و RLS | Tenant Security + Data/owning service | IP فقط identity-related constraints را بررسی می‌کند |
| Semantic equality و compatibility | Contract Governance | IP فقط provenance/authenticity requirements را ارائه می‌کند |
| Envelope، delivery و re-drive | Messaging/API Event Architecture | IP transport topology را تصویب نمی‌کند |
| Sovereign custody و reconnect | Sovereign-specific Security | IP local identity properties را بررسی می‌کند؛ Sovereign Approval مستقل است |
| Privileged recovery و incident policy | Operational Policy Governance | IP credential/identity constraints را تعیین می‌کند، نه execution policy |
| End-to-end sufficiency | Security Architecture | IP disposition ورودی مستقل است، جایگزین آن نیست |
| Eligibility/restoration | Future Eligibility Policy Authority | IP Appointment هیچ Authority ایجاد نمی‌کند |
| Independent conclusion | Independent Security Reviewer | Appointment و IP decisions به‌تنهایی sign-off مستقل نیستند |

همه cross-authority dependencies باقی می‌مانند. یک Authority نمی‌تواند برای Authority دیگر امضا کند، مگر delegation سازمانی صریح و Governance مصوبی وجود داشته باشد که با مرزهای معماری تعارض نداشته باشد.

## L. قالب درخواست تصویب Governance

این قالب عمداً خالی است و فقط توسط Organizational Authority احرازشده در یک اقدام آینده تکمیل می‌شود.

| فیلد | مقدار تصویب‌کننده |
| --- | --- |
| Actual approving organizational authority |  |
| Verified authority reference |  |
| Selected appointment model |  |
| Approved delegation policy |  |
| Effective date |  |
| Decision record |  |
| Signature or authenticated approval reference |  |
| Appointee acceptance reference |  |
| Approved scope and limitations |  |
| Expiration/review condition |  |
| Suspension/revocation authority |  |
| Evidence retention/custodian |  |

Blank fields imply no approval. تکمیل این قالب نیز فقط زمانی Appointment مؤثر ایجاد می‌کند که فرآیند مصوب، authenticity، authority، acceptance و effective conditions همگی احراز شده باشند.

## M. عدم‌تصویب‌های صریح

این Proposal موارد زیر را تصویب یا ایجاد نمی‌کند:

- Appointing Authority، Nominee، Appointee، Reviewer یا Committee واقعی؛
- Appointment، Delegation، sub-delegation، suspension، revocation یا effective date؛
- هیچ disposition برای `IP-01..05`؛
- هیچ Security Architecture Approval یا Independent Security Review sign-off؛
- Governance Standard نهایی یا تغییر در Tracking Register؛
- Tenant، Contract، Messaging، Sovereign، Operational Policy یا Eligibility authority؛
- فناوری Identity، protocol، credential format، cryptography، provider یا secret-management design؛
- risk acceptance، implementation authorization، Production Readiness یا executable `DURABLE_DEFER`؛
- تأیید Implementation Evidence یا اجرای Negative Test.

وضعیت‌های حاکمیتی بدون تغییر:

```text
V3-003 = IN PROGRESS
OD-001..023 = OPEN
SR-CAND-001..024 = PROPOSED — NOT APPROVED
IDENTITY_PLATFORM_SECURITY_AUTHORITY = UNASSIGNED
APPOINTING_AUTHORITY = NOT_VERIFIED
FORMAL_DELEGATION = NOT_ISSUED
IDENTITY_PLATFORM_SECURITY_APPROVAL = PENDING
SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF
IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED
NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED
EXECUTABLE_DURABLE_DEFER = NOT APPROVED
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
```

تصمیم سازمانی بعدی باید ابتدا Appointing Authority را با شاهد معتبر احراز و سپس مدل Appointment، delegation policy، competence floor، conflict rules، duration/review condition، suspension/revocation authority و evidence retention را صریحاً تصویب کند. تا آن زمان Track در وضعیت `UNASSIGNED / NOT_SUBMITTED` باقی می‌ماند.
