// Glue between Horizon's `Game` and `mod_crosshair_indicator`
use crate::game::Game;
use crate::game::Screen;
use crate::game::horizonmod as m;
use crate::game::native_hooks::NativeMod;
use horizon_client::extras_hud::Corners;
use horizon_client::hud::HudBatch;
use horizon_client::{
    chat::ChatSource,
    text::{self, Text},
};

pub fn say_text(game: &mut Game<'_>, body: Text) {
    let focused = game.screen == Screen::Chat;
    game.ui.chat.add(&game.gui.atlas, body, None, ChatSource::Client, game.ticks, focused);
}

pub fn say(game: &mut Game<'_>, message: &str) {
    say_text(game, Text::colored(message, text::GRAY));
}

pub(super) fn on_client_tick_post(game: &mut Game<'_>) {
    if game.title.is_none() {
        if let Some(p) = game.player.as_mut() {
            p.flying = true;
        }
    }
}

pub(super) fn on_remote_use_item_on(game: &mut Game<'_>) {
    say(game, "block interacted")
}
