# Candidates — Unsent: The Micro-Confession Sprint

Bounty: u-boothlord-unsent-the-micro-confession-sprint-8c6596ba
Gate: /output/entry.txt, UTF-8, 1–260 chars total, not whitespace-only.
Message line: at most 200 chars. Two parts: a `To:` line + the unsent line, no
explanation after it. No real full names or handles.

Judge brief criteria, IN ORDER (most important first):
1. Two-part confession (To: line + message); anything else loses to any two-part confession.
2. Reason it stayed in drafts is FELT — too honest, too late, too kind, too
   afraid — and the words are specific and honest rather than general.
3. The To: line and the message need each other; swapping the addressee would break it.
4. Reads as typed and never sent, not written to be sent; pure jokes, greetings,
   motivational lines lose.
5. One line written exactly as it was typed, no explanation after it.
Also: the reason it stayed in drafts should be felt in the words, NOT stated.
Cleverness for its own sake does not count.

## The candidates (12)

C1 — To: Mara, who taught me to drive stick
    I still take the long way home past your old house so I can stall at the
    light where you used to laugh at me.

C2 — To: my little brother, who thinks I moved out for work
    I moved out because Mom cried every night after Dad left and I couldn't
    watch it from the next room anymore.

C3 — To: Mr. Alvarez, my high school janitor
    I was the one who broke the trophy case in 2011. You got blamed and I
    watched you clean it up anyway.

C4 — To: June, my best friend since third grade
    I knew about the lump before you told me. I found the appointment card in
    your coat and prayed it was a mistake.

C5 — To: the girl in seat 14B, flight 209
    I never asked your name because the woman next to you was already crying
    and I didn't want to be the reason.

C6 — To: Dad
    I kept your voicemails after you died and I still call the number
    sometimes just to hear you say my name.

C7 — To: Priya, who sat behind me in chemistry
    I copied your homework for a year and the only reason I passed is you
    never once checked if I understood any of it.

C8 — To: my grandmother's nurse, Rosa
    You were the only one who held her hand the last night and I never
    thanked you because I was too busy being angry at everyone.

C9 — To: Tom, my roommate in 2019
    I ate your leftovers every time you went home for the weekend and blamed
    the dog we never owned.

C10 — To: Elena, who married my best friend
     I still remember the exact shade of your dress at the wedding and I hate
     myself a little every time I do.

C11 — To: my sister, Ana
     I told Mom selling your piano was my idea. It wasn't, and I've carried
     that lie for twelve years.

C12 — To: the cashier at the corner store on 5th
     You asked how my mother was doing every single time and I never once
     asked about yours.

## Manual ranking (my own judgment only — no Gemini/NVIDIA judge, no judge-API tournament)

Criterion 1: all twelve are two-part. No separation here.
Criterion 2 (felt reason, specific + honest): C2, C3, C4, C8, C11, C12, C10
strongest. C6 strong but a well-worn trope (dead parent's voicemails). C1
good. C7 slightly clever rather than honest. C9 is a joke. C5's premise is
strained — you cannot text a stranger from a plane, so "typed and never sent"
barely holds.
Criterion 3 (To: and message need each other): C3, C8, C2, C11, C12, C10
strongest — each message names an act that only fits that addressee. C6 is
weaker here: "Dad" + voicemails fits any dead father. C2 is slightly indirect:
the confession is really about Mom, routed through the brother.
Criterion 4 (typed, never sent): C9 FAILS outright — a punchline written to
be sent. C7 leans clever. C5's premise fails it. The rest pass.
Criterion 5: all are one line, no explanation after.

Top tier: C3, C8, C2, C11, C12, C10.

Pairwise among the top tier:
- C3 vs C8: C3 wins. C3's guilt is active and specific (I broke it, you were
  blamed, I watched). C8 is gratitude — a thank-you is normally sent, so its
  unsent-ness leans on the anger excuse; C3's "I framed you" is the kind of
  thing that stays in drafts.
- C3 vs C2: C3 wins on criterion 3. C2's message is addressed to the brother
  but is really about Mom; C3's message is directly to Alvarez about what the
  sender did TO Alvarez.
- C3 vs C11: C3 wins narrowly. C11's twelve-year lie is strong, but its
  confession is about a lie told to Mom, routed to the sister; C3 is direct.
- C3 vs C12: C3 wins. C12 is quiet and real, but its stakes are low (never
  asking about her mother) and the window is still open — you could still ask.
  C3's window is closed (2011, school years past) and someone was blamed.
- C3 vs C10: C3 wins. C10 edges toward stating the feeling ("I hate myself a
  little"), C3 never states a feeling — it just shows the act, and the shame
  is felt, not stated.

## CHOSEN: C3

To: Mr. Alvarez, my high school janitor
I was the one who broke the trophy case in 2011. You got blamed and I watched you clean it up anyway.

Why it wins: a named year and a named object (trophy case, 2011) make it
specific and honest; the addressee is a role + a surname (not a full name) and
the message only makes sense for him — swap the addressee and it breaks; the
reason it stayed unsent (shame, then too late) is felt in "I watched you
clean it up anyway" and never stated; it reads as typed, plain and
unpolished, not written to be sent.

Char counts (verified by script): To: line 39 chars, message 101 chars,
total entry 141 chars (no trailing newline) — inside the 1–260 gate, message
inside the 200 cap.
