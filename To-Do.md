# Yamagakure Clan RP Website — Project To-Do List

## Phase 1: Environment & Settings Setup
- [x] Initialize virtual environment (`python -m venv venv`).
- [x] Install required packages:
  - `django`
  - `django-ckeditor-5` (Rich Text)
- [x] Configure `settings.py`:
  - [x] Add all `INSTALLED_APPS` (Core, Users, Rulesets, Battleposts, Lore, News, History, + 3rd parties).
  - [x] Set up `AUTH_USER_MODEL = 'users.CustomUser'`.
  - [x] Set up `django-ckeditor-5` settings.
  - [x] Set up `MEDIA_URL` and `MEDIA_ROOT` for image uploads.
  - [x] Set up `STATIC_URL` and create the `static` directory.
  - [ ] Configure `META_SITE_PROTOCOL` and `META_SITE_DOMAIN` for SEO.
- [x] Run initial `makemigrations` and `migrate`.

---

## Phase 2: The Apps & Models (Dynamic Architecture)
*Everything must be completely dynamic (no hardcoding), editable via Django Admin.*

### 1. `core` App (The Engine & Global Settings)
- [x] **Rank Model:** 
  - Level (Integer 1-7, unique), Name.
- [x] **Honorific Model:** 
  - Name, Badge Image, `grants_superuser` (Boolean).
- [ ] **CustomField Model:** (For extreme dynamism)
  - Name, Field Type (Text, Number, Dropdown, Image), Options (for dropdowns), Applies To (Character, Battle, Lore).
- [ ] **CustomFieldValue Model:** 
  - Link to CustomField, Object ID, Value.
- [x] **SiteSetting Model:** 
  - Site Name, Emblem, Background Image, Theme Color, Discord/Facebook links.

### 2. `users` App (Profiles & Clearances)
- [x] **CustomUser Model (extends AbstractUser):**
  - `rank` (FK to Rank, default Level 1).
  - `rp_name`, `avatar`, `bio`.
  - `honorifics` (M2M to Honorific).
  - `combat_xp` (Integer, default 10,000).
  - *Custom Methods:* `is_order_of_ygnis()` (checks for specific honorific), `has_staff_powers()` (Level 6/7 or honorific), `can_view_classified(level)`, `can_manage_user_rank(target_user)`.

### 3. `battleposts` App (The Combat Archive)
- [ ] **BattleTier Model:**
  - Name (URM, MP, PC, etc.), Description (RichText for the massive rules blocks).
- [ ] **BattlePost Model:**
  - Title, Tier (FK).
  - Header Info (Temperature, Weather, Windspeed, Location, Time).
  - Narrative (RichText).
  - Image (Optional).
  - Outcome & Judging (Winner, Judge Notes).
  - Meta: `required_rank` (FK), Tags, Created At, Published status.

### 4. `rulesets` App (The Laws)
- [ ] **RulesetCategory Model:**
  - Name (e.g., "Standard Rules", "Power Tiers").
- [ ] **Ruleset Model:**
  - Category (FK), Title, Content (RichText), Order (Integer).

### 5. `lore` App (Worldbuilding & Map)
- [ ] **LoreCategory Model:** 
  - Name (e.g., "Power System").
- [ ] **Character Model:**
  - Name, Owner (FK to User), Status (Alive/Dead/NPC).
  - Appearance, Backstory, Powers (RichText).
  - Combat Rank (FK), Current XP, `required_rank`.
- [ ] **LoreArticle Model:**
  - Category (FK), Title, Content (RichText), Image, `required_rank`.
- [ ] **MapLocation Model (MPTT Model for Hierarchy):**
  - Name, Parent Location (TreeForeignKey).
  - Description, Image.
  - State Details: Ruling Faction, Is Warzone (Boolean).
  - `required_rank`.

### 6. `history` App (Lore & Progression)
- [ ] **CombatRank Model:**
  - Name (e.g., Elite, Saint), Tier (High/Intermediate/Lower), Min XP, Max XP.
- [ ] **HistoricEvent Model:**
  - Title, Date of Event, Description (RichText), Image, `required_rank`.

### 7. `news` App (Announcements)
- [ ] **NewsUpdate Model:**
  - Title, Content (RichText), Date Posted, Is Pinned (Boolean), `required_rank`.

---

## Phase 3: Admin Configuration
*Register all models and customize the admin interface for easy content management.*
- [ ] **`users/admin.py`:** Use `UserAdmin` to display RP Name, Rank, XP, and Honorifics. Add custom actions to award/deduct XP.
- [ ] **`core/admin.py`:** Register Ranks, Honorifics, Custom Fields (Inline for CustomFieldValues), and SiteSetting.
- [ ] **`battleposts/admin.py`:** Register BattleTiers and BattlePosts. Use a Rich Text editor for the narrative.
- [ ] **`lore/admin.py`:** Register Characters, LoreArticles, and MapLocation (using MPTT admin for drag-and-drop tree sorting).
- [ ] **`rulesets`, `history`, `news`:** Standard admin registration with list displays for easy sorting.

---

## Phase 4: Views & Security Logic
- [ ] **Authentication Views:** Standard login/register, plus Django-allauth URLs for Facebook/Discord OAuth.
- [ ] **Classified Content Gate:** Build a mixin or decorator (`@classified_required(level)`) to protect views based on `request.user.can_view_classified()`.
- [ ] **Rank Management View:** A view that allows Level 6+ users to promote/demote users up to their own level, blocking them from promoting higher than themselves.
- [ ] **CRUD Views (Staff Only):** Create, Update, Delete views for Battle Posts, Lore Articles, News, and Rulesets for staff members.
- [ ] **Filtering:** Implement `django-filter` in the Battle Post list view to filter by Tier, Location, or Participant.

---

## Phase 5: URLs Routing
- [ ] `core/urls.py`: Homepage, Global Settings.
- [ ] `users/urls.py`: Profile, Login/Logout, Social Auth Callbacks, Rank Management.
- [ ] `battleposts/urls.py`: List view, Detail view, Create/Edit views.
- [ ] `rulesets/urls.py`: List categories, view rulesets.
- [ ] `lore/urls.py`: Character list/detail, Map view, Lore article list/detail.
- [ ] `history/urls.py`: Historic Events timeline, Combat Ranks list.
- [ ] `news/urls.py`: News feed, Detail view.
- [ ] `main/urls.py`: Combine all app URLs and serve media/static in development.

---

## Phase 6: Templates & Front-End (The Aesthetic)
- [ ] **Base Template:** Include the Yamagakure Emblem, dynamic navigation bar (hiding links user doesn't have clearance for), and footer.
- [ ] **SEO Integration:** Ensure all templates extend a meta block that pulls title, description, and OG images dynamically.
- [ ] **Authentication Pages:** Style the login/register page with Facebook and Discord buttons.
- [ ] **Battle Post Detail Template:** Recreate the exact visual formatting (❏. Title, ▃▃▃ dividers, BATTLE INFORMATION block, RichText narrative).
- [ ] **Classified Template:** A specific "Classified Intel" screen for when a user clicks on something above their clearance level.
- [ ] **Map Template:** Interactive or visually appealing tree view using the MPTT data.
- [ ] **Profile Dashboard:** Shows User's Rank, XP, Honorific Badges, and their owned Characters.
- [ ] **Ruleset Template:** Clean, readable layout for the massive walls of text (like the T-1 rules).

---

## Phase 7: Final Polish & SEO
- [ ] Verify Google Search indexing is optimized (via `django-meta`).
- [ ] Test Facebook and Discord embeds (OpenGraph tags) by pasting site URLs into those apps.
- [ ] Configure `ALLOWED_HOSTS` and prepare `DEBUG=False` for production.
- [ ] Set up email backend for password resets (via allauth).