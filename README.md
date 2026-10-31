# Claude Warm for BB

A Claude-inspired theme for [BB](https://getbb.app), with cream surfaces, clay accents, warm charcoal, and serif responses.

The theme includes light and dark palettes. It uses embedded Source Serif 4 for responses, BB's bundled Inter for controls, and monospace fonts for code. No external font requests or image assets are required.

## Install

Clone the repository:

```sh
git clone https://github.com/kr3t3n/bb-theme-claude-warm.git
cd bb-theme-claude-warm
```

Find BB's custom theme directory:

```sh
bb theme dir
```

Create a `claude-warm` folder inside that directory. Copy `theme.css`, `theme.json`, and `font-license.txt` into it.

For BB installations that use the default `~/.bb/theme` directory:

```sh
mkdir -p ~/.bb/theme/claude-warm
cp theme.css theme.json font-license.txt ~/.bb/theme/claude-warm/
bb theme set claude-warm
```

The theme applies live. Each window retains its light or dark mode setting. You can also select the palette in Settings → Appearance.

Optional orange favicon:

```sh
bb theme favicon set orange
```

## Typography and spacing

Responses use Source Serif 4 at 17 pixels on desktop and 16 pixels on small screens, with relaxed line spacing. The composer uses 15-pixel sans-serif text, rounded corners, a soft shadow, and a clay focus border.

Code, diffs, and terminals retain monospace text. Status colors retain their separate meanings.

## Customize

Edit `treatments.css`, then rebuild:

```sh
python3 build-theme.py
```

The build script retains the embedded font from `theme.css`. Copy the rebuilt file into BB's theme directory and run `bb theme set claude-warm` again.

BB's theme stylesheet limit is 256 KiB. This theme is approximately 33 KiB. Its CSS selectors were verified with BB 0.48.1; future BB versions may change component selectors.

## Reset

```sh
bb theme reset
```

## License

Theme code is available under the [MIT license](LICENSE).
The embedded Source Serif 4 font uses the [SIL Open Font License 1.1](font-license.txt). It comes from `@fontsource/source-serif-4@5.2.5`, Latin normal weight 400.

Source Serif 4 is an open-licensed substitute for Claude's proprietary typefaces. This is an independent theme, with no affiliation to Anthropic.
