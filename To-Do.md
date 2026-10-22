# Yamagakure Clan RP Website — Project To-Do List

## Phase 1: Environment & Settings Setup
- [x] Initialize virtual environment (`python -m venv venv`).
- [x] Install required packages
- [x] Make applications
---

## Phase 2: The Apps & Models (Dynamic Architecture)
*Everything must be completely dynamic (no hardcoding), editable via Django Admin.*

### 1. `core` App (The Engine & Global Settings)
- [x] **Site settings Mode:**
  - [x] site `name`
  - [x] site `emblem`
  - [x] site `background image`
  - [x] site `color theme`

### 2. `users` App (Profiles & Clearances)
- [x] **Profile Model (extends AbstractUser):**
  - [x] `class_level ` classiefied view level
  - [x] `honorifics` (M2M to Honorific).
  - [x] `combat_xp` (Integer, default 10,000).
  - [ ] *Custom Methods:* `is_order_of_ygnis()` (checks for specific honorific), `has_staff_powers()` (Level 6/7 or honorific), `can_view_classified(level)`, `can_manage_user_rank(target_user)`.

### 3. `battleposts` App (The Combat Archive)
- [x] **BattlePost Model:**
  - [x] `Title`
  - [x] `Ruleset` (from rulesets.models )
  - [ ] `Header Info` (Temperature, Weather, Windspeed, Location, Time).
  - [x] `Narrative` (RichText).
  - [ ] `Image` (Optional).
  - [x]Outcome & Judging (Winner, Judge Notes).
  - [ ] Meta: `required_rank` (FK), Tags, Created At, Published status.

### 4. `rulesets` App (The Laws)
- [x] **RulesetCategory Limits Model:**
  - [x] `Name` (e.g., "Standard Rules", "Power Tiers").
  - [x] `Description`
- [x] **Ruleset Model:**
  - [x] `Name`
  - [ ] `Tier Limit`
  - [x] Category (FK), Title, Content (RichText), Order (Integer).

### 5. `lore` App (System)
- [x] **House Model:**
  - [x] `Name`
  - [x] `Emblem`
- [x] **Power System:**
 - [x] `Name`
 - [x] `Scale` (continental, etc)
 - [x] `Core Concept`
 - [x] `Mechanics`
- [x] **Combat Ranks:**
  - [x] `Rank Name`
  - [x] `Class Type` (Lower, High)
- [x] **Canon Event:**
 - [x] `Name`
 - [x] `Date`
 - [x] `Description`
- [ ] **In-Character Calender Model:**
 - [ ] `Months`
 - [ ] `Days Of The Year`
- [ ] **Legistlature Model:**
 - [ ] `Name`
 - [ ] `Last Date Updated`
 - [ ] `Content`

### 6. `Geography` App (Map)
- [x] **Continent Model:**
  - [x] `Name`
  - [x] `Image map`
  - [x] `Region`
  - [x] `Land Mass`
  - [x] `Description`
- [x] **State Model:**
  - [x] `Name`
  - [x] `Image Map`
  - [x] `Continent`
  - [x] `Biome`
  - [x] `Land mass`
  - [x] `population`
  - [x] `Region`
  - [x] `Description`

### 7. `news` App (Announcements)
- [x] **NewsUpdate Model:**
  - [x] `Title`
  - [x] `Content` (RichText)
  - [x] `Thumbnail`
  - [x] `Date Posted`
  - [x] `Is Pinned (Boolean)`
  - [x] `required_rank`.

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