from __future__ import annotations

from _common import build_parser, get_manifest, load_config, print_config, public_release_unavailable, validate_manifest


def main() -> None:
    parser = build_parser("Train the SHIELD teacher-student MAE encoder.")
    args = parser.parse_args()
    cfg = load_config(args.config, args.manifest)
    cases = validate_manifest(get_manifest(cfg, args.manifest))
    print(f"Validated {cases} manifest case(s) for pretraining.")
    if args.dry_run:
        print_config(cfg)
        return
    public_release_unavailable("Pretraining")


if __name__ == "__main__":
    main()
